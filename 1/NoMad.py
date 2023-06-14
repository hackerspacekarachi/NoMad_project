from PyQt5 import QtCore, QtGui, QtWidgets
from CreateAction import Ui_CreateAction
import ctypes
user32 = ctypes.windll.user32
user32.SetProcessDPIAware()
ax, wae = [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)]


class Ui_NoMad(object):
    def openWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.window.setWindowFlags(QtCore.Qt.Tool)
        self.ui = Ui_CreateAction()
        self.ui.setupUi(self.window)
        self.window.show()    
        
    def setupUi(self, NoMad):
        NoMad.setObjectName("NoMad")
        NoMad.setGeometry(QtCore.QRect(ax*0.106, wae*0.065, 1079, 623))
        NoMad.setFixedHeight(623)
        NoMad.setFixedWidth(1079)
        self.centralwidget = QtWidgets.QWidget(NoMad)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame.setToolTipDuration(-2)
        self.frame.setStyleSheet("background-color: rgb(231, 231, 231);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setLineWidth(0)
        self.frame.setMidLineWidth(3)
        self.frame.setObjectName("frame")
        self.pushButton = QtWidgets.QPushButton(self.frame, clicked = lambda: self.openWindow())
        self.pushButton.setGeometry(QtCore.QRect(100, 140, 51, 51))
        self.pushButton.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton.setMaximumSize(QtCore.QSize(51, 51))
        self.pushButton.setStyleSheet("\n"
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
        self.pushButton.setCheckable(True)
        self.pushButton.setObjectName("pushButton")
        self.buttonGroup = QtWidgets.QButtonGroup(NoMad)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame, clicked = lambda: self.openWindow())
        self.pushButton_2.setGeometry(QtCore.QRect(10, 140, 85, 291))
        self.pushButton_2.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_2.setMaximumSize(QtCore.QSize(85, 300))
        self.pushButton_2.setStyleSheet("background-color: rgb(51, 51, 51);\n"
"font: 8pt \"Arial\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"border-width: 2px;\n"
"border-radius: 15px;")
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.buttonGroup.addButton(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.frame, clicked = lambda: self.openWindow())
        self.pushButton_3.setGeometry(QtCore.QRect(160, 140, 51, 51))
        self.pushButton_3.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_3.setMaximumSize(QtCore.QSize(51, 51))
        self.pushButton_3.setStyleSheet("\n"
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
        self.pushButton_3.setCheckable(True)
        self.pushButton_3.setObjectName("pushButton_3")
        self.buttonGroup.addButton(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.frame, clicked = lambda: self.openWindow())
        self.pushButton_4.setGeometry(QtCore.QRect(280, 140, 51, 51))
        self.pushButton_4.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_4.setMaximumSize(QtCore.QSize(51, 51))
        self.pushButton_4.setStyleSheet("\n"
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
        self.pushButton_4.setCheckable(True)
        self.pushButton_4.setObjectName("pushButton_4")
        self.buttonGroup.addButton(self.pushButton_4)
        self.pushButton_5 = QtWidgets.QPushButton(self.frame, clicked = lambda: self.openWindow())
        self.pushButton_5.setGeometry(QtCore.QRect(220, 140, 51, 51))
        self.pushButton_5.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_5.setMaximumSize(QtCore.QSize(51, 51))
        self.pushButton_5.setStyleSheet("\n"
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
        self.pushButton_5.setCheckable(True)
        self.pushButton_5.setObjectName("pushButton_5")
        self.buttonGroup.addButton(self.pushButton_5)
        self.pushButton_6 = QtWidgets.QPushButton(self.frame, clicked = lambda: self.openWindow())
        self.pushButton_6.setGeometry(QtCore.QRect(400, 140, 51, 51))
        self.pushButton_6.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_6.setMaximumSize(QtCore.QSize(51, 51))
        self.pushButton_6.setStyleSheet("\n"
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
        self.pushButton_6.setCheckable(True)
        self.pushButton_6.setObjectName("pushButton_6")
        self.buttonGroup.addButton(self.pushButton_6)
        self.pushButton_7 = QtWidgets.QPushButton(self.frame, clicked = lambda: self.openWindow())
        self.pushButton_7.setGeometry(QtCore.QRect(460, 140, 51, 51))
        self.pushButton_7.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_7.setMaximumSize(QtCore.QSize(51, 51))
        self.pushButton_7.setStyleSheet("\n"
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
        self.pushButton_7.setCheckable(True)
        self.pushButton_7.setObjectName("pushButton_7")
        self.buttonGroup.addButton(self.pushButton_7)
        self.pushButton_8 = QtWidgets.QPushButton(self.frame, clicked = lambda: self.openWindow())
        self.pushButton_8.setGeometry(QtCore.QRect(340, 140, 51, 51))
        self.pushButton_8.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_8.setMaximumSize(QtCore.QSize(51, 51))
        self.pushButton_8.setStyleSheet("\n"
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
        self.pushButton_8.setCheckable(True)
        self.pushButton_8.setObjectName("pushButton_8")
        self.buttonGroup.addButton(self.pushButton_8)
        self.pushButton_10 = QtWidgets.QPushButton(self.frame, clicked = lambda: self.openWindow())
        self.pushButton_10.setGeometry(QtCore.QRect(640, 140, 51, 51))
        self.pushButton_10.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_10.setMaximumSize(QtCore.QSize(51, 51))
        self.pushButton_10.setStyleSheet("\n"
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
        self.pushButton_10.setCheckable(True)
        self.pushButton_10.setObjectName("pushButton_10")
        self.buttonGroup.addButton(self.pushButton_10)
        self.pushButton_11 = QtWidgets.QPushButton(self.frame, clicked = lambda: self.openWindow())
        self.pushButton_11.setGeometry(QtCore.QRect(580, 140, 51, 51))
        self.pushButton_11.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_11.setMaximumSize(QtCore.QSize(51, 51))
        self.pushButton_11.setStyleSheet("\n"
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
        self.pushButton_11.setCheckable(True)
        self.pushButton_11.setObjectName("pushButton_11")
        self.buttonGroup.addButton(self.pushButton_11)
        self.pushButton_12 = QtWidgets.QPushButton(self.frame, clicked = lambda: self.openWindow())
        self.pushButton_12.setGeometry(QtCore.QRect(700, 140, 51, 51))
        self.pushButton_12.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_12.setMaximumSize(QtCore.QSize(51, 51))
        self.pushButton_12.setStyleSheet("\n"
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
        self.pushButton_12.setCheckable(True)
        self.pushButton_12.setObjectName("pushButton_12")
        self.buttonGroup.addButton(self.pushButton_12)
        self.pushButton_14 = QtWidgets.QPushButton(self.frame, clicked = lambda: self.openWindow())
        self.pushButton_14.setGeometry(QtCore.QRect(100, 200, 78, 51))
        self.pushButton_14.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_14.setMaximumSize(QtCore.QSize(78, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_14.setFont(font)
        self.pushButton_14.setStyleSheet("\n"
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
        self.pushButton_14.setCheckable(True)
        self.pushButton_14.setObjectName("pushButton_14")
        self.buttonGroup.addButton(self.pushButton_14)
        self.pushButton_16 = QtWidgets.QPushButton(self.frame, clicked = lambda: self.openWindow())
        self.pushButton_16.setGeometry(QtCore.QRect(100, 260, 91, 51))
        self.pushButton_16.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_16.setMaximumSize(QtCore.QSize(91, 51))
        self.pushButton_16.setStyleSheet("\n"
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
        self.pushButton_16.setCheckable(True)
        self.pushButton_16.setObjectName("pushButton_16")
        self.buttonGroup.addButton(self.pushButton_16)
        self.pushButton_17 = QtWidgets.QPushButton(self.frame, clicked = lambda: self.openWindow())
        self.pushButton_17.setGeometry(QtCore.QRect(100, 320, 111, 51))
        self.pushButton_17.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_17.setMaximumSize(QtCore.QSize(118, 51))
        self.pushButton_17.setStyleSheet("\n"
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
        self.pushButton_17.setCheckable(True)
        self.pushButton_17.setAutoDefault(False)
        self.pushButton_17.setObjectName("pushButton_17")
        self.buttonGroup.addButton(self.pushButton_17)
        self.pushButton_13 = QtWidgets.QPushButton(self.frame, clicked = lambda: self.openWindow())
        self.pushButton_13.setGeometry(QtCore.QRect(190, 200, 51, 51))
        self.pushButton_13.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_13.setMaximumSize(QtCore.QSize(51, 51))
        self.pushButton_13.setStyleSheet("\n"
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
        self.pushButton_13.setCheckable(True)
        self.pushButton_13.setObjectName("pushButton_13")
        self.buttonGroup.addButton(self.pushButton_13)
        self.pushButton_19 = QtWidgets.QPushButton(self.frame, clicked = lambda: self.openWindow())
        self.pushButton_19.setGeometry(QtCore.QRect(250, 200, 51, 51))
        self.pushButton_19.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_19.setMaximumSize(QtCore.QSize(51, 51))
        self.pushButton_19.setStyleSheet("\n"
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
        self.pushButton_19.setCheckable(True)
        self.pushButton_19.setObjectName("pushButton_19")
        self.buttonGroup.addButton(self.pushButton_19)
        self.pushButton_20 = QtWidgets.QPushButton(self.frame, clicked = lambda: self.openWindow())
        self.pushButton_20.setGeometry(QtCore.QRect(550, 200, 51, 51))
        self.pushButton_20.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_20.setMaximumSize(QtCore.QSize(51, 51))
        self.pushButton_20.setStyleSheet("\n"
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
        self.pushButton_20.setCheckable(True)
        self.pushButton_20.setObjectName("pushButton_20")
        self.buttonGroup.addButton(self.pushButton_20)
        self.pushButton_21 = QtWidgets.QPushButton(self.frame, clicked = lambda: self.openWindow())
        self.pushButton_21.setGeometry(QtCore.QRect(370, 200, 51, 51))
        self.pushButton_21.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_21.setMaximumSize(QtCore.QSize(51, 51))
        self.pushButton_21.setStyleSheet("\n"
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
        self.pushButton_21.setCheckable(True)
        self.pushButton_21.setObjectName("pushButton_21")
        self.buttonGroup.addButton(self.pushButton_21)
        self.pushButton_22 = QtWidgets.QPushButton(self.frame, clicked = lambda: self.openWindow())
        self.pushButton_22.setGeometry(QtCore.QRect(490, 200, 51, 51))
        self.pushButton_22.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_22.setMaximumSize(QtCore.QSize(51, 51))
        self.pushButton_22.setStyleSheet("\n"
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
        self.pushButton_22.setCheckable(True)
        self.pushButton_22.setObjectName("pushButton_22")
        self.buttonGroup.addButton(self.pushButton_22)
        self.pushButton_23 = QtWidgets.QPushButton(self.frame, clicked = lambda: self.openWindow())
        self.pushButton_23.setGeometry(QtCore.QRect(670, 200, 51, 51))
        self.pushButton_23.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_23.setMaximumSize(QtCore.QSize(51, 51))
        self.pushButton_23.setStyleSheet("\n"
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
        self.pushButton_23.setCheckable(True)
        self.pushButton_23.setObjectName("pushButton_23")
        self.buttonGroup.addButton(self.pushButton_23)
        self.pushButton_24 = QtWidgets.QPushButton(self.frame, clicked = lambda: self.openWindow())
        self.pushButton_24.setGeometry(QtCore.QRect(430, 200, 51, 51))
        self.pushButton_24.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_24.setMaximumSize(QtCore.QSize(51, 51))
        self.pushButton_24.setStyleSheet("\n"
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
        self.pushButton_24.setCheckable(True)
        self.pushButton_24.setObjectName("pushButton_24")
        self.buttonGroup.addButton(self.pushButton_24)
        self.pushButton_25 = QtWidgets.QPushButton(self.frame, clicked = lambda: self.openWindow())
        self.pushButton_25.setGeometry(QtCore.QRect(610, 200, 51, 51))
        self.pushButton_25.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_25.setMaximumSize(QtCore.QSize(51, 51))
        self.pushButton_25.setStyleSheet("\n"
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
        self.pushButton_25.setCheckable(True)
        self.pushButton_25.setObjectName("pushButton_25")
        self.buttonGroup.addButton(self.pushButton_25)
        self.pushButton_26 = QtWidgets.QPushButton(self.frame, clicked = lambda: self.openWindow())
        self.pushButton_26.setGeometry(QtCore.QRect(310, 200, 51, 51))
        self.pushButton_26.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_26.setMaximumSize(QtCore.QSize(51, 51))
        self.pushButton_26.setStyleSheet("\n"
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
        self.pushButton_26.setCheckable(True)
        self.pushButton_26.setObjectName("pushButton_26")
        self.buttonGroup.addButton(self.pushButton_26)
        self.pushButton_27 = QtWidgets.QPushButton(self.frame, clicked = lambda: self.openWindow())
        self.pushButton_27.setGeometry(QtCore.QRect(380, 260, 51, 51))
        self.pushButton_27.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_27.setMaximumSize(QtCore.QSize(51, 51))
        self.pushButton_27.setStyleSheet("\n"
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
        self.pushButton_27.setCheckable(True)
        self.pushButton_27.setObjectName("pushButton_27")
        self.buttonGroup.addButton(self.pushButton_27)
        self.pushButton_28 = QtWidgets.QPushButton(self.frame, clicked = lambda: self.openWindow())
        self.pushButton_28.setGeometry(QtCore.QRect(680, 260, 51, 51))
        self.pushButton_28.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_28.setMaximumSize(QtCore.QSize(51, 51))
        self.pushButton_28.setStyleSheet("\n"
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
        self.pushButton_28.setCheckable(True)
        self.pushButton_28.setObjectName("pushButton_28")
        self.buttonGroup.addButton(self.pushButton_28)
        self.pushButton_29 = QtWidgets.QPushButton(self.frame, clicked = lambda: self.openWindow())
        self.pushButton_29.setGeometry(QtCore.QRect(320, 260, 51, 51))
        self.pushButton_29.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_29.setMaximumSize(QtCore.QSize(51, 51))
        self.pushButton_29.setStyleSheet("\n"
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
        self.pushButton_29.setCheckable(True)
        self.pushButton_29.setObjectName("pushButton_29")
        self.buttonGroup.addButton(self.pushButton_29)
        self.pushButton_30 = QtWidgets.QPushButton(self.frame, clicked = lambda: self.openWindow())
        self.pushButton_30.setGeometry(QtCore.QRect(560, 260, 51, 51))
        self.pushButton_30.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_30.setMaximumSize(QtCore.QSize(51, 51))
        self.pushButton_30.setStyleSheet("\n"
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
        self.pushButton_30.setCheckable(True)
        self.pushButton_30.setObjectName("pushButton_30")
        self.buttonGroup.addButton(self.pushButton_30)
        self.pushButton_31 = QtWidgets.QPushButton(self.frame, clicked = lambda: self.openWindow())
        self.pushButton_31.setGeometry(QtCore.QRect(440, 260, 51, 51))
        self.pushButton_31.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_31.setMaximumSize(QtCore.QSize(51, 51))
        self.pushButton_31.setStyleSheet("\n"
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
        self.pushButton_31.setCheckable(True)
        self.pushButton_31.setObjectName("pushButton_31")
        self.buttonGroup.addButton(self.pushButton_31)
        self.pushButton_32 = QtWidgets.QPushButton(self.frame, clicked = lambda: self.openWindow())
        self.pushButton_32.setGeometry(QtCore.QRect(500, 260, 51, 51))
        self.pushButton_32.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_32.setMaximumSize(QtCore.QSize(51, 51))
        self.pushButton_32.setStyleSheet("\n"
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
        self.pushButton_32.setCheckable(True)
        self.pushButton_32.setObjectName("pushButton_32")
        self.buttonGroup.addButton(self.pushButton_32)
        self.pushButton_33 = QtWidgets.QPushButton(self.frame, clicked = lambda: self.openWindow())
        self.pushButton_33.setGeometry(QtCore.QRect(620, 260, 51, 51))
        self.pushButton_33.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_33.setMaximumSize(QtCore.QSize(51, 51))
        self.pushButton_33.setStyleSheet("\n"
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
        self.pushButton_33.setCheckable(True)
        self.pushButton_33.setObjectName("pushButton_33")
        self.buttonGroup.addButton(self.pushButton_33)
        self.pushButton_34 = QtWidgets.QPushButton(self.frame, clicked = lambda: self.openWindow())
        self.pushButton_34.setGeometry(QtCore.QRect(260, 260, 51, 51))
        self.pushButton_34.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_34.setMaximumSize(QtCore.QSize(51, 51))
        self.pushButton_34.setStyleSheet("\n"
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
        self.pushButton_34.setCheckable(True)
        self.pushButton_34.setObjectName("pushButton_34")
        self.buttonGroup.addButton(self.pushButton_34)
        self.pushButton_35 = QtWidgets.QPushButton(self.frame, clicked = lambda: self.openWindow())
        self.pushButton_35.setGeometry(QtCore.QRect(200, 260, 51, 51))
        self.pushButton_35.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_35.setMaximumSize(QtCore.QSize(51, 51))
        self.pushButton_35.setStyleSheet("\n"
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
        self.pushButton_35.setCheckable(True)
        self.pushButton_35.setObjectName("pushButton_35")
        self.buttonGroup.addButton(self.pushButton_35)
        self.pushButton_36 = QtWidgets.QPushButton(self.frame, clicked = lambda: self.openWindow())
        self.pushButton_36.setGeometry(QtCore.QRect(400, 320, 51, 51))
        self.pushButton_36.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_36.setMaximumSize(QtCore.QSize(51, 51))
        self.pushButton_36.setStyleSheet("\n"
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
        self.pushButton_36.setCheckable(True)
        self.pushButton_36.setObjectName("pushButton_36")
        self.buttonGroup.addButton(self.pushButton_36)
        self.pushButton_39 = QtWidgets.QPushButton(self.frame, clicked = lambda: self.openWindow())
        self.pushButton_39.setGeometry(QtCore.QRect(580, 320, 51, 51))
        self.pushButton_39.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_39.setMaximumSize(QtCore.QSize(51, 51))
        self.pushButton_39.setStyleSheet("\n"
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
        self.pushButton_39.setCheckable(True)
        self.pushButton_39.setObjectName("pushButton_39")
        self.buttonGroup.addButton(self.pushButton_39)
        self.pushButton_40 = QtWidgets.QPushButton(self.frame, clicked = lambda: self.openWindow())
        self.pushButton_40.setGeometry(QtCore.QRect(460, 320, 51, 51))
        self.pushButton_40.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_40.setMaximumSize(QtCore.QSize(51, 51))
        self.pushButton_40.setStyleSheet("\n"
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
        self.pushButton_40.setCheckable(True)
        self.pushButton_40.setObjectName("pushButton_40")
        self.buttonGroup.addButton(self.pushButton_40)
        self.pushButton_41 = QtWidgets.QPushButton(self.frame, clicked = lambda: self.openWindow())
        self.pushButton_41.setGeometry(QtCore.QRect(520, 320, 51, 51))
        self.pushButton_41.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_41.setMaximumSize(QtCore.QSize(51, 51))
        self.pushButton_41.setStyleSheet("\n"
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
        self.pushButton_41.setCheckable(True)
        self.pushButton_41.setObjectName("pushButton_41")
        self.buttonGroup.addButton(self.pushButton_41)
        self.pushButton_42 = QtWidgets.QPushButton(self.frame, clicked = lambda: self.openWindow())
        self.pushButton_42.setGeometry(QtCore.QRect(640, 320, 51, 51))
        self.pushButton_42.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_42.setMaximumSize(QtCore.QSize(51, 51))
        self.pushButton_42.setStyleSheet("\n"
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
        self.pushButton_42.setCheckable(True)
        self.pushButton_42.setObjectName("pushButton_42")
        self.buttonGroup.addButton(self.pushButton_42)
        self.pushButton_37 = QtWidgets.QPushButton(self.frame, clicked = lambda: self.openWindow())
        self.pushButton_37.setGeometry(QtCore.QRect(170, 380, 64, 51))
        self.pushButton_37.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_37.setMaximumSize(QtCore.QSize(64, 51))
        self.pushButton_37.setStyleSheet("\n"
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
        self.pushButton_37.setCheckable(True)
        self.pushButton_37.setObjectName("pushButton_37")
        self.buttonGroup.addButton(self.pushButton_37)
        self.pushButton_45 = QtWidgets.QPushButton(self.frame, clicked = lambda: self.openWindow())
        self.pushButton_45.setGeometry(QtCore.QRect(240, 380, 64, 51))
        self.pushButton_45.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_45.setMaximumSize(QtCore.QSize(64, 51))
        self.pushButton_45.setStyleSheet("\n"
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
        self.pushButton_45.setCheckable(True)
        self.pushButton_45.setObjectName("pushButton_45")
        self.buttonGroup.addButton(self.pushButton_45)
        self.pushButton_46 = QtWidgets.QPushButton(self.frame, clicked = lambda: self.openWindow())
        self.pushButton_46.setGeometry(QtCore.QRect(310, 380, 371, 51))
        self.pushButton_46.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_46.setMaximumSize(QtCore.QSize(380, 51))
        self.pushButton_46.setStyleSheet("\n"
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
        self.pushButton_46.setText("")
        self.pushButton_46.setCheckable(True)
        self.pushButton_46.setObjectName("pushButton_46")
        self.buttonGroup.addButton(self.pushButton_46)
        self.pushButton_47 = QtWidgets.QPushButton(self.frame, clicked = lambda: self.openWindow())
        self.pushButton_47.setGeometry(QtCore.QRect(690, 380, 51, 51))
        self.pushButton_47.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_47.setMaximumSize(QtCore.QSize(51, 51))
        self.pushButton_47.setStyleSheet("\n"
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
        self.pushButton_47.setCheckable(True)
        self.pushButton_47.setObjectName("pushButton_47")
        self.buttonGroup.addButton(self.pushButton_47)
        self.pushButton_49 = QtWidgets.QPushButton(self.frame, clicked = lambda: self.openWindow())
        self.pushButton_49.setGeometry(QtCore.QRect(700, 320, 51, 51))
        self.pushButton_49.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_49.setMaximumSize(QtCore.QSize(51, 51))
        self.pushButton_49.setStyleSheet("\n"
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
        self.pushButton_49.setCheckable(True)
        self.pushButton_49.setObjectName("pushButton_49")
        self.buttonGroup.addButton(self.pushButton_49)
        self.pushButton_48 = QtWidgets.QPushButton(self.frame, clicked = lambda: self.openWindow())
        self.pushButton_48.setGeometry(QtCore.QRect(820, 140, 51, 51))
        self.pushButton_48.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_48.setMaximumSize(QtCore.QSize(51, 51))
        self.pushButton_48.setStyleSheet("\n"
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
        self.pushButton_48.setCheckable(True)
        self.pushButton_48.setObjectName("pushButton_48")
        self.buttonGroup.addButton(self.pushButton_48)
        self.pushButton_50 = QtWidgets.QPushButton(self.frame, clicked = lambda: self.openWindow())
        self.pushButton_50.setGeometry(QtCore.QRect(760, 140, 51, 51))
        self.pushButton_50.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_50.setMaximumSize(QtCore.QSize(51, 51))
        self.pushButton_50.setStyleSheet("\n"
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
        self.pushButton_50.setCheckable(True)
        self.pushButton_50.setObjectName("pushButton_50")
        self.buttonGroup.addButton(self.pushButton_50)
        self.pushButton_51 = QtWidgets.QPushButton(self.frame, clicked = lambda: self.openWindow())
        self.pushButton_51.setGeometry(QtCore.QRect(880, 140, 105, 51))
        self.pushButton_51.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_51.setMaximumSize(QtCore.QSize(105, 51))
        self.pushButton_51.setStyleSheet("\n"
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
        self.pushButton_51.setCheckable(True)
        self.pushButton_51.setObjectName("pushButton_51")
        self.buttonGroup.addButton(self.pushButton_51)
        self.pushButton_52 = QtWidgets.QPushButton(self.frame, clicked = lambda: self.openWindow())
        self.pushButton_52.setGeometry(QtCore.QRect(850, 200, 51, 51))
        self.pushButton_52.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_52.setMaximumSize(QtCore.QSize(51, 51))
        self.pushButton_52.setStyleSheet("\n"
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
        self.pushButton_52.setCheckable(True)
        self.pushButton_52.setObjectName("pushButton_52")
        self.buttonGroup.addButton(self.pushButton_52)
        self.pushButton_53 = QtWidgets.QPushButton(self.frame, clicked = lambda: self.openWindow())
        self.pushButton_53.setGeometry(QtCore.QRect(790, 200, 51, 51))
        self.pushButton_53.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_53.setMaximumSize(QtCore.QSize(51, 51))
        self.pushButton_53.setStyleSheet("\n"
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
        self.pushButton_53.setCheckable(True)
        self.pushButton_53.setObjectName("pushButton_53")
        self.buttonGroup.addButton(self.pushButton_53)
        self.pushButton_54 = QtWidgets.QPushButton(self.frame, clicked = lambda: self.openWindow())
        self.pushButton_54.setGeometry(QtCore.QRect(730, 200, 51, 51))
        self.pushButton_54.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_54.setMaximumSize(QtCore.QSize(51, 51))
        self.pushButton_54.setStyleSheet("\n"
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
        self.pushButton_54.setCheckable(True)
        self.pushButton_54.setObjectName("pushButton_54")
        self.buttonGroup.addButton(self.pushButton_54)
        self.pushButton_55 = QtWidgets.QPushButton(self.frame, clicked = lambda: self.openWindow())
        self.pushButton_55.setGeometry(QtCore.QRect(910, 200, 71, 51))
        self.pushButton_55.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_55.setMaximumSize(QtCore.QSize(105, 51))
        self.pushButton_55.setStyleSheet("\n"
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
        self.pushButton_55.setCheckable(True)
        self.pushButton_55.setObjectName("pushButton_55")
        self.buttonGroup.addButton(self.pushButton_55)
        self.pushButton_56 = QtWidgets.QPushButton(self.frame, clicked = lambda: self.openWindow())
        self.pushButton_56.setGeometry(QtCore.QRect(800, 260, 51, 51))
        self.pushButton_56.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_56.setMaximumSize(QtCore.QSize(51, 51))
        self.pushButton_56.setStyleSheet("\n"
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
        self.pushButton_56.setCheckable(True)
        self.pushButton_56.setObjectName("pushButton_56")
        self.buttonGroup.addButton(self.pushButton_56)
        self.pushButton_57 = QtWidgets.QPushButton(self.frame, clicked = lambda: self.openWindow())
        self.pushButton_57.setGeometry(QtCore.QRect(740, 260, 51, 51))
        self.pushButton_57.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_57.setMaximumSize(QtCore.QSize(51, 51))
        self.pushButton_57.setStyleSheet("\n"
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
        self.pushButton_57.setCheckable(True)
        self.pushButton_57.setObjectName("pushButton_57")
        self.buttonGroup.addButton(self.pushButton_57)
        self.pushButton_58 = QtWidgets.QPushButton(self.frame, clicked = lambda: self.openWindow())
        self.pushButton_58.setGeometry(QtCore.QRect(860, 260, 121, 51))
        self.pushButton_58.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_58.setMaximumSize(QtCore.QSize(380, 51))
        self.pushButton_58.setStyleSheet("\n"
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
        self.pushButton_58.setCheckable(True)
        self.pushButton_58.setObjectName("pushButton_58")
        self.buttonGroup.addButton(self.pushButton_58)
        self.pushButton_59 = QtWidgets.QPushButton(self.frame, clicked = lambda: self.openWindow())
        self.pushButton_59.setGeometry(QtCore.QRect(760, 320, 51, 51))
        self.pushButton_59.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_59.setMaximumSize(QtCore.QSize(51, 51))
        self.pushButton_59.setStyleSheet("\n"
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
        self.pushButton_59.setCheckable(True)
        self.pushButton_59.setObjectName("pushButton_59")
        self.buttonGroup.addButton(self.pushButton_59)
        self.pushButton_60 = QtWidgets.QPushButton(self.frame, clicked = lambda: self.openWindow())
        self.pushButton_60.setGeometry(QtCore.QRect(820, 320, 101, 51))
        self.pushButton_60.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_60.setMaximumSize(QtCore.QSize(380, 51))
        self.pushButton_60.setStyleSheet("\n"
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
        self.pushButton_60.setCheckable(True)
        self.pushButton_60.setObjectName("pushButton_60")
        self.buttonGroup.addButton(self.pushButton_60)
        self.pushButton_61 = QtWidgets.QPushButton(self.frame, clicked = lambda: self.openWindow())
        self.pushButton_61.setGeometry(QtCore.QRect(930, 320, 51, 50))
        self.pushButton_61.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_61.setMaximumSize(QtCore.QSize(51, 51))
        self.pushButton_61.setStyleSheet("\n"
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
        self.pushButton_61.setCheckable(True)
        self.pushButton_61.setObjectName("pushButton_61")
        self.buttonGroup.addButton(self.pushButton_61)
        self.pushButton_62 = QtWidgets.QPushButton(self.frame, clicked = lambda: self.openWindow())
        self.pushButton_62.setGeometry(QtCore.QRect(810, 380, 51, 51))
        self.pushButton_62.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_62.setMaximumSize(QtCore.QSize(51, 51))
        self.pushButton_62.setStyleSheet("\n"
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
        self.pushButton_62.setCheckable(True)
        self.pushButton_62.setObjectName("pushButton_62")
        self.buttonGroup.addButton(self.pushButton_62)
        self.pushButton_63 = QtWidgets.QPushButton(self.frame, clicked = lambda: self.openWindow())
        self.pushButton_63.setGeometry(QtCore.QRect(750, 380, 51, 51))
        self.pushButton_63.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_63.setMaximumSize(QtCore.QSize(51, 51))
        self.pushButton_63.setStyleSheet("\n"
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
        self.pushButton_63.setCheckable(True)
        self.pushButton_63.setObjectName("pushButton_63")
        self.buttonGroup.addButton(self.pushButton_63)
        self.pushButton_64 = QtWidgets.QPushButton(self.frame, clicked = lambda: self.openWindow())
        self.pushButton_64.setGeometry(QtCore.QRect(870, 380, 51, 51))
        self.pushButton_64.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_64.setMaximumSize(QtCore.QSize(51, 51))
        self.pushButton_64.setStyleSheet("\n"
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
        self.pushButton_64.setCheckable(True)
        self.pushButton_64.setObjectName("pushButton_64")
        self.buttonGroup.addButton(self.pushButton_64)
        self.pushButton_65 = QtWidgets.QPushButton(self.frame, clicked = lambda: self.openWindow())
        self.pushButton_65.setGeometry(QtCore.QRect(930, 380, 51, 51))
        self.pushButton_65.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_65.setMaximumSize(QtCore.QSize(51, 51))
        self.pushButton_65.setStyleSheet("\n"
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
        self.pushButton_65.setCheckable(True)
        self.pushButton_65.setObjectName("pushButton_65")
        self.buttonGroup.addButton(self.pushButton_65)
        self.pushButton_66 = QtWidgets.QPushButton(self.frame, clicked = lambda: self.openWindow())
        self.pushButton_66.setGeometry(QtCore.QRect(990, 380, 51, 51))
        self.pushButton_66.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_66.setMaximumSize(QtCore.QSize(51, 51))
        self.pushButton_66.setStyleSheet("\n"
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
        self.pushButton_66.setCheckable(True)
        self.pushButton_66.setObjectName("pushButton_66")
        self.buttonGroup.addButton(self.pushButton_66)
        self.pushButton_67 = QtWidgets.QPushButton(self.frame, clicked = lambda: self.openWindow())
        self.pushButton_67.setGeometry(QtCore.QRect(520, 140, 51, 51))
        self.pushButton_67.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_67.setMaximumSize(QtCore.QSize(51, 51))
        self.pushButton_67.setStyleSheet("\n"
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
        self.pushButton_67.setCheckable(True)
        self.pushButton_67.setObjectName("pushButton_67")

        self.pushButton_68 = QtWidgets.QPushButton(self.frame)
        self.pushButton_68.setGeometry(QtCore.QRect(965, 0, 17, 17))
        self.pushButton_68.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_68.setMaximumSize(QtCore.QSize(88, 32))
        self.pushButton_68.setStyleSheet("QPushButton:checked {\n"
"background-color: none;\n"
"color: rgb(89, 89, 89);\n"
"border-radius: 15px;\n"
"font: 28pt \"Arial\";\n"
"}\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: none;\n"
"  border-radius: 15px;\n"
"  color: rgb(89, 89, 89);\n"
"  font: 28pt \"Arial\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  /* Change the background color when the button is hovered over */\n"
"  color: rgb(173, 173, 173)\n"
"}")
        self.pushButton_68.setCheckable(True)
        self.pushButton_68.setAutoRepeat(False)
        self.pushButton_68.setObjectName("pushButton_68")

        self.pushButton_69 = QtWidgets.QPushButton(self.frame)
        self.pushButton_69.setGeometry(QtCore.QRect(1030, 0, 25, 25))
        self.pushButton_69.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_69.setMaximumSize(QtCore.QSize(88, 32))
        self.pushButton_69.setStyleSheet("QPushButton:checked {\n"
"background-color: none;\n"
"color: rgb(89, 89, 89);\n"
"border-radius: 15px;\n"
"font: 25pt \"Arial\";\n"
"}\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: none;\n"
"  border-radius: 15px;\n"
"  color: rgb(89, 89, 89);\n"
"  font: 25pt \"Arial\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  /* Change the background color when the button is hovered over */\n"
"  color: rgb(245, 75, 90)\n" #(232, 17, 35)
"}")
        self.pushButton_69.setCheckable(True)
        self.pushButton_69.setAutoRepeat(False)
        self.pushButton_69.setObjectName("pushButton_69")

        self.buttonGroup.addButton(self.pushButton_67)
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(0, 130, 1051, 311))
        self.frame_2.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"font: 8pt \"Arial\";\n"
"color: rgb(255, 255, 255);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 25px;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.pushButton_43 = QtWidgets.QPushButton(self.frame_2, clicked = lambda: self.openWindow())
        self.pushButton_43.setGeometry(QtCore.QRect(280, 190, 51, 51))
        self.pushButton_43.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_43.setMaximumSize(QtCore.QSize(51, 51))
        self.pushButton_43.setStyleSheet("\n"
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
        self.pushButton_43.setCheckable(True)
        self.pushButton_43.setObjectName("pushButton_43")
        self.buttonGroup.addButton(self.pushButton_43)
        self.pushButton_44 = QtWidgets.QPushButton(self.frame_2, clicked = lambda: self.openWindow())
        self.pushButton_44.setGeometry(QtCore.QRect(220, 190, 51, 51))
        self.pushButton_44.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_44.setMaximumSize(QtCore.QSize(51, 51))
        self.pushButton_44.setStyleSheet("\n"
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
        self.pushButton_44.setCheckable(True)
        self.pushButton_44.setObjectName("pushButton_44")
        self.buttonGroup.addButton(self.pushButton_44)
        self.pushButton_38 = QtWidgets.QPushButton(self.frame_2, clicked = lambda: self.openWindow())
        self.pushButton_38.setGeometry(QtCore.QRect(340, 190, 51, 51))
        self.pushButton_38.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_38.setMaximumSize(QtCore.QSize(51, 51))
        self.pushButton_38.setStyleSheet("\n"
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
        self.pushButton_38.setCheckable(True)
        self.pushButton_38.setObjectName("pushButton_38")
        self.buttonGroup.addButton(self.pushButton_38)
        self.pushButton_18 = QtWidgets.QPushButton(self.frame_2, clicked = lambda: self.openWindow())
        self.pushButton_18.setGeometry(QtCore.QRect(100, 250, 64, 47))
        self.pushButton_18.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_18.setMaximumSize(QtCore.QSize(64, 57))
        self.pushButton_18.setStyleSheet("\n"
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
        self.pushButton_18.setCheckable(True)
        self.pushButton_18.setAutoRepeatDelay(296)
        self.pushButton_18.setObjectName("pushButton_18")
        self.buttonGroup.addButton(self.pushButton_18)
        self.pushButton_9 = QtWidgets.QPushButton(self.frame)
        self.pushButton_9.setGeometry(QtCore.QRect(430, 540, 191, 31))
        self.pushButton_9.setStyleSheet("\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: black;\n"
"  border: none;\n"
"  border-radius: 15px;\n"
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
        self.pushButton_9.setObjectName("pushButton_9")
        self.frame_2.raise_()
        self.pushButton_47.raise_()
        self.pushButton_23.raise_()
        self.pushButton_49.raise_()
        self.pushButton_28.raise_()
        self.pushButton_12.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.pushButton_3.raise_()
        self.pushButton_4.raise_()
        self.pushButton_5.raise_()
        self.pushButton_6.raise_()
        self.pushButton_7.raise_()
        self.pushButton_8.raise_()
        self.pushButton_10.raise_()
        self.pushButton_11.raise_()
        self.pushButton_14.raise_()
        self.pushButton_16.raise_()
        self.pushButton_17.raise_()
        self.pushButton_13.raise_()
        self.pushButton_19.raise_()
        self.pushButton_20.raise_()
        self.pushButton_21.raise_()
        self.pushButton_22.raise_()
        self.pushButton_24.raise_()
        self.pushButton_25.raise_()
        self.pushButton_26.raise_()
        self.pushButton_27.raise_()
        self.pushButton_29.raise_()
        self.pushButton_30.raise_()
        self.pushButton_31.raise_()
        self.pushButton_32.raise_()
        self.pushButton_33.raise_()
        self.pushButton_34.raise_()
        self.pushButton_35.raise_()
        self.pushButton_36.raise_()
        self.pushButton_39.raise_()
        self.pushButton_40.raise_()
        self.pushButton_41.raise_()
        self.pushButton_42.raise_()
        self.pushButton_37.raise_()
        self.pushButton_45.raise_()
        self.pushButton_46.raise_()
        self.pushButton_48.raise_()
        self.pushButton_50.raise_()
        self.pushButton_51.raise_()
        self.pushButton_52.raise_()
        self.pushButton_53.raise_()
        self.pushButton_54.raise_()
        self.pushButton_55.raise_()
        self.pushButton_56.raise_()
        self.pushButton_57.raise_()
        self.pushButton_58.raise_()
        self.pushButton_59.raise_()
        self.pushButton_60.raise_()
        self.pushButton_61.raise_()
        self.pushButton_62.raise_()
        self.pushButton_63.raise_()
        self.pushButton_64.raise_()
        self.pushButton_65.raise_()
        self.pushButton_66.raise_()
        self.pushButton_67.raise_()
        self.pushButton_9.raise_()
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        NoMad.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(NoMad)
        self.statusbar.setObjectName("statusbar")
        NoMad.setStatusBar(self.statusbar)

        self.retranslateUi(NoMad)
        QtCore.QMetaObject.connectSlotsByName(NoMad)

    def retranslateUi(self, NoMad):
        _translate = QtCore.QCoreApplication.translate
        NoMad.setWindowTitle(_translate("NoMad", "MainWindow"))
        NoMad.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        self.pushButton.setText(_translate("NoMad", "Esc"))
        self.pushButton_3.setText(_translate("NoMad", "!\n"
"1"))
        self.pushButton_4.setText(_translate("NoMad", "#\n"
" 3"))
        self.pushButton_5.setText(_translate("NoMad", "@\n"
" 2"))
        self.pushButton_6.setText(_translate("NoMad", "%\n"
" 5"))
        self.pushButton_7.setText(_translate("NoMad", "^\n"
" 6"))
        self.pushButton_8.setText(_translate("NoMad", "$ \n"
" 4"))
        self.pushButton_10.setText(_translate("NoMad", "( \n"
"9"))
        self.pushButton_11.setText(_translate("NoMad", "*\n"
" 8"))
        self.pushButton_12.setText(_translate("NoMad", ") \n"
"0"))
        self.pushButton_14.setText(_translate("NoMad", "Tab"))
        self.pushButton_16.setText(_translate("NoMad", "Caps Lock"))
        self.pushButton_17.setText(_translate("NoMad", "Shift"))
        self.pushButton_13.setText(_translate("NoMad", "Q"))
        self.pushButton_19.setText(_translate("NoMad", "W"))
        self.pushButton_20.setText(_translate("NoMad", "U"))
        self.pushButton_21.setText(_translate("NoMad", "R"))
        self.pushButton_22.setText(_translate("NoMad", "Y"))
        self.pushButton_23.setText(_translate("NoMad", "O"))
        self.pushButton_24.setText(_translate("NoMad", "T"))
        self.pushButton_25.setText(_translate("NoMad", "I"))
        self.pushButton_26.setText(_translate("NoMad", "E"))
        self.pushButton_27.setText(_translate("NoMad", "F"))
        self.pushButton_28.setText(_translate("NoMad", "L"))
        self.pushButton_29.setText(_translate("NoMad", "D"))
        self.pushButton_30.setText(_translate("NoMad", "J"))
        self.pushButton_31.setText(_translate("NoMad", "G"))
        self.pushButton_32.setText(_translate("NoMad", "H"))
        self.pushButton_33.setText(_translate("NoMad", "K"))
        self.pushButton_34.setText(_translate("NoMad", "S"))
        self.pushButton_35.setText(_translate("NoMad", "A"))
        self.pushButton_36.setText(_translate("NoMad", "V"))
        self.pushButton_39.setText(_translate("NoMad", "M"))
        self.pushButton_40.setText(_translate("NoMad", "B"))
        self.pushButton_41.setText(_translate("NoMad", "N"))
        self.pushButton_42.setText(_translate("NoMad", "< \n"
","))
        self.pushButton_37.setText(_translate("NoMad", "Opt"))
        self.pushButton_45.setText(_translate("NoMad", "Cmd"))
        self.pushButton_47.setText(_translate("NoMad", "Cmd"))
        self.pushButton_49.setText(_translate("NoMad", ">\n"
" ."))
        self.pushButton_48.setText(_translate("NoMad", "+\n"
" ="))
        self.pushButton_50.setText(_translate("NoMad", "-\n"
"_"))
        self.pushButton_51.setText(_translate("NoMad", "Backspace"))
        self.pushButton_52.setText(_translate("NoMad", "} \n"
"]"))
        self.pushButton_53.setText(_translate("NoMad", "{\n"
" ["))
        self.pushButton_54.setText(_translate("NoMad", "P"))
        self.pushButton_55.setText(_translate("NoMad", "| \n"
"\\"))
        self.pushButton_56.setText(_translate("NoMad", "\" \n"
"\'"))
        self.pushButton_57.setText(_translate("NoMad", ":\n"
" ;"))
        self.pushButton_58.setText(_translate("NoMad", "Enter"))
        self.pushButton_59.setText(_translate("NoMad", "?\n"
" /"))
        self.pushButton_60.setText(_translate("NoMad", "Shift"))
        self.pushButton_61.setText(_translate("NoMad", "↑"))
        self.pushButton_62.setText(_translate("NoMad", "Ctrl"))
        self.pushButton_63.setText(_translate("NoMad", "Fn"))
        self.pushButton_64.setText(_translate("NoMad", "←"))
        self.pushButton_65.setText(_translate("NoMad", "↓"))
        self.pushButton_66.setText(_translate("NoMad", "→"))
        self.pushButton_67.setText(_translate("NoMad", "&\n"
" 7"))
        self.pushButton_68.setText(_translate("NoMad", "-"))
        self.pushButton_68.clicked.connect(NoMad.showMinimized)
        self.pushButton_69.setText(_translate("NoMad", "×"))
        self.pushButton_69.clicked.connect(NoMad.close)

        self.pushButton_43.setText(_translate("NoMad", "X"))
        self.pushButton_44.setText(_translate("NoMad", "Z"))
        self.pushButton_38.setText(_translate("NoMad", "C"))
        self.pushButton_18.setText(_translate("NoMad", "Ctrl"))
        self.pushButton_9.setText(_translate("NoMad", "Save Profile"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    NoMad = QtWidgets.QMainWindow()
    ui = Ui_NoMad()
    ui.setupUi(NoMad)
    NoMad.show()
    sys.exit(app.exec_())
