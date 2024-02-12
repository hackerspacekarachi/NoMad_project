from PyQt5 import QtCore, QtGui, QtWidgets
from Save import Ui_Save
from PIL import Image
import os, sys, json, time
import ctypes, shutil, subprocess
user32 = ctypes.windll.user32
user32.SetProcessDPIAware()
ax, wae = [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)]

class Ui_NoMad(object):
    global a, b, la, la_x, buzzer #Using 'a' for Vector popup, 'b' for save toggle
    a, b, la, la_x, buzzer = 0, 0, 4, 630, 1


    def openCreateAction(self):
        self.CreateAction.setGeometry(QtCore.QRect(NoMad.frameGeometry().width()-421, 43, 400, NoMad.frameGeometry().height()-114))
        self.profiles_area.setGeometry(QtCore.QRect(0, 190, 370, NoMad.frameGeometry().height()-300))
        # self.verticalScrollBar.setGeometry(QtCore.QRect(350, 140, 16, NoMad.frameGeometry().height()-280))

    def closeCreateAction(self):
        self.CreateAction.setGeometry(QtCore.QRect(NoMad.frameGeometry().width()-421, 43, 0, 0))

    
    def openOptions(self):
        self.options.setGeometry(QtCore.QRect(NoMad.frameGeometry().width()-421, 43, 400, NoMad.frameGeometry().height()-114))

        # update create action size
        self.CreateAction.setGeometry(QtCore.QRect(NoMad.frameGeometry().width()-421, 43, 400, NoMad.frameGeometry().height()-114))
        self.profiles_area.setGeometry(QtCore.QRect(0, 190, 370, NoMad.frameGeometry().height()-300))

    def closeOptions(self):
        self.options.setGeometry(QtCore.QRect(NoMad.frameGeometry().width()-421, 43, 0, 0))

        # update create action size
        self.CreateAction.setGeometry(QtCore.QRect(NoMad.frameGeometry().width()-421, 43, 400, NoMad.frameGeometry().height()-114))
        self.profiles_area.setGeometry(QtCore.QRect(0, 190, 370, NoMad.frameGeometry().height()-300))


    def under_dev(self):
        self.error_dialog.showMessage('Panel under Development!')

    def resource_path(self, relative_path):
        """ Get absolute path to resource, works for dev and for PyInstaller """
        """ https://youtu.be/xJAM8_Lx5mY """
        try:
            # PyInstaller creates a temp folder and stores path in _MEIPASS
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)

    def save_toggle(self):
        global b
        b +=1
        ratio = (135 * (NoMad.frameGeometry().width()//2)) // 586
        wdt = (NoMad.frameGeometry().width()//2)-ratio
        hgt = NoMad.frameGeometry().height()-225
        if b%2 != 0:
            self.frame_9.setGeometry(QtCore.QRect(wdt,  hgt, 195, 86))
        else:
            self.frame_9.setGeometry(QtCore.QRect(wdt,  hgt, 0, 0))


    def buttonz(self, total):
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
                if len(x) == total:
                    Flag = False
            count2 +=1
                
        # y distancing
        for i in range(total):
            # After 5 counts increase y by 60
            if count%5==0 and count!=0:
                # increased y for new line
                y += 60
                
            list.append([x[i],y])
            count+=1
        return list
    

    def action(self, jsn, num):
        self.pushButton_c = QtWidgets.QPushButton(self.profiles_area_2)
        self.pushButton_c.setGeometry(QtCore.QRect(num[0], num[1], 51, 51))
        self.pushButton_c.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_c.setMaximumSize(QtCore.QSize(51, 51))
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
        icon5.addPixmap(QtGui.QPixmap(jsn['image_path']), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.pushButton_c.setIcon(icon5)
        self.pushButton_c.setIconSize(QtCore.QSize(35, 35))
        self.pushButton_c.setToolTip(jsn['settings']['action'])
        self.pushButton_c.raise_()
        self.pushButton_c.raise_()

    def panel(self):
        self.profiles_area = QtWidgets.QWidget(self.CreateAction)
        self.profiles_area.setGeometry(QtCore.QRect(0, 190, 370, 320))
        self.profiles_area.setStyleSheet("background-color: no color;")
        self.profiles_area.setObjectName("profiles_area")

        self.verticalLayout_c = QtWidgets.QVBoxLayout(self.profiles_area)
        self.verticalLayout_c.setObjectName("verticalLayout_c")
        self.verticalLayout_c.setContentsMargins(0,0,0,0)
        self.scrollArea_c = QtWidgets.QScrollArea(self.profiles_area)
        self.scrollArea_c.setStyleSheet("QScrollArea {\n"
                                        "background-color: no color;\n"
                                        "border: none;\n"
                                        "}\n"
                                        "QScrollBar::handle:vertical {\n"
                                        "  border: none;\n"
                                        "  background-color: rgb(59, 59, 90);\n"
                                        "}")
        self.scrollArea_c.setWidgetResizable(True)
        self.scrollArea_c.setObjectName("scrollArea_c")
        self.scrollAreaWidgetContents_c = QtWidgets.QWidget(self.scrollArea_c) #self.scrollArea_c
        self.scrollAreaWidgetContents_c.setGeometry(QtCore.QRect(0, 0, 424, 45665))
        self.scrollAreaWidgetContents_c.setObjectName("scrollAreaWidgetContents_c")
        self.verticalLayout_2c = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_c)
        self.verticalLayout_2c.setObjectName("verticalLayout_2")
        self.verticalLayout_2c.setContentsMargins(0,0,0,0)
        self.profiles_area_2 = QtWidgets.QFrame(self.scrollAreaWidgetContents_c)
        self.profiles_area_2.setMinimumSize(QtCore.QSize(0, 45647))
        self.profiles_area_2.setStyleSheet("background-color: white;")
        self.profiles_area_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.profiles_area_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.profiles_area_2.setObjectName("profiles_area_2")
        self.verticalLayout_2c.addWidget(self.profiles_area_2)
        self.scrollArea_c.setWidget(self.scrollAreaWidgetContents_c)
        self.verticalLayout_c.addWidget(self.scrollArea_c)


    def save_actions(self, folder_name):
        
        folder_name = 'Actions/' + folder_name + '/Action'

        os.makedirs(folder_name, exist_ok=True)  # create the folder if it doesn't exist

        count = 0
        for file_name in os.listdir(folder_name+'/'):
            if file_name.endswith(".json"):
                count +=1
            else:
                pass
        
        dimens = self.buttonz(count)
        var = []
        for file_name in os.listdir(folder_name+'/'):
            if file_name.endswith(".json"):
                with open(folder_name+'/'+file_name, 'r') as p:
                    var.append(json.load(p))
            else:
                pass
            
        if len(var) == 0 and len(dimens) == 0:
            pass
        else:
            for vv,dd in zip(var,dimens):
                self.action(vv, dd)

    def hide_frame_5(self):
        self.options_5.hide()
        self.addKeystrokeButton_o.hide()

    def hide_button(self):
        self.addKeystrokeButton_o.setVisible(False)

    def show_dialog(self):
        dialog = QtWidgets.QMessageBox()
        dialog.setText('Profile has been saved')
        dialog.setWindowTitle('NOMAD')
        dialog.setIcon(QtWidgets.QMessageBox.Warning)
        dialog.exec_()

    def popup(self):
        global buzzer
        user_input, ok_pressed = QtWidgets.QInputDialog.getText(self, "Input Popup", "Enter 1 or 2:")
        if ok_pressed and user_input:
            buzzer = user_input
        return

    def save_profile(self):
        global comb1, comb2, comb3
        if not os.path.isdir('Actions/'+self.commandLinkButton_6.text()):
             QtWidgets.QMessageBox.warning(self.centralwidget, "Warning", "Profile doesn't exist!")
             return
        
        # Get the relevant information from the UI widgets
        if self.image_path is None:
                # show an error message if no image is selected
                QtWidgets.QMessageBox.warning(self.centralwidget, "Warning", "Please select an image first.")
                return

        else:
                image_path = self.image_path  # get the original image file path
                # file_name, ext = os.path.splitext(image_path)  # get the file name and extension
                png_path = 'Actions/'+self.commandLinkButton_6.text()+'/Action/icon/'
                os.makedirs(png_path, exist_ok=True)
                png_path = png_path +image_path.split('/')[-1]  # set the IMG file path with the original file name
                self.image_label.pixmap().save(png_path, "PNG")  # save the image as a PNG file
                settings = {"action": self.lineEdit_o.text(),
                        "delay": self.lineEdit_2o.text(),
                        "delay2": self.lineEdit_3o.text(),
                        "delay3": self.lineEdit_4o.text(),
                        "combobox1": comb1,
                        "combobox2": comb2,
                        "combobox3": comb3, # "" if 'comb3' in globals() and comb3 is not None else comb3
                        "checkbox": self.checkBox_o.isChecked(),
                        "color": "#ff0000"}

                # Create a dictionary with the image path and settings
                profile = {"image_path": png_path, "settings": settings}
                # print('Profiles/icon/'+image_path.split('/')[-1])


                # Write the dictionary to a JSON file inside the "Profiles" folder
                folder_path = '/'.join(png_path.split('/')[:3])
                os.makedirs(folder_path, exist_ok=True)  # create the folder if it doesn't exist
                file_name = "NOMAD_" + str(int(time.time())) + ".json"
                file_path = os.path.join(folder_path, file_name)
                with open(file_path, 'w') as file:
                        json.dump(profile, file, indent=4)

                self.show_dialog()


    def pushButton_handler(self):
        filename, _ = QtWidgets.QFileDialog.getOpenFileName()
        if filename:
            pixmap = QtGui.QPixmap(filename)
            icon = QtGui.QIcon(pixmap)
            self.pushButton_o.setIcon(icon)
            self.pushButton_o.setIconSize(QtCore.QSize(64, 64))
            self.image_label.setPixmap(pixmap)  # set the loaded pixmap to the image_label
            self.image_path = filename  # update the image_path attribute with the selected file path
   

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

    def menu_triggered(self, binary, text, no):
        global comb1, comb2, comb3
        comb3 = ""
        binary.setText(text)
        menu_obj = binary.menu()
        menu_obj.close()
        
        if no == 1:
             comb1 = text
        elif no == 2:
             comb2 = text
        else:
             comb3 = text

    def saveWindow(self):
        self.save_toggle()
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Save()
        self.ui.setupUi(self.window)
        self.window.show()
        NoMad.close()
        # for child in self.frame_5.findChildren(QtWidgets.QPushButton):
        #     child.setEnabled(False)


    def profiles(self):
        global f5_y
        f5_y = 10

        os.makedirs('Actions', exist_ok=True)

        if len(os.listdir('Actions')) == 0:
                self.commandLinkButton_6.setText("Save profile first")
                self.commandLinkButton_6.setStyleSheet("color: rgb(192,192,192);\n"
                "background-color: none;\n"
                "font: 12pt \"Work Sans\";\n"
                "border: none;\n"
                "")

        else:
            for j in os.listdir('Actions'):
                for i in os.listdir('Actions/'+j):
                    if i.endswith(".json"):
                        with open('Actions/'+j+"/"+i) as p:
                            data = json.load(p)
                                        
                        self.pushButton_ = QtWidgets.QPushButton(self.frame_5, clicked = lambda checked, text=data['name']: self.live(text))
                        self.pushButton_.setGeometry(QtCore.QRect(10, f5_y, 130, 25))
                        self.pushButton_.setText(data['name'])
                        # self.pushButton_.clicked.connect(header.setText(datavar['name']))
                        self.pushButton_.setStyleSheet("\n"
                        "\n"
                        "QPushButton {\n"
                        "  /* Set the background color and border for the button */\n"
                        "  background-color: #e7e7e7;\n"
                        "  font: 8pt \"Work Sans\";\n"
                        "  border: none;\n"
                        "  border-radius: 12px;\n"
                        "  color: black;\n"
                        "}\n"
                        "\n"
                        "QPushButton:hover {\n"
                        "  /* Change the background color when the button is hovered over */\n"
                        "  background-color: rgb(238, 255, 1);\n"
                        "  color: black;\n"
                        "}\n"
                        "\n"
                        "QPushButton:pressed {\n"
                        "  /* Change the background color when the button is pressed */\n"
                        "  background-color: black;\n"
                        "  color: rgb(238, 255, 1);\n"
                        "}")
                        self.pushButton_.setObjectName("pushButton_")

                        # space
                        f5_y += 35
                
                        self.commandLinkButton_6.setText(data['name'])
                        self.commandLinkButton_6.setStyleSheet("color: #000000;\n"
                        "background-color: none;\n"
                        "font: 10pt \"Work Sans\";\n"
                        "border: none;\n"
                        "")

                        # Brush color
                        self.pushButton_85.setStyleSheet(f"background-color: {data['color']};\n"
                        "font: 8pt \"Arial\";\n"
                        "color: rgb(0, 0, 0);\n"
                        "border-style: none;\n"
                        "border-radius: 12px;")

        self.pushButton_0 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_0.setGeometry(QtCore.QRect(10, f5_y, 130, 25))
        self.pushButton_0.setText("+ Add new")
        
        self.pushButton_0.setStyleSheet("\n"
        "\n"
        "QPushButton {\n"
        "  /* Set the background color and border for the button */\n"
        "  background-color: black;\n"
        "  font: 8pt \"Work Sans\";\n"
        "  border: none;\n"
        "  border-radius: 12px;\n"
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
        self.pushButton_0.setObjectName("pushButton_0")

        f5_y += 35

    def update(self):
        global buzzer
        buzzer = int(input('Enter 1 or 2: '))
        self.save_actions('Profile'+str(buzzer)+'_demo') #self.commandLinkButton_6.text()


    def live(self, text):
        # global buzzer

        self.commandLinkButton_6.setText(text)
        # self.save_actions(text)
        # QtWidgets.QApplication.processEvents()

        for i in os.listdir('Actions/'+self.commandLinkButton_6.text()):
            if i.endswith(".json"):
                with open('Actions/'+self.commandLinkButton_6.text()+"/"+i) as p:
                        data = json.load(p)

        self.pushButton_85.setStyleSheet(f"background-color: {data['color']};\n"
                "font: 8pt \"Arial\";\n"
                "color: rgb(0, 0, 0);\n"
                "border-style: none;\n"
                "border-radius: 12px;")
        
        # buzzer = True


    def layers(self):
        global la, la_x

        self.pushButton_00 = QtWidgets.QPushButton(self.frame_81)
        self.pushButton_00.setGeometry(QtCore.QRect(la_x, 10, 25, 25)) #35
        self.pushButton_00.setMinimumSize(QtCore.QSize(25, 25))
        self.pushButton_00.setMaximumSize(QtCore.QSize(25, 25))
        self.pushButton_00.setText(str(la))
        self.pushButton_00.setStyleSheet("\n"
        "QPushButton:checked {\n"
        "  background-color: rgb(0, 0, 0);\n"
        "  font: 6pt \"Arial\";\n"
        "  color: rgb(255, 255, 255);\n"
        "  border-radius: 12px;\n"
        "}\n"
        "\n"
        "QPushButton {\n"
        "  /* Set the background color and border for the button */\n"
        "  background-color: rgb(255,255,255);\n"
        "  font: 6pt \"Arial\";\n"
        "  border-radius: 12px;\n"
        "  border-style: none;\n"
        "  color: rgb(0, 0, 0);\n"
        "}")
        self.pushButton_00.setObjectName("pushButton_00")
        self.pushButton_00.setCheckable(True)
        self.Lay_f8.addWidget(self.pushButton_00)

        la +=1
        la_x +=40
        # self.pushButton_89.setGeometry(QtCore.QRect(la_x, 10, 25, 25))
        self.frame_81.setGeometry(QtCore.QRect(0, 0, la_x, 45))

    def Vect_art(self):

        global a 
        a +=1
        if a%2 != 0:
        #     self.profiles()
            self.frame_5.setGeometry(QtCore.QRect(15, 120, 151, f5_y))
        else:
            self.frame_5.setGeometry(QtCore.QRect(15, 120, 0, 0))


    def on_button_clicked(self):
        color = QtWidgets.QColorDialog.getColor()

        if color.isValid():
            self.pushButton_85.setStyleSheet(f"background-color: {color.name()};\n"
                "font: 8pt \"Arial\";\n"
                "color: rgb(0, 0, 0);\n"
                "border-style: none;\n"
                "border-radius: 12px;")
            
            for i in os.listdir('Actions/'+self.commandLinkButton_6.text()):
                if i.endswith(".json"):
                    with open('Actions/'+self.commandLinkButton_6.text()+"/"+i, 'r') as file:
                        data = json.load(file)
                        data["color"] = color.name()
                
                    with open('Actions/'+self.commandLinkButton_6.text()+"/"+i, 'w') as file:
                        json.dump(data, file, indent=4)
        

        
    def setupUi(self, NoMad):
        NoMad.setObjectName("NoMad")
        app_icon = QtGui.QIcon()
        pic = self.resource_path('Icons/logo.png')
        app_icon.addFile(pic) # , QtCore.QSize(60,18)
        # app_icon.addPixmap(QtGui.QPixmap('Icons/logo.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        NoMad.setWindowIcon(app_icon)
        NoMad.setGeometry(QtCore.QRect(int(ax*0.106), int(wae*0.065), 1079, 623))
        # NoMad.setFixedHeight(623)
        # NoMad.setFixedWidth(1079)

        feed_b = Image.open(self.resource_path('Icons/feed_back.png'))
        user = Image.open(self.resource_path('Icons/user.png'))
        feed_b.save("feed_back.png", "PNG")
        user.save("user.png", "PNG")

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

        ###########################################################################
        ########################### CREATE_ACTION #################################
        ###########################################################################
        
        self.CreateAction = QtWidgets.QFrame(self.frame)
        self.CreateAction.setStyleSheet("QFrame { background-color: rgb(255, 255, 255);\n"
                                        "} \n"
                                        "\n"
                                        " QScrollBar:vertical {\n"
                                        "    border: none;\n"
                                        "    background: lightgrey;\n"
                                        "    width: 14px;\n"
                                        "    margin: 15px 0 15px 0;\n"
                                        "    border-radius: 7px;\n"
                                        " }\n"
                                        "/*  HANDLE BAR VERTICAL */\n"
                                        "QScrollBar::handle:vertical {    \n"
                                        "    background-color: #3c3c3c;\n"
                                        "    min-height: 150px;\n"
                                        "    border-radius: 7px;\n"
                                        "}\n"
                                        "QScrollBar::handle:vertical:hover{    \n"
                                        "    background-color: #3c3c3c;\n"
                                        "}\n"
                                        "QScrollBar::handle:vertical:pressed {    \n"
                                        "    background-color: #3c3c3c;\n"
                                        "}\n"
                                        "\n"
                                        "/* BTN TOP - SCROLLBAR */\n"
                                        "QScrollBar::sub-line:vertical {\n"
                                        "    border: none;\n"
                                        "    background-color: lightgrey;\n"
                                        "    height: 15px;\n"
                                        "    border-top-left-radius: 7px;\n"
                                        "    border-top-right-radius: 7px;\n"
                                        "}\n"
                                        "QScrollBar::sub-line:vertical:hover {    \n"
                                        "    background-color: lightgrey;\n"
                                        "}\n"
                                        "QScrollBar::sub-line:vertical:pressed {    \n"
                                        "    background-color: lightgrey;\n"
                                        "}\n"
                                        "\n")
        self.CreateAction.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.CreateAction.setFrameShadow(QtWidgets.QFrame.Raised)
        self.CreateAction.setObjectName("CreateAction")
        self.CreateAction.setGeometry(QtCore.QRect(NoMad.frameGeometry().width()-421, 43, 400, NoMad.frameGeometry().height()-114))


        self.pushButton_4c = QtWidgets.QPushButton(self.CreateAction)
        self.pushButton_4c.setGeometry(QtCore.QRect(190, 50, 88, 32))
        self.pushButton_4c.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_4c.setMaximumSize(QtCore.QSize(88, 32))
        font = QtGui.QFont()
        font.setFamily("Work Sans Light")
        self.pushButton_4c.setFont(font)
        self.pushButton_4c.setStyleSheet("QPushButton:checked {\n"
"background-color: rgb(238, 255, 1);\n"
"color: black;\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: black;\n"
"  border-radius: 15px;\n"
"  color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  /* Change the background color when the button is hovered over */\n"
"  color: rgb(173, 173, 173)\n"
"}")
        self.pushButton_4c.setCheckable(True)
        self.pushButton_4c.setObjectName("pushButton_4c")
        self.buttonGroup_c = QtWidgets.QButtonGroup(self.CreateAction)
        self.buttonGroup_c.setObjectName("buttonGroup_c")
        self.buttonGroup_c.addButton(self.pushButton_4c)
        self.pushButton_3c = QtWidgets.QPushButton(self.CreateAction)
        self.pushButton_3c.setGeometry(QtCore.QRect(100, 50, 88, 32))
        self.pushButton_3c.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_3c.setMaximumSize(QtCore.QSize(88, 32))
        font = QtGui.QFont()
        font.setFamily("Work Sans Light")
        self.pushButton_3c.setFont(font)
        self.pushButton_3c.setStyleSheet("QPushButton:checked {\n"
"background-color: rgb(238, 255, 1);\n"
"color: black;\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: black;\n"
"  border-radius: 15px;\n"
"  color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  /* Change the background color when the button is hovered over */\n"
"  color: rgb(173, 173, 173)\n"
"}")
        self.pushButton_3c.setCheckable(True)
        self.pushButton_3c.setChecked(True)
        self.pushButton_3c.setObjectName("pushButton_3c")
        self.buttonGroup_c.addButton(self.pushButton_3c)
        self.pushButton_5c = QtWidgets.QPushButton(self.CreateAction)
        self.pushButton_5c.setGeometry(QtCore.QRect(280, 50, 88, 32))
        self.pushButton_5c.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_5c.setMaximumSize(QtCore.QSize(88, 32))
        font = QtGui.QFont()
        font.setFamily("Work Sans Light")
        self.pushButton_5c.setFont(font)
        self.pushButton_5c.setStyleSheet("QPushButton:checked {\n"
"background-color: rgb(238, 255, 1);\n"
"color: black;\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: black;\n"
"  border-radius: 15px;\n"
"  color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  /* Change the background color when the button is hovered over */\n"
"  color: rgb(173, 173, 173)\n"
"}")
        self.pushButton_5c.setCheckable(True)
        self.pushButton_5c.setObjectName("pushButton_5c")
        self.buttonGroup_c.addButton(self.pushButton_5c)
        self.pushButton_2c = QtWidgets.QPushButton(self.CreateAction)
        self.pushButton_2c.setGeometry(QtCore.QRect(10, 50, 88, 32))
        self.pushButton_2c.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_2c.setMaximumSize(QtCore.QSize(88, 32))
        font = QtGui.QFont()
        font.setFamily("Work Sans Light")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_2c.setFont(font)
        self.pushButton_2c.setStyleSheet("QPushButton:checked {\n"
"background-color: rgb(238, 255, 1);\n"
"color: black;\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: black;\n"
"  border-radius: 15px;\n"
"  color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  /* Change the background color when the button is hovered over */\n"
"  color: rgb(173, 173, 173)\n"
"}")
        self.pushButton_2c.setCheckable(True)
        self.pushButton_2c.setAutoRepeat(False)
        self.pushButton_2c.setObjectName("pushButton_2c")
        self.buttonGroup_c.addButton(self.pushButton_2c)

        self.pushButton_7c = QtWidgets.QPushButton(self.CreateAction, clicked = lambda: self.closeCreateAction())
        self.pushButton_7c.setGeometry(QtCore.QRect(0, 3, 88, 32))
        self.pushButton_7c.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_7c.setMaximumSize(QtCore.QSize(88, 32))
        self.pushButton_7c.setFont(font)
        self.pushButton_7c.setStyleSheet("QPushButton:checked {\n"
"background-color: none;\n"
"color: rgb(89, 89, 89);\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: none;\n"
"  border-radius: 15px;\n"
"  color: rgb(89, 89, 89);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  /* Change the background color when the button is hovered over */\n"
"  color: rgb(173, 173, 173)\n"
"}")
        self.pushButton_7c.setCheckable(True)
        self.pushButton_7c.setAutoRepeat(False)
        self.pushButton_7c.setObjectName("pushButton_7c")

        self.pushButton_6c = QtWidgets.QPushButton(self.CreateAction, clicked = lambda: self.openOptions())
        self.pushButton_6c.setGeometry(QtCore.QRect(10, 100, 361, 31))
        self.pushButton_6c.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_6c.setMaximumSize(QtCore.QSize(16777215, 13516535))
        font = QtGui.QFont()
        font.setFamily("Work Sans Light")
        self.pushButton_6c.setFont(font)
        self.pushButton_6c.setStyleSheet("\n"
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
        self.pushButton_6c.setObjectName("pushButton_6c")
        self.label_c = QtWidgets.QLabel(self.CreateAction)
        self.label_c.setGeometry(QtCore.QRect(20, 160, 41, 20))
        self.label_c.setStyleSheet("font: 8pt \"Work Sans Medium\";")
        self.label_c.setObjectName("label_c")

        self.profiles_area = QtWidgets.QWidget(self.CreateAction)
        self.profiles_area.setGeometry(QtCore.QRect(0, 190, 370, 320))
        self.profiles_area.setStyleSheet("background-color: no color;")
        self.profiles_area.setObjectName("profiles_area")

        self.verticalLayout_c = QtWidgets.QVBoxLayout(self.profiles_area)
        self.verticalLayout_c.setObjectName("verticalLayout_c")
        self.verticalLayout_c.setContentsMargins(0,0,0,0)
        self.scrollArea_c = QtWidgets.QScrollArea(self.profiles_area)
        self.scrollArea_c.setStyleSheet("QScrollArea {\n"
                                        "background-color: no color;\n"
                                        "border: none;\n"
                                        "}\n"
                                        "QScrollBar::handle:vertical {\n"
                                        "  border: none;\n"
                                        "  background-color: rgb(59, 59, 90);\n"
                                        "}")
        self.scrollArea_c.setWidgetResizable(True)
        self.scrollArea_c.setObjectName("scrollArea_c")
        self.scrollAreaWidgetContents_c = QtWidgets.QWidget(self.scrollArea_c) #self.scrollArea_c
        self.scrollAreaWidgetContents_c.setGeometry(QtCore.QRect(0, 0, 424, 45665))
        self.scrollAreaWidgetContents_c.setObjectName("scrollAreaWidgetContents_c")
        self.verticalLayout_2c = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_c)
        self.verticalLayout_2c.setObjectName("verticalLayout_2")
        self.verticalLayout_2c.setContentsMargins(0,0,0,0)
        self.profiles_area_2 = QtWidgets.QFrame(self.scrollAreaWidgetContents_c)
        self.profiles_area_2.setMinimumSize(QtCore.QSize(0, 45647))
        self.profiles_area_2.setStyleSheet("background-color: white;")
        self.profiles_area_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.profiles_area_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.profiles_area_2.setObjectName("profiles_area_2")
        self.verticalLayout_2c.addWidget(self.profiles_area_2)
        self.scrollArea_c.setWidget(self.scrollAreaWidgetContents_c)
        self.verticalLayout_c.addWidget(self.scrollArea_c)


        ###########################################################################
        ########################### CREATE_ACTION #################################
        ############################################################### END #######


        ###########################################################################
        ###########################    OPTIONS    #################################
        ###########################################################################

        self.options = QtWidgets.QFrame(self.frame)
        self.options.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.options.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.options.setFrameShadow(QtWidgets.QFrame.Raised)
        self.options.setObjectName("options")
        self.options.setGeometry(QtCore.QRect(NoMad.frameGeometry().width()-327, 1, 0,0))

        # Define the image label object and set its properties
        self.image_label = QtWidgets.QLabel(self.options)
        self.image_label.setGeometry(QtCore.QRect(110, 110, 0, 0))
        # self.image_label.setText("")
        # self.image_label.setScaledContents(True)
        self.image_path = None  # add a new attribute to store the file path of the selected image

        self.pushButton_20o = QtWidgets.QPushButton(self.options)
        self.pushButton_20o.setGeometry(QtCore.QRect(280, 50, 88, 32))
        self.pushButton_20o.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_20o.setMaximumSize(QtCore.QSize(88, 32))
        font = QtGui.QFont()
        font.setFamily("Work Sans Light")
        self.pushButton_20o.setFont(font)
        self.pushButton_20o.setStyleSheet("QPushButton:checked {\n"
"background-color: rgb(238, 255, 1);\n"
"color: black;\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: black;\n"
"  border-radius: 15px;\n"
"  color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  /* Change the background color when the button is hovered over */\n"
"  color: rgb(173, 173, 173)\n"
"}")
        self.pushButton_20o.setCheckable(True)
        self.pushButton_20o.setObjectName("pushButton_20o")
        self.buttonGroup_o= QtWidgets.QButtonGroup(self.options)
        self.buttonGroup_o.setObjectName("buttonGroup_o")
        self.buttonGroup_o.addButton(self.pushButton_20o)
        self.pushButton_17o = QtWidgets.QPushButton(self.options)
        self.pushButton_17o.setGeometry(QtCore.QRect(10, 50, 88, 32))
        self.pushButton_17o.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_17o.setMaximumSize(QtCore.QSize(88, 32))
        font = QtGui.QFont()
        font.setFamily("Work Sans Light")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_17o.setFont(font)
        self.pushButton_17o.setStyleSheet("QPushButton:checked {\n"
"background-color: rgb(238, 255, 1);\n"
"color: black;\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: black;\n"
"  border-radius: 15px;\n"
"  color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  /* Change the background color when the button is hovered over */\n"
"  color: rgb(173, 173, 173)\n"
"}")
        self.pushButton_17o.setCheckable(True)
        self.pushButton_17o.setAutoRepeat(False)
        self.pushButton_17o.setObjectName("pushButton_17o")
        self.buttonGroup_o.addButton(self.pushButton_17o)

        self.pushButton_22o = QtWidgets.QPushButton(self.options, clicked = lambda: self.closeOptions())
        self.pushButton_22o.setGeometry(QtCore.QRect(0, 3, 88, 32))
        self.pushButton_22o.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_22o.setMaximumSize(QtCore.QSize(88, 32))
        self.pushButton_22o.setFont(font)
        self.pushButton_22o.setStyleSheet("QPushButton:checked {\n"
"background-color: none;\n"
"color: rgb(89, 89, 89);\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: none;\n"
"  border-radius: 15px;\n"
"  color: rgb(89, 89, 89);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  /* Change the background color when the button is hovered over */\n"
"  color: rgb(173, 173, 173)\n"
"}")
        self.pushButton_22o.setCheckable(True)
        self.pushButton_22o.setAutoRepeat(False)
        self.pushButton_22o.setObjectName("pushButton_22o")

        self.pushButton_18o = QtWidgets.QPushButton(self.options)
        self.pushButton_18o.setGeometry(QtCore.QRect(100, 50, 88, 32))
        self.pushButton_18o.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_18o.setMaximumSize(QtCore.QSize(88, 32))
        font = QtGui.QFont()
        font.setFamily("Work Sans Light")
        self.pushButton_18o.setFont(font)
        self.pushButton_18o.setStyleSheet("QPushButton:checked {\n"
"background-color: rgb(238, 255, 1);\n"
"color: black;\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: black;\n"
"  border-radius: 15px;\n"
"  color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  /* Change the background color when the button is hovered over */\n"
"  color: rgb(173, 173, 173)\n"
"}")
        self.pushButton_18o.setCheckable(True)
        self.pushButton_18o.setChecked(True)
        self.pushButton_18o.setObjectName("pushButton_18o")
        self.buttonGroup_o.addButton(self.pushButton_18o)
        self.pushButton_19o = QtWidgets.QPushButton(self.options)
        self.pushButton_19o.setGeometry(QtCore.QRect(190, 50, 88, 32))
        self.pushButton_19o.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_19o.setMaximumSize(QtCore.QSize(88, 32))
        font = QtGui.QFont()
        font.setFamily("Work Sans Light")
        self.pushButton_19o.setFont(font)
        self.pushButton_19o.setStyleSheet("QPushButton:checked {\n"
"background-color: rgb(238, 255, 1);\n"
"color: black;\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: black;\n"
"  border-radius: 15px;\n"
"  color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  /* Change the background color when the button is hovered over */\n"
"  color: rgb(173, 173, 173)\n"
"}")
        self.pushButton_19o.setCheckable(True)
        self.pushButton_19o.setObjectName("pushButton_19o")
        self.buttonGroup_o.addButton(self.pushButton_19o)
        self.label_o = QtWidgets.QLabel(self.options)
        self.label_o.setGeometry(QtCore.QRect(110, 120, 111, 16))
        self.label_o.setStyleSheet("font: 8pt \"Work Sans Light\";")
        self.label_o.setObjectName("label_o")
        self.pushButton_o = QtWidgets.QPushButton(self.options)
        self.pushButton_o.setGeometry(QtCore.QRect(20, 120, 71, 71))
        self.pushButton_o.setStyleSheet("\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: #f2f2f2;\n"
"  border: none;\n"
"  border-radius: 10px;\n"
"  color: black;\n"
"}\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"  /* Change the background color when the button is pressed */\n"
"  background-color: #3d3d3d;\n"
"  color: white;\n"
"}")
        self.pushButton_o.setText("")
        icon1 = QtGui.QIcon()
        pic = self.resource_path("Icons/add.png")
        icon1.addPixmap(QtGui.QPixmap(pic), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_o.setIcon(icon1)
        self.pushButton_o.setIconSize(QtCore.QSize(35, 35))
        self.pushButton_o.setObjectName("pushButton_o")
        self.lineEdit_o = QtWidgets.QLineEdit(self.options)
        self.lineEdit_o.setGeometry(QtCore.QRect(110, 140, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Work Sans Light")
        self.lineEdit_o.setFont(font)
        self.lineEdit_o.setStyleSheet("QLineEdit {\n"
"    border: 1px solid black;\n"
"    border-radius: 15px;\n"
"    background-color: rgb(242, 242, 242);\n"
"    border-color: #f2f2f2;\n"
"}\n"
"\n"
"QLineEdit::placeholder {\n"
"    padding-left:10px;\n"
"}")
        self.lineEdit_o.setText("")
        self.lineEdit_o.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit_o.setClearButtonEnabled(True)
        self.lineEdit_o.setObjectName("lineEdit_o")
        self.checkBox_o = QtWidgets.QCheckBox(self.options)
        self.checkBox_o.setGeometry(QtCore.QRect(110, 170, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Work Sans Light")
        font.setPointSize(8)
        self.checkBox_o.setFont(font)
        self.checkBox_o.setStyleSheet("")
        self.checkBox_o.setObjectName("checkBox_o")
        self.checkBox_o.setStyleSheet("QCheckBox::indicator:unchecked { border: 1px solid black;\n border-radius: 3px;}\n"
                                      "QCheckBox::indicator:checked { border: 1px solid black;\n border-radius: 3px;\n background-color: #af50ff;}")
        self.line_o = QtWidgets.QFrame(self.options)
        self.line_o.setGeometry(QtCore.QRect(20, 210, 341, 16))
        self.line_o.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_o.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_o.setObjectName("line_o")
        self.options_2 = QtWidgets.QFrame(self.options)
        self.options_2.setGeometry(QtCore.QRect(40, 240, 301, 41))
        self.options_2.setStyleSheet("    border: 1px solid black;\n"
"    border-radius: 20px;\n"
"    background-color: rgb(242, 242, 242);\n"
"    border-color: #f2f2f2;\n"
"")
        self.options_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.options_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.options_2.setObjectName("options_2")

        menu_o = QtWidgets.QMenu()
        menu_o.setStyleSheet("""
        QMenu {
            font: 8pt "Work Sans Medium";
            background-color: #3e3e3e;
            color: white;
            border-radius: 13px;
            border: 2px solid #3e3e3e;
        }

        QMenu::item:selected {
            background-color: #af55ff;
            color: white; 
        }

        /* set the color for the disabled item */
        QMenu::item:disabled {
        background-color: #3e3e3e;
        color: White;
        }
        """)
        menu_o.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint | QtCore.Qt.FramelessWindowHint)
        #menu_o.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        menu_o.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        alphanumerics = [str(i) for i in range(10)] + [chr(i) for i in range(ord('A'), ord('Z')+1)]
        function_keys = ['F{}'.format(i) for i in range(1, 25)]

        K1 = [
            '←', '→', '↑', '↓', 'Tab', 'Space', 'Esc', 'Return', 'Backspace', 'Home', 'End', 'PgUp',
            'PgDown', 'Help', 'Del', 'Execute', 'ins', 'Print', 'Printer', 'Select', {'Alphanumeric': alphanumerics},
            {'Numpad': ['Numpad 0', 'Numpad 1', 'Numpad 2','Numpad 3','Numpad 4', 'Numpad 5','Numpad 6','Numpad 7','Numpad 8','Numpad 9',
            'Numpad *','Numpad +','Numpad -','Numpad .','Numpad /','Numpad Clear', 'Numpad Enter' ]},
            {'F-Keys': function_keys},
           {'Others': ["'",',','-','.','/',';','=','Back','Clear','Favourites','Forward','Home Page','Launch (0)','Launch (1)',
           'Launch Mail','Media Next','Media Play','Media Previous','Media Stop','Menu','Pause','Play','Refresh','Search','Sleep',
           'Stop','Volume Down','Volume Mute','Volume Up','Zoom','[','\\',']']},
           'Shift','Ctrl','Alt','Win' 
        ]

        self.binary_o = QtWidgets.QToolButton(self.options_2)
        self.binary_o.setText("Keystroke 1")
        self.binary_o.setStyleSheet('''
                    font: 8pt "Work Sans";
                    background-color: white;
                    color: black;
                    border-radius: 8px;
                    text-align: left;
                   
                    ''')
        self.binary_o.setGeometry(QtCore.QRect(50, 10, 221, 21))
        self.binary_o.setPopupMode(QtWidgets.QToolButton.InstantPopup)
        menu_o.triggered.connect(lambda y: self.menu_triggered(self.binary_o, y.text(),1))

        self.binary_o.setMenu(menu_o)
        self.add_menu(K1, menu_o)

        self.toolButton_o = QtWidgets.QToolButton(self.options_2)
        self.toolButton_o.setGeometry(QtCore.QRect(10, 10, 31, 21))
        self.toolButton_o.setText("")
        self.toolButton_o.setObjectName("toolButton_o")
        self.options_3 = QtWidgets.QFrame(self.options)
        self.options_3.setGeometry(QtCore.QRect(40, 320, 301, 41))
        self.options_3.setStyleSheet("    border: 1px solid black;\n"
"    border-radius: 20px;\n"
"    background-color: rgb(242, 242, 242);\n"
"    border-color: #f2f2f2;\n"
"")
        self.options_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.options_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.options_3.setObjectName("options_3")

        menu_2o = QtWidgets.QMenu()
        menu_2o.setStyleSheet("""
        QMenu {
            font: 8pt "Work Sans Medium";
            background-color: #3e3e3e;
            color: white;
            border-radius: 13px;
            border: 2px solid #3e3e3e;
        }

        QMenu::item:selected {
            background-color: #af55ff;
            color: white; 
        }

        /* set the color for the disabled item */
        QMenu::item:disabled {
        background-color: #3e3e3e;
        color: White;
        }
        """)
        menu_2o.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint | QtCore.Qt.FramelessWindowHint)
        #menu.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        menu_2o.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        
        self.binary_2o = QtWidgets.QToolButton(self.options_3)
        self.binary_2o.setText("Keystroke 2")
        self.binary_2o.setStyleSheet('''
                    font: 8pt "Work Sans";
                    background-color: white;
                    color: black;
                    border-radius: 8px;
                    text-align: left;
                   
                    ''')
        self.binary_2o.setGeometry(QtCore.QRect(50, 10, 221, 21))
        self.binary_2o.setPopupMode(QtWidgets.QToolButton.InstantPopup)
        menu_2o.triggered.connect(lambda y: self.menu_triggered(self.binary_2o, y.text(),2))


        self.binary_2o.setMenu(menu_2o)
        self.add_menu(K1, menu_2o)

        self.toolButton_2o = QtWidgets.QToolButton(self.options_3)
        self.toolButton_2o.setGeometry(QtCore.QRect(10, 10, 31, 21))
        self.toolButton_2o.setText("")
        self.toolButton_2o.setObjectName("toolButton_2o")
        self.lineEdit_2o = QtWidgets.QLineEdit(self.options)
        self.lineEdit_2o.setGeometry(QtCore.QRect(150, 290, 81, 20))
        font = QtGui.QFont()
        font.setFamily("Work Sans Light")
        self.lineEdit_2o.setFont(font)
        self.lineEdit_2o.setStyleSheet("    border: 1px solid black;\n"
"    border-radius: 10px;\n"
"    background-color: rgb(242, 242, 242);\n"
"    border-color: #f2f2f2;\n"
"")
        self.lineEdit_2o.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2o.setObjectName("lineEdit_2o")
        self.lineEdit_3o = QtWidgets.QLineEdit(self.options)
        self.lineEdit_3o.setGeometry(QtCore.QRect(150, 370, 81, 20))
        font = QtGui.QFont()
        font.setFamily("Work Sans Light")
        self.lineEdit_3o.setFont(font)
        self.lineEdit_3o.setStyleSheet("    border: 1px solid black;\n"
"    border-radius: 10px;\n"
"    background-color: rgb(242, 242, 242);\n"
"    border-color: #f2f2f2;\n"
"")
        self.lineEdit_3o.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_3o.setObjectName("lineEdit_3o")
        self.pushButton_2o = QtWidgets.QPushButton(self.options)
        self.pushButton_2o.setGeometry(QtCore.QRect(10, 500, 361, 31))
        self.pushButton_2o.clicked.connect(self.save_profile)
        font = QtGui.QFont()
        font.setFamily("Work Sans Light")
        self.pushButton_2o.setFont(font)
        self.pushButton_2o.setStyleSheet("\n"
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
        self.pushButton_2o.setObjectName("pushButton_2o")
        self.options_4 = QtWidgets.QFrame(self.options)
        self.options_4.setGeometry(QtCore.QRect(40, 400, 301, 41))
        self.options_4.setStyleSheet("    border: 1px solid black;\n"
"    border-radius: 20px;\n"
"    background-color: rgb(242, 242, 242);\n"
"    border-color: #f2f2f2;\n"
"")
        self.options_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.options_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.options_4.setObjectName("options_4")

        menu_3o = QtWidgets.QMenu()
        menu_3o.setStyleSheet("""
        QMenu {
            font: 8pt "Work Sans Medium";
            background-color: #3e3e3e;
            color: white;
            border-radius: 13px;
            border: 2px solid #3e3e3e;
        }

        QMenu::item:selected {
            background-color: #af55ff;
            color: white; 
        }

        /* set the color for the disabled item */
        QMenu::item:disabled {
        background-color: #3e3e3e;
        color: White;
        }
        """)
        menu_3o.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint | QtCore.Qt.FramelessWindowHint)
        menu_3o.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        
        self.binary_3o = QtWidgets.QToolButton(self.options_4)
        self.binary_3o.setText("Keystroke 3")
        self.binary_3o.setStyleSheet('''
                    font: 8pt "Work Sans";
                    background-color: white;
                    color: black;
                    border-radius: 8px;
                    text-align: left;
                   
                    ''')
        self.binary_3o.setGeometry(QtCore.QRect(50, 10, 221, 21))
        self.binary_3o.setPopupMode(QtWidgets.QToolButton.InstantPopup)
        menu_3o.triggered.connect(lambda y: self.menu_triggered(self.binary_3o, y.text(),3))

        self.binary_3o.setMenu(menu_3o)
        self.add_menu(K1, menu_3o)

        self.toolButton_3o = QtWidgets.QToolButton(self.options_4)
        self.toolButton_3o.setGeometry(QtCore.QRect(10, 9, 31, 20))
        self.toolButton_3o.setText("")
        self.toolButton_3o.setObjectName("toolButton_3o")
        self.lineEdit_4o = QtWidgets.QLineEdit(self.options)
        self.lineEdit_4o.setGeometry(QtCore.QRect(150, 450, 81, 20))
        font = QtGui.QFont()
        font.setFamily("Work Sans Light")
        self.lineEdit_4o.setFont(font)
        self.lineEdit_4o.setStyleSheet("    border: 1px solid black;\n"
"    border-radius: 10px;\n"
"    background-color: rgb(242, 242, 242);\n"
"    border-color: #f2f2f2;\n"
"")
        self.lineEdit_4o.setText("")
        self.lineEdit_4o.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_4o.setObjectName("lineEdit_4o")
        self.options_5 = QtWidgets.QFrame(self.options)
        self.options_5.setGeometry(QtCore.QRect(30, 400, 331, 71))
        self.options_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.options_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.options_5.setObjectName("options_5")
        self.addKeystrokeButton_o = QtWidgets.QPushButton(self.options_5)
        self.addKeystrokeButton_o.setGeometry(QtCore.QRect(10, 20, 301, 31))
        self.addKeystrokeButton_o.setStyleSheet("\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: #f2f2f2;\n"
"  border: none;\n"
"  border-radius: 15px;\n"
"  color: black;\n"
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
"}")
        self.addKeystrokeButton_o.setObjectName("addKeystrokeButton_o")

        self.addKeystrokeButton_o.clicked.connect(self.hide_button)
        self.addKeystrokeButton_o.clicked.connect(self.hide_frame_5)


        ###########################################################################
        ###########################    OPTIONS    #################################
        ############################################################### END #######

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

        self.frame_6 = QtWidgets.QFrame(self.frame)
        self.frame_6.setGeometry(QtCore.QRect(0, 43, 1151, 32))
        self.frame_6.setMinimumSize(QtCore.QSize(1151, 32))
        self.frame_6.setMaximumSize(QtCore.QSize(16777215, 32))
        self.frame_6.setStyleSheet("background-color: no color;\n"
"font: 8pt \"Arial\";\n"
"color: rgb(255, 255, 255);\n")
# "border-style: outset;\n"
# "border-width: 2px;\n"
# "border-radius: 25px;"
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.boxLayout.addWidget(self.frame_6,0,QtCore.Qt.AlignTop) #,0,QtCore.Qt.AlignCenter
        

        self.frame_8 = QtWidgets.QFrame(self.frame)
        self.frame_8.setGeometry(QtCore.QRect(0, 90, 1151, 45))
        self.frame_8.setMinimumSize(QtCore.QSize(1151, 45))
        self.frame_8.setMaximumSize(QtCore.QSize(16777215, 45))
        self.frame_8.setStyleSheet("background-color: no color;\n"
"font: 8pt \"Arial\";\n"
"color: rgb(255, 255, 255);\n")
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.boxLayout.addWidget(self.frame_8,0,QtCore.Qt.AlignTop)
        self.boxLayout.addStretch()

        self.frame_81 = QtWidgets.QFrame(self.frame_8)
        self.frame_81.setGeometry(QtCore.QRect(0, 0, 0, 45))
        self.frame_81.setMinimumSize(QtCore.QSize(115, 45))
        self.frame_81.setMaximumSize(QtCore.QSize(16777215, 45))
        self.frame_81.setStyleSheet("background-color: no color;\n"
"font: 8pt \"Arial\";\n"
"color: rgb(255, 255, 255);\n")
        self.frame_81.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_81.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_81.setObjectName("frame_81")

        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(0, 180, 1047, 313))
        self.frame_2.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"font: 8pt \"Arial\";\n"
"color: rgb(255, 255, 255);\n"
"border-style: outset;\n"
"border-width: 4px;\n"
"border-radius: 20px;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setMinimumSize(QtCore.QSize(1047, 313))
        self.frame_2.setMaximumSize(QtCore.QSize(1047, 313))
        # self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.boxLayout.addWidget(self.frame_2,0,QtCore.Qt.AlignCenter) #,0,QtCore.Qt.AlignCenter
        self.boxLayout.addStretch()

        self.frame_5 = QtWidgets.QFrame(self.frame)  # Vector Art
        self.frame_5.setGeometry(QtCore.QRect(15, 120, 0, 0))
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

        self.frame_7 = QtWidgets.QFrame(self.frame)
        self.frame_7.setGeometry(QtCore.QRect(0, 530, 1151, 55))
        self.frame_7.setMinimumSize(QtCore.QSize(1151, 75))
        self.frame_7.setMaximumSize(QtCore.QSize(16777215, 75))
        self.frame_7.setStyleSheet("background-color: no color;\n"
"font: 8pt \"Arial\";\n"
"color: rgb(255, 255, 255);\n")
# "border-style: outset;\n"
# "border-width: 2px;\n"
# "border-radius: 25px;")
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.boxLayout.addWidget(self.frame_7, 0, QtCore.Qt.AlignBottom) #,0,QtCore.Qt.AlignCenter

        self.frame_9 = QtWidgets.QFrame(self.frame)  # Vector Art
        self.frame_9.setGeometry(QtCore.QRect( (NoMad.frameGeometry().width()//2)-85,  NoMad.frameGeometry().height()-200, 0, 0))
        self.frame_9.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 8pt \"Arial\";\n"
"color: rgb(0, 0, 0);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 16px;"
"border-color: rgb(255, 255, 255);")
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")


        self.pushButton_97 = QtWidgets.QPushButton(self.frame_9)
        self.pushButton_97.setGeometry(QtCore.QRect(10, 10, 175, 28))
        self.pushButton_97.setText("Save")
        self.pushButton_97.setStyleSheet("\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: black;\n"
"  font: 8pt \"Work Sans\";\n"
"  border: none;\n"
"  border-radius: 14px;\n"
"  color: white;\n"
"}\n"
"QPushButton:pressed {\n"
"  /* Change the background color when the button is pressed */\n"
"  background-color: rgb(173, 173, 173);\n"
"  color: black;\n"
"}")
        self.pushButton_97.setObjectName("pushButton_97")

        self.pushButton_98 = QtWidgets.QPushButton(self.frame_9, clicked= lambda: self.saveWindow())
        self.pushButton_98.setGeometry(QtCore.QRect(10, 45, 175, 28))
        self.pushButton_98.setText("+Save new profile")
        self.pushButton_98.setStyleSheet("\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: rgb(238, 255, 1);\n"
"  font: 8pt \"Work Sans\";\n"
"  border: none;\n"
"  border-radius: 12px;\n"
"  color: black;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  /* Change the background color when the button is pressed */\n"
"  background-color: rgb(173, 173, 173);\n"
"  color: black;\n"
"}")
        self.pushButton_98.setObjectName("pushButton_98")

        self.pushButton = QtWidgets.QPushButton(self.frame_2, clicked = lambda: self.popup())
        self.pushButton.setGeometry(QtCore.QRect(104, 16, 53, 53))
        self.pushButton.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton.setMaximumSize(QtCore.QSize(53, 53))
        self.pushButton.setStyleSheet("\n"
"QPushButton:checked {\n"
"color: white;\n"
"border-radius: 12px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: rgb(51,51,51);\n"
"  font: 5pt;\n"
"  border-radius: 12px;\n"
"  border-style: none;\n"
"  color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  /* Change the background color when the button is hovered over */\n"
"  color: rgb(197, 197, 197);\n"
"  border: 2px solid;\n"
"  border-color: #af55ff;\n"
"}")
        self.pushButton.setCheckable(True)
        self.pushButton.setObjectName("pushButton")
        self.buttonGroup.addButton(self.pushButton)

        self.pushButton_3 = QtWidgets.QPushButton(self.frame_2, clicked = lambda: self.openCreateAction())
        self.pushButton_3.setGeometry(QtCore.QRect(162, 16, 53, 53))
        self.pushButton_3.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_3.setMaximumSize(QtCore.QSize(53, 53))
        self.pushButton_3.setStyleSheet("\n"
"QPushButton:checked {\n"
"background-color: #af55ff;\n"
"color: white;\n"
"border-radius: 12px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: rgb(51,51,51);\n"
"  font: 5pt;\n"
"  border-radius: 12px;\n"
"  border-style: none;\n"
"  color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  /* Change the background color when the button is hovered over */\n"
"  color: rgb(197, 197, 197);\n"
"  border: 2px solid;\n"
"  border-color: #af55ff;\n"
"}")
        self.pushButton_3.setCheckable(True)
        self.pushButton_3.setObjectName("pushButton_3")
        self.buttonGroup.addButton(self.pushButton_3)

        self.pushButton_4 = QtWidgets.QPushButton(self.frame_2, clicked = lambda: self.openCreateAction())
        self.pushButton_4.setGeometry(QtCore.QRect(278, 16, 53, 53))
        self.pushButton_4.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_4.setMaximumSize(QtCore.QSize(53, 53))
        self.pushButton_4.setStyleSheet("\n"
"QPushButton:checked {\n"
"background-color: #af55ff;\n"
"color: white;\n"
"border-radius: 12px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: rgb(51,51,51);\n"
"  font: 5pt;\n"
"  border-radius: 12px;\n"
"  border-style: none;\n"
"  color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  /* Change the background color when the button is hovered over */\n"
"  color: rgb(197, 197, 197);\n"
"  border: 2px solid;\n"
"  border-color: #af55ff;\n"
"}")
        self.pushButton_4.setCheckable(True)
        self.pushButton_4.setObjectName("pushButton_4")
        self.buttonGroup.addButton(self.pushButton_4)

        self.pushButton_5 = QtWidgets.QPushButton(self.frame_2, clicked = lambda: self.openCreateAction())
        self.pushButton_5.setGeometry(QtCore.QRect(220, 16, 53, 53))
        self.pushButton_5.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_5.setMaximumSize(QtCore.QSize(53, 53))
        self.pushButton_5.setStyleSheet("\n"
"QPushButton:checked {\n"
"background-color: #af55ff;\n"
"color: white;\n"
"border-radius: 12px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: rgb(51,51,51);\n"
"  font: 5pt;\n"
"  border-radius: 12px;\n"
"  border-style: none;\n"
"  color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  /* Change the background color when the button is hovered over */\n"
"  color: rgb(197, 197, 197);\n"
"  border: 2px solid;\n"
"  border-color: #af55ff;\n"
"}")
        self.pushButton_5.setCheckable(True)
        self.pushButton_5.setObjectName("pushButton_5")
        self.buttonGroup.addButton(self.pushButton_5)

        self.pushButton_6 = QtWidgets.QPushButton(self.frame_2, clicked = lambda: self.openCreateAction())
        self.pushButton_6.setGeometry(QtCore.QRect(394, 16, 53, 53))
        self.pushButton_6.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_6.setMaximumSize(QtCore.QSize(53, 53))
        self.pushButton_6.setStyleSheet("\n"
"QPushButton:checked {\n"
"background-color: #af55ff;\n"
"color: white;\n"
"border-radius: 12px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: rgb(51,51,51);\n"
"  font: 5pt;\n"
"  border-radius: 12px;\n"
"  border-style: none;\n"
"  color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  /* Change the background color when the button is hovered over */\n"
"  color: rgb(197, 197, 197);\n"
"  border: 2px solid;\n"
"  border-color: #af55ff;\n"
"}")
        self.pushButton_6.setCheckable(True)
        self.pushButton_6.setObjectName("pushButton_6")
        self.buttonGroup.addButton(self.pushButton_6)

        self.pushButton_7 = QtWidgets.QPushButton(self.frame_2, clicked = lambda: self.openCreateAction())
        self.pushButton_7.setGeometry(QtCore.QRect(452, 16, 53, 53))
        self.pushButton_7.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_7.setMaximumSize(QtCore.QSize(53, 53))
        self.pushButton_7.setStyleSheet("\n"
"QPushButton:checked {\n"
"background-color: #af55ff;\n"
"color: white;\n"
"border-radius: 12px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: rgb(51,51,51);\n"
"  font: 5pt;\n"
"  border-radius: 12px;\n"
"  border-style: none;\n"
"  color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  /* Change the background color when the button is hovered over */\n"
"  color: rgb(197, 197, 197);\n"
"  border: 2px solid;\n"
"  border-color: #af55ff;\n"
"}")
        self.pushButton_7.setCheckable(True)
        self.pushButton_7.setObjectName("pushButton_7")
        self.buttonGroup.addButton(self.pushButton_7)

        self.pushButton_8 = QtWidgets.QPushButton(self.frame_2, clicked = lambda: self.openCreateAction())
        self.pushButton_8.setGeometry(QtCore.QRect(336, 16, 53, 53))
        self.pushButton_8.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_8.setMaximumSize(QtCore.QSize(53, 53))
        self.pushButton_8.setStyleSheet("\n"
"QPushButton:checked {\n"
"background-color: #af55ff;\n"
"color: white;\n"
"border-radius: 12px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: rgb(51,51,51);\n"
"  font: 5pt;\n"
"  border-radius: 12px;\n"
"  border-style: none;\n"
"  color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  /* Change the background color when the button is hovered over */\n"
"  color: rgb(197, 197, 197);\n"
"  border: 2px solid;\n"
"  border-color: #af55ff;\n"
"}")
        self.pushButton_8.setCheckable(True)
        self.pushButton_8.setObjectName("pushButton_8")
        self.buttonGroup.addButton(self.pushButton_8)

        self.pushButton_10 = QtWidgets.QPushButton(self.frame_2, clicked = lambda: self.openCreateAction())
        self.pushButton_10.setGeometry(QtCore.QRect(626, 16, 53, 53))
        self.pushButton_10.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_10.setMaximumSize(QtCore.QSize(53, 53))
        self.pushButton_10.setStyleSheet("\n"
"QPushButton:checked {\n"
"background-color: #af55ff;\n"
"color: white;\n"
"border-radius: 12px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: rgb(51,51,51);\n"
"  font: 5pt;\n"
"  border-radius: 12px;\n"
"  border-style: none;\n"
"  color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  /* Change the background color when the button is hovered over */\n"
"  color: rgb(197, 197, 197);\n"
"  border: 2px solid;\n"
"  border-color: #af55ff;\n"
"}")
        self.pushButton_10.setCheckable(True)
        self.pushButton_10.setObjectName("pushButton_10")
        self.buttonGroup.addButton(self.pushButton_10)

        self.pushButton_11 = QtWidgets.QPushButton(self.frame_2, clicked = lambda: self.openCreateAction())
        self.pushButton_11.setGeometry(QtCore.QRect(568, 16, 53, 53))
        self.pushButton_11.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_11.setMaximumSize(QtCore.QSize(53, 53))
        self.pushButton_11.setStyleSheet("\n"
"QPushButton:checked {\n"
"background-color: #af55ff;\n"
"color: white;\n"
"border-radius: 12px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: rgb(51,51,51);\n"
"  font: 5pt;\n"
"  border-radius: 12px;\n"
"  border-style: none;\n"
"  color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  /* Change the background color when the button is hovered over */\n"
"  color: rgb(197, 197, 197);\n"
"  border: 2px solid;\n"
"  border-color: #af55ff;\n"
"}")
        self.pushButton_11.setCheckable(True)
        self.pushButton_11.setObjectName("pushButton_11")
        self.buttonGroup.addButton(self.pushButton_11)

        self.pushButton_12 = QtWidgets.QPushButton(self.frame_2, clicked = lambda: self.openCreateAction())
        self.pushButton_12.setGeometry(QtCore.QRect(684, 16, 53, 53))
        self.pushButton_12.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_12.setMaximumSize(QtCore.QSize(53, 53))
        self.pushButton_12.setStyleSheet("\n"
"QPushButton:checked {\n"
"background-color: #af55ff;\n"
"color: white;\n"
"border-radius: 12px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: rgb(51,51,51);\n"
"  font: 5pt;\n"
"  border-radius: 12px;\n"
"  border-style: none;\n"
"  color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  /* Change the background color when the button is hovered over */\n"
"  color: rgb(197, 197, 197);\n"
"  border: 2px solid;\n"
"  border-color: #af55ff;\n"
"}")
        self.pushButton_12.setCheckable(True)
        self.pushButton_12.setObjectName("pushButton_12")
        self.buttonGroup.addButton(self.pushButton_12)

        self.pushButton_13 = QtWidgets.QPushButton(self.frame_2, clicked = lambda: self.openCreateAction())
        self.pushButton_13.setGeometry(QtCore.QRect(187, 73, 53, 53))
        self.pushButton_13.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_13.setMaximumSize(QtCore.QSize(53, 53))
        self.pushButton_13.setStyleSheet("\n"
"QPushButton:checked {\n"
"background-color: #af55ff;\n"
"color: white;\n"
"border-radius: 12px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  font: 5pt;\n"
"  background-color: rgb(51,51,51);\n"
"  border-radius: 12px;\n"
"  border-style: none;\n"
"  color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  /* Change the background color when the button is hovered over */\n"
"  color: rgb(197, 197, 197);\n"
"  border: 2px solid;\n"
"  border-color: #af55ff;\n"
"}")
        self.pushButton_13.setCheckable(True)
        self.pushButton_13.setObjectName("pushButton_13")
        self.buttonGroup.addButton(self.pushButton_13)

        self.pushButton_14 = QtWidgets.QPushButton(self.frame_2, clicked = lambda: self.openCreateAction())
        self.pushButton_14.setGeometry(QtCore.QRect(104, 73, 78, 53))
        self.pushButton_14.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_14.setMaximumSize(QtCore.QSize(78, 53))
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
"border-radius: 12px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: rgb(51,51,51);\n"
"  font: 5pt;\n"
"  border-radius: 12px;\n"
"  border-style: none;\n"
"  color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  /* Change the background color when the button is hovered over */\n"
"  color: rgb(197, 197, 197);\n"
"  border: 2px solid;\n"
"  border-color: #af55ff;\n"
"}")
        self.pushButton_14.setCheckable(True)
        self.pushButton_14.setObjectName("pushButton_14")
        self.buttonGroup.addButton(self.pushButton_14)

        self.pushButton_16 = QtWidgets.QPushButton(self.frame_2, clicked = lambda: self.openCreateAction())
        self.pushButton_16.setGeometry(QtCore.QRect(104, 130, 91, 53))
        self.pushButton_16.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_16.setMaximumSize(QtCore.QSize(91, 53))
        self.pushButton_16.setStyleSheet("\n"
"QPushButton:checked {\n"
"background-color: #af55ff;\n"
"color: white;\n"
"border-radius: 12px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: rgb(51,51,51);\n"
"  font: 5pt;\n"
"  border-radius: 12px;\n"
"  border-style: none;\n"
"  color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  /* Change the background color when the button is hovered over */\n"
"  color: rgb(197, 197, 197);\n"
"  border: 2px solid;\n"
"  border-color: #af55ff;\n"
"}")
        self.pushButton_16.setCheckable(True)
        self.pushButton_16.setObjectName("pushButton_16")
        self.buttonGroup.addButton(self.pushButton_16)

        self.pushButton_17 = QtWidgets.QPushButton(self.frame_2, clicked = lambda: self.openCreateAction())
        self.pushButton_17.setGeometry(QtCore.QRect(104, 187, 111, 53))
        self.pushButton_17.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_17.setMaximumSize(QtCore.QSize(118, 53))
        self.pushButton_17.setStyleSheet("\n"
"QPushButton:checked {\n"
"background-color: #af55ff;\n"
"color: white;\n"
"border-radius: 12px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: rgb(51,51,51);\n"
"  font: 5pt;\n"
"  border-radius: 12px;\n"
"  border-style: none;\n"
"  color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  /* Change the background color when the button is hovered over */\n"
"  color: rgb(197, 197, 197);\n"
"  border: 2px solid;\n"
"  border-color: #af55ff;\n"
"}")
        self.pushButton_17.setCheckable(True)
        self.pushButton_17.setAutoDefault(False)
        self.pushButton_17.setObjectName("pushButton_17")
        self.buttonGroup.addButton(self.pushButton_17)

        self.pushButton_19 = QtWidgets.QPushButton(self.frame_2, clicked = lambda: self.openCreateAction())
        self.pushButton_19.setGeometry(QtCore.QRect(245, 73, 53, 53))
        self.pushButton_19.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_19.setMaximumSize(QtCore.QSize(53, 53))
        self.pushButton_19.setStyleSheet("\n"
"QPushButton:checked {\n"
"background-color: #af55ff;\n"
"color: white;\n"
"border-radius: 12px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: rgb(51,51,51);\n"
"  font: 5pt;\n"
"  border-radius: 12px;\n"
"  border-style: none;\n"
"  color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  /* Change the background color when the button is hovered over */\n"
"  color: rgb(197, 197, 197);\n"
"  border: 2px solid;\n"
"  border-color: #af55ff;\n"
"}")
        self.pushButton_19.setCheckable(True)
        self.pushButton_19.setObjectName("pushButton_19")
        self.buttonGroup.addButton(self.pushButton_19)

        self.pushButton_20 = QtWidgets.QPushButton(self.frame_2, clicked = lambda: self.openCreateAction())
        self.pushButton_20.setGeometry(QtCore.QRect(535, 73, 53, 53))
        self.pushButton_20.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_20.setMaximumSize(QtCore.QSize(53, 53))
        self.pushButton_20.setStyleSheet("\n"
"QPushButton:checked {\n"
"background-color: #af55ff;\n"
"color: white;\n"
"border-radius: 12px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: rgb(51,51,51);\n"
"  font: 5pt;\n"
"  border-radius: 12px;\n"
"  border-style: none;\n"
"  color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  /* Change the background color when the button is hovered over */\n"
"  color: rgb(197, 197, 197);\n"
"  border: 2px solid;\n"
"  border-color: #af55ff;\n"
"}")
        self.pushButton_20.setCheckable(True)
        self.pushButton_20.setObjectName("pushButton_20")
        self.buttonGroup.addButton(self.pushButton_20)

        self.pushButton_21 = QtWidgets.QPushButton(self.frame_2, clicked = lambda: self.openCreateAction())
        self.pushButton_21.setGeometry(QtCore.QRect(361, 73, 53, 53))
        self.pushButton_21.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_21.setMaximumSize(QtCore.QSize(53, 53))
        self.pushButton_21.setStyleSheet("\n"
"QPushButton:checked {\n"
"background-color: #af55ff;\n"
"color: white;\n"
"border-radius: 12px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: rgb(51,51,51);\n"
"  font: 5pt;\n"
"  border-radius: 12px;\n"
"  border-style: none;\n"
"  color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  /* Change the background color when the button is hovered over */\n"
"  color: rgb(197, 197, 197);\n"
"  border: 2px solid;\n"
"  border-color: #af55ff;\n"
"}")
        self.pushButton_21.setCheckable(True)
        self.pushButton_21.setObjectName("pushButton_21")
        self.buttonGroup.addButton(self.pushButton_21)

        self.pushButton_22 = QtWidgets.QPushButton(self.frame_2, clicked = lambda: self.openCreateAction())
        self.pushButton_22.setGeometry(QtCore.QRect(477, 73, 53, 53))
        self.pushButton_22.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_22.setMaximumSize(QtCore.QSize(53, 53))
        self.pushButton_22.setStyleSheet("\n"
"QPushButton:checked {\n"
"background-color: #af55ff;\n"
"color: white;\n"
"border-radius: 12px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: rgb(51,51,51);\n"
"  font: 5pt;\n"
"  border-radius: 12px;\n"
"  border-style: none;\n"
"  color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  /* Change the background color when the button is hovered over */\n"
"  color: rgb(197, 197, 197);\n"
"  border: 2px solid;\n"
"  border-color: #af55ff;\n"
"}")
        self.pushButton_22.setCheckable(True)
        self.pushButton_22.setObjectName("pushButton_22")
        self.buttonGroup.addButton(self.pushButton_22)

        self.pushButton_23 = QtWidgets.QPushButton(self.frame_2, clicked = lambda: self.openCreateAction())
        self.pushButton_23.setGeometry(QtCore.QRect(651, 73, 53, 53))
        self.pushButton_23.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_23.setMaximumSize(QtCore.QSize(53, 53))
        self.pushButton_23.setStyleSheet("\n"
"QPushButton:checked {\n"
"background-color: #af55ff;\n"
"color: white;\n"
"border-radius: 12px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: rgb(51,51,51);\n"
"  font: 5pt;\n"
"  border-radius: 12px;\n"
"  border-style: none;\n"
"  color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  /* Change the background color when the button is hovered over */\n"
"  color: rgb(197, 197, 197);\n"
"  border: 2px solid;\n"
"  border-color: #af55ff;\n"
"}")
        self.pushButton_23.setCheckable(True)
        self.pushButton_23.setObjectName("pushButton_23")
        self.buttonGroup.addButton(self.pushButton_23)

        self.pushButton_24 = QtWidgets.QPushButton(self.frame_2, clicked = lambda: self.openCreateAction())
        self.pushButton_24.setGeometry(QtCore.QRect(419, 73, 53, 53))
        self.pushButton_24.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_24.setMaximumSize(QtCore.QSize(53, 53))
        self.pushButton_24.setStyleSheet("\n"
"QPushButton:checked {\n"
"background-color: #af55ff;\n"
"color: white;\n"
"border-radius: 12px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: rgb(51,51,51);\n"
"  font: 5pt;\n"
"  border-radius: 12px;\n"
"  border-style: none;\n"
"  color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  /* Change the background color when the button is hovered over */\n"
"  color: rgb(197, 197, 197);\n"
"  border: 2px solid;\n"
"  border-color: #af55ff;\n"
"}")
        self.pushButton_24.setCheckable(True)
        self.pushButton_24.setObjectName("pushButton_24")
        self.buttonGroup.addButton(self.pushButton_24)

        self.pushButton_25 = QtWidgets.QPushButton(self.frame_2, clicked = lambda: self.openCreateAction())
        self.pushButton_25.setGeometry(QtCore.QRect(593, 73, 53, 53))
        self.pushButton_25.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_25.setMaximumSize(QtCore.QSize(53, 53))
        self.pushButton_25.setStyleSheet("\n"
"QPushButton:checked {\n"
"background-color: #af55ff;\n"
"color: white;\n"
"border-radius: 12px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: rgb(51,51,51);\n"
"  font: 5pt;\n"
"  border-radius: 12px;\n"
"  border-style: none;\n"
"  color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  /* Change the background color when the button is hovered over */\n"
"  color: rgb(197, 197, 197);\n"
"  border: 2px solid;\n"
"  border-color: #af55ff;\n"
"}")
        self.pushButton_25.setCheckable(True)
        self.pushButton_25.setObjectName("pushButton_25")
        self.buttonGroup.addButton(self.pushButton_25)

        self.pushButton_26 = QtWidgets.QPushButton(self.frame_2, clicked = lambda: self.openCreateAction())
        self.pushButton_26.setGeometry(QtCore.QRect(303, 73, 53, 53))
        self.pushButton_26.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_26.setMaximumSize(QtCore.QSize(53, 53))
        self.pushButton_26.setStyleSheet("\n"
"QPushButton:checked {\n"
"background-color: #af55ff;\n"
"color: white;\n"
"border-radius: 12px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: rgb(51,51,51);\n"
"  font: 5pt;\n"
"  border-radius: 12px;\n"
"  border-style: none;\n"
"  color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  /* Change the background color when the button is hovered over */\n"
"  color: rgb(197, 197, 197);\n"
"  border: 2px solid;\n"
"  border-color: #af55ff;\n"
"}")
        self.pushButton_26.setCheckable(True)
        self.pushButton_26.setObjectName("pushButton_26")
        self.buttonGroup.addButton(self.pushButton_26)

        self.pushButton_27 = QtWidgets.QPushButton(self.frame_2, clicked = lambda: self.openCreateAction())
        self.pushButton_27.setGeometry(QtCore.QRect(374, 130, 53, 53))
        self.pushButton_27.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_27.setMaximumSize(QtCore.QSize(53, 53))
        self.pushButton_27.setStyleSheet("\n"
"QPushButton:checked {\n"
"background-color: #af55ff;\n"
"color: white;\n"
"border-radius: 12px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: rgb(51,51,51);\n"
"  font: 5pt;\n"
"  border-radius: 12px;\n"
"  border-style: none;\n"
"  color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  /* Change the background color when the button is hovered over */\n"
"  color: rgb(197, 197, 197);\n"
"  border: 2px solid;\n"
"  border-color: #af55ff;\n"
"}")
        self.pushButton_27.setCheckable(True)
        self.pushButton_27.setObjectName("pushButton_27")
        self.buttonGroup.addButton(self.pushButton_27)

        self.pushButton_28 = QtWidgets.QPushButton(self.frame_2, clicked = lambda: self.openCreateAction())
        self.pushButton_28.setGeometry(QtCore.QRect(664, 130, 53, 53))
        self.pushButton_28.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_28.setMaximumSize(QtCore.QSize(53, 53))
        self.pushButton_28.setStyleSheet("\n"
"QPushButton:checked {\n"
"background-color: #af55ff;\n"
"color: white;\n"
"border-radius: 12px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: rgb(51,51,51);\n"
"  font: 5pt;\n"
"  border-radius: 12px;\n"
"  border-style: none;\n"
"  color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  /* Change the background color when the button is hovered over */\n"
"  color: rgb(197, 197, 197);\n"
"  border: 2px solid;\n"
"  border-color: #af55ff;\n"
"}")
        self.pushButton_28.setCheckable(True)
        self.pushButton_28.setObjectName("pushButton_28")
        self.buttonGroup.addButton(self.pushButton_28)

        self.pushButton_29 = QtWidgets.QPushButton(self.frame_2, clicked = lambda: self.openCreateAction())
        self.pushButton_29.setGeometry(QtCore.QRect(316, 130, 53, 53))
        self.pushButton_29.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_29.setMaximumSize(QtCore.QSize(53, 53))
        self.pushButton_29.setStyleSheet("\n"
"QPushButton:checked {\n"
"background-color: #af55ff;\n"
"color: white;\n"
"border-radius: 12px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: rgb(51,51,51);\n"
"  font: 5pt;\n"
"  border-radius: 12px;\n"
"  border-style: none;\n"
"  color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  /* Change the background color when the button is hovered over */\n"
"  color: rgb(197, 197, 197);\n"
"  border: 2px solid;\n"
"  border-color: #af55ff;\n"
"}")
        self.pushButton_29.setCheckable(True)
        self.pushButton_29.setObjectName("pushButton_29")
        self.buttonGroup.addButton(self.pushButton_29)

        self.pushButton_30 = QtWidgets.QPushButton(self.frame_2, clicked = lambda: self.openCreateAction())
        self.pushButton_30.setGeometry(QtCore.QRect(548, 130, 53, 53))
        self.pushButton_30.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_30.setMaximumSize(QtCore.QSize(53, 53))
        self.pushButton_30.setStyleSheet("\n"
"QPushButton:checked {\n"
"background-color: #af55ff;\n"
"color: white;\n"
"border-radius: 12px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: rgb(51,51,51);\n"
"  font: 5pt;\n"
"  border-radius: 12px;\n"
"  border-style: none;\n"
"  color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  /* Change the background color when the button is hovered over */\n"
"  color: rgb(197, 197, 197);\n"
"  border: 2px solid;\n"
"  border-color: #af55ff;\n"
"}")
        self.pushButton_30.setCheckable(True)
        self.pushButton_30.setObjectName("pushButton_30")
        self.buttonGroup.addButton(self.pushButton_30)

        self.pushButton_31 = QtWidgets.QPushButton(self.frame_2, clicked = lambda: self.openCreateAction())
        self.pushButton_31.setGeometry(QtCore.QRect(432, 130, 53, 53))
        self.pushButton_31.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_31.setMaximumSize(QtCore.QSize(53, 53))
        self.pushButton_31.setStyleSheet("\n"
"QPushButton:checked {\n"
"background-color: #af55ff;\n"
"color: white;\n"
"border-radius: 12px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: rgb(51,51,51);\n"
"  font: 5pt;\n"
"  border-radius: 12px;\n"
"  border-style: none;\n"
"  color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  /* Change the background color when the button is hovered over */\n"
"  color: rgb(197, 197, 197);\n"
"  border: 2px solid;\n"
"  border-color: #af55ff;\n"
"}")
        self.pushButton_31.setCheckable(True)
        self.pushButton_31.setObjectName("pushButton_31")
        self.buttonGroup.addButton(self.pushButton_31)

        self.pushButton_32 = QtWidgets.QPushButton(self.frame_2, clicked = lambda: self.openCreateAction())
        self.pushButton_32.setGeometry(QtCore.QRect(490, 130, 53, 53))
        self.pushButton_32.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_32.setMaximumSize(QtCore.QSize(53, 53))
        self.pushButton_32.setStyleSheet("\n"
"QPushButton:checked {\n"
"background-color: #af55ff;\n"
"color: white;\n"
"border-radius: 12px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: rgb(51,51,51);\n"
"  font: 5pt;\n"
"  border-radius: 12px;\n"
"  border-style: none;\n"
"  color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  /* Change the background color when the button is hovered over */\n"
"  color: rgb(197, 197, 197);\n"
"  border: 2px solid;\n"
"  border-color: #af55ff;\n"
"}")
        self.pushButton_32.setCheckable(True)
        self.pushButton_32.setObjectName("pushButton_32")
        self.buttonGroup.addButton(self.pushButton_32)

        self.pushButton_33 = QtWidgets.QPushButton(self.frame_2, clicked = lambda: self.openCreateAction())
        self.pushButton_33.setGeometry(QtCore.QRect(606, 130, 53, 53))
        self.pushButton_33.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_33.setMaximumSize(QtCore.QSize(53, 53))
        self.pushButton_33.setStyleSheet("\n"
"QPushButton:checked {\n"
"background-color: #af55ff;\n"
"color: white;\n"
"border-radius: 12px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: rgb(51,51,51);\n"
"  font: 5pt;\n"
"  border-radius: 12px;\n"
"  border-style: none;\n"
"  color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  /* Change the background color when the button is hovered over */\n"
"  color: rgb(197, 197, 197);\n"
"  border: 2px solid;\n"
"  border-color: #af55ff;\n"
"}")
        self.pushButton_33.setCheckable(True)
        self.pushButton_33.setObjectName("pushButton_33")
        self.buttonGroup.addButton(self.pushButton_33)

        self.pushButton_34 = QtWidgets.QPushButton(self.frame_2, clicked = lambda: self.openCreateAction())
        self.pushButton_34.setGeometry(QtCore.QRect(258, 130, 53, 53))
        self.pushButton_34.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_34.setMaximumSize(QtCore.QSize(53, 53))
        self.pushButton_34.setStyleSheet("\n"
"QPushButton:checked {\n"
"background-color: #af55ff;\n"
"color: white;\n"
"border-radius: 12px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: rgb(51,51,51);\n"
"  font: 5pt;\n"
"  border-radius: 12px;\n"
"  border-style: none;\n"
"  color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  /* Change the background color when the button is hovered over */\n"
"  color: rgb(197, 197, 197);\n"
"  border: 2px solid;\n"
"  border-color: #af55ff;\n"
"}")
        self.pushButton_34.setCheckable(True)
        self.pushButton_34.setObjectName("pushButton_34")
        self.buttonGroup.addButton(self.pushButton_34)

        self.pushButton_35 = QtWidgets.QPushButton(self.frame_2, clicked = lambda: self.openCreateAction())
        self.pushButton_35.setGeometry(QtCore.QRect(200, 130, 53, 53))
        self.pushButton_35.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_35.setMaximumSize(QtCore.QSize(53, 53))
        self.pushButton_35.setStyleSheet("\n"
"QPushButton:checked {\n"
"background-color: #af55ff;\n"
"color: white;\n"
"border-radius: 12px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: rgb(51,51,51);\n"
"  font: 5pt;\n"
"  border-radius: 12px;\n"
"  border-style: none;\n"
"  color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  /* Change the background color when the button is hovered over */\n"
"  color: rgb(197, 197, 197);\n"
"  border: 2px solid;\n"
"  border-color: #af55ff;\n"
"}")
        self.pushButton_35.setCheckable(True)
        self.pushButton_35.setObjectName("pushButton_35")
        self.buttonGroup.addButton(self.pushButton_35)

        self.pushButton_36 = QtWidgets.QPushButton(self.frame_2, clicked = lambda: self.openCreateAction())
        self.pushButton_36.setGeometry(QtCore.QRect(394, 187, 53, 53))
        self.pushButton_36.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_36.setMaximumSize(QtCore.QSize(53, 53))
        self.pushButton_36.setStyleSheet("\n"
"QPushButton:checked {\n"
"background-color: #af55ff;\n"
"color: white;\n"
"border-radius: 12px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: rgb(51,51,51);\n"
"  font: 5pt;\n"
"  border-radius: 12px;\n"
"  border-style: none;\n"
"  color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  /* Change the background color when the button is hovered over */\n"
"  color: rgb(197, 197, 197);\n"
"  border: 2px solid;\n"
"  border-color: #af55ff;\n"
"}")
        self.pushButton_36.setCheckable(True)
        self.pushButton_36.setObjectName("pushButton_36")
        self.buttonGroup.addButton(self.pushButton_36)

        self.pushButton_37 = QtWidgets.QPushButton(self.frame_2, clicked = lambda: self.openCreateAction())
        self.pushButton_37.setGeometry(QtCore.QRect(173, 244, 64, 53))
        self.pushButton_37.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_37.setMaximumSize(QtCore.QSize(64, 53))
        self.pushButton_37.setStyleSheet("\n"
"QPushButton:checked {\n"
"background-color: #af55ff;\n"
"color: white;\n"
"border-radius: 12px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: rgb(51,51,51);\n"
"  font: 5pt;\n"
"  border-radius: 12px;\n"
"  border-style: none;\n"
"  color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  /* Change the background color when the button is hovered over */\n"
"  color: rgb(197, 197, 197);\n"
"  border: 2px solid;\n"
"  border-color: #af55ff;\n"
"}")
        self.pushButton_37.setCheckable(True)
        self.pushButton_37.setObjectName("pushButton_37")
        self.buttonGroup.addButton(self.pushButton_37)

        self.pushButton_45 = QtWidgets.QPushButton(self.frame_2, clicked = lambda: self.openCreateAction())
        self.pushButton_45.setGeometry(QtCore.QRect(242, 244, 64, 53))
        self.pushButton_45.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_45.setMaximumSize(QtCore.QSize(64, 53))
        self.pushButton_45.setStyleSheet("\n"
"QPushButton:checked {\n"
"background-color: #af55ff;\n"
"color: white;\n"
"border-radius: 12px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: rgb(51,51,51);\n"
"  font: 5pt;\n"
"  border-radius: 12px;\n"
"  border-style: none;\n"
"  color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  /* Change the background color when the button is hovered over */\n"
"  color: rgb(197, 197, 197);\n"
"  border: 2px solid;\n"
"  border-color: #af55ff;\n"
"}")
        self.pushButton_45.setCheckable(True)
        self.pushButton_45.setObjectName("pushButton_45")
        self.buttonGroup.addButton(self.pushButton_45)

        self.pushButton_46 = QtWidgets.QPushButton(self.frame_2, clicked = lambda: self.openCreateAction())
        self.pushButton_46.setGeometry(QtCore.QRect(311, 244, 371, 53))
        self.pushButton_46.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_46.setMaximumSize(QtCore.QSize(380, 53))
        self.pushButton_46.setStyleSheet("\n"
"QPushButton:checked {\n"
"background-color: #af55ff;\n"
"color: white;\n"
"border-radius: 12px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: rgb(51,51,51);\n"
"  font: 5pt;\n"
"  border-radius: 12px;\n"
"  border-style: none;\n"
"  color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  /* Change the background color when the button is hovered over */\n"
"  color: rgb(197, 197, 197);\n"
"  border: 2px solid;\n"
"  border-color: #af55ff;\n"
"}")
        self.pushButton_46.setText("")
        self.pushButton_46.setCheckable(True)
        self.pushButton_46.setObjectName("pushButton_46")
        self.buttonGroup.addButton(self.pushButton_46)

        self.pushButton_47 = QtWidgets.QPushButton(self.frame_2, clicked = lambda: self.openCreateAction())
        self.pushButton_47.setGeometry(QtCore.QRect(687, 244, 53, 53))
        self.pushButton_47.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_47.setMaximumSize(QtCore.QSize(53, 53))
        self.pushButton_47.setStyleSheet("\n"
"QPushButton:checked {\n"
"background-color: #af55ff;\n"
"color: white;\n"
"border-radius: 12px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: rgb(51,51,51);\n"
"  font: 5pt;\n"
"  border-radius: 12px;\n"
"  border-style: none;\n"
"  color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  /* Change the background color when the button is hovered over */\n"
"  color: rgb(197, 197, 197);\n"
"  border: 2px solid;\n"
"  border-color: #af55ff;\n"
"}")
        self.pushButton_47.setCheckable(True)
        self.pushButton_47.setObjectName("pushButton_47")
        self.buttonGroup.addButton(self.pushButton_47)

        self.pushButton_48 = QtWidgets.QPushButton(self.frame_2, clicked = lambda: self.openCreateAction())
        self.pushButton_48.setGeometry(QtCore.QRect(800, 16, 53, 53))
        self.pushButton_48.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_48.setMaximumSize(QtCore.QSize(53, 53))
        self.pushButton_48.setStyleSheet("\n"
"QPushButton:checked {\n"
"background-color: #af55ff;\n"
"color: white;\n"
"border-radius: 12px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: rgb(51,51,51);\n"
"  font: 5pt;\n"
"  border-radius: 12px;\n"
"  border-style: none;\n"
"  color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  /* Change the background color when the button is hovered over */\n"
"  color: rgb(197, 197, 197);\n"
"  border: 2px solid;\n"
"  border-color: #af55ff;\n"
"}")
        self.pushButton_48.setCheckable(True)
        self.pushButton_48.setObjectName("pushButton_48")
        self.buttonGroup.addButton(self.pushButton_48)

        self.pushButton_50 = QtWidgets.QPushButton(self.frame_2, clicked = lambda: self.openCreateAction())
        self.pushButton_50.setGeometry(QtCore.QRect(742, 16, 53, 53))
        self.pushButton_50.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_50.setMaximumSize(QtCore.QSize(53, 53))
        self.pushButton_50.setStyleSheet("\n"
"QPushButton:checked {\n"
"background-color: #af55ff;\n"
"color: white;\n"
"border-radius: 12px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: rgb(51,51,51);\n"
"  font: 5pt;\n"
"  border-radius: 12px;\n"
"  border-style: none;\n"
"  color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  /* Change the background color when the button is hovered over */\n"
"  color: rgb(197, 197, 197);\n"
"  border: 2px solid;\n"
"  border-color: #af55ff;\n"
"}")
        self.pushButton_50.setCheckable(True)
        self.pushButton_50.setObjectName("pushButton_50")
        self.buttonGroup.addButton(self.pushButton_50)

        self.pushButton_51 = QtWidgets.QPushButton(self.frame_2, clicked = lambda: self.openCreateAction())
        self.pushButton_51.setGeometry(QtCore.QRect(858, 16, 114, 53))
        self.pushButton_51.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_51.setMaximumSize(QtCore.QSize(114, 53))
        self.pushButton_51.setStyleSheet("\n"
"QPushButton:checked {\n"
"background-color: #af55ff;\n"
"color: white;\n"
"border-radius: 12px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: rgb(51,51,51);\n"
"  font: 5pt;\n"
"  border-radius: 12px;\n"
"  border-style: none;\n"
"  color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  /* Change the background color when the button is hovered over */\n"
"  color: rgb(197, 197, 197);\n"
"  border: 2px solid;\n"
"  border-color: #af55ff;\n"
"}")
        self.pushButton_51.setCheckable(True)
        self.pushButton_51.setObjectName("pushButton_51")
        self.buttonGroup.addButton(self.pushButton_51)

        self.pushButton_52 = QtWidgets.QPushButton(self.frame_2, clicked = lambda: self.openCreateAction())
        self.pushButton_52.setGeometry(QtCore.QRect(825, 73, 53, 53))
        self.pushButton_52.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_52.setMaximumSize(QtCore.QSize(53, 53))
        self.pushButton_52.setStyleSheet("\n"
"QPushButton:checked {\n"
"background-color: #af55ff;\n"
"color: white;\n"
"border-radius: 12px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: rgb(51,51,51);\n"
"  font: 5pt;\n"
"  border-radius: 12px;\n"
"  border-style: none;\n"
"  color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  /* Change the background color when the button is hovered over */\n"
"  color: rgb(197, 197, 197);\n"
"  border: 2px solid;\n"
"  border-color: #af55ff;\n"
"}")
        self.pushButton_52.setCheckable(True)
        self.pushButton_52.setObjectName("pushButton_52")
        self.buttonGroup.addButton(self.pushButton_52)

        self.pushButton_53 = QtWidgets.QPushButton(self.frame_2, clicked = lambda: self.openCreateAction())
        self.pushButton_53.setGeometry(QtCore.QRect(767, 73, 53, 53))
        self.pushButton_53.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_53.setMaximumSize(QtCore.QSize(53, 53))
        self.pushButton_53.setStyleSheet("\n"
"QPushButton:checked {\n"
"background-color: #af55ff;\n"
"color: white;\n"
"border-radius: 12px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: rgb(51,51,51);\n"
"  font: 5pt;\n"
"  border-radius: 12px;\n"
"  border-style: none;\n"
"  color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  /* Change the background color when the button is hovered over */\n"
"  color: rgb(197, 197, 197);\n"
"  border: 2px solid;\n"
"  border-color: #af55ff;\n"
"}")
        self.pushButton_53.setCheckable(True)
        self.pushButton_53.setObjectName("pushButton_53")
        self.buttonGroup.addButton(self.pushButton_53)

        self.pushButton_54 = QtWidgets.QPushButton(self.frame_2, clicked = lambda: self.openCreateAction())
        self.pushButton_54.setGeometry(QtCore.QRect(709, 73, 53, 53))
        self.pushButton_54.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_54.setMaximumSize(QtCore.QSize(53, 53))
        self.pushButton_54.setStyleSheet("\n"
"QPushButton:checked {\n"
"background-color: #af55ff;\n"
"color: white;\n"
"border-radius: 12px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: rgb(51,51,51);\n"
"  font: 5pt;\n"
"  border-radius: 12px;\n"
"  border-style: none;\n"
"  color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  /* Change the background color when the button is hovered over */\n"
"  color: rgb(197, 197, 197);\n"
"  border: 2px solid;\n"
"  border-color: #af55ff;\n"
"}")
        self.pushButton_54.setCheckable(True)
        self.pushButton_54.setObjectName("pushButton_54")
        self.buttonGroup.addButton(self.pushButton_54)

        self.pushButton_55 = QtWidgets.QPushButton(self.frame_2, clicked = lambda: self.openCreateAction())
        self.pushButton_55.setGeometry(QtCore.QRect(883, 73, 88, 53))
        self.pushButton_55.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_55.setMaximumSize(QtCore.QSize(105, 53))
        self.pushButton_55.setStyleSheet("\n"
"QPushButton:checked {\n"
"background-color: #af55ff;\n"
"color: white;\n"
"border-radius: 12px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: rgb(51,51,51);\n"
"  font: 5pt;\n"
"  border-radius: 12px;\n"
"  border-style: none;\n"
"  color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  /* Change the background color when the button is hovered over */\n"
"  color: rgb(197, 197, 197);\n"
"  border: 2px solid;\n"
"  border-color: #af55ff;\n"
"}")
        self.pushButton_55.setCheckable(True)
        self.pushButton_55.setObjectName("pushButton_55")
        self.buttonGroup.addButton(self.pushButton_55)

        self.pushButton_56 = QtWidgets.QPushButton(self.frame_2, clicked = lambda: self.openCreateAction())
        self.pushButton_56.setGeometry(QtCore.QRect(780, 130, 53, 53))
        self.pushButton_56.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_56.setMaximumSize(QtCore.QSize(53, 53))
        self.pushButton_56.setStyleSheet("\n"
"QPushButton:checked {\n"
"background-color: #af55ff;\n"
"color: white;\n"
"border-radius: 12px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: rgb(51,51,51);\n"
"  font: 5pt;\n"
"  border-radius: 12px;\n"
"  border-style: none;\n"
"  color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  /* Change the background color when the button is hovered over */\n"
"  color: rgb(197, 197, 197);\n"
"  border: 2px solid;\n"
"  border-color: #af55ff;\n"
"}")
        self.pushButton_56.setCheckable(True)
        self.pushButton_56.setObjectName("pushButton_56")
        self.buttonGroup.addButton(self.pushButton_56)

        self.pushButton_57 = QtWidgets.QPushButton(self.frame_2, clicked = lambda: self.openCreateAction())
        self.pushButton_57.setGeometry(QtCore.QRect(722, 130, 53, 53))
        self.pushButton_57.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_57.setMaximumSize(QtCore.QSize(53, 53))
        self.pushButton_57.setStyleSheet("\n"
"QPushButton:checked {\n"
"background-color: #af55ff;\n"
"color: white;\n"
"border-radius: 12px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: rgb(51,51,51);\n"
"  font: 5pt;\n"
"  border-radius: 12px;\n"
"  border-style: none;\n"
"  color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  /* Change the background color when the button is hovered over */\n"
"  color: rgb(197, 197, 197);\n"
"  border: 2px solid;\n"
"  border-color: #af55ff;\n"
"}")
        self.pushButton_57.setCheckable(True)
        self.pushButton_57.setObjectName("pushButton_57")
        self.buttonGroup.addButton(self.pushButton_57)

        self.pushButton_58 = QtWidgets.QPushButton(self.frame_2, clicked = lambda: self.openCreateAction())
        self.pushButton_58.setGeometry(QtCore.QRect(838, 130, 134, 53))
        self.pushButton_58.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_58.setMaximumSize(QtCore.QSize(380, 53))
        self.pushButton_58.setStyleSheet("\n"
"QPushButton:checked {\n"
"background-color: #af55ff;\n"
"color: white;\n"
"border-radius: 12px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: rgb(51,51,51);\n"
"  font: 5pt;\n"
"  border-radius: 12px;\n"
"  border-style: none;\n"
"  color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  /* Change the background color when the button is hovered over */\n"
"  color: rgb(197, 197, 197);\n"
"  border: 2px solid;\n"
"  border-color: #af55ff;\n"
"}")
        self.pushButton_58.setCheckable(True)
        self.pushButton_58.setObjectName("pushButton_58")
        self.buttonGroup.addButton(self.pushButton_58)

        self.pushButton_60 = QtWidgets.QPushButton(self.frame_2, clicked = lambda: self.openCreateAction())
        self.pushButton_60.setGeometry(QtCore.QRect(800, 187, 114, 53))
        self.pushButton_60.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_60.setMaximumSize(QtCore.QSize(380, 53))
        self.pushButton_60.setStyleSheet("\n"
"QPushButton:checked {\n"
"background-color: #af55ff;\n"
"color: white;\n"
"border-radius: 12px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: rgb(51,51,51);\n"
"  font: 5pt;\n"
"  border-radius: 12px;\n"
"  border-style: none;\n"
"  color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  /* Change the background color when the button is hovered over */\n"
"  color: rgb(197, 197, 197);\n"
"  border: 2px solid;\n"
"  border-color: #af55ff;\n"
"}")
        self.pushButton_60.setCheckable(True)
        self.pushButton_60.setObjectName("pushButton_60")
        self.buttonGroup.addButton(self.pushButton_60)

        self.pushButton_61 = QtWidgets.QPushButton(self.frame_2, clicked = lambda: self.openCreateAction())
        self.pushButton_61.setGeometry(QtCore.QRect(919, 187, 53, 53))
        self.pushButton_61.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_61.setMaximumSize(QtCore.QSize(53, 53))
        self.pushButton_61.setStyleSheet("\n"
"QPushButton:checked {\n"
"background-color: #af55ff;\n"
"color: white;\n"
"border-radius: 12px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: rgb(51,51,51);\n"
"  font: 5pt;\n"
"  border-radius: 12px;\n"
"  border-style: none;\n"
"  color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  /* Change the background color when the button is hovered over */\n"
"  color: rgb(197, 197, 197);\n"
"  border: 2px solid;\n"
"  border-color: #af55ff;\n"
"}")
        self.pushButton_61.setCheckable(True)
        self.pushButton_61.setObjectName("pushButton_61")
        self.buttonGroup.addButton(self.pushButton_61)

        self.pushButton_62 = QtWidgets.QPushButton(self.frame_2, clicked = lambda: self.openCreateAction())
        self.pushButton_62.setGeometry(QtCore.QRect(803, 244, 53, 53))
        self.pushButton_62.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_62.setMaximumSize(QtCore.QSize(53, 53))
        self.pushButton_62.setStyleSheet("\n"
"QPushButton:checked {\n"
"background-color: #af55ff;\n"
"color: white;\n"
"border-radius: 12px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: rgb(51,51,51);\n"
"  font: 5pt;\n"
"  border-radius: 12px;\n"
"  border-style: none;\n"
"  color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  /* Change the background color when the button is hovered over */\n"
"  color: rgb(197, 197, 197);\n"
"  border: 2px solid;\n"
"  border-color: #af55ff;\n"
"}")
        self.pushButton_62.setCheckable(True)
        self.pushButton_62.setObjectName("pushButton_62")
        self.buttonGroup.addButton(self.pushButton_62)

        self.pushButton_63 = QtWidgets.QPushButton(self.frame_2, clicked = lambda: self.openCreateAction())
        self.pushButton_63.setGeometry(QtCore.QRect(745, 244, 53, 53))
        self.pushButton_63.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_63.setMaximumSize(QtCore.QSize(53, 53))
        self.pushButton_63.setStyleSheet("\n"
"QPushButton:checked {\n"
"background-color: #af55ff;\n"
"color: white;\n"
"border-radius: 12px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: rgb(51,51,51);\n"
"  font: 5pt;\n"
"  border-radius: 12px;\n"
"  border-style: none;\n"
"  color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  /* Change the background color when the button is hovered over */\n"
"  color: rgb(197, 197, 197);\n"
"  border: 2px solid;\n"
"  border-color: #af55ff;\n"
"}")
        self.pushButton_63.setCheckable(True)
        self.pushButton_63.setObjectName("pushButton_63")
        self.buttonGroup.addButton(self.pushButton_63)

        self.pushButton_64 = QtWidgets.QPushButton(self.frame_2, clicked = lambda: self.openCreateAction())
        self.pushButton_64.setGeometry(QtCore.QRect(861, 244, 53, 53))
        self.pushButton_64.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_64.setMaximumSize(QtCore.QSize(53, 53))
        self.pushButton_64.setStyleSheet("\n"
"QPushButton:checked {\n"
"background-color: #af55ff;\n"
"color: white;\n"
"border-radius: 12px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: rgb(51,51,51);\n"
"  font: 5pt;\n"
"  border-radius: 12px;\n"
"  border-style: none;\n"
"  color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  /* Change the background color when the button is hovered over */\n"
"  color: rgb(197, 197, 197);\n"
"  border: 2px solid;\n"
"  border-color: #af55ff;\n"
"}")
        self.pushButton_64.setCheckable(True)
        self.pushButton_64.setObjectName("pushButton_64")
        self.buttonGroup.addButton(self.pushButton_64)

        self.pushButton_65 = QtWidgets.QPushButton(self.frame_2, clicked = lambda: self.openCreateAction())
        self.pushButton_65.setGeometry(QtCore.QRect(919, 244, 53, 53))
        self.pushButton_65.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_65.setMaximumSize(QtCore.QSize(53, 53))
        self.pushButton_65.setStyleSheet("\n"
"QPushButton:checked {\n"
"background-color: #af55ff;\n"
"color: white;\n"
"border-radius: 12px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: rgb(51,51,51);\n"
"  font: 5pt;\n"
"  border-radius: 12px;\n"
"  border-style: none;\n"
"  color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  /* Change the background color when the button is hovered over */\n"
"  color: rgb(197, 197, 197);\n"
"  border: 2px solid;\n"
"  border-color: #af55ff;\n"
"}")
        self.pushButton_65.setCheckable(True)
        self.pushButton_65.setObjectName("pushButton_65")
        self.buttonGroup.addButton(self.pushButton_65)

        self.pushButton_66 = QtWidgets.QPushButton(self.frame_2, clicked = lambda: self.openCreateAction())
        self.pushButton_66.setGeometry(QtCore.QRect(977, 244, 53, 53))
        self.pushButton_66.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_66.setMaximumSize(QtCore.QSize(53, 53))
        self.pushButton_66.setStyleSheet("\n"
"QPushButton:checked {\n"
"background-color: #af55ff;\n"
"color: white;\n"
"border-radius: 12px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: rgb(51,51,51);\n"
"  font: 5pt;\n"
"  border-radius: 12px;\n"
"  border-style: none;\n"
"  color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  /* Change the background color when the button is hovered over */\n"
"  color: rgb(197, 197, 197);\n"
"  border: 2px solid;\n"
"  border-color: #af55ff;\n"
"}")
        self.pushButton_66.setCheckable(True)
        self.pushButton_66.setObjectName("pushButton_66")
        self.buttonGroup.addButton(self.pushButton_66)

        self.pushButton_67 = QtWidgets.QPushButton(self.frame_2, clicked = lambda: self.openCreateAction())
        self.pushButton_67.setGeometry(QtCore.QRect(510, 16, 53, 53))
        self.pushButton_67.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_67.setMaximumSize(QtCore.QSize(53, 53))
        self.pushButton_67.setStyleSheet("\n"
"QPushButton:checked {\n"
"background-color: #af55ff;\n"
"color: white;\n"
"border-radius: 12px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: rgb(51,51,51);\n"
"  font: 5pt;\n"
"  border-radius: 12px;\n"
"  border-style: none;\n"
"  color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  /* Change the background color when the button is hovered over */\n"
"  color: rgb(197, 197, 197);\n"
"  border: 2px solid;\n"
"  border-color: #af55ff;\n"
"}")
        self.pushButton_67.setCheckable(True)
        self.pushButton_67.setObjectName("pushButton_67")
        self.buttonGroup.addButton(self.pushButton_67)

        self.pushButton_70 = QtWidgets.QPushButton(self.frame_2, clicked = lambda: self.openCreateAction())
        self.pushButton_70.setGeometry(QtCore.QRect(987, 26, 31, 31))
        self.pushButton_70.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_70.setMaximumSize(QtCore.QSize(53, 53))
        self.pushButton_70.setStyleSheet("\n"
"QPushButton:checked {\n"
"background-color: #af55ff;\n"
"color: white;\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: #c2c2c2;\n"
"  font: 5pt;\n"
"  border-radius: 15px;\n"
"  border-style: none;\n"
"  color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  /* Change the background color when the button is hovered over */\n"
"  color: rgb(197, 197, 197);\n"
"  border: 2px solid;\n"
"  border-color: #af55ff;\n"
"}")
        self.pushButton_70.setText("")
        self.pushButton_70.setCheckable(True)
        self.pushButton_70.setObjectName("pushButton_70")
        self.buttonGroup.addButton(self.pushButton_70)

        self.pushButton_71 = QtWidgets.QPushButton(self.frame_2, clicked = lambda: self.openCreateAction())
        self.pushButton_71.setGeometry(QtCore.QRect(977, 73, 53, 53))
        self.pushButton_71.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_71.setMaximumSize(QtCore.QSize(53, 53))
        self.pushButton_71.setStyleSheet("\n"
"QPushButton:checked {\n"
"background-color: #af55ff;\n"
"color: white;\n"
"border-radius: 12px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: rgb(51,51,51);\n"
"  font: 5pt;\n"
"  border-radius: 12px;\n"
"  border-style: none;\n"
"  color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  /* Change the background color when the button is hovered over */\n"
"  color: rgb(197, 197, 197);\n"
"  border: 2px solid;\n"
"  border-color: #af55ff;\n"
"}")
        self.pushButton_71.setCheckable(True)
        self.pushButton_71.setObjectName("pushButton_71")
        self.buttonGroup.addButton(self.pushButton_71)

        self.pushButton_72 = QtWidgets.QPushButton(self.frame_2, clicked = lambda: self.openCreateAction())
        self.pushButton_72.setGeometry(QtCore.QRect(977, 130, 53, 53))
        self.pushButton_72.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_72.setMaximumSize(QtCore.QSize(53, 53))
        self.pushButton_72.setStyleSheet("\n"
"QPushButton:checked {\n"
"background-color: #af55ff;\n"
"color: white;\n"
"border-radius: 12px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: rgb(51,51,51);\n"
"  font: 5pt;\n"
"  border-radius: 12px;\n"
"  border-style: none;\n"
"  color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  /* Change the background color when the button is hovered over */\n"
"  color: rgb(197, 197, 197);\n"
"  border: 2px solid;\n"
"  border-color: #af55ff;\n"
"}")
        self.pushButton_72.setCheckable(True)
        self.pushButton_72.setObjectName("pushButton_72")
        self.buttonGroup.addButton(self.pushButton_72)

        self.pushButton_73 = QtWidgets.QPushButton(self.frame_2, clicked = lambda: self.openCreateAction())
        self.pushButton_73.setGeometry(QtCore.QRect(977, 187, 53, 53))
        self.pushButton_73.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_73.setMaximumSize(QtCore.QSize(53, 53))
        self.pushButton_73.setStyleSheet("\n"
"QPushButton:checked {\n"
"background-color: #af55ff;\n"
"color: white;\n"
"border-radius: 12px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: rgb(51,51,51);\n"
"  font: 5pt;\n"
"  border-radius: 12px;\n"
"  border-style: none;\n"
"  color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  /* Change the background color when the button is hovered over */\n"
"  color: rgb(197, 197, 197);\n"
"  border: 2px solid;\n"
"  border-color: #af55ff;\n"
"}")
        self.pushButton_73.setCheckable(True)
        self.pushButton_73.setObjectName("pushButton_73")
        self.buttonGroup.addButton(self.pushButton_73)

        self.pushButton_74 = QtWidgets.QPushButton(self.frame_2, clicked = lambda: self.openCreateAction())
        self.pushButton_74.setGeometry(QtCore.QRect(57, 260, 27, 27))
        self.pushButton_74.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_74.setMaximumSize(QtCore.QSize(53, 53))
        self.pushButton_74.setStyleSheet("\n"
"QPushButton:checked {\n"
"background-color: #af55ff;\n"
"color: white;\n"
"border-radius: 13px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: rgb(51,51,51);\n"
"  border-radius: 13px;\n"
"  border-style: none;\n"
"  color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  /* Change the background color when the button is hovered over */\n"
"  color: rgb(197, 197, 197);\n"
"  border: 2px solid;\n"
"  border-color: #af55ff;\n"
"}")
        self.pushButton_74.setText("")
        self.pushButton_74.setCheckable(True)
        self.pushButton_74.setObjectName("pushButton_74")
        self.buttonGroup.addButton(self.pushButton_74)

        self.pushButton_75 = QtWidgets.QPushButton(self.frame_2, clicked = lambda: self.openCreateAction())
        self.pushButton_75.setGeometry(QtCore.QRect(20, 260, 27, 27))
        self.pushButton_75.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_75.setMaximumSize(QtCore.QSize(53, 53))
        self.pushButton_75.setStyleSheet("\n"
"QPushButton:checked {\n"
"background-color: #af55ff;\n"
"color: white;\n"
"border-radius: 13px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: rgb(51,51,51);\n"
"  border-radius: 13px;\n"
"  border-style: none;\n"
"  color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  /* Change the background color when the button is hovered over */\n"
"  color: rgb(197, 197, 197);\n"
"  border: 2px solid;\n"
"  border-color: #af55ff;\n"
"}")
        self.pushButton_75.setText("")
        self.pushButton_75.setCheckable(True)
        self.pushButton_75.setObjectName("pushButton_75")
        self.buttonGroup.addButton(self.pushButton_75)

        self.pushButton_76 = QtWidgets.QPushButton(self.frame_2, clicked = lambda: self.openCreateAction())
        self.pushButton_76.setGeometry(QtCore.QRect(57, 24, 27, 27))
        self.pushButton_76.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_76.setMaximumSize(QtCore.QSize(53, 53))
        self.pushButton_76.setStyleSheet("\n"
"QPushButton:checked {\n"
"background-color: #af55ff;\n"
"color: white;\n"
"border-radius: 13px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: #c2c2c2;\n"
"  border-radius: 13px;\n"
"  border-style: none;\n"
"  color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  /* Change the background color when the button is hovered over */\n"
"  color: rgb(197, 197, 197);\n"
"  border: 2px solid;\n"
"  border-color: #af55ff;\n"
"}")
        self.pushButton_76.setText("")
        self.pushButton_76.setCheckable(True)
        self.pushButton_76.setObjectName("pushButton_76")
        self.buttonGroup.addButton(self.pushButton_76)

        self.pushButton_77 = QtWidgets.QPushButton(self.frame_2, clicked = lambda: self.openCreateAction())
        self.pushButton_77.setGeometry(QtCore.QRect(20, 24, 27, 27))
        self.pushButton_77.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_77.setMaximumSize(QtCore.QSize(53, 53))
        self.pushButton_77.setStyleSheet("\n"
"QPushButton:checked {\n"
"background-color: #af55ff;\n"
"color: white;\n"
"border-radius: 13px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: #c2c2c2;\n"
"  border-radius: 13px;\n"
"  border-style: none;\n"
"  color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  /* Change the background color when the button is hovered over */\n"
"  color: rgb(197, 197, 197);\n"
"  border: 2px solid;\n"
"  border-color: #af55ff;\n"
"}")
        self.pushButton_77.setText("")
        self.pushButton_77.setCheckable(True)
        self.pushButton_77.setObjectName("pushButton_77")
        self.buttonGroup.addButton(self.pushButton_77)

        self.pushButton_78 = QtWidgets.QPushButton(self.frame_2, clicked = lambda: self.openCreateAction())
        self.pushButton_78.setGeometry(QtCore.QRect(22, 75, 58, 130))
        self.pushButton_78.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_78.setMaximumSize(QtCore.QSize(81, 201))
        self.pushButton_78.setStyleSheet("\n"
"QPushButton:checked {\n"
"background-color: #af55ff;\n"
"color: white;\n"
"border-radius: 6px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: #c2c2c2;\n"
"  border-radius: 6px;\n"
"  border-style: none;\n"
"  color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  /* Change the background color when the button is hovered over */\n"
"  color: rgb(197, 197, 197);\n"
"  border: 2px solid;\n"
"  border-color: #af55ff;\n"
"}")
        self.pushButton_78.setText("")
        self.pushButton_78.setCheckable(True)
        self.pushButton_78.setObjectName("pushButton_78")
        self.buttonGroup.addButton(self.pushButton_78)

        self.pushButton_81 = QtWidgets.QPushButton(self.frame_2, clicked = lambda: self.openCreateAction())
        self.pushButton_81.setGeometry(QtCore.QRect(57, 224, 27, 27))
        self.pushButton_81.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_81.setMaximumSize(QtCore.QSize(53, 53))
        self.pushButton_81.setStyleSheet("\n"
"QPushButton:checked {\n"
"background-color: #af55ff;\n"
"color: white;\n"
"border-radius: 13px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: rgb(51,51,51);\n"
"  border-radius: 13px;\n"
"  border-style: none;\n"
"  color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  /* Change the background color when the button is hovered over */\n"
"  color: rgb(197, 197, 197);\n"
"  border: 2px solid;\n"
"  border-color: #af55ff;\n"
"}")
        self.pushButton_81.setText("")
        self.pushButton_81.setCheckable(True)
        self.pushButton_81.setObjectName("pushButton_81")
        self.buttonGroup.addButton(self.pushButton_81)

        self.pushButton_82 = QtWidgets.QPushButton(self.frame_2, clicked = lambda: self.openCreateAction())
        self.pushButton_82.setGeometry(QtCore.QRect(20, 224, 27, 27))
        self.pushButton_82.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_82.setMaximumSize(QtCore.QSize(53, 53))
        self.pushButton_82.setStyleSheet("\n"
"QPushButton:checked {\n"
"background-color: #af55ff;\n"
"color: white;\n"
"border-radius: 13px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: rgb(51,51,51);\n"
"  border-radius: 13px;\n"
"  border-style: none;\n"
"  color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  /* Change the background color when the button is hovered over */\n"
"  color: rgb(197, 197, 197);\n"
"  border: 2px solid;\n"
"  border-color: #af55ff;\n"
"}")
        self.pushButton_82.setText("")
        self.pushButton_82.setCheckable(True)
        self.pushButton_82.setObjectName("pushButton_82")
        self.buttonGroup.addButton(self.pushButton_82)


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

#         self.pushButton_93 = QtWidgets.QPushButton(self.frame_5)
#         self.pushButton_93.setGeometry(QtCore.QRect(10, 10, 130, 25))
#         self.pushButton_93.setText("Vector Art")
#         self.pushButton_93.setStyleSheet("\n"
# "\n"
# "QPushButton {\n"
# "  /* Set the background color and border for the button */\n"
# "  background-color: #e7e7e7;\n"
# "  font: 8pt \"Work Sans\";\n"
# "  border: none;\n"
# "  border-radius: 12px;\n"
# "  color: black;\n"
# "}\n"
# "\n"
# "QPushButton:hover {\n"
# "  /* Change the background color when the button is hovered over */\n"
# "  background-color:nocolor;\n"
# "  color: rgb(173, 173, 173)\n"
# "}\n"
# "\n"
# "QPushButton:pressed {\n"
# "  /* Change the background color when the button is pressed */\n"
# "  background-color: rgb(238, 255, 1);\n"
# "  color: black;\n"
# "}")
#         self.pushButton_93.setObjectName("pushButton_93")

#         self.pushButton_94 = QtWidgets.QPushButton(self.frame_5)
#         self.pushButton_94.setGeometry(QtCore.QRect(10, 45, 130, 25))
#         self.pushButton_94.setText("Video editing")
#         self.pushButton_94.setStyleSheet("\n"
# "\n"
# "QPushButton {\n"
# "  /* Set the background color and border for the button */\n"
# "  background-color: #e7e7e7;\n"
# "  font: 8pt \"Work Sans\";\n"
# "  border: none;\n"
# "  border-radius: 12px;\n"
# "  color: black;\n"
# "}\n"
# "\n"
# "QPushButton:hover {\n"
# "  /* Change the background color when the button is hovered over */\n"
# "  background-color:nocolor;\n"
# "  color: rgb(173, 173, 173)\n"
# "}\n"
# "\n"
# "QPushButton:pressed {\n"
# "  /* Change the background color when the button is pressed */\n"
# "  background-color: rgb(238, 255, 1);\n"
# "  color: black;\n"
# "}")
#         self.pushButton_94.setObjectName("pushButton_94")

#         self.pushButton_95 = QtWidgets.QPushButton(self.frame_5)
#         self.pushButton_95.setGeometry(QtCore.QRect(10, 80, 130, 25))
#         self.pushButton_95.setText("Figma UI")
#         self.pushButton_95.setStyleSheet("\n"
# "\n"
# "QPushButton {\n"
# "  /* Set the background color and border for the button */\n"
# "  background-color: #e7e7e7;\n"
# "  font: 8pt \"Work Sans\";\n"
# "  border: none;\n"
# "  border-radius: 12px;\n"
# "  color: black;\n"
# "}\n"
# "\n"
# "QPushButton:hover {\n"
# "  /* Change the background color when the button is hovered over */\n"
# "  background-color:nocolor;\n"
# "  color: rgb(173, 173, 173)\n"
# "}\n"
# "\n"
# "QPushButton:pressed {\n"
# "  /* Change the background color when the button is pressed */\n"
# "  background-color: rgb(238, 255, 1);\n"
# "  color: black;\n"
# "}")
#         self.pushButton_95.setObjectName("pushButton_95")

#         self.pushButton_96 = QtWidgets.QPushButton(self.frame_5)
#         self.pushButton_96.setGeometry(QtCore.QRect(10, 115, 130, 25))
#         self.pushButton_96.setText("+ Add new")
#         self.pushButton_96.setStyleSheet("\n"
# "\n"
# "QPushButton {\n"
# "  /* Set the background color and border for the button */\n"
# "  background-color: black;\n"
# "  font: 8pt \"Work Sans\";\n"
# "  border: none;\n"
# "  border-radius: 12px;\n"
# "  color: white;\n"
# "}\n"
# "\n"
# "QPushButton:hover {\n"
# "  /* Change the background color when the button is hovered over */\n"
# "  background-color:nocolor;\n"
# "  color: rgb(173, 173, 173)\n"
# "}\n"
# "\n"
# "QPushButton:pressed {\n"
# "  /* Change the background color when the button is pressed */\n"
# "  background-color: rgb(238, 255, 1);\n"
# "  color: black;\n"
# "}")
#         self.pushButton_96.setObjectName("pushButton_96")

        self.pushButton_43 = QtWidgets.QPushButton(self.frame_2, clicked = lambda: self.openCreateAction())
        self.pushButton_43.setGeometry(QtCore.QRect(278, 187, 53, 53))
        self.pushButton_43.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_43.setMaximumSize(QtCore.QSize(53, 53))
        self.pushButton_43.setStyleSheet("\n"
"QPushButton:checked {\n"
"background-color: #af55ff;\n"
"color: white;\n"
"border-radius: 12px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: rgb(51,51,51);\n"
"  font: 5pt;\n"
"  border-radius: 12px;\n"
"  border-style: none;\n"
"  color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  /* Change the background color when the button is hovered over */\n"
"  color: rgb(197, 197, 197);\n"
"  border: 2px solid;\n"
"  border-color: #af55ff;\n"
"}")
        self.pushButton_43.setCheckable(True)
        self.pushButton_43.setObjectName("pushButton_43")
        self.buttonGroup.addButton(self.pushButton_43)

        self.pushButton_44 = QtWidgets.QPushButton(self.frame_2, clicked = lambda: self.openCreateAction())
        self.pushButton_44.setGeometry(QtCore.QRect(220, 187, 53, 53))
        self.pushButton_44.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_44.setMaximumSize(QtCore.QSize(53, 53))
        self.pushButton_44.setStyleSheet("\n"
"QPushButton:checked {\n"
"background-color: #af55ff;\n"
"color: white;\n"
"border-radius: 12px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: rgb(51,51,51);\n"
"  font: 5pt;\n"
"  border-radius: 12px;\n"
"  border-style: none;\n"
"  color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  /* Change the background color when the button is hovered over */\n"
"  color: rgb(197, 197, 197);\n"
"  border: 2px solid;\n"
"  border-color: #af55ff;\n"
"}")
        self.pushButton_44.setCheckable(True)
        self.pushButton_44.setObjectName("pushButton_44")
        self.buttonGroup.addButton(self.pushButton_44)
        self.pushButton_38 = QtWidgets.QPushButton(self.frame_2, clicked = lambda: self.openCreateAction())
        self.pushButton_38.setGeometry(QtCore.QRect(336, 187, 53, 53))
        self.pushButton_38.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_38.setMaximumSize(QtCore.QSize(53, 53))
        self.pushButton_38.setStyleSheet("\n"
"QPushButton:checked {\n"
"background-color: #af55ff;\n"
"color: white;\n"
"border-radius: 12px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: rgb(51,51,51);\n"
"  font: 5pt;\n"
"  border-radius: 12px;\n"
"  border-style: none;\n"
"  color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  /* Change the background color when the button is hovered over */\n"
"  color: rgb(197, 197, 197);\n"
"  border: 2px solid;\n"
"  border-color: #af55ff;\n"
"}")
        self.pushButton_38.setCheckable(True)
        self.pushButton_38.setObjectName("pushButton_38")
        self.buttonGroup.addButton(self.pushButton_38)

        self.pushButton_39 = QtWidgets.QPushButton(self.frame_2, clicked = lambda: self.openCreateAction())
        self.pushButton_39.setGeometry(QtCore.QRect(568, 187, 53, 53))
        self.pushButton_39.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_39.setMaximumSize(QtCore.QSize(53, 53))
        self.pushButton_39.setStyleSheet("\n"
"QPushButton:checked {\n"
"background-color: #af55ff;\n"
"color: white;\n"
"border-radius: 12px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: rgb(51,51,51);\n"
"  font: 5pt;\n"
"  border-radius: 12px;\n"
"  border-style: none;\n"
"  color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  /* Change the background color when the button is hovered over */\n"
"  color: rgb(197, 197, 197);\n"
"  border: 2px solid;\n"
"  border-color: #af55ff;\n"
"}")
        self.pushButton_39.setCheckable(True)
        self.pushButton_39.setObjectName("pushButton_39")
        self.buttonGroup.addButton(self.pushButton_39)

        self.pushButton_40 = QtWidgets.QPushButton(self.frame_2, clicked = lambda: self.openCreateAction())
        self.pushButton_40.setGeometry(QtCore.QRect(452, 187, 53, 53))
        self.pushButton_40.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_40.setMaximumSize(QtCore.QSize(53, 53))
        self.pushButton_40.setStyleSheet("\n"
"QPushButton:checked {\n"
"background-color: #af55ff;\n"
"color: white;\n"
"border-radius: 12px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: rgb(51,51,51);\n"
"  font: 5pt;\n"
"  border-radius: 12px;\n"
"  border-style: none;\n"
"  color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  /* Change the background color when the button is hovered over */\n"
"  color: rgb(197, 197, 197);\n"
"  border: 2px solid;\n"
"  border-color: #af55ff;\n"
"}")
        self.pushButton_40.setCheckable(True)
        self.pushButton_40.setObjectName("pushButton_40")
        self.buttonGroup.addButton(self.pushButton_40)

        self.pushButton_41 = QtWidgets.QPushButton(self.frame_2, clicked = lambda: self.openCreateAction())
        self.pushButton_41.setGeometry(QtCore.QRect(510, 187, 53, 53))
        self.pushButton_41.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_41.setMaximumSize(QtCore.QSize(53, 53))
        self.pushButton_41.setStyleSheet("\n"
"QPushButton:checked {\n"
"background-color: #af55ff;\n"
"color: white;\n"
"border-radius: 12px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: rgb(51,51,51);\n"
"  font: 5pt;\n"
"  border-radius: 12px;\n"
"  border-style: none;\n"
"  color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  /* Change the background color when the button is hovered over */\n"
"  color: rgb(197, 197, 197);\n"
"  border: 2px solid;\n"
"  border-color: #af55ff;\n"
"}")
        self.pushButton_41.setCheckable(True)
        self.pushButton_41.setObjectName("pushButton_41")
        self.buttonGroup.addButton(self.pushButton_41)

        self.pushButton_42 = QtWidgets.QPushButton(self.frame_2, clicked = lambda: self.openCreateAction())
        self.pushButton_42.setGeometry(QtCore.QRect(626, 187, 53, 53))
        self.pushButton_42.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_42.setMaximumSize(QtCore.QSize(53, 53))
        self.pushButton_42.setStyleSheet("\n"
"QPushButton:checked {\n"
"background-color: #af55ff;\n"
"color: white;\n"
"border-radius: 12px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: rgb(51,51,51);\n"
"  font: 5pt;\n"
"  border-radius: 12px;\n"
"  border-style: none;\n"
"  color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  /* Change the background color when the button is hovered over */\n"
"  color: rgb(197, 197, 197);\n"
"  border: 2px solid;\n"
"  border-color: #af55ff;\n"
"}")
        self.pushButton_42.setCheckable(True)
        self.pushButton_42.setObjectName("pushButton_42")
        self.buttonGroup.addButton(self.pushButton_42)

        self.pushButton_49 = QtWidgets.QPushButton(self.frame_2, clicked = lambda: self.openCreateAction())
        self.pushButton_49.setGeometry(QtCore.QRect(684, 187, 53, 53))
        self.pushButton_49.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_49.setMaximumSize(QtCore.QSize(53, 53))
        self.pushButton_49.setStyleSheet("\n"
"QPushButton:checked {\n"
"background-color: #af55ff;\n"
"color: white;\n"
"border-radius: 12px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: rgb(51,51,51);\n"
"  font: 5pt;\n"
"  border-radius: 12px;\n"
"  border-style: none;\n"
"  color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  /* Change the background color when the button is hovered over */\n"
"  color: rgb(197, 197, 197);\n"
"  border: 2px solid;\n"
"  border-color: #af55ff;\n"
"}")
        self.pushButton_49.setCheckable(True)
        self.pushButton_49.setObjectName("pushButton_49")
        self.buttonGroup.addButton(self.pushButton_49)

        self.pushButton_59 = QtWidgets.QPushButton(self.frame_2, clicked = lambda: self.openCreateAction())
        self.pushButton_59.setGeometry(QtCore.QRect(742, 187, 53, 53))
        self.pushButton_59.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_59.setMaximumSize(QtCore.QSize(53, 53))
        self.pushButton_59.setStyleSheet("\n"
"QPushButton:checked {\n"
"background-color: #af55ff;\n"
"color: white;\n"
"border-radius: 12px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: rgb(51,51,51);\n"
"  font: 5pt;\n"
"  border-radius: 12px;\n"
"  border-style: none;\n"
"  color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  /* Change the background color when the button is hovered over */\n"
"  color: rgb(197, 197, 197);\n"
"  border: 2px solid;\n"
"  border-color: #af55ff;\n"
"}")
        self.pushButton_59.setCheckable(True)
        self.pushButton_59.setObjectName("pushButton_59")
        self.buttonGroup.addButton(self.pushButton_59)

        self.pushButton_18 = QtWidgets.QPushButton(self.frame_2, clicked = lambda: self.openCreateAction())
        self.pushButton_18.setGeometry(QtCore.QRect(104, 244, 64, 53))
        self.pushButton_18.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_18.setMaximumSize(QtCore.QSize(64, 57))
        self.pushButton_18.setStyleSheet("\n"
"QPushButton:checked {\n"
"background-color: #af55ff;\n"
"color: white;\n"
"border-radius: 12px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: rgb(51,51,51);\n"
"  font: 5pt;\n"
"  border-radius: 12px;\n"
"  border-style: none;\n"
"  color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  /* Change the background color when the button is hovered over */\n"
"  color: rgb(197, 197, 197);\n"
"  border: 2px solid;\n"
"  border-color: #af55ff;\n"
"}")
        self.pushButton_18.setCheckable(True)
        self.pushButton_18.setAutoRepeatDelay(296)
        self.pushButton_18.setObjectName("pushButton_18")
        self.buttonGroup.addButton(self.pushButton_18)

        self.commandLinkButton = QtWidgets.QCommandLinkButton(self.frame_4)
        self.commandLinkButton.setGeometry(QtCore.QRect(1050, 0, 100, 40))
        self.commandLinkButton.setMinimumSize(QtCore.QSize(111, 40))
        self.commandLinkButton.setMaximumSize(QtCore.QSize(111, 40))
        # font = QtGui.QFont()
        # font.setFamily("Cambria") # Segoe UI
        # font.setPointSize(6)
        # self.commandLinkButton.setFont(font)
        self.commandLinkButton.setText(" Community")
        self.commandLinkButton.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 7pt \"Work Sans\";\n"
# "font-weight: bold;\n"
"background-color: rgb(238,255,0);\n"
"border: none;\n"
"")
        icon = QtGui.QIcon()
        pic = self.resource_path("Icons/www.png")
        icon.addPixmap(QtGui.QPixmap(pic), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.commandLinkButton.setIcon(icon)
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.Lay_f4.addWidget(self.commandLinkButton,1,QtCore.Qt.AlignRight)

        self.Lay_f6 = QtWidgets.QHBoxLayout(self.frame_6)
        self.Lay_f6.setObjectName("Lay_f6")
        # self.Lay_f6.setSpacing(0)
        self.Lay_f6.setContentsMargins(0,0,0,0)

        self.commandLinkButton_2 = QtWidgets.QCommandLinkButton(self.frame_6)
        self.commandLinkButton_2.setGeometry(QtCore.QRect(10, 0, 100, 41))
        font = QtGui.QFont()
        font.setFamily("Work Sans") # Segoe UI
        self.commandLinkButton_2.setFont(font)
        self.commandLinkButton_2.setText("Profile")
        self.commandLinkButton_2.setStyleSheet("color: #c2c2c2;\n"
"background-color: none;\n"
"font: 8pt \"Work Sans\";\n"
"border: none;\n"
"")
        icon = QtGui.QIcon()
        pic = self.resource_path("Icons/profile.png")
        icon.addPixmap(QtGui.QPixmap(pic), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.commandLinkButton_2.setIcon(icon)
        self.commandLinkButton_2.setObjectName("commandLinkButton_2")
        self.Lay_f6.addWidget(self.commandLinkButton_2,0,QtCore.Qt.AlignLeft)

        self.Lay_f8 = QtWidgets.QHBoxLayout(self.frame_8)
        self.Lay_f8.setObjectName("Lay_f8")
        self.Lay_f8.setContentsMargins(0,0,0,0)

        self.commandLinkButton_6 = QtWidgets.QCommandLinkButton(self.frame_8, clicked = lambda: self.Vect_art())
        self.commandLinkButton_6.setGeometry(QtCore.QRect(5, 5, 100, 41)) #30
        self.commandLinkButton_6.setText("Save profile first")
        self.commandLinkButton_6.setStyleSheet("color: rgb(192,192,192);\n"
"background-color: none;\n"
"font: 12pt \"Work Sans\";\n"
"border: none;\n"
"")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("xyz.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.commandLinkButton_6.setIcon(icon)
        self.commandLinkButton_6.setObjectName("commandLinkButton_6")
        self.Lay_f8.addWidget(self.commandLinkButton_6,0,QtCore.Qt.AlignLeft)

        # self.profiles()

        # https://stackoverflow.com/questions/49828339/how-to-properly-manage-text-and-icon-with-qtoolbutton
        self.pushButton_90 = QtWidgets.QPushButton(self.frame_8, clicked = lambda: self.Vect_art())
        self.pushButton_90.setGeometry(QtCore.QRect(104, 15, 17, 17)) #40
        icon = QtGui.QIcon()
        pic = self.resource_path("Icons/next.png")
        icon.addPixmap(QtGui.QPixmap(pic), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_90.setIcon(icon)
        self.pushButton_90.setStyleSheet("background-color: none;\n"
"color: none;\n"
"border-style: none;\n"
"border-radius: none;")
        self.pushButton_90.setObjectName("pushButton_90")
        self.Lay_f8.addWidget(self.pushButton_90,0,QtCore.Qt.AlignLeft)
        self.Lay_f8.addStretch(1)

        self.Lay_f81 = QtWidgets.QHBoxLayout(self.frame_81)
        self.Lay_f81.setObjectName("Lay_f81")
        self.Lay_f81.setContentsMargins(0,0,0,0)
        self.Lay_f81.addStretch(1)
        

        self.pushButton_85 = QtWidgets.QPushButton(self.frame_81, clicked= lambda: self.on_button_clicked())
        self.pushButton_85.setGeometry(QtCore.QRect(330, 10, 25, 25)) #35
        self.pushButton_85.setMinimumSize(QtCore.QSize(25, 25))
        self.pushButton_85.setMaximumSize(QtCore.QSize(25, 25))
        self.pushButton_85.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"font: 8pt \"Arial\";\n"
"color: rgb(0, 0, 0);\n"
"border-style: none;\n"
"border-radius: 12px;")
        self.pushButton_85.setObjectName("pushButton_85")
        self.Lay_f81.addWidget(self.pushButton_85,0,QtCore.Qt.AlignLeft)

        self.pushButton_84 = QtWidgets.QPushButton(self.frame_81)
        self.pushButton_84.setGeometry(QtCore.QRect(365, 10, 130, 25)) #35
        self.pushButton_84.setMinimumSize(QtCore.QSize(130, 25))
        self.pushButton_84.setMaximumSize(QtCore.QSize(130, 25))
        self.pushButton_84.setText("Quick brush")
        self.pushButton_84.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 8pt \"Work Sans\";\n"
"color: rgb(0, 0, 0);\n"
"border-style: none;\n"
"border-radius: 12px;")
        self.pushButton_84.setObjectName("pushButton_84")
        self.Lay_f81.addWidget(self.pushButton_84,0,QtCore.Qt.AlignLeft)

        # self.brushGroup = QtWidgets.QButtonGroup(self.frame)
        # self.brushGroup.setObjectName("brushGroup")

        self.pushButton_86 = QtWidgets.QPushButton(self.frame_81)
        self.pushButton_86.setGeometry(QtCore.QRect(510, 10, 25, 25)) #35
        self.pushButton_86.setMinimumSize(QtCore.QSize(25, 25))
        self.pushButton_86.setMaximumSize(QtCore.QSize(25, 25))
        self.pushButton_86.setText("1")
        self.pushButton_86.setStyleSheet("\n"
"QPushButton:checked {\n"
"  background-color: rgb(0, 0, 0);\n"
"  font: 6pt \"Arial\";\n"
"  color: rgb(255, 255, 255);\n"
"  border-radius: 12px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: rgb(255,255,255);\n"
"  font: 6pt \"Arial\";\n"
"  border-radius: 12px;\n"
"  border-style: none;\n"
"  color: rgb(0, 0, 0);\n"
"}")
        self.pushButton_86.setObjectName("pushButton_86")
        self.pushButton_86.setCheckable(True)
        self.Lay_f81.addWidget(self.pushButton_86,0,QtCore.Qt.AlignLeft)

        self.pushButton_87 = QtWidgets.QPushButton(self.frame_81)
        self.pushButton_87.setGeometry(QtCore.QRect(550, 10, 25, 25)) #35
        self.pushButton_87.setMinimumSize(QtCore.QSize(25, 25))
        self.pushButton_87.setMaximumSize(QtCore.QSize(25, 25))
        self.pushButton_87.setText("2")
        self.pushButton_87.setStyleSheet("\n"
"QPushButton:checked {\n"
"  background-color: rgb(0, 0, 0);\n"
"  font: 6pt \"Arial\";\n"
"  color: rgb(255, 255, 255);\n"
"  border-radius: 12px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: rgb(255,255,255);\n"
"  font: 6pt \"Arial\";\n"
"  border-radius: 12px;\n"
"  border-style: none;\n"
"  color: rgb(0, 0, 0);\n"
"}")
        self.pushButton_87.setObjectName("pushButton_87")
        self.pushButton_87.setCheckable(True)
        self.Lay_f81.addWidget(self.pushButton_87,0,QtCore.Qt.AlignLeft)

        self.pushButton_88 = QtWidgets.QPushButton(self.frame_81)
        self.pushButton_88.setGeometry(QtCore.QRect(590, 10, 25, 25)) #35
        self.pushButton_88.setMinimumSize(QtCore.QSize(25, 25))
        self.pushButton_88.setMaximumSize(QtCore.QSize(25, 25))
        self.pushButton_88.setText("3")
        self.pushButton_88.setStyleSheet("\n"
"QPushButton:checked {\n"
"  background-color: rgb(0, 0, 0);\n"
"  font: 6pt \"Arial\";\n"
"  color: rgb(255, 255, 255);\n"
"  border-radius: 12px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: rgb(255,255,255);\n"
"  font: 6pt \"Arial\";\n"
"  border-radius: 12px;\n"
"  border-style: none;\n"
"  color: rgb(0, 0, 0);\n"
"}")
        self.pushButton_88.setObjectName("pushButton_88")
        self.pushButton_88.setCheckable(True)
        self.Lay_f81.addWidget(self.pushButton_88,0,QtCore.Qt.AlignLeft)

        self.pushButton_89 = QtWidgets.QPushButton(self.frame_81)
        self.pushButton_89.setGeometry(QtCore.QRect(630, 10, 25, 25)) #35
        self.pushButton_89.setMinimumSize(QtCore.QSize(25, 25))
        self.pushButton_89.setMaximumSize(QtCore.QSize(25, 25))
        self.pushButton_89.setText("4")
        self.pushButton_89.setStyleSheet("\n"
"QPushButton:checked {\n"
"  background-color: rgb(0, 0, 0);\n"
"  font: 6pt \"Arial\";\n"
"  color: rgb(255, 255, 255);\n"
"  border-radius: 12px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: rgb(255,255,255);\n"
"  font: 6pt \"Arial\";\n"
"  border-radius: 12px;\n"
"  border-style: none;\n"
"  color: rgb(0, 0, 0);\n"
"}")
        self.pushButton_89.setObjectName("pushButton_89")
        self.pushButton_89.setCheckable(True)
        self.Lay_f81.addWidget(self.pushButton_89,0,QtCore.Qt.AlignLeft)
        self.Lay_f81.addStretch(3)

#         self.pushButton_89 = QtWidgets.QPushButton(self.frame_81, clicked= lambda: self.under_dev())
#         self.pushButton_89.setGeometry(QtCore.QRect(630, 10, 25, 25)) #35
#         self.pushButton_89.setMinimumSize(QtCore.QSize(25, 25))
#         self.pushButton_89.setMaximumSize(QtCore.QSize(25, 25))
#         self.pushButton_89.setText("+")
#         self.pushButton_89.setStyleSheet("\n"
# "QPushButton:pressed {\n"
# "  background-color: rgb(0, 0, 0);\n"
# "  font: 6pt \"Arial\";\n"
# "  color: rgb(255, 255, 255);\n"
# "  border-radius: 12px;\n"
# "}\n"
# "\n"
# "QPushButton {\n"
# "  /* Set the background color and border for the button */\n"
# "  background-color: rgb(255,255,255);\n"
# "  font: 6pt \"Arial\";\n"
# "  border-radius: 12px;\n"
# "  border-style: none;\n"
# "  color: rgb(0, 0, 0);\n"
# "}")
#         self.pushButton_89.setObjectName("pushButton_89")
#         self.pushButton_89.setCheckable(True)
#         self.Lay_f81.addWidget(self.pushButton_89,0,QtCore.Qt.AlignLeft)
#         self.Lay_f81.addStretch(3)
        
        self.Lay_f8.addWidget(self.frame_81,0,QtCore.Qt.AlignHCenter)
        self.Lay_f8.addStretch(1)

        self.commandLinkButton_5 = QtWidgets.QCommandLinkButton(self.frame_8)
        self.commandLinkButton_5.setGeometry(QtCore.QRect(880, 0, 200, 41)) #25
        # self.commandLinkButton_5.setIconSize(QtCore.QSize(64, 64))
        self.commandLinkButton_5.setText("Illustrator.exe")
        self.commandLinkButton_5.setStyleSheet("color: #000000;\n"
"background-color: none;\n"
"font: 12pt \"Work Sans\";\n"
"border: none;\n")
        icon = QtGui.QIcon()
        pic = self.resource_path("Icons/illustrator.png")
        icon.addPixmap(QtGui.QPixmap(pic), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.commandLinkButton_5.setIcon(icon)
        self.commandLinkButton_5.setObjectName("commandLinkButton_5")
        self.Lay_f8.addWidget(self.commandLinkButton_5,0,QtCore.Qt.AlignRight)

        self.pushButton_91 = QtWidgets.QPushButton(self.frame_8)
        self.pushButton_91.setGeometry(QtCore.QRect(1030, 13, 17, 17)) #38
        icon = QtGui.QIcon()
        pic = self.resource_path("Icons/next.png")
        icon.addPixmap(QtGui.QPixmap(pic), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_91.setIcon(icon)
        self.pushButton_91.setStyleSheet("background-color: none;\n"
"color: none;\n"
"border-style: none;\n"
"border-radius: none;")
        self.pushButton_91.setObjectName("pushButton_91")
        self.Lay_f8.addWidget(self.pushButton_91,0,QtCore.Qt.AlignRight)


        self.commandLinkButton_3 = QtWidgets.QCommandLinkButton(self.frame_6)
        self.commandLinkButton_3.setGeometry(QtCore.QRect(440, 0, 100, 41))
        self.commandLinkButton_3.setText("Layers")
        self.commandLinkButton_3.setStyleSheet("color: #c2c2c2;\n"
"background-color: none;\n"
"font: 8pt \"Work Sans\";\n"
"border: none;\n"
"")
        icon = QtGui.QIcon()
        pic = self.resource_path("Icons/layers.png")
        icon.addPixmap(QtGui.QPixmap(pic), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.commandLinkButton_3.setIcon(icon)
        self.commandLinkButton_3.setObjectName("commandLinkButton_3")
        self.Lay_f6.addWidget(self.commandLinkButton_3,0,QtCore.Qt.AlignCenter)

        self.commandLinkButton_4 = QtWidgets.QCommandLinkButton(self.frame_6)
        self.commandLinkButton_4.setGeometry(QtCore.QRect(880, 0, 200, 41))
        # font = QtGui.QFont()
        # font.setFamily("Cambria") # Segoe UI
        # self.commandLinkButton_4.setFont(font)
        self.commandLinkButton_4.setText("Automation software")
        self.commandLinkButton_4.setStyleSheet("color: #c2c2c2;\n"
"background-color: none;\n"
"font: 8pt \"Work Sans\";\n"
"border: none;\n"
"")
        icon = QtGui.QIcon()
        pic = self.resource_path("Icons/link.png")
        icon.addPixmap(QtGui.QPixmap(pic), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.commandLinkButton_4.setIcon(icon)
        self.commandLinkButton_4.setObjectName("commandLinkButton_4")
        self.Lay_f6.addWidget(self.commandLinkButton_4,0,QtCore.Qt.AlignRight)


        self.Lay_f7 = QtWidgets.QHBoxLayout(self.frame_7)
        self.Lay_f7.setObjectName("Lay_f7")

        self.pushButton_92 = QtWidgets.QPushButton(self.frame_7)
        self.pushButton_92.setGeometry(QtCore.QRect(5, 25, 141, 31))
        self.pushButton_92.setMinimumSize(QtCore.QSize(141, 31))
        self.pushButton_92.setMaximumSize(QtCore.QSize(141, 31))
        self.pushButton_92.setStyleSheet("\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: no color;\n"
"  font: 8pt \"Work Sans\";\n"
"  color: black;\n"
"  border: none;\n"
"  border-image: url(user.png);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  /* Change the background color when the button is hovered over */\n"
"  background-color: white;\n"
"  color: rgb(173, 173, 173);\n"
"  border: none;\n"
"  border-radius: 15px;\n"
"  border-image: url(feed_back.png)"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  /* Change the background color when the button is pressed */\n"
"  background-color: rgb(238, 255, 1);\n"
"  color: black;\n"
"  border-image: url(feed_back.png)"
"}")
        self.pushButton_92.setObjectName("pushButton_92")
        self.Lay_f7.addWidget(self.pushButton_92,0,QtCore.Qt.AlignLeft)
        self.Lay_f7.addStretch(3)

        self.pushButton_9 = QtWidgets.QPushButton(self.frame_7, clicked = lambda: self.save_toggle())
        self.pushButton_9.setGeometry(QtCore.QRect(430, 10, 191, 31))
        self.pushButton_9.setMinimumSize(QtCore.QSize(191, 31))
        self.pushButton_9.setMaximumSize(QtCore.QSize(191, 31))
        self.pushButton_9.setStyleSheet("\n"
"\n"
"QPushButton {\n"
"  /* Set the background color and border for the button */\n"
"  background-color: black;\n"
"  font: 8pt \"Work Sans\";\n" 
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
        self.Lay_f7.addWidget(self.pushButton_9,0,QtCore.Qt.AlignCenter)
        self.Lay_f7.addStretch(5)

        self.error_dialog = QtWidgets.QErrorMessage()

        
        self.CreateAction.raise_()
        # self.scrollArea.raise_()
        self.options.raise_()
        self.pushButton_47.raise_()
        self.pushButton_23.raise_()
        self.pushButton_49.raise_()
        self.pushButton_28.raise_()
        self.pushButton_12.raise_()
        self.pushButton.raise_()
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
        self.pushButton_70.raise_()
        self.pushButton_71.raise_()
        self.pushButton_72.raise_()
        self.pushButton_73.raise_()
        self.pushButton_74.raise_()
        self.pushButton_75.raise_()
        self.pushButton_76.raise_()
        self.pushButton_77.raise_()
        self.pushButton_78.raise_()
        self.commandLinkButton.raise_()
        self.pushButton_81.raise_()
        self.pushButton_82.raise_()
        self.frame_5.raise_()
        self.gridLayout.addWidget(self.frame)
        NoMad.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(NoMad)
        self.statusbar.setObjectName("statusbar")
        NoMad.setStatusBar(self.statusbar)

        self.retranslateUi(NoMad)
        QtCore.QMetaObject.connectSlotsByName(NoMad)

    def retranslateUi(self, NoMad):
        global buzzer
        _translate = QtCore.QCoreApplication.translate
        NoMad.setWindowTitle(_translate("NoMad", "Input"))  # MainWindow
        self.profiles()
        # NoMad.setWindowFlags(QtCore.Qt.WindowFlags() | QtCore.Qt.FramelessWindowHint)
        self.pushButton.setText(_translate("NoMad", "Esc"))
        self.pushButton_3.setText(_translate("NoMad", "!\n"
" \n1"))
        self.pushButton_4.setText(_translate("NoMad", "#\n"
" \n3"))
        self.pushButton_5.setText(_translate("NoMad", "@\n"
" \n2"))
        self.pushButton_6.setText(_translate("NoMad", "%\n"
" \n5"))
        self.pushButton_7.setText(_translate("NoMad", "^\n"
" \n6"))
        self.pushButton_8.setText(_translate("NoMad", "$ \n"
" \n4"))
        self.pushButton_10.setText(_translate("NoMad", "( \n"
" \n9"))
        self.pushButton_11.setText(_translate("NoMad", "*\n"
" \n8"))
        self.pushButton_12.setText(_translate("NoMad", ") \n"
" \n0"))
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
" \n,"))
        self.pushButton_37.setText(_translate("NoMad", "Opt"))
        self.pushButton_45.setText(_translate("NoMad", "Cmd"))
        self.pushButton_47.setText(_translate("NoMad", "Cmd"))
        self.pushButton_49.setText(_translate("NoMad", ">\n"
" \n."))
        self.pushButton_48.setText(_translate("NoMad", "+\n"
" \n="))
        self.pushButton_50.setText(_translate("NoMad", "-\n"
" \n_"))
        self.pushButton_51.setText(_translate("NoMad", "Backspace"))
        self.pushButton_52.setText(_translate("NoMad", "} \n"
" \n]"))
        self.pushButton_53.setText(_translate("NoMad", "{\n"
" \n["))
        self.pushButton_54.setText(_translate("NoMad", "P"))
        self.pushButton_55.setText(_translate("NoMad", "| \n"
" \n\\"))
        self.pushButton_56.setText(_translate("NoMad", "\" \n"
"\n\'"))
        self.pushButton_57.setText(_translate("NoMad", ":\n"
" \n;"))
        self.pushButton_58.setText(_translate("NoMad", "Enter"))
        self.pushButton_59.setText(_translate("NoMad", "?\n"
" \n/"))
        self.pushButton_60.setText(_translate("NoMad", "Shift"))
        self.pushButton_61.setText(_translate("NoMad", "↑"))
        self.pushButton_62.setText(_translate("NoMad", "Ctrl"))
        self.pushButton_63.setText(_translate("NoMad", "Fn"))
        self.pushButton_64.setText(_translate("NoMad", "←"))
        self.pushButton_65.setText(_translate("NoMad", "↓"))
        self.pushButton_66.setText(_translate("NoMad", "→"))
        self.pushButton_67.setText(_translate("NoMad", "&&\n"
" \n7"))
        self.pushButton_70.setText(_translate("NoMad", ""))
        self.pushButton_71.setText(_translate("NoMad", "Page\nUp"))
        self.pushButton_72.setText(_translate("NoMad", "Page\nDown"))
        self.pushButton_73.setText(_translate("NoMad", "Home"))

        self.pushButton_43.setText(_translate("NoMad", "X"))
        self.pushButton_44.setText(_translate("NoMad", "Z"))
        self.pushButton_38.setText(_translate("NoMad", "C"))
        self.pushButton_18.setText(_translate("NoMad", "Ctrl"))
        self.pushButton_9.setText(_translate("NoMad", "Save Profile"))

        self.pushButton_4c.setText(_translate("NoMad", "MIDI"))
        self.pushButton_3c.setText(_translate("NoMad", "Action"))
        self.pushButton_5c.setText(_translate("NoMad", "Lighting"))
        self.pushButton_2c.setText(_translate("NoMad", "Basic"))
        self.pushButton_7c.setText(_translate("NoMad", "←  Back"))
        self.pushButton_6c.setText(_translate("NoMad", "+ Create new action"))
        self.label_c.setText(_translate("NoMad", "Design"))

        self.pushButton_20o.setText(_translate("NoMad", "Lighting"))
        self.pushButton_17o.setText(_translate("NoMad", "Basic"))
        self.pushButton_22o.setText(_translate("NoMad", "←  Back"))
        self.pushButton_18o.setText(_translate("NoMad", "Action"))
        self.pushButton_19o.setText(_translate("NoMad", "MIDI"))
        self.label_o.setText(_translate("NoMad", "Name your action:"))
        self.lineEdit_o.setPlaceholderText(_translate("NoMad", "  Insert action here..."))
        self.checkBox_o.setText(_translate("NoMad", "enable multi-tap"))
        self.lineEdit_2o.setPlaceholderText(_translate("NoMad", "+ add delay"))
        self.lineEdit_3o.setPlaceholderText(_translate("NoMad", "+ add delay"))
        self.pushButton_2o.setText(_translate("NoMad", "Save"))
        self.lineEdit_4o.setPlaceholderText(_translate("NoMad", "+ add delay"))
        self.addKeystrokeButton_o.setText(_translate("NoMad", "+ Add Keystroke"))
        self.pushButton_o.clicked.connect(self.pushButton_handler)

        self.last_size = NoMad.size()

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.check_window_size)
        self.timer.start(100)  # Check every second (adjust as needed)


    def check_window_size(self):  # Using to keep navigations updated
        current_size = NoMad.size()
        if current_size != self.last_size:
            if  self.CreateAction.frameGeometry().width() != 0:

                self.CreateAction.setGeometry(QtCore.QRect(NoMad.frameGeometry().width()-421, 43, 400, NoMad.frameGeometry().height()-114))
                self.profiles_area.setGeometry(QtCore.QRect(0, 190, 370, NoMad.frameGeometry().height()-300))
                

                if self.options.frameGeometry().width() != 0:
                        
                        self.options.setGeometry(QtCore.QRect(NoMad.frameGeometry().width()-421, 43, 400, NoMad.frameGeometry().height()-114))

                        self.CreateAction.setGeometry(QtCore.QRect(NoMad.frameGeometry().width()-421, 43, 400, NoMad.frameGeometry().height()-114)) # update create action size
                        self.profiles_area.setGeometry(QtCore.QRect(0, 190, 370, NoMad.frameGeometry().height()-300))
        
            self.last_size = current_size
            


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    NoMad = QtWidgets.QMainWindow()
    ui = Ui_NoMad()
    ui.setupUi(NoMad)
    NoMad.show()
    sys.exit(app.exec_())
