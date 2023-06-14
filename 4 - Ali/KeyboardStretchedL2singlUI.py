from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDesktopWidget
from CreateAction import Ui_CreateAction
import ctypes
user32 = ctypes.windll.user32
user32.SetProcessDPIAware()
ax, wae = [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)]


class Ui_NoMad(object):
    def openWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_CreateAction()
        self.ui.setupUi(self.window)    
        self.window.show()  

    def setupUi(self, NoMad):
        NoMad.setObjectName("NoMad")
        NoMad.resize(1105, 587)
        self.centralwidget = QtWidgets.QWidget(NoMad)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame_9 = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_9.sizePolicy().hasHeightForWidth())
        self.frame_9.setSizePolicy(sizePolicy)
        self.frame_9.setMaximumSize(QtCore.QSize(1081, 341))
        self.frame_9.setMouseTracking(False)
        self.frame_9.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame_9.setAutoFillBackground(False)
        self.frame_9.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"font: 8pt \"Arial\";\n"
"color: rgb(255, 255, 255);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 25px;")
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setLineWidth(1)
        self.frame_9.setMidLineWidth(0)
        self.frame_9.setObjectName("frame_9")
        self.frame_20 = QtWidgets.QFrame(self.frame_9)
        self.frame_20.setGeometry(QtCore.QRect(100, 11, 961, 59))
        self.frame_20.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_20.setObjectName("frame_20")
        self.pushButton_194 = QtWidgets.QPushButton(self.frame_20, clicked = lambda: self.openWindow())
        self.pushButton_194.setGeometry(QtCore.QRect(10, 0, 55, 55))
        self.pushButton_194.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_194.setMaximumSize(QtCore.QSize(55, 55))
        self.pushButton_194.setStyleSheet("\n"
"QPushButton:checked {\n"
"background-color: #af55ff;\n"
"color: white;\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: rgb(51,51,51);\n"
"  border-radius: 15px;\n"
"  border-style: none;\n"
"  color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  /* Change the background color when the button is hovered over */\n"
"  color: rgb(197, 197, 197)\n"
"}")
        self.pushButton_194.setCheckable(True)
        self.pushButton_194.setObjectName("pushButton_194")
        self.buttonGroup = QtWidgets.QButtonGroup(NoMad)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.pushButton_194)
        self.pushButton_195 = QtWidgets.QPushButton(self.frame_20, clicked = lambda: self.openWindow())
        self.pushButton_195.setGeometry(QtCore.QRect(310, 0, 55, 55))
        self.pushButton_195.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_195.setMaximumSize(QtCore.QSize(55, 55))
        self.pushButton_195.setStyleSheet("\n"
"QPushButton:checked {\n"
"background-color: #af55ff;\n"
"color: white;\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: rgb(51,51,51);\n"
"  border-radius: 15px;\n"
"  border-style: none;\n"
"  color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  /* Change the background color when the button is hovered over */\n"
"  color: rgb(197, 197, 197)\n"
"}")
        self.pushButton_195.setCheckable(True)
        self.pushButton_195.setObjectName("pushButton_195")
        self.buttonGroup.addButton(self.pushButton_195)
        self.pushButton_196 = QtWidgets.QPushButton(self.frame_20, clicked = lambda: self.openWindow())
        self.pushButton_196.setGeometry(QtCore.QRect(550, 0, 55, 55))
        self.pushButton_196.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_196.setMaximumSize(QtCore.QSize(55, 55))
        self.pushButton_196.setStyleSheet("\n"
"QPushButton:checked {\n"
"background-color: #af55ff;\n"
"color: white;\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: rgb(51,51,51);\n"
"  border-radius: 15px;\n"
"  border-style: none;\n"
"  color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  /* Change the background color when the button is hovered over */\n"
"  color: rgb(197, 197, 197)\n"
"}")
        self.pushButton_196.setCheckable(True)
        self.pushButton_196.setObjectName("pushButton_196")
        self.buttonGroup.addButton(self.pushButton_196)
        self.pushButton_197 = QtWidgets.QPushButton(self.frame_20, clicked = lambda: self.openWindow())
        self.pushButton_197.setGeometry(QtCore.QRect(430, 0, 55, 55))
        self.pushButton_197.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_197.setMaximumSize(QtCore.QSize(55, 55))
        self.pushButton_197.setStyleSheet("\n"
"QPushButton:checked {\n"
"background-color: #af55ff;\n"
"color: white;\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: rgb(51,51,51);\n"
"  border-radius: 15px;\n"
"  border-style: none;\n"
"  color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  /* Change the background color when the button is hovered over */\n"
"  color: rgb(197, 197, 197)\n"
"}")
        self.pushButton_197.setCheckable(True)
        self.pushButton_197.setObjectName("pushButton_197")
        self.buttonGroup.addButton(self.pushButton_197)
        self.pushButton_198 = QtWidgets.QPushButton(self.frame_20, clicked = lambda: self.openWindow())
        self.pushButton_198.setGeometry(QtCore.QRect(730, 0, 55, 55))
        self.pushButton_198.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_198.setMaximumSize(QtCore.QSize(55, 55))
        self.pushButton_198.setStyleSheet("\n"
"QPushButton:checked {\n"
"background-color: #af55ff;\n"
"color: white;\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: rgb(51,51,51);\n"
"  border-radius: 15px;\n"
"  border-style: none;\n"
"  color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  /* Change the background color when the button is hovered over */\n"
"  color: rgb(197, 197, 197)\n"
"}")
        self.pushButton_198.setCheckable(True)
        self.pushButton_198.setObjectName("pushButton_198")
        self.buttonGroup.addButton(self.pushButton_198)
        self.pushButton_199 = QtWidgets.QPushButton(self.frame_20, clicked = lambda: self.openWindow())
        self.pushButton_199.setGeometry(QtCore.QRect(370, 0, 55, 55))
        self.pushButton_199.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_199.setMaximumSize(QtCore.QSize(55, 55))
        self.pushButton_199.setStyleSheet("\n"
"QPushButton:checked {\n"
"background-color: #af55ff;\n"
"color: white;\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: rgb(51,51,51);\n"
"  border-radius: 15px;\n"
"  border-style: none;\n"
"  color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  /* Change the background color when the button is hovered over */\n"
"  color: rgb(197, 197, 197)\n"
"}")
        self.pushButton_199.setCheckable(True)
        self.pushButton_199.setObjectName("pushButton_199")
        self.buttonGroup.addButton(self.pushButton_199)
        self.pushButton_200 = QtWidgets.QPushButton(self.frame_20, clicked = lambda: self.openWindow())
        self.pushButton_200.setGeometry(QtCore.QRect(130, 0, 55, 55))
        self.pushButton_200.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_200.setMaximumSize(QtCore.QSize(55, 55))
        self.pushButton_200.setStyleSheet("\n"
"QPushButton:checked {\n"
"background-color: #af55ff;\n"
"color: white;\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: rgb(51,51,51);\n"
"  border-radius: 15px;\n"
"  border-style: none;\n"
"  color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  /* Change the background color when the button is hovered over */\n"
"  color: rgb(197, 197, 197)\n"
"}")
        self.pushButton_200.setCheckable(True)
        self.pushButton_200.setObjectName("pushButton_200")
        self.buttonGroup.addButton(self.pushButton_200)
        self.pushButton_201 = QtWidgets.QPushButton(self.frame_20, clicked = lambda: self.openWindow())
        self.pushButton_201.setGeometry(QtCore.QRect(790, 0, 105, 55))
        self.pushButton_201.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_201.setMaximumSize(QtCore.QSize(105, 55))
        self.pushButton_201.setStyleSheet("\n"
"QPushButton:checked {\n"
"background-color: #af55ff;\n"
"color: white;\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: rgb(51,51,51);\n"
"  border-radius: 15px;\n"
"  border-style: none;\n"
"  color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  /* Change the background color when the button is hovered over */\n"
"  color: rgb(197, 197, 197)\n"
"}")
        self.pushButton_201.setCheckable(True)
        self.pushButton_201.setObjectName("pushButton_201")
        self.buttonGroup.addButton(self.pushButton_201)
        self.pushButton_202 = QtWidgets.QPushButton(self.frame_20, clicked = lambda: self.openWindow())
        self.pushButton_202.setGeometry(QtCore.QRect(70, 0, 55, 55))
        self.pushButton_202.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_202.setMaximumSize(QtCore.QSize(55, 55))
        self.pushButton_202.setStyleSheet("\n"
"QPushButton:checked {\n"
"background-color: #af55ff;\n"
"color: white;\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: rgb(51,51,51);\n"
"  border-radius: 15px;\n"
"  border-style: none;\n"
"  color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  /* Change the background color when the button is hovered over */\n"
"  color: rgb(197, 197, 197)\n"
"}")
        self.pushButton_202.setCheckable(True)
        self.pushButton_202.setObjectName("pushButton_202")
        self.buttonGroup.addButton(self.pushButton_202)
        self.pushButton_203 = QtWidgets.QPushButton(self.frame_20, clicked = lambda: self.openWindow())
        self.pushButton_203.setGeometry(QtCore.QRect(670, 0, 55, 55))
        self.pushButton_203.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_203.setMaximumSize(QtCore.QSize(55, 55))
        self.pushButton_203.setStyleSheet("\n"
"QPushButton:checked {\n"
"background-color: #af55ff;\n"
"color: white;\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: rgb(51,51,51);\n"
"  border-radius: 15px;\n"
"  border-style: none;\n"
"  color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  /* Change the background color when the button is hovered over */\n"
"  color: rgb(197, 197, 197)\n"
"}")
        self.pushButton_203.setCheckable(True)
        self.pushButton_203.setObjectName("pushButton_203")
        self.buttonGroup.addButton(self.pushButton_203)
        self.pushButton_204 = QtWidgets.QPushButton(self.frame_20, clicked = lambda: self.openWindow())
        self.pushButton_204.setGeometry(QtCore.QRect(490, 0, 55, 55))
        self.pushButton_204.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_204.setMaximumSize(QtCore.QSize(55, 55))
        self.pushButton_204.setStyleSheet("\n"
"QPushButton:checked {\n"
"background-color: #af55ff;\n"
"color: white;\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: rgb(51,51,51);\n"
"  border-radius: 15px;\n"
"  border-style: none;\n"
"  color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  /* Change the background color when the button is hovered over */\n"
"  color: rgb(197, 197, 197)\n"
"}")
        self.pushButton_204.setCheckable(True)
        self.pushButton_204.setObjectName("pushButton_204")
        self.buttonGroup.addButton(self.pushButton_204)
        self.pushButton_205 = QtWidgets.QPushButton(self.frame_20, clicked = lambda: self.openWindow())
        self.pushButton_205.setGeometry(QtCore.QRect(190, 0, 55, 55))
        self.pushButton_205.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_205.setMaximumSize(QtCore.QSize(55, 55))
        self.pushButton_205.setStyleSheet("\n"
"QPushButton:checked {\n"
"background-color: #af55ff;\n"
"color: white;\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: rgb(51,51,51);\n"
"  border-radius: 15px;\n"
"  border-style: none;\n"
"  color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  /* Change the background color when the button is hovered over */\n"
"  color: rgb(197, 197, 197)\n"
"}")
        self.pushButton_205.setCheckable(True)
        self.pushButton_205.setObjectName("pushButton_205")
        self.buttonGroup.addButton(self.pushButton_205)
        self.pushButton_206 = QtWidgets.QPushButton(self.frame_20, clicked = lambda: self.openWindow())
        self.pushButton_206.setGeometry(QtCore.QRect(250, 0, 55, 55))
        self.pushButton_206.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_206.setMaximumSize(QtCore.QSize(55, 55))
        self.pushButton_206.setStyleSheet("\n"
"QPushButton:checked {\n"
"background-color: #af55ff;\n"
"color: white;\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: rgb(51,51,51);\n"
"  border-radius: 15px;\n"
"  border-style: none;\n"
"  color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  /* Change the background color when the button is hovered over */\n"
"  color: rgb(197, 197, 197)\n"
"}")
        self.pushButton_206.setCheckable(True)
        self.pushButton_206.setObjectName("pushButton_206")
        self.buttonGroup.addButton(self.pushButton_206)
        self.pushButton_207 = QtWidgets.QPushButton(self.frame_20, clicked = lambda: self.openWindow())
        self.pushButton_207.setGeometry(QtCore.QRect(610, 0, 55, 55))
        self.pushButton_207.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_207.setMaximumSize(QtCore.QSize(55, 55))
        self.pushButton_207.setStyleSheet("\n"
"QPushButton:checked {\n"
"background-color: #af55ff;\n"
"color: white;\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: rgb(51,51,51);\n"
"  border-radius: 15px;\n"
"  border-style: none;\n"
"  color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  /* Change the background color when the button is hovered over */\n"
"  color: rgb(197, 197, 197)\n"
"}")
        self.pushButton_207.setCheckable(True)
        self.pushButton_207.setObjectName("pushButton_207")
        self.buttonGroup.addButton(self.pushButton_207)
        self.pushButton_261 = QtWidgets.QPushButton(self.frame_20, clicked = lambda: self.openWindow())
        self.pushButton_261.setGeometry(QtCore.QRect(910, 10, 31, 31))
        self.pushButton_261.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_261.setMaximumSize(QtCore.QSize(51, 51))
        self.pushButton_261.setStyleSheet("\n"
"QPushButton:checked {\n"
"background-color: #af55ff;\n"
"color: white;\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: rgb(51,51,51);\n"
"  border-radius: 15px;\n"
"  border-style: none;\n"
"  color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  /* Change the background color when the button is hovered over */\n"
"  color: rgb(197, 197, 197)\n"
"}")
        self.pushButton_261.setText("")
        self.pushButton_261.setCheckable(True)
        self.pushButton_261.setObjectName("pushButton_261")
        self.buttonGroup.addButton(self.pushButton_261)
        self.frame_21 = QtWidgets.QFrame(self.frame_9)
        self.frame_21.setGeometry(QtCore.QRect(100, 76, 961, 59))
        self.frame_21.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_21.setObjectName("frame_21")
        self.pushButton_208 = QtWidgets.QPushButton(self.frame_21, clicked = lambda: self.openWindow())
        self.pushButton_208.setGeometry(QtCore.QRect(10, 0, 85, 55))
        self.pushButton_208.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_208.setMaximumSize(QtCore.QSize(85, 55))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_208.setFont(font)
        self.pushButton_208.setStyleSheet("\n"
"QPushButton:checked {\n"
"background-color: #af55ff;\n"
"color: white;\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: rgb(51,51,51);\n"
"  border-radius: 15px;\n"
"  border-style: none;\n"
"  color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  /* Change the background color when the button is hovered over */\n"
"  color: rgb(197, 197, 197)\n"
"}")
        self.pushButton_208.setCheckable(True)
        self.pushButton_208.setObjectName("pushButton_208")
        self.buttonGroup.addButton(self.pushButton_208)
        self.pushButton_209 = QtWidgets.QPushButton(self.frame_21, clicked = lambda: self.openWindow())
        self.pushButton_209.setGeometry(QtCore.QRect(220, 0, 55, 55))
        self.pushButton_209.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_209.setMaximumSize(QtCore.QSize(55, 55))
        self.pushButton_209.setStyleSheet("\n"
"QPushButton:checked {\n"
"background-color: #af55ff;\n"
"color: white;\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: rgb(51,51,51);\n"
"  border-radius: 15px;\n"
"  border-style: none;\n"
"  color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  /* Change the background color when the button is hovered over */\n"
"  color: rgb(197, 197, 197)\n"
"}")
        self.pushButton_209.setCheckable(True)
        self.pushButton_209.setObjectName("pushButton_209")
        self.buttonGroup.addButton(self.pushButton_209)
        self.pushButton_210 = QtWidgets.QPushButton(self.frame_21, clicked = lambda: self.openWindow())
        self.pushButton_210.setGeometry(QtCore.QRect(700, 0, 55, 55))
        self.pushButton_210.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_210.setMaximumSize(QtCore.QSize(55, 55))
        self.pushButton_210.setStyleSheet("\n"
"QPushButton:checked {\n"
"background-color: #af55ff;\n"
"color: white;\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: rgb(51,51,51);\n"
"  border-radius: 15px;\n"
"  border-style: none;\n"
"  color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  /* Change the background color when the button is hovered over */\n"
"  color: rgb(197, 197, 197)\n"
"}")
        self.pushButton_210.setCheckable(True)
        self.pushButton_210.setObjectName("pushButton_210")
        self.buttonGroup.addButton(self.pushButton_210)
        self.pushButton_211 = QtWidgets.QPushButton(self.frame_21, clicked = lambda: self.openWindow())
        self.pushButton_211.setGeometry(QtCore.QRect(580, 0, 55, 55))
        self.pushButton_211.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_211.setMaximumSize(QtCore.QSize(55, 55))
        self.pushButton_211.setStyleSheet("\n"
"QPushButton:checked {\n"
"background-color: #af55ff;\n"
"color: white;\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: rgb(51,51,51);\n"
"  border-radius: 15px;\n"
"  border-style: none;\n"
"  color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  /* Change the background color when the button is hovered over */\n"
"  color: rgb(197, 197, 197)\n"
"}")
        self.pushButton_211.setCheckable(True)
        self.pushButton_211.setObjectName("pushButton_211")
        self.buttonGroup.addButton(self.pushButton_211)
        self.pushButton_212 = QtWidgets.QPushButton(self.frame_21, clicked = lambda: self.openWindow())
        self.pushButton_212.setGeometry(QtCore.QRect(340, 0, 55, 55))
        self.pushButton_212.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_212.setMaximumSize(QtCore.QSize(55, 55))
        self.pushButton_212.setStyleSheet("\n"
"QPushButton:checked {\n"
"background-color: #af55ff;\n"
"color: white;\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: rgb(51,51,51);\n"
"  border-radius: 15px;\n"
"  border-style: none;\n"
"  color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  /* Change the background color when the button is hovered over */\n"
"  color: rgb(197, 197, 197)\n"
"}")
        self.pushButton_212.setCheckable(True)
        self.pushButton_212.setObjectName("pushButton_212")
        self.buttonGroup.addButton(self.pushButton_212)
        self.pushButton_213 = QtWidgets.QPushButton(self.frame_21, clicked = lambda: self.openWindow())
        self.pushButton_213.setGeometry(QtCore.QRect(400, 0, 55, 55))
        self.pushButton_213.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_213.setMaximumSize(QtCore.QSize(55, 55))
        self.pushButton_213.setStyleSheet("\n"
"QPushButton:checked {\n"
"background-color: #af55ff;\n"
"color: white;\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: rgb(51,51,51);\n"
"  border-radius: 15px;\n"
"  border-style: none;\n"
"  color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  /* Change the background color when the button is hovered over */\n"
"  color: rgb(197, 197, 197)\n"
"}")
        self.pushButton_213.setCheckable(True)
        self.pushButton_213.setObjectName("pushButton_213")
        self.buttonGroup.addButton(self.pushButton_213)
        self.pushButton_214 = QtWidgets.QPushButton(self.frame_21, clicked = lambda: self.openWindow())
        self.pushButton_214.setGeometry(QtCore.QRect(520, 0, 55, 55))
        self.pushButton_214.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_214.setMaximumSize(QtCore.QSize(55, 55))
        self.pushButton_214.setStyleSheet("\n"
"QPushButton:checked {\n"
"background-color: #af55ff;\n"
"color: white;\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: rgb(51,51,51);\n"
"  border-radius: 15px;\n"
"  border-style: none;\n"
"  color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  /* Change the background color when the button is hovered over */\n"
"  color: rgb(197, 197, 197)\n"
"}")
        self.pushButton_214.setCheckable(True)
        self.pushButton_214.setObjectName("pushButton_214")
        self.buttonGroup.addButton(self.pushButton_214)
        self.pushButton_215 = QtWidgets.QPushButton(self.frame_21, clicked = lambda: self.openWindow())
        self.pushButton_215.setGeometry(QtCore.QRect(160, 0, 55, 55))
        self.pushButton_215.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_215.setMaximumSize(QtCore.QSize(55, 55))
        self.pushButton_215.setStyleSheet("\n"
"QPushButton:checked {\n"
"background-color: #af55ff;\n"
"color: white;\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: rgb(51,51,51);\n"
"  border-radius: 15px;\n"
"  border-style: none;\n"
"  color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  /* Change the background color when the button is hovered over */\n"
"  color: rgb(197, 197, 197)\n"
"}")
        self.pushButton_215.setCheckable(True)
        self.pushButton_215.setObjectName("pushButton_215")
        self.buttonGroup.addButton(self.pushButton_215)
        self.pushButton_216 = QtWidgets.QPushButton(self.frame_21, clicked = lambda: self.openWindow())
        self.pushButton_216.setGeometry(QtCore.QRect(640, 0, 55, 55))
        self.pushButton_216.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_216.setMaximumSize(QtCore.QSize(55, 55))
        self.pushButton_216.setStyleSheet("\n"
"QPushButton:checked {\n"
"background-color: #af55ff;\n"
"color: white;\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: rgb(51,51,51);\n"
"  border-radius: 15px;\n"
"  border-style: none;\n"
"  color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  /* Change the background color when the button is hovered over */\n"
"  color: rgb(197, 197, 197)\n"
"}")
        self.pushButton_216.setCheckable(True)
        self.pushButton_216.setObjectName("pushButton_216")
        self.buttonGroup.addButton(self.pushButton_216)
        self.pushButton_217 = QtWidgets.QPushButton(self.frame_21, clicked = lambda: self.openWindow())
        self.pushButton_217.setGeometry(QtCore.QRect(100, 0, 55, 55))
        self.pushButton_217.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_217.setMaximumSize(QtCore.QSize(55, 55))
        self.pushButton_217.setStyleSheet("\n"
"QPushButton:checked {\n"
"background-color: #af55ff;\n"
"color: white;\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: rgb(51,51,51);\n"
"  border-radius: 15px;\n"
"  border-style: none;\n"
"  color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  /* Change the background color when the button is hovered over */\n"
"  color: rgb(197, 197, 197)\n"
"}")
        self.pushButton_217.setCheckable(True)
        self.pushButton_217.setObjectName("pushButton_217")
        self.buttonGroup.addButton(self.pushButton_217)
        self.pushButton_218 = QtWidgets.QPushButton(self.frame_21, clicked = lambda: self.openWindow())
        self.pushButton_218.setGeometry(QtCore.QRect(820, 0, 75, 55))
        self.pushButton_218.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_218.setMaximumSize(QtCore.QSize(105, 55))
        self.pushButton_218.setStyleSheet("\n"
"QPushButton:checked {\n"
"background-color: #af55ff;\n"
"color: white;\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: rgb(51,51,51);\n"
"  border-radius: 15px;\n"
"  border-style: none;\n"
"  color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  /* Change the background color when the button is hovered over */\n"
"  color: rgb(197, 197, 197)\n"
"}")
        self.pushButton_218.setCheckable(True)
        self.pushButton_218.setObjectName("pushButton_218")
        self.buttonGroup.addButton(self.pushButton_218)
        self.pushButton_219 = QtWidgets.QPushButton(self.frame_21, clicked = lambda: self.openWindow())
        self.pushButton_219.setGeometry(QtCore.QRect(760, 0, 55, 55))
        self.pushButton_219.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_219.setMaximumSize(QtCore.QSize(55, 55))
        self.pushButton_219.setStyleSheet("\n"
"QPushButton:checked {\n"
"background-color: #af55ff;\n"
"color: white;\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: rgb(51,51,51);\n"
"  border-radius: 15px;\n"
"  border-style: none;\n"
"  color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  /* Change the background color when the button is hovered over */\n"
"  color: rgb(197, 197, 197)\n"
"}")
        self.pushButton_219.setCheckable(True)
        self.pushButton_219.setObjectName("pushButton_219")
        self.buttonGroup.addButton(self.pushButton_219)
        self.pushButton_220 = QtWidgets.QPushButton(self.frame_21, clicked = lambda: self.openWindow())
        self.pushButton_220.setGeometry(QtCore.QRect(460, 0, 55, 55))
        self.pushButton_220.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_220.setMaximumSize(QtCore.QSize(55, 55))
        self.pushButton_220.setStyleSheet("\n"
"QPushButton:checked {\n"
"background-color: #af55ff;\n"
"color: white;\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: rgb(51,51,51);\n"
"  border-radius: 15px;\n"
"  border-style: none;\n"
"  color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  /* Change the background color when the button is hovered over */\n"
"  color: rgb(197, 197, 197)\n"
"}")
        self.pushButton_220.setCheckable(True)
        self.pushButton_220.setObjectName("pushButton_220")
        self.buttonGroup.addButton(self.pushButton_220)
        self.pushButton_221 = QtWidgets.QPushButton(self.frame_21, clicked = lambda: self.openWindow())
        self.pushButton_221.setGeometry(QtCore.QRect(280, 0, 55, 55))
        self.pushButton_221.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_221.setMaximumSize(QtCore.QSize(55, 55))
        self.pushButton_221.setStyleSheet("\n"
"QPushButton:checked {\n"
"background-color: #af55ff;\n"
"color: white;\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: rgb(51,51,51);\n"
"  border-radius: 15px;\n"
"  border-style: none;\n"
"  color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  /* Change the background color when the button is hovered over */\n"
"  color: rgb(197, 197, 197)\n"
"}")
        self.pushButton_221.setCheckable(True)
        self.pushButton_221.setObjectName("pushButton_221")
        self.buttonGroup.addButton(self.pushButton_221)
        self.pushButton_260 = QtWidgets.QPushButton(self.frame_21, clicked = lambda: self.openWindow())
        self.pushButton_260.setGeometry(QtCore.QRect(900, 0, 55, 55))
        self.pushButton_260.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_260.setMaximumSize(QtCore.QSize(55, 55))
        self.pushButton_260.setStyleSheet("\n"
"QPushButton:checked {\n"
"background-color: #af55ff;\n"
"color: white;\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: rgb(51,51,51);\n"
"  border-radius: 15px;\n"
"  border-style: none;\n"
"  color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  /* Change the background color when the button is hovered over */\n"
"  color: rgb(197, 197, 197)\n"
"}")
        self.pushButton_260.setCheckable(True)
        self.pushButton_260.setObjectName("pushButton_260")
        self.buttonGroup.addButton(self.pushButton_260)
        self.frame_22 = QtWidgets.QFrame(self.frame_9)
        self.frame_22.setGeometry(QtCore.QRect(100, 141, 961, 59))
        self.frame_22.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_22.setObjectName("frame_22")
        self.pushButton_222 = QtWidgets.QPushButton(self.frame_22, clicked = lambda: self.openWindow())
        self.pushButton_222.setGeometry(QtCore.QRect(10, 0, 95, 55))
        self.pushButton_222.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_222.setMaximumSize(QtCore.QSize(95, 55))
        self.pushButton_222.setStyleSheet("\n"
"QPushButton:checked {\n"
"background-color: #af55ff;\n"
"color: white;\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: rgb(51,51,51);\n"
"  border-radius: 15px;\n"
"  border-style: none;\n"
"  color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  /* Change the background color when the button is hovered over */\n"
"  color: rgb(197, 197, 197)\n"
"}")
        self.pushButton_222.setCheckable(True)
        self.pushButton_222.setObjectName("pushButton_222")
        self.buttonGroup.addButton(self.pushButton_222)
        self.pushButton_223 = QtWidgets.QPushButton(self.frame_22, clicked = lambda: self.openWindow())
        self.pushButton_223.setGeometry(QtCore.QRect(230, 0, 55, 55))
        self.pushButton_223.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_223.setMaximumSize(QtCore.QSize(55, 55))
        self.pushButton_223.setStyleSheet("\n"
"QPushButton:checked {\n"
"background-color: #af55ff;\n"
"color: white;\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: rgb(51,51,51);\n"
"  border-radius: 15px;\n"
"  border-style: none;\n"
"  color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  /* Change the background color when the button is hovered over */\n"
"  color: rgb(197, 197, 197)\n"
"}")
        self.pushButton_223.setCheckable(True)
        self.pushButton_223.setObjectName("pushButton_223")
        self.buttonGroup.addButton(self.pushButton_223)
        self.pushButton_224 = QtWidgets.QPushButton(self.frame_22, clicked = lambda: self.openWindow())
        self.pushButton_224.setGeometry(QtCore.QRect(410, 0, 55, 55))
        self.pushButton_224.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_224.setMaximumSize(QtCore.QSize(55, 55))
        self.pushButton_224.setStyleSheet("\n"
"QPushButton:checked {\n"
"background-color: #af55ff;\n"
"color: white;\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: rgb(51,51,51);\n"
"  border-radius: 15px;\n"
"  border-style: none;\n"
"  color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  /* Change the background color when the button is hovered over */\n"
"  color: rgb(197, 197, 197)\n"
"}")
        self.pushButton_224.setCheckable(True)
        self.pushButton_224.setObjectName("pushButton_224")
        self.buttonGroup.addButton(self.pushButton_224)
        self.pushButton_225 = QtWidgets.QPushButton(self.frame_22, clicked = lambda: self.openWindow())
        self.pushButton_225.setGeometry(QtCore.QRect(770, 0, 125, 55))
        self.pushButton_225.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_225.setMaximumSize(QtCore.QSize(380, 55))
        self.pushButton_225.setStyleSheet("\n"
"QPushButton:checked {\n"
"background-color: #af55ff;\n"
"color: white;\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: rgb(51,51,51);\n"
"  border-radius: 15px;\n"
"  border-style: none;\n"
"  color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  /* Change the background color when the button is hovered over */\n"
"  color: rgb(197, 197, 197)\n"
"}")
        self.pushButton_225.setCheckable(True)
        self.pushButton_225.setObjectName("pushButton_225")
        self.buttonGroup.addButton(self.pushButton_225)
        self.pushButton_226 = QtWidgets.QPushButton(self.frame_22, clicked = lambda: self.openWindow())
        self.pushButton_226.setGeometry(QtCore.QRect(710, 0, 55, 55))
        self.pushButton_226.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_226.setMaximumSize(QtCore.QSize(55, 55))
        self.pushButton_226.setStyleSheet("\n"
"QPushButton:checked {\n"
"background-color: #af55ff;\n"
"color: white;\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: rgb(51,51,51);\n"
"  border-radius: 15px;\n"
"  border-style: none;\n"
"  color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  /* Change the background color when the button is hovered over */\n"
"  color: rgb(197, 197, 197)\n"
"}")
        self.pushButton_226.setCheckable(True)
        self.pushButton_226.setObjectName("pushButton_226")
        self.buttonGroup.addButton(self.pushButton_226)
        self.pushButton_227 = QtWidgets.QPushButton(self.frame_22, clicked = lambda: self.openWindow())
        self.pushButton_227.setGeometry(QtCore.QRect(590, 0, 55, 55))
        self.pushButton_227.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_227.setMaximumSize(QtCore.QSize(55, 55))
        self.pushButton_227.setStyleSheet("\n"
"QPushButton:checked {\n"
"background-color: #af55ff;\n"
"color: white;\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: rgb(51,51,51);\n"
"  border-radius: 15px;\n"
"  border-style: none;\n"
"  color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  /* Change the background color when the button is hovered over */\n"
"  color: rgb(197, 197, 197)\n"
"}")
        self.pushButton_227.setCheckable(True)
        self.pushButton_227.setObjectName("pushButton_227")
        self.buttonGroup.addButton(self.pushButton_227)
        self.pushButton_228 = QtWidgets.QPushButton(self.frame_22, clicked = lambda: self.openWindow())
        self.pushButton_228.setGeometry(QtCore.QRect(530, 0, 55, 55))
        self.pushButton_228.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_228.setMaximumSize(QtCore.QSize(55, 55))
        self.pushButton_228.setStyleSheet("\n"
"QPushButton:checked {\n"
"background-color: #af55ff;\n"
"color: white;\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: rgb(51,51,51);\n"
"  border-radius: 15px;\n"
"  border-style: none;\n"
"  color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  /* Change the background color when the button is hovered over */\n"
"  color: rgb(197, 197, 197)\n"
"}")
        self.pushButton_228.setCheckable(True)
        self.pushButton_228.setObjectName("pushButton_228")
        self.buttonGroup.addButton(self.pushButton_228)
        self.pushButton_229 = QtWidgets.QPushButton(self.frame_22, clicked = lambda: self.openWindow())
        self.pushButton_229.setGeometry(QtCore.QRect(470, 0, 55, 55))
        self.pushButton_229.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_229.setMaximumSize(QtCore.QSize(55, 55))
        self.pushButton_229.setStyleSheet("\n"
"QPushButton:checked {\n"
"background-color: #af55ff;\n"
"color: white;\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: rgb(51,51,51);\n"
"  border-radius: 15px;\n"
"  border-style: none;\n"
"  color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  /* Change the background color when the button is hovered over */\n"
"  color: rgb(197, 197, 197)\n"
"}")
        self.pushButton_229.setCheckable(True)
        self.pushButton_229.setObjectName("pushButton_229")
        self.buttonGroup.addButton(self.pushButton_229)
        self.pushButton_230 = QtWidgets.QPushButton(self.frame_22, clicked = lambda: self.openWindow())
        self.pushButton_230.setGeometry(QtCore.QRect(650, 0, 55, 55))
        self.pushButton_230.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_230.setMaximumSize(QtCore.QSize(55, 55))
        self.pushButton_230.setStyleSheet("\n"
"QPushButton:checked {\n"
"background-color: #af55ff;\n"
"color: white;\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: rgb(51,51,51);\n"
"  border-radius: 15px;\n"
"  border-style: none;\n"
"  color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  /* Change the background color when the button is hovered over */\n"
"  color: rgb(197, 197, 197)\n"
"}")
        self.pushButton_230.setCheckable(True)
        self.pushButton_230.setObjectName("pushButton_230")
        self.buttonGroup.addButton(self.pushButton_230)
        self.pushButton_231 = QtWidgets.QPushButton(self.frame_22, clicked = lambda: self.openWindow())
        self.pushButton_231.setGeometry(QtCore.QRect(110, 0, 55, 55))
        self.pushButton_231.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_231.setMaximumSize(QtCore.QSize(55, 55))
        self.pushButton_231.setStyleSheet("\n"
"QPushButton:checked {\n"
"background-color: #af55ff;\n"
"color: white;\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: rgb(51,51,51);\n"
"  border-radius: 15px;\n"
"  border-style: none;\n"
"  color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  /* Change the background color when the button is hovered over */\n"
"  color: rgb(197, 197, 197)\n"
"}")
        self.pushButton_231.setCheckable(True)
        self.pushButton_231.setObjectName("pushButton_231")
        self.buttonGroup.addButton(self.pushButton_231)
        self.pushButton_232 = QtWidgets.QPushButton(self.frame_22, clicked = lambda: self.openWindow())
        self.pushButton_232.setGeometry(QtCore.QRect(290, 0, 55, 55))
        self.pushButton_232.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_232.setMaximumSize(QtCore.QSize(55, 55))
        self.pushButton_232.setStyleSheet("\n"
"QPushButton:checked {\n"
"background-color: #af55ff;\n"
"color: white;\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: rgb(51,51,51);\n"
"  border-radius: 15px;\n"
"  border-style: none;\n"
"  color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  /* Change the background color when the button is hovered over */\n"
"  color: rgb(197, 197, 197)\n"
"}")
        self.pushButton_232.setCheckable(True)
        self.pushButton_232.setObjectName("pushButton_232")
        self.buttonGroup.addButton(self.pushButton_232)
        self.pushButton_233 = QtWidgets.QPushButton(self.frame_22, clicked = lambda: self.openWindow())
        self.pushButton_233.setGeometry(QtCore.QRect(350, 0, 55, 55))
        self.pushButton_233.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_233.setMaximumSize(QtCore.QSize(55, 55))
        self.pushButton_233.setStyleSheet("\n"
"QPushButton:checked {\n"
"background-color: #af55ff;\n"
"color: white;\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: rgb(51,51,51);\n"
"  border-radius: 15px;\n"
"  border-style: none;\n"
"  color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  /* Change the background color when the button is hovered over */\n"
"  color: rgb(197, 197, 197)\n"
"}")
        self.pushButton_233.setCheckable(True)
        self.pushButton_233.setObjectName("pushButton_233")
        self.buttonGroup.addButton(self.pushButton_233)
        self.pushButton_234 = QtWidgets.QPushButton(self.frame_22, clicked = lambda: self.openWindow())
        self.pushButton_234.setGeometry(QtCore.QRect(170, 0, 55, 55))
        self.pushButton_234.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_234.setMaximumSize(QtCore.QSize(55, 55))
        self.pushButton_234.setStyleSheet("\n"
"QPushButton:checked {\n"
"background-color: #af55ff;\n"
"color: white;\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: rgb(51,51,51);\n"
"  border-radius: 15px;\n"
"  border-style: none;\n"
"  color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  /* Change the background color when the button is hovered over */\n"
"  color: rgb(197, 197, 197)\n"
"}")
        self.pushButton_234.setCheckable(True)
        self.pushButton_234.setObjectName("pushButton_234")
        self.buttonGroup.addButton(self.pushButton_234)
        self.pushButton_259 = QtWidgets.QPushButton(self.frame_22, clicked = lambda: self.openWindow())
        self.pushButton_259.setGeometry(QtCore.QRect(900, 0, 55, 55))
        self.pushButton_259.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_259.setMaximumSize(QtCore.QSize(55, 55))
        self.pushButton_259.setStyleSheet("\n"
"QPushButton:checked {\n"
"background-color: #af55ff;\n"
"color: white;\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: rgb(51,51,51);\n"
"  border-radius: 15px;\n"
"  border-style: none;\n"
"  color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  /* Change the background color when the button is hovered over */\n"
"  color: rgb(197, 197, 197)\n"
"}")
        self.pushButton_259.setCheckable(True)
        self.pushButton_259.setObjectName("pushButton_259")
        self.buttonGroup.addButton(self.pushButton_259)
        self.frame_23 = QtWidgets.QFrame(self.frame_9)
        self.frame_23.setGeometry(QtCore.QRect(100, 206, 961, 59))
        self.frame_23.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_23.setObjectName("frame_23")
        self.pushButton_235 = QtWidgets.QPushButton(self.frame_23, clicked = lambda: self.openWindow())
        self.pushButton_235.setGeometry(QtCore.QRect(10, 0, 115, 55))
        self.pushButton_235.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_235.setMaximumSize(QtCore.QSize(118, 55))
        self.pushButton_235.setStyleSheet("\n"
"QPushButton:checked {\n"
"background-color: #af55ff;\n"
"color: white;\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: rgb(51,51,51);\n"
"  border-radius: 15px;\n"
"  border-style: none;\n"
"  color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  /* Change the background color when the button is hovered over */\n"
"  color: rgb(197, 197, 197)\n"
"}")
        self.pushButton_235.setCheckable(True)
        self.pushButton_235.setAutoDefault(False)
        self.pushButton_235.setObjectName("pushButton_235")
        self.buttonGroup.addButton(self.pushButton_235)
        self.pushButton_236 = QtWidgets.QPushButton(self.frame_23, clicked = lambda: self.openWindow())
        self.pushButton_236.setGeometry(QtCore.QRect(490, 0, 55, 55))
        self.pushButton_236.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_236.setMaximumSize(QtCore.QSize(55, 55))
        self.pushButton_236.setStyleSheet("\n"
"QPushButton:checked {\n"
"background-color: #af55ff;\n"
"color: white;\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: rgb(51,51,51);\n"
"  border-radius: 15px;\n"
"  border-style: none;\n"
"  color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  /* Change the background color when the button is hovered over */\n"
"  color: rgb(197, 197, 197)\n"
"}")
        self.pushButton_236.setCheckable(True)
        self.pushButton_236.setObjectName("pushButton_236")
        self.buttonGroup.addButton(self.pushButton_236)
        self.pushButton_237 = QtWidgets.QPushButton(self.frame_23, clicked = lambda: self.openWindow())
        self.pushButton_237.setGeometry(QtCore.QRect(430, 0, 55, 55))
        self.pushButton_237.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_237.setMaximumSize(QtCore.QSize(55, 55))
        self.pushButton_237.setStyleSheet("\n"
"QPushButton:checked {\n"
"background-color: #af55ff;\n"
"color: white;\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: rgb(51,51,51);\n"
"  border-radius: 15px;\n"
"  border-style: none;\n"
"  color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  /* Change the background color when the button is hovered over */\n"
"  color: rgb(197, 197, 197)\n"
"}")
        self.pushButton_237.setCheckable(True)
        self.pushButton_237.setObjectName("pushButton_237")
        self.buttonGroup.addButton(self.pushButton_237)
        self.pushButton_238 = QtWidgets.QPushButton(self.frame_23, clicked = lambda: self.openWindow())
        self.pushButton_238.setGeometry(QtCore.QRect(610, 0, 55, 55))
        self.pushButton_238.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_238.setMaximumSize(QtCore.QSize(55, 55))
        self.pushButton_238.setStyleSheet("\n"
"QPushButton:checked {\n"
"background-color: #af55ff;\n"
"color: white;\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: rgb(51,51,51);\n"
"  border-radius: 15px;\n"
"  border-style: none;\n"
"  color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  /* Change the background color when the button is hovered over */\n"
"  color: rgb(197, 197, 197)\n"
"}")
        self.pushButton_238.setCheckable(True)
        self.pushButton_238.setObjectName("pushButton_238")
        self.buttonGroup.addButton(self.pushButton_238)
        self.pushButton_239 = QtWidgets.QPushButton(self.frame_23, clicked = lambda: self.openWindow())
        self.pushButton_239.setGeometry(QtCore.QRect(250, 0, 55, 55))
        self.pushButton_239.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_239.setMaximumSize(QtCore.QSize(55, 55))
        self.pushButton_239.setStyleSheet("\n"
"QPushButton:checked {\n"
"background-color: #af55ff;\n"
"color: white;\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: rgb(51,51,51);\n"
"  border-radius: 15px;\n"
"  border-style: none;\n"
"  color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  /* Change the background color when the button is hovered over */\n"
"  color: rgb(197, 197, 197)\n"
"}")
        self.pushButton_239.setCheckable(True)
        self.pushButton_239.setObjectName("pushButton_239")
        self.buttonGroup.addButton(self.pushButton_239)
        self.pushButton_240 = QtWidgets.QPushButton(self.frame_23, clicked = lambda: self.openWindow())
        self.pushButton_240.setGeometry(QtCore.QRect(840, 0, 55, 55))
        self.pushButton_240.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_240.setMaximumSize(QtCore.QSize(55, 55))
        self.pushButton_240.setStyleSheet("\n"
"QPushButton:checked {\n"
"background-color: #af55ff;\n"
"color: white;\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: rgb(51,51,51);\n"
"  border-radius: 15px;\n"
"  border-style: none;\n"
"  color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  /* Change the background color when the button is hovered over */\n"
"  color: rgb(197, 197, 197)\n"
"}")
        self.pushButton_240.setCheckable(True)
        self.pushButton_240.setObjectName("pushButton_240")
        self.buttonGroup.addButton(self.pushButton_240)
        self.pushButton_241 = QtWidgets.QPushButton(self.frame_23, clicked = lambda: self.openWindow())
        self.pushButton_241.setGeometry(QtCore.QRect(550, 0, 55, 55))
        self.pushButton_241.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_241.setMaximumSize(QtCore.QSize(55, 55))
        self.pushButton_241.setStyleSheet("\n"
"QPushButton:checked {\n"
"background-color: #af55ff;\n"
"color: white;\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: rgb(51,51,51);\n"
"  border-radius: 15px;\n"
"  border-style: none;\n"
"  color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  /* Change the background color when the button is hovered over */\n"
"  color: rgb(197, 197, 197)\n"
"}")
        self.pushButton_241.setCheckable(True)
        self.pushButton_241.setObjectName("pushButton_241")
        self.buttonGroup.addButton(self.pushButton_241)
        self.pushButton_242 = QtWidgets.QPushButton(self.frame_23, clicked = lambda: self.openWindow())
        self.pushButton_242.setGeometry(QtCore.QRect(190, 0, 55, 55))
        self.pushButton_242.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_242.setMaximumSize(QtCore.QSize(55, 55))
        self.pushButton_242.setStyleSheet("\n"
"QPushButton:checked {\n"
"background-color: #af55ff;\n"
"color: white;\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: rgb(51,51,51);\n"
"  border-radius: 15px;\n"
"  border-style: none;\n"
"  color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  /* Change the background color when the button is hovered over */\n"
"  color: rgb(197, 197, 197)\n"
"}")
        self.pushButton_242.setCheckable(True)
        self.pushButton_242.setObjectName("pushButton_242")
        self.buttonGroup.addButton(self.pushButton_242)
        self.pushButton_243 = QtWidgets.QPushButton(self.frame_23, clicked = lambda: self.openWindow())
        self.pushButton_243.setGeometry(QtCore.QRect(130, 0, 55, 55))
        self.pushButton_243.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_243.setMaximumSize(QtCore.QSize(55, 55))
        self.pushButton_243.setStyleSheet("\n"
"QPushButton:checked {\n"
"background-color: #af55ff;\n"
"color: white;\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: rgb(51,51,51);\n"
"  border-radius: 15px;\n"
"  border-style: none;\n"
"  color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  /* Change the background color when the button is hovered over */\n"
"  color: rgb(197, 197, 197)\n"
"}")
        self.pushButton_243.setCheckable(True)
        self.pushButton_243.setObjectName("pushButton_243")
        self.buttonGroup.addButton(self.pushButton_243)
        self.pushButton_244 = QtWidgets.QPushButton(self.frame_23, clicked = lambda: self.openWindow())
        self.pushButton_244.setGeometry(QtCore.QRect(370, 0, 55, 55))
        self.pushButton_244.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_244.setMaximumSize(QtCore.QSize(55, 55))
        self.pushButton_244.setStyleSheet("\n"
"QPushButton:checked {\n"
"background-color: #af55ff;\n"
"color: white;\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: rgb(51,51,51);\n"
"  border-radius: 15px;\n"
"  border-style: none;\n"
"  color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  /* Change the background color when the button is hovered over */\n"
"  color: rgb(197, 197, 197)\n"
"}")
        self.pushButton_244.setCheckable(True)
        self.pushButton_244.setObjectName("pushButton_244")
        self.buttonGroup.addButton(self.pushButton_244)
        self.pushButton_245 = QtWidgets.QPushButton(self.frame_23, clicked = lambda: self.openWindow())
        self.pushButton_245.setGeometry(QtCore.QRect(730, 0, 105, 55))
        self.pushButton_245.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_245.setMaximumSize(QtCore.QSize(380, 55))
        self.pushButton_245.setStyleSheet("\n"
"QPushButton:checked {\n"
"background-color: #af55ff;\n"
"color: white;\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: rgb(51,51,51);\n"
"  border-radius: 15px;\n"
"  border-style: none;\n"
"  color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  /* Change the background color when the button is hovered over */\n"
"  color: rgb(197, 197, 197)\n"
"}")
        self.pushButton_245.setCheckable(True)
        self.pushButton_245.setObjectName("pushButton_245")
        self.buttonGroup.addButton(self.pushButton_245)
        self.pushButton_246 = QtWidgets.QPushButton(self.frame_23, clicked = lambda: self.openWindow())
        self.pushButton_246.setGeometry(QtCore.QRect(670, 0, 55, 55))
        self.pushButton_246.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_246.setMaximumSize(QtCore.QSize(55, 55))
        self.pushButton_246.setStyleSheet("\n"
"QPushButton:checked {\n"
"background-color: #af55ff;\n"
"color: white;\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: rgb(51,51,51);\n"
"  border-radius: 15px;\n"
"  border-style: none;\n"
"  color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  /* Change the background color when the button is hovered over */\n"
"  color: rgb(197, 197, 197)\n"
"}")
        self.pushButton_246.setCheckable(True)
        self.pushButton_246.setObjectName("pushButton_246")
        self.buttonGroup.addButton(self.pushButton_246)
        self.pushButton_247 = QtWidgets.QPushButton(self.frame_23, clicked = lambda: self.openWindow())
        self.pushButton_247.setGeometry(QtCore.QRect(310, 0, 55, 55))
        self.pushButton_247.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_247.setMaximumSize(QtCore.QSize(55, 55))
        self.pushButton_247.setStyleSheet("\n"
"QPushButton:checked {\n"
"background-color: #af55ff;\n"
"color: white;\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: rgb(51,51,51);\n"
"  border-radius: 15px;\n"
"  border-style: none;\n"
"  color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  /* Change the background color when the button is hovered over */\n"
"  color: rgb(197, 197, 197)\n"
"}")
        self.pushButton_247.setCheckable(True)
        self.pushButton_247.setObjectName("pushButton_247")
        self.buttonGroup.addButton(self.pushButton_247)
        self.pushButton_258 = QtWidgets.QPushButton(self.frame_23, clicked = lambda: self.openWindow())
        self.pushButton_258.setGeometry(QtCore.QRect(900, 0, 55, 55))
        self.pushButton_258.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_258.setMaximumSize(QtCore.QSize(55, 55))
        self.pushButton_258.setStyleSheet("\n"
"QPushButton:checked {\n"
"background-color: #af55ff;\n"
"color: white;\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: rgb(51,51,51);\n"
"  border-radius: 15px;\n"
"  border-style: none;\n"
"  color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  /* Change the background color when the button is hovered over */\n"
"  color: rgb(197, 197, 197)\n"
"}")
        self.pushButton_258.setCheckable(True)
        self.pushButton_258.setObjectName("pushButton_258")
        self.buttonGroup.addButton(self.pushButton_258)
        self.frame_24 = QtWidgets.QFrame(self.frame_9)
        self.frame_24.setGeometry(QtCore.QRect(100, 271, 961, 59))
        self.frame_24.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_24.setObjectName("frame_24")
        self.pushButton_248 = QtWidgets.QPushButton(self.frame_24, clicked = lambda: self.openWindow())
        self.pushButton_248.setGeometry(QtCore.QRect(10, 0, 64, 55))
        self.pushButton_248.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_248.setMaximumSize(QtCore.QSize(64, 55))
        self.pushButton_248.setStyleSheet("\n"
"QPushButton:checked {\n"
"background-color: #af55ff;\n"
"color: white;\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: rgb(51,51,51);\n"
"  border-radius: 15px;\n"
"  border-style: none;\n"
"  color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  /* Change the background color when the button is hovered over */\n"
"  color: rgb(197, 197, 197)\n"
"}")
        self.pushButton_248.setCheckable(True)
        self.pushButton_248.setAutoRepeatDelay(296)
        self.pushButton_248.setObjectName("pushButton_248")
        self.buttonGroup.addButton(self.pushButton_248)
        self.pushButton_249 = QtWidgets.QPushButton(self.frame_24, clicked = lambda: self.openWindow())
        self.pushButton_249.setGeometry(QtCore.QRect(80, 0, 64, 55))
        self.pushButton_249.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_249.setMaximumSize(QtCore.QSize(64, 55))
        self.pushButton_249.setStyleSheet("\n"
"QPushButton:checked {\n"
"background-color: #af55ff;\n"
"color: white;\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: rgb(51,51,51);\n"
"  border-radius: 15px;\n"
"  border-style: none;\n"
"  color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  /* Change the background color when the button is hovered over */\n"
"  color: rgb(197, 197, 197)\n"
"}")
        self.pushButton_249.setCheckable(True)
        self.pushButton_249.setObjectName("pushButton_249")
        self.buttonGroup.addButton(self.pushButton_249)
        self.pushButton_250 = QtWidgets.QPushButton(self.frame_24, clicked = lambda: self.openWindow())
        self.pushButton_250.setGeometry(QtCore.QRect(220, 0, 374, 55))
        self.pushButton_250.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_250.setMaximumSize(QtCore.QSize(380, 55))
        self.pushButton_250.setStyleSheet("\n"
"QPushButton:checked {\n"
"background-color: #af55ff;\n"
"color: white;\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: rgb(51,51,51);\n"
"  border-radius: 15px;\n"
"  border-style: none;\n"
"  color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  /* Change the background color when the button is hovered over */\n"
"  color: rgb(197, 197, 197)\n"
"}")
        self.pushButton_250.setText("")
        self.pushButton_250.setCheckable(True)
        self.pushButton_250.setObjectName("pushButton_250")
        self.buttonGroup.addButton(self.pushButton_250)
        self.pushButton_251 = QtWidgets.QPushButton(self.frame_24, clicked = lambda: self.openWindow())
        self.pushButton_251.setGeometry(QtCore.QRect(840, 0, 55, 55))
        self.pushButton_251.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_251.setMaximumSize(QtCore.QSize(55, 55))
        self.pushButton_251.setStyleSheet("\n"
"QPushButton:checked {\n"
"background-color: #af55ff;\n"
"color: white;\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: rgb(51,51,51);\n"
"  border-radius: 15px;\n"
"  border-style: none;\n"
"  color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  /* Change the background color when the button is hovered over */\n"
"  color: rgb(197, 197, 197)\n"
"}")
        self.pushButton_251.setCheckable(True)
        self.pushButton_251.setObjectName("pushButton_251")
        self.buttonGroup.addButton(self.pushButton_251)
        self.pushButton_252 = QtWidgets.QPushButton(self.frame_24, clicked = lambda: self.openWindow())
        self.pushButton_252.setGeometry(QtCore.QRect(150, 0, 64, 55))
        self.pushButton_252.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_252.setMaximumSize(QtCore.QSize(64, 55))
        self.pushButton_252.setStyleSheet("\n"
"QPushButton:checked {\n"
"background-color: #af55ff;\n"
"color: white;\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: rgb(51,51,51);\n"
"  border-radius: 15px;\n"
"  border-style: none;\n"
"  color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  /* Change the background color when the button is hovered over */\n"
"  color: rgb(197, 197, 197)\n"
"}")
        self.pushButton_252.setCheckable(True)
        self.pushButton_252.setObjectName("pushButton_252")
        self.buttonGroup.addButton(self.pushButton_252)
        self.pushButton_253 = QtWidgets.QPushButton(self.frame_24, clicked = lambda: self.openWindow())
        self.pushButton_253.setGeometry(QtCore.QRect(900, 0, 55, 55))
        self.pushButton_253.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_253.setMaximumSize(QtCore.QSize(55, 55))
        self.pushButton_253.setStyleSheet("\n"
"QPushButton:checked {\n"
"background-color: #af55ff;\n"
"color: white;\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: rgb(51,51,51);\n"
"  border-radius: 15px;\n"
"  border-style: none;\n"
"  color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  /* Change the background color when the button is hovered over */\n"
"  color: rgb(197, 197, 197)\n"
"}")
        self.pushButton_253.setCheckable(True)
        self.pushButton_253.setObjectName("pushButton_253")
        self.buttonGroup.addButton(self.pushButton_253)
        self.pushButton_254 = QtWidgets.QPushButton(self.frame_24, clicked = lambda: self.openWindow())
        self.pushButton_254.setGeometry(QtCore.QRect(600, 0, 55, 55))
        self.pushButton_254.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_254.setMaximumSize(QtCore.QSize(64, 55))
        self.pushButton_254.setStyleSheet("\n"
"QPushButton:checked {\n"
"background-color: #af55ff;\n"
"color: white;\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: rgb(51,51,51);\n"
"  border-radius: 15px;\n"
"  border-style: none;\n"
"  color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  /* Change the background color when the button is hovered over */\n"
"  color: rgb(197, 197, 197)\n"
"}")
        self.pushButton_254.setCheckable(True)
        self.pushButton_254.setObjectName("pushButton_254")
        self.buttonGroup.addButton(self.pushButton_254)
        self.pushButton_255 = QtWidgets.QPushButton(self.frame_24, clicked = lambda: self.openWindow())
        self.pushButton_255.setGeometry(QtCore.QRect(780, 0, 55, 55))
        self.pushButton_255.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_255.setMaximumSize(QtCore.QSize(55, 55))
        self.pushButton_255.setStyleSheet("\n"
"QPushButton:checked {\n"
"background-color: #af55ff;\n"
"color: white;\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: rgb(51,51,51);\n"
"  border-radius: 15px;\n"
"  border-style: none;\n"
"  color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  /* Change the background color when the button is hovered over */\n"
"  color: rgb(197, 197, 197)\n"
"}")
        self.pushButton_255.setCheckable(True)
        self.pushButton_255.setObjectName("pushButton_255")
        self.buttonGroup.addButton(self.pushButton_255)
        self.pushButton_256 = QtWidgets.QPushButton(self.frame_24, clicked = lambda: self.openWindow())
        self.pushButton_256.setGeometry(QtCore.QRect(720, 0, 55, 55))
        self.pushButton_256.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_256.setMaximumSize(QtCore.QSize(64, 55))
        self.pushButton_256.setStyleSheet("\n"
"QPushButton:checked {\n"
"background-color: #af55ff;\n"
"color: white;\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: rgb(51,51,51);\n"
"  border-radius: 15px;\n"
"  border-style: none;\n"
"  color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  /* Change the background color when the button is hovered over */\n"
"  color: rgb(197, 197, 197)\n"
"}")
        self.pushButton_256.setCheckable(True)
        self.pushButton_256.setObjectName("pushButton_256")
        self.buttonGroup.addButton(self.pushButton_256)
        self.pushButton_257 = QtWidgets.QPushButton(self.frame_24, clicked = lambda: self.openWindow())
        self.pushButton_257.setGeometry(QtCore.QRect(660, 0, 55, 55))
        self.pushButton_257.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_257.setMaximumSize(QtCore.QSize(64, 55))
        self.pushButton_257.setStyleSheet("\n"
"QPushButton:checked {\n"
"background-color: #af55ff;\n"
"color: white;\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: rgb(51,51,51);\n"
"  border-radius: 15px;\n"
"  border-style: none;\n"
"  color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  /* Change the background color when the button is hovered over */\n"
"  color: rgb(197, 197, 197)\n"
"}")
        self.pushButton_257.setCheckable(True)
        self.pushButton_257.setObjectName("pushButton_257")
        self.buttonGroup.addButton(self.pushButton_257)
        self.frame = QtWidgets.QFrame(self.frame_9)
        self.frame.setGeometry(QtCore.QRect(10, 10, 90, 321))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame, clicked = lambda: self.openWindow())
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setMinimumSize(QtCore.QSize(70, 0))
        self.pushButton_2.setMaximumSize(QtCore.QSize(50, 300))
        self.pushButton_2.setStyleSheet("\n"
"QPushButton:checked {\n"
"background-color: #af55ff;\n"
"color: white;\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: #c2c2c2;\n"
"  border-radius: 15px;\n"
"  border-style: none;\n"
"  color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  /* Change the background color when the button is hovered over */\n"
"  color: rgb(197, 197, 197)\n"
"}")
        self.pushButton_2.setText("")
        self.pushButton_2.setCheckable(True)
        self.pushButton_2.setChecked(False)
        self.pushButton_2.setObjectName("pushButton_2")
        self.buttonGroup.addButton(self.pushButton_2)
        self.gridLayout_5.addWidget(self.pushButton_2, 1, 0, 1, 1)
        self.frame_5 = QtWidgets.QFrame(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setMaximumSize(QtCore.QSize(16777215, 85))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_5)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_72 = QtWidgets.QPushButton(self.frame_5, clicked = lambda: self.openWindow())
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_72.sizePolicy().hasHeightForWidth())
        self.pushButton_72.setSizePolicy(sizePolicy)
        self.pushButton_72.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_72.setStyleSheet("\n"
"QPushButton:checked {\n"
"background-color: #af55ff;\n"
"color: white;\n"
"border-radius: 9.8px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: rgb(51,51,51);\n"
"  border-radius: 9.8px;\n"
"  border-style: none;\n"
"  color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  /* Change the background color when the button is hovered over */\n"
"  color: rgb(197, 197, 197)\n"
"}")
        self.pushButton_72.setText("")
        self.pushButton_72.setCheckable(True)
        self.pushButton_72.setObjectName("pushButton_72")
        self.buttonGroup.addButton(self.pushButton_72)
        self.gridLayout.addWidget(self.pushButton_72, 0, 0, 1, 1)
        self.pushButton_71 = QtWidgets.QPushButton(self.frame_5, clicked = lambda: self.openWindow())
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_71.sizePolicy().hasHeightForWidth())
        self.pushButton_71.setSizePolicy(sizePolicy)
        self.pushButton_71.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_71.setStyleSheet("\n"
"QPushButton:checked {\n"
"background-color: #af55ff;\n"
"color: white;\n"
"border-radius: 9.8px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: rgb(51,51,51);\n"
"  border-radius: 9.8px;\n"
"  border-style: none;\n"
"  color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  /* Change the background color when the button is hovered over */\n"
"  color: rgb(197, 197, 197)\n"
"}")
        self.pushButton_71.setText("")
        self.pushButton_71.setCheckable(True)
        self.pushButton_71.setObjectName("pushButton_71")
        self.buttonGroup.addButton(self.pushButton_71)
        self.gridLayout.addWidget(self.pushButton_71, 0, 1, 1, 1)
        self.pushButton_73 = QtWidgets.QPushButton(self.frame_5, clicked = lambda: self.openWindow())
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_73.sizePolicy().hasHeightForWidth())
        self.pushButton_73.setSizePolicy(sizePolicy)
        self.pushButton_73.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_73.setStyleSheet("\n"
"QPushButton:checked {\n"
"background-color: #af55ff;\n"
"color: white;\n"
"border-radius: 9.8px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: rgb(51,51,51);\n"
"  border-radius: 9.8px;\n"
"  border-style: none;\n"
"  color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  /* Change the background color when the button is hovered over */\n"
"  color: rgb(197, 197, 197)\n"
"}")
        self.pushButton_73.setText("")
        self.pushButton_73.setCheckable(True)
        self.pushButton_73.setObjectName("pushButton_73")
        self.buttonGroup.addButton(self.pushButton_73)
        self.gridLayout.addWidget(self.pushButton_73, 1, 0, 1, 1)
        self.pushButton_74 = QtWidgets.QPushButton(self.frame_5, clicked = lambda: self.openWindow())
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_74.sizePolicy().hasHeightForWidth())
        self.pushButton_74.setSizePolicy(sizePolicy)
        self.pushButton_74.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_74.setStyleSheet("\n"
"QPushButton:checked {\n"
"background-color: #af55ff;\n"
"color: white;\n"
"border-radius: 9.8px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: rgb(51,51,51);\n"
"  border-radius: 9.8px;\n"
"  border-style: none;\n"
"  color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  /* Change the background color when the button is hovered over */\n"
"  color: rgb(197, 197, 197)\n"
"}")
        self.pushButton_74.setText("")
        self.pushButton_74.setCheckable(True)
        self.pushButton_74.setObjectName("pushButton_74")
        self.buttonGroup.addButton(self.pushButton_74)
        self.gridLayout.addWidget(self.pushButton_74, 1, 1, 1, 1)
        self.gridLayout_5.addWidget(self.frame_5, 2, 0, 1, 1)
        self.frame_2 = QtWidgets.QFrame(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.pushButton_75 = QtWidgets.QPushButton(self.frame_2, clicked = lambda: self.openWindow())
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_75.sizePolicy().hasHeightForWidth())
        self.pushButton_75.setSizePolicy(sizePolicy)
        self.pushButton_75.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_75.setStyleSheet("\n"
"QPushButton:checked {\n"
"background-color: #af55ff;\n"
"color: white;\n"
"border-radius: 9.8px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: #c2c2c2;\n"
"  border-radius: 9.8px;\n"
"  border-style: none;\n"
"  color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  /* Change the background color when the button is hovered over */\n"
"  color: rgb(197, 197, 197)\n"
"}")
        self.pushButton_75.setText("")
        self.pushButton_75.setCheckable(True)
        self.pushButton_75.setObjectName("pushButton_75")
        self.buttonGroup.addButton(self.pushButton_75)
        self.gridLayout_4.addWidget(self.pushButton_75, 0, 0, 1, 1)
        self.pushButton_76 = QtWidgets.QPushButton(self.frame_2, clicked = lambda: self.openWindow())
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_76.sizePolicy().hasHeightForWidth())
        self.pushButton_76.setSizePolicy(sizePolicy)
        self.pushButton_76.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_76.setStyleSheet("\n"
"QPushButton:checked {\n"
"background-color: #af55ff;\n"
"color: white;\n"
"border-radius: 9.8px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: #c2c2c2;\n"
"  border-radius: 9.8px;\n"
"  border-style: none;\n"
"  color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  /* Change the background color when the button is hovered over */\n"
"  color: rgb(197, 197, 197)\n"
"}")
        self.pushButton_76.setText("")
        self.pushButton_76.setCheckable(True)
        self.pushButton_76.setObjectName("pushButton_76")
        self.buttonGroup.addButton(self.pushButton_76)
        self.gridLayout_4.addWidget(self.pushButton_76, 0, 1, 1, 1)
        self.gridLayout_5.addWidget(self.frame_2, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frame_9, 0, 0, 1, 1)
        self.frame_6 = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy)
        self.frame_6.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_6.setMouseTracking(False)
        self.frame_6.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.frame_6)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.pushButton_86 = QtWidgets.QPushButton(self.frame_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_86.sizePolicy().hasHeightForWidth())
        self.pushButton_86.setSizePolicy(sizePolicy)
        self.pushButton_86.setMaximumSize(QtCore.QSize(200, 25))
        self.pushButton_86.setMouseTracking(False)
        self.pushButton_86.setStyleSheet("\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: black;\n"
"  border: none;\n"
"  border-radius: 10px;\n"
"  color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  /* Change the background color when the button is hovered over */\n"
"  background-color:nocolor;\n"
"  color: rgb(173, 173, 173)\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  /* Change the background color when the button is pressed */\n"
"  background-color: rgb(238, 255, 1);\n"
"  color: black;\n"
"}")
        self.pushButton_86.setObjectName("pushButton_86")
        self.gridLayout_7.addWidget(self.pushButton_86, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frame_6, 1, 0, 1, 1)
        NoMad.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(NoMad)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1105, 21))
        self.menubar.setObjectName("menubar")
        NoMad.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(NoMad)
        self.statusbar.setObjectName("statusbar")
        NoMad.setStatusBar(self.statusbar)

        self.retranslateUi(NoMad)
        QtCore.QMetaObject.connectSlotsByName(NoMad) 

    def retranslateUi(self, NoMad):
        _translate = QtCore.QCoreApplication.translate
        NoMad.setWindowTitle(_translate("NoMad", "MainWindow"))
        self.pushButton_194.setText(_translate("NoMad", "Esc"))
        self.pushButton_195.setText(_translate("NoMad", "%\n"
"\n"
" 5"))
        self.pushButton_196.setText(_translate("NoMad", "( \n"
"\n"
"9"))
        self.pushButton_197.setText(_translate("NoMad", "&&\n"
"\n"
" 7"))
        self.pushButton_198.setText(_translate("NoMad", "+\n"
" \n"
"="))
        self.pushButton_199.setText(_translate("NoMad", "^\n"
" \n"
"6"))
        self.pushButton_200.setText(_translate("NoMad", "@\n"
"\n"
" 2"))
        self.pushButton_201.setText(_translate("NoMad", "Backspace"))
        self.pushButton_202.setText(_translate("NoMad", "!\n"
"\n"
"1"))
        self.pushButton_203.setText(_translate("NoMad", "-\n"
"\n"
"_"))
        self.pushButton_204.setText(_translate("NoMad", "*\n"
" \n"
"8"))
        self.pushButton_205.setText(_translate("NoMad", "#\n"
"\n"
" 3"))
        self.pushButton_206.setText(_translate("NoMad", "$ \n"
"\n"
" 4"))
        self.pushButton_207.setText(_translate("NoMad", ") \n"
"\n"
"0"))
        self.pushButton_208.setText(_translate("NoMad", "Tab"))
        self.pushButton_209.setText(_translate("NoMad", "E"))
        self.pushButton_210.setText(_translate("NoMad", "{\n"
" \n"
"["))
        self.pushButton_211.setText(_translate("NoMad", "O"))
        self.pushButton_212.setText(_translate("NoMad", "T"))
        self.pushButton_213.setText(_translate("NoMad", "Y"))
        self.pushButton_214.setText(_translate("NoMad", "I"))
        self.pushButton_215.setText(_translate("NoMad", "W"))
        self.pushButton_216.setText(_translate("NoMad", "P"))
        self.pushButton_217.setText(_translate("NoMad", "Q"))
        self.pushButton_218.setText(_translate("NoMad", "| \n"
"\n"
"\\"))
        self.pushButton_219.setText(_translate("NoMad", "} \n"
"\n"
"]"))
        self.pushButton_220.setText(_translate("NoMad", "U"))
        self.pushButton_221.setText(_translate("NoMad", "R"))
        self.pushButton_260.setText(_translate("NoMad", "Page \n"
" Up"))
        self.pushButton_222.setText(_translate("NoMad", "Caps Lock"))
        self.pushButton_223.setText(_translate("NoMad", "D"))
        self.pushButton_224.setText(_translate("NoMad", "H"))
        self.pushButton_225.setText(_translate("NoMad", "Enter"))
        self.pushButton_226.setText(_translate("NoMad", "\" \n"
"\n"
"\'"))
        self.pushButton_227.setText(_translate("NoMad", "L"))
        self.pushButton_228.setText(_translate("NoMad", "K"))
        self.pushButton_229.setText(_translate("NoMad", "J"))
        self.pushButton_230.setText(_translate("NoMad", ":\n"
"\n"
" ;"))
        self.pushButton_231.setText(_translate("NoMad", "A"))
        self.pushButton_232.setText(_translate("NoMad", "F"))
        self.pushButton_233.setText(_translate("NoMad", "G"))
        self.pushButton_234.setText(_translate("NoMad", "S"))
        self.pushButton_259.setText(_translate("NoMad", "Page \n"
" Down"))
        self.pushButton_235.setText(_translate("NoMad", "Shift"))
        self.pushButton_236.setText(_translate("NoMad", "M"))
        self.pushButton_237.setText(_translate("NoMad", "N"))
        self.pushButton_238.setText(_translate("NoMad", ">\n"
" \n"
"."))
        self.pushButton_239.setText(_translate("NoMad", "C"))
        self.pushButton_240.setText(_translate("NoMad", "↑"))
        self.pushButton_241.setText(_translate("NoMad", "< \n"
"\n"
","))
        self.pushButton_242.setText(_translate("NoMad", "X"))
        self.pushButton_243.setText(_translate("NoMad", "Z"))
        self.pushButton_244.setText(_translate("NoMad", "B"))
        self.pushButton_245.setText(_translate("NoMad", "Shift"))
        self.pushButton_246.setText(_translate("NoMad", "?\n"
"\n"
" /"))
        self.pushButton_247.setText(_translate("NoMad", "V"))
        self.pushButton_258.setText(_translate("NoMad", "Home"))
        self.pushButton_248.setText(_translate("NoMad", "Ctrl"))
        self.pushButton_249.setText(_translate("NoMad", "Opt"))
        self.pushButton_251.setText(_translate("NoMad", "↓"))
        self.pushButton_252.setText(_translate("NoMad", "Cmd"))
        self.pushButton_253.setText(_translate("NoMad", "→"))
        self.pushButton_254.setText(_translate("NoMad", "Cmd"))
        self.pushButton_255.setText(_translate("NoMad", "←"))
        self.pushButton_256.setText(_translate("NoMad", "Ctrl"))
        self.pushButton_257.setText(_translate("NoMad", "Fn"))
        self.pushButton_86.setText(_translate("NoMad", "Save Profile"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    NoMad = QtWidgets.QMainWindow()
    ui = Ui_NoMad()
    ui.setupUi(NoMad)
    NoMad.show()
    sys.exit(app.exec_())
