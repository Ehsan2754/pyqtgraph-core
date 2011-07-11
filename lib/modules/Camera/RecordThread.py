import time
from lib.filetypes.ImageFile import *
from Mutex import Mutex
from PyQt4 import QtGui, QtCore
import debug
from metaarray import MetaArray
import numpy as np
import ptime

class RecordThread(QtCore.QThread):
    
    sigShowMessage = QtCore.Signal(object)
    sigRecordingFailed = QtCore.Signal()
    
    def __init__(self, ui, manager):
        QtCore.QThread.__init__(self)
        self.ui = ui
        self.m = manager
        #QtCore.QObject.connect(self.ui.cam, QtCore.SIGNAL('newFrame'), self.newCamFrame)
        self.ui.cam.sigNewFrame.connect(self.newCamFrame)
        
        #QtCore.QObject.connect(ui.ui.btnRecord, QtCore.SIGNAL('toggled(bool)'), self.toggleRecord)
        ui.ui.btnRecord.toggled.connect(self.toggleRecord)
        #QtCore.QObject.connect(ui.ui.btnSnap, QtCore.SIGNAL('clicked()'), self.snapClicked)
        ui.ui.btnSnap.clicked.connect(self.snapClicked)
        self.recording = False
        self.recordStart = False
        self.recordStop = False
        self.takeSnap = False
        self.currentRecord = None
        
        self.lock = Mutex(QtCore.QMutex.Recursive)
        self.camLock = Mutex()
        self.newCamFrames = []
        
    def newCamFrame(self, frame=None):
        if frame is None:
            return
        with self.lock:
            newRec = self.recordStart
            lastRec = self.recordStop
            if self.recordStop:
                self.recording = False
                self.recordStop = False
            if self.recordStart:
                self.recordStart = False
                self.recording = True
            recording = self.recording or lastRec
            takeSnap = self.takeSnap
            self.takeSnap = False
            recFile = self.currentRecord
        if recording or takeSnap:
            with self.camLock:
                ## remember the record/snap/storageDir states since they might change 
                ## before the write thread gets to this frame
                self.newCamFrames.append({'frame': frame, 'record': recording, 'snap': takeSnap, 'newRec': newRec, 'lastRec': lastRec})
    
    def run(self):
        self.stopThread = False
        
        while True:
            try:
                with self.camLock:
                    handleCamFrames = self.newCamFrames[:]
                    self.newCamFrames = []
            except:
                debug.printExc('Error in camera recording thread:')
                break
            
            try:
                while len(handleCamFrames) > 0:
                    self.handleCamFrame(handleCamFrames.pop(0))
            except:
                debug.printExc('Error in camera recording thread:')
                self.toggleRecord(False)
                #self.emit(QtCore.SIGNAL('recordingFailed'))
                self.sigRecordingFailed.emit()
                
            time.sleep(10e-3)
            
            #print "  RecordThread run: stop check"
            with self.lock as l:
                #print "  RecordThread run:   got lock"
                if self.stopThread:
                    #print "  RecordThread run:   stop requested, exiting loop"
                    break
            #print "  RecordThread run:   unlocked"


    def handleCamFrame(self, frame):
        (data, info) = frame['frame']
        
        if frame['record']:
            if frame['newRec']:
                self.startFrameTime = info['time']
                
            arrayInfo = [
                {'name': 'Time', 'values': array([info['time'] - self.startFrameTime]), 'units': 's'},
                {'name': 'X'},
                {'name': 'Y'}
            ]
            #import random
            #if random.random() < 0.01:
                #raise Exception("TEST")
            data = MetaArray(data[np.newaxis], info=arrayInfo)
            if frame['newRec']:
                self.currentRecord = self.m.getCurrentDir().writeFile(data, 'video', autoIncrement=True, info=info, appendAxis='Time')
                self.currentFrameNum = 0
            else:
                now = ptime.time()
                data.write(self.currentRecord.name(), appendAxis='Time')
                print "Frame write: %0.2gms" % (1000*(ptime.time()-now))
                s = 1.0/self.currentFrameNum
                
            self.showMessage("Recording %s - %d" % (self.currentRecord.name(), self.currentFrameNum))
            
            self.currentFrameNum += 1
            
            if frame['lastRec']:
                dur = info['time'] - self.startFrameTime
                self.currentRecord.setInfo({'frames': self.currentFrameNum, 'duration': dur, 'averageFPS': ((self.currentFrameNum-1)/dur)})
                self.showMessage('Finished recording %s - %d frames, %02f sec' % (self.currentRecord.name(), self.currentFrameNum, dur)) 
                
            
        
        if frame['snap']:
            fileName = 'image.tif'
            
            fh = self.m.getCurrentDir().writeFile(data, fileName, info, fileType="ImageFile", autoIncrement=True)
            fn = fh.name()
            self.showMessage("Saved image %s" % fn)
            with self.lock:
                self.takeSnap = False
    
    def showMessage(self, msg):
        #self.emit(QtCore.SIGNAL('showMessage'), msg)
        self.sigShowMessage.emit(msg)
    
    def snapClicked(self):
        with self.lock:
            self.takeSnap = True

    def toggleRecord(self, b):
        with self.lock:
            if b:
                self.recordStart = True
            else:
                if self.recording:
                    self.recordStop = True

    def stop(self):
        #QtCore.QObject.disconnect(self.ui.cam, QtCore.SIGNAL('newFrame'), self.newCamFrame)
        self.ui.cam.sigNewFrame.disconnect(self.newCamFrame)
        #print "RecordThread stop.."    
        with self.lock:
        #print "  RecordThread stop: locked"
            self.stopThread = True
        #print "  RecordThread stop: done"
        