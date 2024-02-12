# from PyQt5 import QtCore, QtGui, QtWidgets

# class Ui_Dialog(object):
#     def setupUi(self, Dialog):
#         Dialog.setObjectName("Dialog")
#         Dialog.resize(695, 404)
#         self.keyboard_area = QtWidgets.QWidget(Dialog)
#         self.keyboard_area.setGeometry(QtCore.QRect(0, 0, 1337, 400))
#         self.keyboard_area.setStyleSheet("background-color: no color;")
#         self.keyboard_area.setObjectName("keyboard_area")

#         self.horizLayout_keyboard = QtWidgets.QHBoxLayout(self.keyboard_area)
#         self.horizLayout_keyboard.setObjectName("horizLayout_keyboard")
#         self.horizLayout_keyboard.setContentsMargins(0, 0, 0, 0)

        

#         self.scrollArea_keyboard = QtWidgets.QScrollArea(self.keyboard_area)
#         self.scrollArea_keyboard.setStyleSheet("QScrollArea {background-color: no color; border: none;}")
#         self.scrollArea_keyboard.setWidgetResizable(True)
#         self.scrollArea_keyboard.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)  # Turn off default horizontal scrollbar
#         self.scrollArea_keyboard.setObjectName("scrollArea_keyboard")
#         self.scrollWidget_keyboard = QtWidgets.QWidget(self.scrollArea_keyboard)
#         self.scrollWidget_keyboard.setGeometry(QtCore.QRect(0, 0, 1840, 424))
#         self.scrollWidget_keyboard.setStyleSheet("background-color: no color;")
#         self.scrollWidget_keyboard.setObjectName("scrollWidget_keyboard")
#         self.horizLayout_keyboard_2 = QtWidgets.QHBoxLayout(self.scrollWidget_keyboard)
#         self.horizLayout_keyboard_2.setObjectName("verticalLayout_2")
#         self.horizLayout_keyboard_2.setContentsMargins(0, 0, 0, 0)

#         # Create a horizontal QScrollBar
#           # Set the initial position to the center
#         self.abc = QtWidgets.QScrollBar(self.keyboard_area)
#         # self.abc.setGeometry(QtCore.QRect(0, 80, 1840, 14))
#         self.abc.setOrientation(QtCore.Qt.Horizontal)
#         self.abc.setSliderPosition(50)
#         self.abc.valueChanged.connect(self.scrollArea_keyboard.horizontalScrollBar().setValue)
#         # self.horizLayout_keyboard.addWidget(self.abc)

#         self.scrollArea_keyboard.setWidget(self.scrollWidget_keyboard)
#         self.horizLayout_keyboard.addWidget(self.scrollArea_keyboard)
#         # self.horizLayout_keyboard.addWidget(self.abc)
        

#         self.last_frame = QtWidgets.QFrame(self.scrollWidget_keyboard)
#         self.last_frame.setGeometry(QtCore.QRect(0, 0, 1840, 413))
#         self.last_frame.setMinimumSize(QtCore.QSize(1840, 0))
#         self.last_frame.setStyleSheet("background-color: #e7e7e7;")
#         self.last_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
#         self.last_frame.setFrameShadow(QtWidgets.QFrame.Raised)
#         self.last_frame.setObjectName("last_frame")
#         self.horizLayout_keyboard_2.addWidget(self.last_frame)

#         self.keyboardLayout = QtWidgets.QHBoxLayout(self.last_frame)
#         self.keyboardLayout.setObjectName("keyboardLayout")
#         self.keyboardLayout.setContentsMargins(0, 0, 0, 0)

#         self.frame_2 = QtWidgets.QFrame(self.last_frame)
#         self.frame_2.setGeometry(QtCore.QRect(0, 180, 1047, 313))
#         self.frame_2.setStyleSheet("background-color: rgb(0, 0, 0); font: 8pt \"Arial\"; color: rgb(255, 255, 255); border-style: outset; border-width: 4px; border-radius: 20px;")
#         self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
#         self.frame_2.setMinimumSize(QtCore.QSize(1047, 313))
#         self.frame_2.setMaximumSize(QtCore.QSize(1047, 313))
#         self.frame_2.setObjectName("frame_2")
#         self.keyboardLayout.addWidget(self.frame_2, 0, QtCore.Qt.AlignCenter)

#         self.retranslateUi(Dialog)
#         QtCore.QMetaObject.connectSlotsByName(Dialog)

#     def retranslateUi(self, Dialog):
#         _translate = QtCore.QCoreApplication.translate
#         Dialog.setWindowTitle(_translate("Dialog", "Dialog"))

# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     Dialog = QtWidgets.QDialog()
#     ui = Ui_Dialog()
#     ui.setupUi(Dialog)
#     Dialog.show()
#     sys.exit(app.exec_())




# CODE THAT CONNECTS SCROLLBAR WITH SCROLLAREA
    

# from PyQt5 import QtWidgets, QtCore

# class MyWindow(QtWidgets.QWidget):
#     def __init__(self):
#         super().__init__()

#         self.scroll_area = QtWidgets.QScrollArea(self)
#         self.scroll_area.setWidgetResizable(True)

#         self.scroll_widget = QtWidgets.QWidget(self.scroll_area)
#         self.scroll_widget.setGeometry(QtCore.QRect(0, 0, 400, 300))

#         self.scroll_area.setWidget(self.scroll_widget)

#         self.scroll_bar = QtWidgets.QScrollBar(QtCore.Qt.Horizontal, self)
#         self.scroll_bar.setMaximum(800)
#         self.scroll_bar.valueChanged.connect(self.scroll_area.horizontalScrollBar().setValue)

#         layout = QtWidgets.QVBoxLayout(self)
#         layout.addWidget(self.scroll_area)
#         layout.addWidget(self.scroll_bar)

# if __name__ == '__main__':
#     import sys
#     app = QtWidgets.QApplication([])
#     window = MyWindow()
#     window.show()
#     sys.exit(app.exec_())




from PyQt5 import QtCore, QtGui, QtWidgets
import pyautogui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(695, 404)
        self.keyboard_area = QtWidgets.QWidget(Dialog)
        self.keyboard_area.setGeometry(QtCore.QRect(0, 0, 1337, 400))
        self.keyboard_area.setStyleSheet("background-color: no color;")
        self.keyboard_area.setObjectName("keyboard_area")

        self.horizLayout_keyboard = QtWidgets.QHBoxLayout(self.keyboard_area)
        self.horizLayout_keyboard.setObjectName("horizLayout_keyboard")
        self.horizLayout_keyboard.setContentsMargins(0, 0, 0, 0)

        # Create a horizontal QScrollBar
        self.abc = QtWidgets.QScrollBar(QtCore.Qt.Horizontal)
        self.abc.setSliderPosition(50)  # Set the initial position to the center
        self.horizLayout_keyboard.addWidget(self.abc)

        self.scrollArea_keyboard = QtWidgets.QScrollArea(self.keyboard_area)
        self.scrollArea_keyboard.setStyleSheet("QScrollArea {background-color: no color; border: none;}")
        self.scrollArea_keyboard.setWidgetResizable(True)
        self.scrollArea_keyboard.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)  # Turn off default horizontal scrollbar
        self.scrollArea_keyboard.setObjectName("scrollArea_keyboard")
        self.scrollWidget_keyboard = QtWidgets.QWidget(self.scrollArea_keyboard)
        self.scrollWidget_keyboard.setGeometry(QtCore.QRect(0, 0, 1840, 424))
        self.scrollWidget_keyboard.setStyleSheet("background-color: no color;")
        self.scrollWidget_keyboard.setObjectName("scrollWidget_keyboard")
        self.horizLayout_keyboard_2 = QtWidgets.QHBoxLayout(self.scrollWidget_keyboard)
        self.horizLayout_keyboard_2.setObjectName("verticalLayout_2")
        self.horizLayout_keyboard_2.setContentsMargins(0, 0, 0, 0)

        self.scrollArea_keyboard.setWidget(self.scrollWidget_keyboard)
        self.horizLayout_keyboard.addWidget(self.scrollArea_keyboard)

        self.last_frame = QtWidgets.QFrame(self.scrollWidget_keyboard)
        self.last_frame.setGeometry(QtCore.QRect(0, 0, 1840, 413))
        self.last_frame.setMinimumSize(QtCore.QSize(1840, 0))
        self.last_frame.setStyleSheet("background-color: #e7e7e7;")
        self.last_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.last_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.last_frame.setObjectName("last_frame")
        self.horizLayout_keyboard_2.addWidget(self.last_frame)

        self.keyboardLayout = QtWidgets.QHBoxLayout(self.last_frame)
        self.keyboardLayout.setObjectName("keyboardLayout")
        self.keyboardLayout.setContentsMargins(0, 0, 0, 0)

        self.frame_2 = QtWidgets.QFrame(self.last_frame)
        self.frame_2.setGeometry(QtCore.QRect(0, 180, 1047, 313))
        self.frame_2.setStyleSheet("background-color: rgb(0, 0, 0); font: 8pt \"Arial\"; color: rgb(255, 255, 255); border-style: outset; border-width: 4px; border-radius: 20px;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setMinimumSize(QtCore.QSize(1047, 313))
        self.frame_2.setMaximumSize(QtCore.QSize(1047, 313))
        self.frame_2.setObjectName("frame_2")

        # Connect the clicked signal to the custom function
        self.frame_2.mousePressEvent = self.frame_2_clicked

        self.keyboardLayout.addWidget(self.frame_2, 0, QtCore.Qt.AlignCenter)

        # Create a timer to click the button every 5 seconds
        self.timer = QtCore.QTimer(Dialog)
        self.timer.timeout.connect(self.auto_click_button)
        self.timer.start(5000)  # 5000 milliseconds = 5 seconds

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))

    def frame_2_clicked(self, event):
        # Change the background color of self.frame_2 when it's clicked
        if self.frame_2.palette().color(QtGui.QPalette.Window) == QtGui.QColor(0, 0, 0):
            self.frame_2.setStyleSheet("background-color: rgb(255, 0, 0); font: 8pt \"Arial\"; color: rgb(255, 255, 255); border-style: outset; border-width: 4px; border-radius: 20px;")
            pyautogui.press('right')
        else:
            self.frame_2.setStyleSheet("background-color: rgb(0, 0, 0); font: 8pt \"Arial\"; color: rgb(255, 255, 255); border-style: outset; border-width: 4px; border-radius: 20px;")
            pyautogui.press('right')

    def auto_click_button(self):
        # Simulate a click on the button
        self.frame_2.mousePressEvent(QtGui.QMouseEvent(QtCore.QEvent.MouseButtonPress, QtCore.QPoint(), QtCore.Qt.LeftButton, QtCore.Qt.LeftButton, QtCore.Qt.NoModifier))
        self.frame_2.mousePressEvent(QtGui.QMouseEvent(QtCore.QEvent.MouseButtonRelease, QtCore.QPoint(), QtCore.Qt.LeftButton, QtCore.Qt.LeftButton, QtCore.Qt.NoModifier))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)

    auto_click_thread = QtCore.QThread()
    auto_click_thread.run = ui.auto_click_button
    auto_click_thread.start()
    
    Dialog.show()
    sys.exit(app.exec_())