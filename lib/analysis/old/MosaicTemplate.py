# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './lib/analysis/old/MosaicTemplate.ui'
#
# Created: Sun Mar  4 09:45:52 2012
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_4 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.splitter_2 = QtGui.QSplitter(self.centralwidget)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName(_fromUtf8("splitter_2"))
        self.widget = QtGui.QWidget(self.splitter_2)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.setRootBtn = QtGui.QPushButton(self.widget)
        self.setRootBtn.setObjectName(_fromUtf8("setRootBtn"))
        self.verticalLayout_3.addWidget(self.setRootBtn)
        self.fileTree = DirTreeWidget(self.widget)
        self.fileTree.setObjectName(_fromUtf8("fileTree"))
        self.verticalLayout_3.addWidget(self.fileTree)
        self.loadBtn = QtGui.QPushButton(self.widget)
        self.loadBtn.setObjectName(_fromUtf8("loadBtn"))
        self.verticalLayout_3.addWidget(self.loadBtn)
        self.groupBox = QtGui.QGroupBox(self.widget)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox)
        self.gridLayout.setMargin(0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.transformList = QtGui.QListView(self.groupBox)
        self.transformList.setObjectName(_fromUtf8("transformList"))
        self.gridLayout.addWidget(self.transformList, 0, 0, 1, 4)
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.translateXSpin = QtGui.QDoubleSpinBox(self.groupBox)
        self.translateXSpin.setObjectName(_fromUtf8("translateXSpin"))
        self.gridLayout.addWidget(self.translateXSpin, 1, 1, 1, 2)
        self.translateYSpin = QtGui.QDoubleSpinBox(self.groupBox)
        self.translateYSpin.setObjectName(_fromUtf8("translateYSpin"))
        self.gridLayout.addWidget(self.translateYSpin, 1, 3, 1, 1)
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.rotateSpin = QtGui.QDoubleSpinBox(self.groupBox)
        self.rotateSpin.setObjectName(_fromUtf8("rotateSpin"))
        self.gridLayout.addWidget(self.rotateSpin, 2, 1, 1, 3)
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.scaleYSpin = QtGui.QDoubleSpinBox(self.groupBox)
        self.scaleYSpin.setObjectName(_fromUtf8("scaleYSpin"))
        self.gridLayout.addWidget(self.scaleYSpin, 3, 3, 1, 1)
        self.scaleXSpin = QtGui.QDoubleSpinBox(self.groupBox)
        self.scaleXSpin.setObjectName(_fromUtf8("scaleXSpin"))
        self.gridLayout.addWidget(self.scaleXSpin, 3, 1, 1, 2)
        self.saveBtn = QtGui.QPushButton(self.groupBox)
        self.saveBtn.setObjectName(_fromUtf8("saveBtn"))
        self.gridLayout.addWidget(self.saveBtn, 4, 0, 1, 2)
        self.saveAllBtn = QtGui.QPushButton(self.groupBox)
        self.saveAllBtn.setObjectName(_fromUtf8("saveAllBtn"))
        self.gridLayout.addWidget(self.saveAllBtn, 4, 2, 1, 2)
        self.verticalLayout_3.addWidget(self.groupBox)
        self.splitter = QtGui.QSplitter(self.splitter_2)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.widget1 = QtGui.QWidget(self.splitter)
        self.widget1.setObjectName(_fromUtf8("widget1"))
        self.gridLayout_3 = QtGui.QGridLayout(self.widget1)
        self.gridLayout_3.setMargin(0)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.groupBox_3 = QtGui.QGroupBox(self.widget1)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox_3)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.addMarkerBtn = QtGui.QPushButton(self.groupBox_3)
        self.addMarkerBtn.setObjectName(_fromUtf8("addMarkerBtn"))
        self.gridLayout_2.addWidget(self.addMarkerBtn, 0, 0, 1, 1)
        self.delMarkerPen = QtGui.QPushButton(self.groupBox_3)
        self.delMarkerPen.setObjectName(_fromUtf8("delMarkerPen"))
        self.gridLayout_2.addWidget(self.delMarkerPen, 0, 1, 1, 1)
        self.markerList = QtGui.QListView(self.groupBox_3)
        self.markerList.setObjectName(_fromUtf8("markerList"))
        self.gridLayout_2.addWidget(self.markerList, 1, 0, 1, 2)
        self.gridLayout_3.addWidget(self.groupBox_3, 0, 0, 1, 1)
        self.groupBox_2 = QtGui.QGroupBox(self.widget1)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.normalizeBtn = QtGui.QPushButton(self.groupBox_2)
        self.normalizeBtn.setObjectName(_fromUtf8("normalizeBtn"))
        self.verticalLayout.addWidget(self.normalizeBtn)
        self.blendBtn = QtGui.QPushButton(self.groupBox_2)
        self.blendBtn.setObjectName(_fromUtf8("blendBtn"))
        self.verticalLayout.addWidget(self.blendBtn)
        self.autoRangeBtn = QtGui.QPushButton(self.groupBox_2)
        self.autoRangeBtn.setObjectName(_fromUtf8("autoRangeBtn"))
        self.verticalLayout.addWidget(self.autoRangeBtn)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.gridLayout_3.addWidget(self.groupBox_2, 0, 1, 1, 1)
        self.groupBox_4 = QtGui.QGroupBox(self.widget1)
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.exportSvgBtn = QtGui.QPushButton(self.groupBox_4)
        self.exportSvgBtn.setObjectName(_fromUtf8("exportSvgBtn"))
        self.verticalLayout_2.addWidget(self.exportSvgBtn)
        self.exportPngBtn = QtGui.QPushButton(self.groupBox_4)
        self.exportPngBtn.setObjectName(_fromUtf8("exportPngBtn"))
        self.verticalLayout_2.addWidget(self.exportPngBtn)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.gridLayout_3.addWidget(self.groupBox_4, 0, 2, 1, 1)
        self.canvas = Canvas(self.splitter)
        self.canvas.setObjectName(_fromUtf8("canvas"))
        self.gridLayout_4.addWidget(self.splitter_2, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Mosaic", None, QtGui.QApplication.UnicodeUTF8))
        self.setRootBtn.setText(QtGui.QApplication.translate("MainWindow", "--> Set Root Directory", None, QtGui.QApplication.UnicodeUTF8))
        self.loadBtn.setText(QtGui.QApplication.translate("MainWindow", "Load Selected -->", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("MainWindow", "Transformations", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Translate", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Rotate", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "Scale", None, QtGui.QApplication.UnicodeUTF8))
        self.saveBtn.setText(QtGui.QApplication.translate("MainWindow", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.saveAllBtn.setText(QtGui.QApplication.translate("MainWindow", "Save All", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("MainWindow", "Markers", None, QtGui.QApplication.UnicodeUTF8))
        self.addMarkerBtn.setText(QtGui.QApplication.translate("MainWindow", "Add...", None, QtGui.QApplication.UnicodeUTF8))
        self.delMarkerPen.setText(QtGui.QApplication.translate("MainWindow", "Del", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("MainWindow", "Image Correction", None, QtGui.QApplication.UnicodeUTF8))
        self.normalizeBtn.setText(QtGui.QApplication.translate("MainWindow", "Normalize", None, QtGui.QApplication.UnicodeUTF8))
        self.blendBtn.setText(QtGui.QApplication.translate("MainWindow", "Blend", None, QtGui.QApplication.UnicodeUTF8))
        self.autoRangeBtn.setText(QtGui.QApplication.translate("MainWindow", "Auto Range", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_4.setTitle(QtGui.QApplication.translate("MainWindow", "Export", None, QtGui.QApplication.UnicodeUTF8))
        self.exportSvgBtn.setText(QtGui.QApplication.translate("MainWindow", "SVG", None, QtGui.QApplication.UnicodeUTF8))
        self.exportPngBtn.setText(QtGui.QApplication.translate("MainWindow", "PNG", None, QtGui.QApplication.UnicodeUTF8))

from Canvas import Canvas
from DirTreeWidget import DirTreeWidget
