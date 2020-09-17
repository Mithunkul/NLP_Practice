import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QSizePolicy, QStyleFactory
import sqlite3

from Analytics import *
from ImageGallery import *


class bottleLaneDashboard(QtWidgets.QWidget, Analytics, ImageGallery):
    
    
    def mainGUI(self):
        
        self.TOP_FRAME = QtWidgets.QFrame()
        self.TOP_FRAME.setStyleSheet("background-color:rgba(100,100,100) ")
        self.TOP_FRAME.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        
        self.TOP_HBOX = QtWidgets.QHBoxLayout()
        
        self.HOME_BUTTON = QtWidgets.QPushButton("Home")
        self.HOME_BUTTON.setStyleSheet("background-color:rgba(100,100,100); color:white; border: 0px")
        self.HOME_BUTTON.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.HOME_BUTTON.setFont(QtGui.QFont("Ford Antenna Light", 13, QtGui.QFont.Normal))
        self.HOME_BUTTON.clicked.connect(lambda event, menu= "Home":self.run_screens(event, menu))
        
        TOPLABEL = QtWidgets.QLabel("Enter Title Here")
        TOPLABEL.setFont(QtGui.QFont("Ford Antenna Light", 22, QtGui.QFont.Normal))
        TOPLABEL.setStyleSheet("background-color:rgba(100,100,100); color:rgba(255,255,255)")
        
        ANALYTICS =  QtWidgets.QPushButton("Analytics")
#        ANALYTICS.setFlat(True)
        ANALYTICS.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        ANALYTICS.setFont(QtGui.QFont("Ford Antenna Light", 13, QtGui.QFont.Normal))
        ANALYTICS.setStyleSheet("color:rgba(220,220,220); border: 0px")
        ANALYTICS.clicked.connect(lambda event, menu= "Analytics":self.run_screens(event, menu))
        
        IMAGEGALLERY =  QtWidgets.QPushButton("Image Gallery")
#        IMAGEGALLERY.setFlat(True)
        IMAGEGALLERY.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        IMAGEGALLERY.setFont(QtGui.QFont("Ford Antenna Light", 13, QtGui.QFont.Normal))
        IMAGEGALLERY.setStyleSheet("color:rgba(220,220,220); border: 0px")
        IMAGEGALLERY.clicked.connect(lambda event, menu= "Image Gallery":self.run_screens(event, menu))
        
        self.TOP_HBOX.addWidget(self.HOME_BUTTON)
        self.TOP_HBOX.addStretch(1)
        self.TOP_HBOX.addWidget(TOPLABEL)
        self.TOP_HBOX.addStretch(1)
        self.TOP_HBOX.addWidget(ANALYTICS)
        self.TOP_HBOX.addSpacing(20)
        self.TOP_HBOX.addWidget(IMAGEGALLERY)
        self.TOP_HBOX.addSpacing(20)
        
        self.TOP_FRAME.setLayout(self.TOP_HBOX)
        self.MAIN_VBOX.addWidget(self.TOP_FRAME)
        
        self.homeScreen()
     
    #----------------------------------------------------------------------------------------------------------------#   
        
    def clearLayout(self, layout):
        while layout.count():
            child = layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
        
        
    #----------------------------------------------------------------------------------------------------------------#   
    
    def homeScreen(self):
        self.MAIN_GRID_LAYOUT = QtWidgets.QGridLayout()
        self.GBOX_FOR_HOME_MASTER_FRAME = QtWidgets.QGridLayout()
        self.HOME_MASTER_FRAME = QtWidgets.QFrame()
        self.HOME_MASTER_FRAME.setStyleSheet("background-color: white" )
        
        
        self.HOME_MASTER_FRAME.setLayout(self.GBOX_FOR_HOME_MASTER_FRAME)
        self.MAIN_GRID_LAYOUT.addWidget(self.HOME_MASTER_FRAME,  0 , 0)
        self.MAIN_VBOX.addLayout(self.MAIN_GRID_LAYOUT)
     
        
    #----------------------------------------------------------------------------------------------------------------#
     
    def run_screens(self, event=None, menu=None):
        self.hide_screens()
        
        if menu=="Home":
            self.HOME_MASTER_FRAME.show()
        if menu=="Analytics":
            self.analyticsScreen()
        elif menu=="Image Gallery":
            self.imageGalleryScreen()
     
        
    #----------------------------------------------------------------------------------------------------------------#
            
    def flatten(self, llist):
        ret = [ ]
        for sublist in llist:
            for subelement in sublist:
                ret.append(subelement)
                
        return ret

    #----------------------------------------------------------------------------------------------------------------#        
            
        
    def hide_screens(self):
        
        self.HOME_MASTER_FRAME.hide()
        
        try:
            self.ANALYTICS_SCROLL.hide()
        except Exception as e:
            print(e)
        try:
            self.IMAGEGALLERY_SCROLL.hide()   
        except Exception as e:
            print(e)
        
    #----------------------------------------------------------------------------------------------------------------#
    
    def __init__(self):
        super(bottleLaneDashboard, self).__init__()
        self.setWindowTitle("Title Here")
        self.setWindowState(self.windowState()|QtCore.Qt.WindowMaximized)
        self.MAIN_VBOX = QtWidgets.QVBoxLayout()
        self.MAIN_VBOX.setSpacing(0)
        self.MAIN_VBOX.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.MAIN_VBOX)
        self.setContentsMargins(0, 0, 0, 0)
        
        self.mainGUI()
        self.show()
    
    
    
if __name__ == "__main__":
   
    app = QtCore.QCoreApplication.instance()
    
    if app is None:
        app = QtWidgets.QApplication(sys.argv)
    ui = bottleLaneDashboard()
    app.setStyle(QStyleFactory.create('Fusion'))
    try:
        sys.exit(app.exec_())
    except SystemExit:
        pass