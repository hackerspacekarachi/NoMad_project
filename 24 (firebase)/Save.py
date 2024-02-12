from PyQt5 import QtCore, QtGui, QtWidgets
import os, sys, json, time
import subprocess, threading
from screeninfo import get_monitors
# from PIL import Image
# user32 = ctypes.windll.user32
# user32.SetProcessDPIAware()

monitors = get_monitors()
for monitor in monitors:
    ax, wae = monitor.width,monitor.height

#Community Button
class HoverCommandLinkButton(QtWidgets.QCommandLinkButton):
    def __init__(self, text, parent=None):
        super().__init__(text, parent)
        self.default_text = text
        pic = self.resource_path("Icons/wwww.png")
        self.default_icon = QtGui.QIcon(pic)
        self.set_icon_visible(True)  # Show the icon by default
        self.setGeometry(QtCore.QRect(1050, 0, 100, 40))  # Set the geometry for positioning

    def enterEvent(self, event):
        self.set_icon_visible(False)  # Hide the icon on hover
        self.setText("Coming Soon")
        super().enterEvent(event)

    def leaveEvent(self, event):
        self.set_icon_visible(True)  # Show the icon when the mouse leaves
        self.setText(self.default_text)
        super().leaveEvent(event)

    def set_icon_visible(self, visible):
        icon = self.default_icon if visible else QtGui.QIcon()
        self.setIcon(icon)

    def resource_path(self, relative_path):
        """ Get absolute path to resource, works for dev and for PyInstaller """
        """ https://youtu.be/xJAM8_Lx5mY """
        try:
            # PyInstaller creates a temp folder and stores path in _MEIPASS
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)


class Ui_Save(object):
    
    def resource_path(self, relative_path):
        """ Get absolute path to resource, works for dev and for PyInstaller """
        """ https://youtu.be/xJAM8_Lx5mY """
        try:
            # PyInstaller creates a temp folder and stores path in _MEIPASS
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)


    def buttonz(self, a):
        Flag = True
        list = []
        count = 0
        count2 = 0
        xx = [20, 80, 140, 200, 260]
        x = []
        y = 0  #190
        max_iter = 1200

        # Number of x
        while Flag and count2 < max_iter:
            for i in xx:
                x.append(i)
                if len(x) == a:
                    Flag = False
            count2 +=1
                
        # y distancing
        for i in range(a):
            # After 5 counts increase y by 60
            if count%5==0 and count!=0:
                # increased y for new line
                y += 60
                
            list.append([x[i],y])
            count+=1
        return list
    

    def action(self, var, place, num):

        self.pushButton_c = QtWidgets.QPushButton(place)
        self.pushButton_c.setGeometry(QtCore.QRect(num[0], num[1], 51, 51))
        self.pushButton_c.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_c.setMaximumSize(QtCore.QSize(51, 51))
        font = QtGui.QFont()
        self.pushButton_c.setFont(font)
        self.pushButton_c.setStyleSheet("\n"
        "\n"
        "QPushButton {\n"
        "  /* Set the background color and border for the button */\n"
        "  background-color: #f2f2f2;\n"
        "  border: none;\n"
        "  border-radius: 10px;\n"
        "  padding: 10px 12px;\n"
        "\n"
        "}\n"
        "\n"
        "QPushButton:hover {\n"
        "  /* Change the background color when the button is hovered over */\n"
        "  background-color: #e5e5e5;\n"
        "  color: black;\n"
        "}\n"
        "\n"
        "QPushButton:pressed {\n"
        "  /* Change the background color when the button is pressed */\n"
        "  background-color: #3d3d3d;\n"
        "  color: white;\n"
        "}\n"
        "\n"
        "")
        self.pushButton_c.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(var['image_path']), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.pushButton_c.setIcon(icon5)
        self.pushButton_c.setIconSize(QtCore.QSize(35, 35))
        self.pushButton_c.setToolTip(var['settings']['action'])

    def profiles(self):
        # onlyfiles = next(os.walk("Profiles"))[2] #directory is your directory path as string
        # print(len(onlyfiles))

        if not os.path.exists(self.resource_path('Profiles')):
            os.makedirs('Profiles')
        count = 0
        for file_name in os.listdir(self.resource_path('Profiles/')):
            if file_name.endswith(".json"):
                count +=1
            else:
                pass
        
        dimens = self.buttonz(count)
        var = []
        for file_name in os.listdir(self.resource_path('Profiles/')):
            if file_name.endswith(".json"):

                with open(self.resource_path('Profiles/'+file_name)) as p:
                    var.append(json.load(p))
            else:
                pass

        if len(var) == 0 and len(dimens) == 0:
            pass
        else:
            for a,b in zip(var,dimens):
                self.action(a, self.profiles_area_2, b)

    def show_dialog(self):
        dialog = QtWidgets.QMessageBox()
        dialog.setText('Profile has been saved')
        dialog.setWindowTitle('NOMAD')
        dialog.setIcon(QtWidgets.QMessageBox.Information)
        dialog.exec_()

    def save_profile(self):
        if len(os.listdir('./Actions')) > 0:
            if self.lineEdit_93.text().lower() == [folder.lower() for folder in os.listdir('./Actions')][0]:
                    # show an error message if no image is selected
                    QtWidgets.QMessageBox.warning(self.centralwidget, "Warning", "Profile: "+self.lineEdit_93.text()+" already exists!")
                    return
        
        # Get the relevant information from the UI widgets
        if "" in [self.lineEdit_93.text(),self.lineEdit_94.text(),self.lineEdit_95.text(),self.textEdit_96.toPlainText()]:
                # show an error message if no image is selected
                QtWidgets.QMessageBox.warning(self.centralwidget, "Warning", "Found Incomlpete Field")
                return

        else:

                settings = {"name": self.lineEdit_93.text(),
                        "software": self.lineEdit_94.text(),
                        "tags": self.lineEdit_95.text(),
                        "description": self.textEdit_96.toPlainText(),
                        "color": "#c0c0c0"}

                # Reset Empty All
                self.lineEdit_93.setText("")
                self.lineEdit_94.setText("")
                self.lineEdit_95.setText("")
                self.textEdit_96.setText("")

                os.makedirs("Actions/"+settings["name"], exist_ok=True)


                file_name = "NOMAD_" + str(int(time.time())) + ".json"
                file_path = os.path.join("Actions/"+settings["name"], file_name)
                with open(file_path, 'w') as file:
                        json.dump(settings, file, indent=4)

                self.show_dialog()
   

    def add_menu(self, data, menu_obj):
            if isinstance(data, dict):
                for k, v in data.items():
                    sub_menu = QtWidgets.QMenu(k, menu_obj)
                #     sub_menu.setGeometry(50, 10, None, None)
                    menu_obj.addMenu(sub_menu)
                    self.add_menu(v, sub_menu)
            elif isinstance(data, list):
                for element in data:
                    self.add_menu(element, menu_obj)

            else:
                action = menu_obj.addAction(data)
                action.setIconVisibleInMenu(False)

    def back2Nomad(self):
        a = self.resource_path('NoMad.py')
        thread_login = threading.Thread(target=subprocess.Popen(['python', a]))#, args=(['python', 'NoMad.py']),)
        thread_login.start()
        thread_slideshow = threading.Thread(target=NoMad.close())

        thread_slideshow.start()

        thread_login.join()
        thread_slideshow.join()

        
    def setupUi(self, NoMad):
        # shutil.copy2(self.resource_path('NoMad.py'),'./NoMad.py')
        # shutil.copy2(self.resource_path('Save.py'),'./Save.py')
        # shutil.copy2(self.resource_path('Icons'),'./Icons')
        # os.system("attrib +h /s NoMad.py")
        # os.system("attrib +h /s Save.py")

        NoMad.setObjectName("NoMad")
        app_icon = QtGui.QIcon()
        pic = self.resource_path('Icons/logo.png')
        app_icon.addFile(pic) # , QtCore.QSize(60,18)
        # app_icon.addPixmap(QtGui.QPixmap('Icons/logo.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        NoMad.setWindowIcon(app_icon)
        NoMad.setGeometry(QtCore.QRect(int(ax*0.106), int(wae*0.065), 1079, 623))    # 0, 0


        self.centralwidget = QtWidgets.QWidget(NoMad)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
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


        self.boxLayout = QtWidgets.QVBoxLayout(self.frame)
        self.boxLayout.setObjectName("boxLayout")
        self.boxLayout.setContentsMargins(0,0,0,0)
        # NoMad.setLayout(self.boxLayout)
        
        self.buttonGroup = QtWidgets.QButtonGroup(NoMad)
        self.buttonGroup.setObjectName("buttonGroup")
        

        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setGeometry(QtCore.QRect(0, 0, 1151, 42))  # 0, 27
        self.frame_4.setMinimumSize(QtCore.QSize(1151, 42))
        self.frame_4.setMaximumSize(QtCore.QSize(16777215, 42))
        self.frame_4.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 8pt \"Arial\";\n"
"color: rgb(255, 255, 255);\n")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.boxLayout.addWidget(self.frame_4,0,QtCore.Qt.AlignTop) #,0,QtCore.Qt.AlignCenter
        self.boxLayout.setSpacing(0)
        self.boxLayout.addStretch(3)

        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(15, 50, 41, 20))
        self.label.setStyleSheet("font: 28pt \"Work Sans\"; font-weight: bold;")
        self.label.setText('Save your profile')
        self.label.setObjectName("label")
        self.boxLayout.addWidget(self.label,0,QtCore.Qt.AlignCenter) #,0,QtCore.Qt.AlignCenter
        self.boxLayout.addStretch(1)

        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(15, 50, 41, 20))
        self.label_2.setStyleSheet("font: 14pt \"Work Sans\"; color: rgb(192,192,192);")
        self.label_2.setText('Describe it for the community')
        self.label_2.setObjectName("label_2")
        self.boxLayout.addWidget(self.label_2,0,QtCore.Qt.AlignCenter) #,0,QtCore.Qt.AlignCenter
        self.boxLayout.addStretch(1)
        

        self.frame_5 = QtWidgets.QFrame(self.frame)  # Vector Art
        self.frame_5.setGeometry(QtCore.QRect(15, 120, 300, 160))
        self.frame_5.setMinimumSize(QtCore.QSize(300, 160))
        self.frame_5.setMaximumSize(QtCore.QSize(300, 160))
        self.frame_5.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 8pt \"Arial\";\n"
"color: rgb(0, 0, 0);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 12px;"
"border-color: rgb(255, 255, 255);")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.boxLayout.addWidget(self.frame_5,0,QtCore.Qt.AlignCenter) #,0,QtCore.Qt.AlignCenter
        self.boxLayout.addStretch(3)

        self.frame_7 = QtWidgets.QFrame(self.frame)
        self.frame_7.setGeometry(QtCore.QRect(0, 530, 1151, 55))
        self.frame_7.setMinimumSize(QtCore.QSize(1151, 75))
        self.frame_7.setMaximumSize(QtCore.QSize(16777215, 75))
        self.frame_7.setStyleSheet("background-color: no color;\n"
"font: 8pt \"Arial\";\n"
"color: rgb(255, 255, 255);\n")
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.boxLayout.addWidget(self.frame_7, 0, QtCore.Qt.AlignBottom)

        self.frame_9 = QtWidgets.QFrame(self.frame)
        self.frame_9.setGeometry(QtCore.QRect(0, 585, 1151, 55))
        self.frame_9.setStyleSheet("background-color: no color;\n"
"font: 8pt \"Arial\";\n"
"color: rgb(255, 255, 255);\n")
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.boxLayout.addWidget(self.frame_9, 0, QtCore.Qt.AlignBottom)


        self.Lay_f4 = QtWidgets.QHBoxLayout(self.frame_4)
        self.Lay_f4.setObjectName("Lay_f4")
        # self.Lay_f4.setSpacing(0)
        self.Lay_f4.setContentsMargins(0,0,0,0)

        self.commandLinkButton_7 = QtWidgets.QCommandLinkButton(self.frame_4)
        self.commandLinkButton_7.setGeometry(QtCore.QRect(10, 0, 200, 41))
        self.commandLinkButton_7.setMinimumSize(QtCore.QSize(200, 41))
        self.commandLinkButton_7.setMaximumSize(QtCore.QSize(200, 41))
        # self.commandLinkButton_5.setIconSize(QtCore.QSize(64, 64))
        self.commandLinkButton_7.setText("My profile")
        self.commandLinkButton_7.setStyleSheet("color: #000000;\n"
"background-color: none;\n"
"font: 9pt \"Work Sans\";\n"
"border: none;\n"
"")
        icon = QtGui.QIcon()
        pic = self.resource_path("Icons/my_profile.png")
        icon.addPixmap(QtGui.QPixmap(pic), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.commandLinkButton_7.setIcon(icon)
        self.commandLinkButton_7.setObjectName("commandLinkButton_7")
        self.Lay_f4.addWidget(self.commandLinkButton_7,1,QtCore.Qt.AlignLeft)

        # self.Lay_f4.addStretch(1)

        self.pushButton_79 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_79.setGeometry(QtCore.QRect(0, 0, 111, 41))
        self.pushButton_79.setMinimumSize(QtCore.QSize(111, 41))
        self.pushButton_79.setMaximumSize(QtCore.QSize(111, 41))
        self.pushButton_79.setText("Configurator")
        self.pushButton_79.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 10pt \"Work Sans\";\n"
"background-color: none;\n"
"border: none;\n"
"")
        self.pushButton_79.setObjectName("pushButton_79")
        self.Lay_f4.addWidget(self.pushButton_79,0,QtCore.Qt.AlignCenter)
        

        self.pushButton_80 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_80.setGeometry(QtCore.QRect(0, 0, 111, 41))
        self.pushButton_80.setMinimumSize(QtCore.QSize(111, 41))
        self.pushButton_80.setMaximumSize(QtCore.QSize(111, 41))
        self.pushButton_80.setText("Lighting")
        self.pushButton_80.setStyleSheet("color: #c2c2c2;\n"
"font: 10pt \"Work Sans\";\n"
"background-color: none;\n"
"border: none;\n"
"")
        self.pushButton_80.setObjectName("pushButton_80")
        self.Lay_f4.addWidget(self.pushButton_80,0,QtCore.Qt.AlignCenter)

        self.pushButton_83 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_83.setGeometry(QtCore.QRect(0, 0, 111, 41))
        self.pushButton_83.setMinimumSize(QtCore.QSize(111, 41))
        self.pushButton_83.setMaximumSize(QtCore.QSize(111, 41))
        self.pushButton_83.setText("Setup")
        self.pushButton_83.setStyleSheet("color: #c2c2c2;\n"
"font: 10pt \"Work Sans\";\n"
"background-color: none;\n"
"border: none;\n"
"")
        self.pushButton_83.setObjectName("pushButton_83")
        self.Lay_f4.addWidget(self.pushButton_83,0,QtCore.Qt.AlignCenter)

        self.lineEdit_93 = QtWidgets.QLineEdit(self.frame_5)
        self.lineEdit_93.setGeometry(QtCore.QRect(10, 14, 280, 27))
        self.lineEdit_93.setPlaceholderText("Profile name...")
        self.lineEdit_93.setMaxLength(20)
        self.lineEdit_93.setStyleSheet("\n"
"\n"
"QLineEdit {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: #e7e7e7;\n"
"  font: 8pt \"Work Sans\";\n"
"  padding-left: 15px;\n"
"  border: none;\n"
"  border-radius: 13px;\n"
"  color: black;\n"
"  font-weight: bold;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"  /* Change the background color when the button is hovered over */\n"
"  background-color: #e7e7e7;\n"
"  color: rgb(173, 173, 173)\n"
"}\n"
"\n"
"QLineEdit:pressed {\n"
"  /* Change the background color when the button is pressed */\n"
"  background-color: rgb(238, 255, 1);\n"
"  color: black;\n"
"}")
        self.lineEdit_93.setObjectName("lineEdit_93")

        self.lineEdit_94 = QtWidgets.QLineEdit(self.frame_5)
        self.lineEdit_94.setGeometry(QtCore.QRect(10, 49, 280, 27))
        self.lineEdit_94.setPlaceholderText("Primary software...")
        self.lineEdit_94.setStyleSheet("\n"
"\n"
"QLineEdit {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: #e7e7e7;\n"
"  font: 8pt \"Work Sans\";\n"
"  padding-left: 15px;\n"
"  border: none;\n"
"  border-radius: 13px;\n"
"  color: black;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"  /* Change the background color when the button is hovered over */\n"
"  background-color: #e7e7e7;\n"
"  color: rgb(173, 173, 173)\n"
"}\n"
"\n"
"QLineEdit:pressed {\n"
"  /* Change the background color when the button is pressed */\n"
"  background-color: rgb(238, 255, 1);\n"
"  color: black;\n"
"}")
        self.lineEdit_94.setObjectName("lineEdit_94")

        self.lineEdit_95 = QtWidgets.QLineEdit(self.frame_5)
        self.lineEdit_95.setGeometry(QtCore.QRect(10, 84, 280, 27))
        self.lineEdit_95.setPlaceholderText("Add tags...")
        self.lineEdit_95.setStyleSheet("\n"
"\n"
"QLineEdit {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: #e7e7e7;\n"
"  font: 8pt \"Work Sans\";\n"
"  padding-left: 15px;\n"
"  border: none;\n"
"  border-radius: 13px;\n"
"  color: black;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"  /* Change the background color when the button is hovered over */\n"
"  background-color: #e7e7e7;\n"
"  color: rgb(173, 173, 173)\n"
"}\n"
"\n"
"QLineEdit:pressed {\n"
"  /* Change the background color when the button is pressed */\n"
"  background-color: rgb(238, 255, 1);\n"
"  color: black;\n"
"}")
        self.lineEdit_95.setObjectName("lineEdit_95")

        self.textEdit_96 = QtWidgets.QTextEdit(self.frame_5)
        self.textEdit_96.setGeometry(QtCore.QRect(10, 119, 280, 27))
        self.textEdit_96.setPlaceholderText("Add tiny description...")
        self.textEdit_96.setStyleSheet("\n"
"\n"
"QTextEdit {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: #e7e7e7;\n"
"  font: 8pt \"Work Sans\";\n"
"  padding-left: 13px;\n"
"  border: none;\n"
"  border-radius: 13px;\n"
"  color: black;\n"
"}\n"
"\n"
"QTextEdit:hover {\n"
"  /* Change the background color when the button is hovered over */\n"
"  background-color: #e7e7e7;\n"
"  color: black\n"
"}\n"
"\n"
"QTextEdit:pressed {\n"
"  /* Change the background color when the button is pressed */\n"
"  background-color: rgb(238, 255, 1);\n"
"  color: black;\n"
"}")
        self.textEdit_96.setObjectName("textEdit_96")


        self.commandLinkButton = HoverCommandLinkButton("Community", self.frame_4)
        self.commandLinkButton.setMinimumSize(QtCore.QSize(111, 40))
        self.commandLinkButton.setMaximumSize(QtCore.QSize(111, 40))
        self.commandLinkButton.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 9pt \"Work Sans\" bold;\n"
"background-color: rgb(238,255,0);\n"
"border: none;\n")
        self.Lay_f4.addWidget(self.commandLinkButton,1,QtCore.Qt.AlignRight)


        self.Lay_f7 = QtWidgets.QHBoxLayout(self.frame_7)
        self.Lay_f7.setObjectName("Lay_f7")

        self.pushButton_9 = QtWidgets.QPushButton(self.frame_7, clicked= lambda: self.save_profile())
        self.pushButton_9.setGeometry(QtCore.QRect(430, 10, 181, 25))
        self.pushButton_9.setMinimumSize(QtCore.QSize(181, 31))
        self.pushButton_9.setMaximumSize(QtCore.QSize(181, 31))
        self.pushButton_9.setText("Save")
        self.pushButton_9.setStyleSheet("\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: black;\n"
"  font: 8pt \"Work Sans\";\n" 
"  border: none;\n"
"  border-radius: 14px;\n"
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
        self.Lay_f7.addWidget(self.pushButton_9,0,QtCore.Qt.AlignBottom)


        self.Lay_f9 = QtWidgets.QHBoxLayout(self.frame_9)
        self.Lay_f9.setObjectName("Lay_f9")

        self.pushButton_92 = QtWidgets.QPushButton(self.frame_9) # , clicked=lambda:self.back2Nomad()
        self.pushButton_92.setGeometry(QtCore.QRect(5, 25, 90, 25))
        self.pushButton_92.setMinimumSize(QtCore.QSize(90, 31))
        self.pushButton_92.setMaximumSize(QtCore.QSize(90, 31))
        self.pushButton_92.setText("exit")
        a = self.resource_path('NoMad.py')
        # thread_login = threading.Thread(target=subprocess.Popen(['python', a]))
        # self.pushButton_92.clicked.connect(lambda: subprocess.Popen(['python', a]))
        self.pushButton_92.clicked.connect(NoMad.close)
        self.pushButton_92.setStyleSheet("\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: rgb(192,192,192);\n"
"  font: 8pt \"Work Sans\";\n" 
"  border: none;\n"
"  border-radius: 14px;\n"
"  color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  /* Change the background color when the button is hovered over */\n"
"  background-color:rgb(192,192,192);\n"
"  color: rgb(173, 173, 173)\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  /* Change the background color when the button is pressed */\n"
"  background-color: rgb(192,192,192);\n"
"  color: white;\n"
"}")
        self.pushButton_92.setObjectName("pushButton_92")
        self.Lay_f9.addWidget(self.pushButton_92,0,QtCore.Qt.AlignTop)

        self.error_dialog = QtWidgets.QErrorMessage()


        self.pushButton_9.raise_()
        self.commandLinkButton.raise_()
        self.frame_5.raise_()
        self.gridLayout.addWidget(self.frame)
        NoMad.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(NoMad)
        self.statusbar.setObjectName("statusbar")
        NoMad.setStatusBar(self.statusbar)

        self.retranslateUi(NoMad)
        QtCore.QMetaObject.connectSlotsByName(NoMad)

    def retranslateUi(self, NoMad):
        _translate = QtCore.QCoreApplication.translate
        NoMad.setWindowTitle(_translate("NoMad", "Input"))  # MainWindow
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    NoMad = QtWidgets.QMainWindow()
    ui = Ui_Save()
    ui.setupUi(NoMad)
    NoMad.show()
    sys.exit(app.exec_())
