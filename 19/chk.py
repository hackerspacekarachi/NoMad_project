# from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QColorDialog
# from PyQt5.QtGui import QColor

# class MyWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()

#         self.setWindowTitle("Color Picker Example")
#         self.setGeometry(100, 100, 300, 200)

#         self.button = QPushButton("Select Color", self)
#         self.button.clicked.connect(self.on_button_clicked)
#         self.button.setGeometry(100, 75, 100, 50)

#     def on_button_clicked(self):
#         color = QColorDialog.getColor()

#         if color.isValid():
#             self.button.setStyleSheet(f"background-color: {color.name()};")

# if __name__ == "__main__":
#     app = QApplication([])
#     window = MyWindow()
#     window.show()
#     app.exec_()

# 2222222222222222222
# import sys
# from PyQt5.QtWidgets import QApplication, QWidget, QColorDialog, QPushButton
# from PyQt5.QtGui import QPainter, QColor, QFont
# from PyQt5.QtCore import Qt, QRect


# class ColorPickerWidget(QWidget):
#     def __init__(self):
#         super().__init__()  # Use double underscores for "__init__"
#         self.color = QColor(255, 0, 0)  # Initial color (red)
#         self.button_radius = 50
#         self.button_center = self.button_radius + 10  # Button center position
#         self.button_size = self.button_radius * 2 + 20  # Button size

#         self.setGeometry(300, 300, 200, 150)
#         self.setWindowTitle('Color Picker')

#         self.color_button = QPushButton(self)
#         self.color_button.setGeometry(QRect(10, 10, self.button_size, self.button_size))
#         self.color_button.clicked.connect(self.show_color_dialog)

#     def paintEvent(self, event):
#         painter = QPainter(self)
#         painter.setRenderHint(QPainter.Antialiasing)

#         # Draw circular button
#         painter.setBrush(self.color)
#         painter.drawEllipse(QRect(10, 10, self.button_size, self.button_size))

#     def show_color_dialog(self):
#         color = QColorDialog.getColor(self.color, self)
#         if color.isValid():
#             self.color = color
#             self.update()

#     def mousePressEvent(self, event):
#         # Check if the mouse press event occurred within the circular button
#         if event.button() == Qt.LeftButton and (
#                 (event.pos() - self.color_button.geometry().center()).manhattanLength() <= self.button_radius):
#             self.show_color_dialog()


# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = ColorPickerWidget()
#     window.show()
#     sys.exit(app.exec_())

# 33333333333333333333
# from PyQt5.QtWidgets import QApplication, QMainWindow, QHBoxLayout, QPushButton, QFrame, QWidget

# class MyWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()

#         self.setWindowTitle("Button Example")
#         self.setGeometry(100, 100, 300, 200)

#         # Create a QHBoxLayout for the main widget
#         layout = QHBoxLayout()

#         # Create the left button
#         self.left_button = QPushButton("Left Button")
#         layout.addWidget(self.left_button)

#         # Create the center QFrame
#         self.center_frame = QFrame()
#         self.center_frame_layout = QHBoxLayout(self.center_frame)
#         layout.addWidget(self.center_frame)

#         # Create the right button
#         self.right_button = QPushButton("Right Button")
#         layout.addWidget(self.right_button)

#         # Set the layout to the main widget
#         widget = QWidget()
#         widget.setLayout(layout)
#         self.setCentralWidget(widget)

#         # Create the button in the center frame
#         self.center_button = QPushButton("Center Button")
#         self.center_frame_layout.addWidget(self.center_button)

#         # Connect the center button's clicked signal to the slot
#         self.center_button.clicked.connect(self.add_button_to_center_frame)

#     def add_button_to_center_frame(self):
#         new_button = QPushButton("New Button")
#         self.center_frame_layout.addWidget(new_button)

# if __name__ == "__main__":
#     app = QApplication([])
#     window = MyWindow()
#     window.show()
#     app.exec_()

#  44444444444444444444444444444444
# from PyQt5.QtWidgets import QApplication, QMainWindow, QToolButton, QVBoxLayout, QWidget
# import sys

# class MyWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()

#         central_widget = QWidget(self)
#         layout = QVBoxLayout(central_widget)

#         self.tool_button1 = QToolButton()
#         self.tool_button1.setText("Button 1")
#         self.tool_button1.clicked.connect(self.on_tool_button_clicked)

#         self.tool_button2 = QToolButton()
#         self.tool_button2.setText("Button 2")
#         self.tool_button2.clicked.connect(self.on_tool_button_clicked)

#         layout.addWidget(self.tool_button1)
#         layout.addWidget(self.tool_button2)

#         self.setCentralWidget(central_widget)

#     def on_tool_button_clicked(self):
#         sender_button = self.sender()
#         print("Selected Button Text:", sender_button.text())

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = MyWindow()
#     window.show()
#     sys.exit(app.exec_())
# from PyQt5 import QtCore, QtGui, QtWidgets
# from PyQt5.QtCore import QObject
# import shutil, os

# class Ui_MainWindow(object):

#     def drag_enter_event(self, event):
#         if event.mimeData().hasUrls():
#             event.accept()
#         else:
#             event.ignore()  


#     def drag_move_event(self, event):
#         if event.mimeData().hasUrls():
#             event.setDropAction(QtCore.Qt.CopyAction)
#             event.accept()
#         else:
#             event.ignore()

#     def drop_event(self, event):
#             if event.mimeData().hasUrls():
#                 event.setDropAction(QtCore.Qt.CopyAction)
#                 event.accept()
#                 if len(os.listdir('./Drop folder')) > 0:
#                     shutil.rmtree('./Drop folder')
#                     os.mkdir('Drop folder')
#                 for url in event.mimeData().urls():
#                     name = url.toLocalFile()
#                     shutil.copy2(name,'./Drop folder')
#                 # self.listWidget.setViewMode(QtWidgets.QListWidget.IconMode)  # set the view mode to icon mode
#                 # self.listWidget.setIconSize(QtCore.QSize(100, 100))  # set the size of the icons
#                 # self.listWidget.setResizeMode(QtWidgets.QListWidget.Adjust)  # adjust the size of the items to the available space
#                 # self.listWidget.setWrapping(True)
    

#     def setupUi(self, MainWindow):
#         MainWindow.setObjectName("MainWindow")
#         MainWindow.resize(1006, 602)
#         self.centralwidget = QtWidgets.QWidget(MainWindow)
#         self.centralwidget.setObjectName("centralwidget")
#         self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
#         self.gridLayout.setObjectName("gridLayout")
#         self.frame = QtWidgets.QFrame(self.centralwidget)
#         self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
#         self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
#         self.frame.setObjectName("frame")

#         self.listWidget = QtWidgets.QListWidget(self.frame)
#         self.listWidget.setGeometry(QtCore.QRect(0, 0, 261, 451))
#         self.listWidget.setObjectName("listWidget")
#         self.listWidget.setSelectionMode(
#             QtWidgets.QAbstractItemView.ExtendedSelection
#         )

#         self.listWidget.setStyleSheet("QScrollBar:vertical {"
#                                "    border: none;"
#                                "    background: #f5f5f5;"
#                                "    width: 10px;"
#                                "    margin: 0px 0 0px 0;"
#                                "}"
#                                ""
#                                "QScrollBar::handle:vertical {"
#                                "    background: #555;"
#                                "    min-height: 20px;"
#                                "}"
#                                ""
#                                "QScrollBar::add-line:vertical {"
#                                "    border: none;"
#                                "    background: #f5f5f5;"
#                                "    height: 0px;"
#                                "    subcontrol-position: bottom;"
#                                "    subcontrol-origin: margin;"
#                                "}"
#                                ""
#                                "QScrollBar::sub-line:vertical {"
#                                "    border: none;"
#                                "    background: #f5f5f5;"
#                                "    height: 0px;"
#                                "    subcontrol-position: top;"
#                                "    subcontrol-origin: margin;"
#                                "}")

#         self.listWidget.setObjectName("listWidget")

#         # Enable drag and drop for the QListWidget
#         self.listWidget.setAcceptDrops(True)

#         # Connect signals for drag and drop events (IMAGES)
#         self.listWidget.dragEnterEvent = self.drag_enter_event
#         self.listWidget.dragMoveEvent = self.drag_move_event
#         self.listWidget.dropEvent = self.drop_event


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())
# from PyQt5 import QtWidgets, QtGui

# class HoverCommandLinkButton(QtWidgets.QCommandLinkButton):
#     def __init__(self, text, icon_path, parent=None):
#         super().__init__(text, parent)
#         self.default_text = text
#         self.default_icon = QtGui.QIcon(icon_path)

#         self.setStyleSheet('''
#             QCommandLinkButton {
#                 icon-size: 32px;  /* Set your desired icon size */
#                 padding-right: 0px;  /* Adjust as needed */
#             }
#         ''')

#         self.set_icon_visible(True)  # Show the icon by default

#     def enterEvent(self, event):
#         self.set_icon_visible(False)  # Hide the icon on hover
#         self.set_text("Coming Soon")
#         super().enterEvent(event)

#     def leaveEvent(self, event):
#         self.set_icon_visible(True)  # Show the icon when the mouse leaves
#         self.set_text(self.default_text)
#         super().leaveEvent(event)

#     def set_icon_visible(self, visible):
#         icon = self.default_icon if visible else QtGui.QIcon()
#         self.setIcon(icon)
    
#     def set_text(self, text):
#         label = self.findChild(QtWidgets.QLabel)
#         if label:
#             font = QtGui.QFont("Work Sans", 7)
#             label.setFont(font)
#             label.setText(text)

# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
    
#     window = QtWidgets.QMainWindow()
#     window.setGeometry(100, 100, 400, 200)  # Set the main window's geometry
    
#     frame = QtWidgets.QFrame()
#     frame_layout = QtWidgets.QVBoxLayout(frame)
    
#     # Create a HoverCommandLinkButton with initial text and icon
#     button = HoverCommandLinkButton("Community", "Icons/www.png")
    
#     frame_layout.addWidget(button)
#     window.setCentralWidget(frame)  # Set the QFrame as the central widget
    
#     window.show()
#     sys.exit(app.exec_())
# from PyQt5 import QtWidgets, QtGui, QtCore

# class MyWindow(QtWidgets.QWidget):
#     def __init__(self):
#         super().__init__()

#         self.initUI()

#     def initUI(self):
#         self.setGeometry(100, 100, 400, 400)
#         self.setWindowTitle('Multiple Elements Example')

#         # Create a scroll area to accommodate the elements
#         scroll_area = QtWidgets.QScrollArea(self)
#         scroll_area.setWidgetResizable(True)
#         self.scroll_widget = QtWidgets.QWidget(scroll_area)
#         self.scroll_layout = QtWidgets.QVBoxLayout(self.scroll_widget)
#         scroll_area.setWidget(self.scroll_widget)

#         # Create and add multiple elements to the scroll area
#         num_elements = 15  # You can change this to the desired number of elements
#         for i in range(num_elements):
#             element_frame = QtWidgets.QFrame()
#             element_frame.setGeometry(QtCore.QRect(30, 140, 301, 41))
#             element_frame.setStyleSheet("border: 1px solid black;\n"
#                                         "border-radius: 7px;\n"
#                                         "background-color: rgb(242, 242, 242);\n"
#                                         "border-color: #f2f2f2;")

#             element_layout = QtWidgets.QHBoxLayout(element_frame)

#             binary_o = QtWidgets.QToolButton()
#             binary_o.setText("Click to assign")
#             binary_o.setStyleSheet('font: 9pt "Work Sans";'
#                                    'background-color: white;'
#                                    'color: black;'
#                                    'border-radius: 12px;')
#             binary_o.setPopupMode(QtWidgets.QToolButton.InstantPopup)
#             element_layout.addWidget(binary_o)

#             toolButton_o = QtWidgets.QToolButton()
#             toolButton_o.setText("")
#             pixmap = QtGui.QPixmap("Icons/menu.png")
#             icon = QtGui.QIcon(pixmap)
#             toolButton_o.setIcon(icon)
#             element_layout.addWidget(toolButton_o)

#             lineEdit_2o = QtWidgets.QLineEdit()
#             lineEdit_2o.setFont(QtGui.QFont("Work Sans Light"))
#             lineEdit_2o.setStyleSheet("border: 1px solid black;"
#                                       "border-radius: 10px;"
#                                       "background-color: rgb(242, 242, 242);"
#                                       "border-color: #f2f2f2;")
#             lineEdit_2o.setAlignment(QtCore.Qt.AlignCenter)
#             lineEdit_2o.setPlaceholderText("+ add delay")
#             element_layout.addWidget(lineEdit_2o)

#             self.scroll_layout.addWidget(element_frame)

#         self.show()

# if __name__ == '__main__':
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     window = MyWindow()
#     sys.exit(app.exec_())
# from PyQt5 import QtWidgets

# class MyWindow(QtWidgets.QWidget):
#     def __init__(self):
#         super().__init__()

#         self.initUI()

#     def initUI(self):
#         self.setGeometry(100, 100, 400, 400)
#         self.setWindowTitle('Multiple Buttons Example')

#         # Create a layout to hold the buttons
#         layout = QtWidgets.QVBoxLayout(self)

#         num_buttons = 5  # You can change this to the desired number of buttons

#         # Create buttons in a loop and assign unique names
#         for i in range(1, num_buttons + 1):
#             button = QtWidgets.QPushButton(f'Button {i}', self)
#             button.clicked.connect(lambda _, button_num=i: self.button_clicked(button_num))  # Connect a click event handler
#             layout.addWidget(button)
#             setattr(self, f'button_{i}', button)  # Set button as an attribute of the class

#     def button_clicked(self, button_num):
#         print(f'Button {button_num} clicked!')

# if __name__ == '__main__':
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     window = MyWindow()
#     window.show()
#     sys.exit(app.exec_())
# from PyQt5 import QtWidgets

# class MyWindow(QtWidgets.QWidget):
#     def __init__(self):
#         super().__init__()

#         self.initUI()

#     def initUI(self):
#         self.setGeometry(100, 100, 400, 400)
#         self.setWindowTitle('Multiple Buttons Example')

#         # Create a layout to hold the buttons
#         layout = QtWidgets.QVBoxLayout(self)

#         num_buttons = 5  # You can change this to the desired number of buttons

#         # Create buttons in a loop, assign unique names, and print the attribute name
#         for i in range(1, num_buttons + 1):
#             button = QtWidgets.QPushButton(f'Button {i}', self)
#             button_name = f'button_{i}'  # Generate the attribute name
#             setattr(self, button_name, button)  # Set button as an attribute of the class
#             print(f'Created attribute: {button_name}')  # Print the attribute name
#             button.clicked.connect(lambda _, button_num=i: self.button_clicked(button_num))  # Connect a click event handler
#             layout.addWidget(button)

#     def button_clicked(self, button_num):
#         print(f'Button {button_num} clicked!')

# if __name__ == '__main__':
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     window = MyWindow()
#     window.show()
#     sys.exit(app.exec_())






# from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget, QPushButton
# from PyQt5.QtGui import QPixmap, QColor, QFont, QFontMetrics, QPainter, QIcon
# from PyQt5 import QtCore
# import sys


# def generate_contact_icon(contact_name, icon_size=64):
#     icon = QPixmap(icon_size, icon_size)
#     icon.fill(QColor("transparent"))

#     painter = QPainter(icon)
#     painter.setRenderHint(QPainter.Antialiasing)

#     font = QFont("Arial", 20)
#     painter.setFont(font)

#     font_metrics = QFontMetrics(font)

#     text_width = font_metrics.width(contact_name)
#     text_height = font_metrics.height()
#     x = (icon_size - text_width) / 2
#     y = (icon_size - text_height) / 2 + text_height

#     painter.setPen(QColor("white"))

#     painter.drawText(x, y, contact_name[0].upper())

#     painter.end()

#     return icon




# if __name__ == "__main__":
#     app = QApplication([])

#     contact_name = "John Doe"
#     icon = generate_contact_icon(contact_name)

#     window = QWidget()
#     window.setWindowTitle("Contact Icon")
#     layout = QVBoxLayout()

#     button = QPushButton("Click Me")
#     button.setIconSize(QtCore.QSize(64, 64))  # Set the size of the icon
#     button.setIcon(QIcon(icon))  # Set the icon

#     layout.addWidget(button)
#     window.setLayout(layout)
#     window.show()

#     sys.exit(app.exec_())


# from PyQt5.QtWidgets import QApplication, QVBoxLayout, QWidget, QToolButton
# from PyQt5.QtGui import QPixmap, QIcon, QPainter
# from PyQt5 import QtGui
# from PyQt5 import QtCore
# import sys

# def generate_contact_icon(contact_name, icon_size=64):
#     icon = QPixmap(icon_size, icon_size)
#     icon.fill(QtCore.Qt.transparent)

#     # Customize the icon appearance here
#     painter = QPainter(icon)
#     painter.setRenderHint(QPainter.Antialiasing)
#     painter.setPen(QtGui.QColor("white"))
#     font = painter.font()
#     font.setPixelSize(24)
#     painter.setFont(font)
#     painter.drawText(icon.rect(), QtCore.Qt.AlignCenter, contact_name[0].upper())
#     painter.end()

#     return icon

# if __name__ == "__main__":
#     app = QApplication([])

#     contact_name = "John Doe"
#     icon = generate_contact_icon(contact_name)

#     window = QWidget()
#     window.setWindowTitle("Contact Icon")
#     layout = QVBoxLayout()

#     button = QToolButton()
#     button.setIconSize(QtCore.QSize(64, 64))  # Set the size of the icon

#     # Specify the full path to your icon image file here
#     icon_path = "C:/Users/Dell/Downloads/sceneries/00000000.jpg"
#     button.setIcon(QIcon(icon_path))  # Set the icon

#     button.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)  # Set style to display only the icon

#     layout.addWidget(button)
#     window.setLayout(layout)
#     window.show()

#     sys.exit(app.exec_())

# from PyQt5.QtWidgets import QApplication, QVBoxLayout, QWidget, QToolButton
# from PyQt5.QtGui import QPixmap, QIcon, QPainter
# from PyQt5 import QtGui
# from PyQt5 import QtCore
# import sys, random

# def generate_contact_icon(contact_name, icon_size=64):
#     icon = QPixmap(icon_size, icon_size)
#     icon.fill(QtCore.Qt.transparent)

#     # Customize the icon appearance here
#     painter = QPainter(icon)
#     painter.setRenderHint(QPainter.Antialiasing)
#     painter.setPen(QtGui.QColor(f"#{random.randint(000000,999999)}"))
#     font = painter.font()
#     font.setPixelSize(24)
#     painter.setFont(font)
#     painter.drawText(icon.rect(), QtCore.Qt.AlignCenter, contact_name[:2])
#     painter.end()

#     return icon

# if __name__ == "__main__":
#     app = QApplication([])

#     contact_name = "John go Doe"
#     first_letter = "".join(next(zip(*contact_name.split()))).upper()
#     icon = generate_contact_icon(first_letter)

#     window = QWidget()
#     window.setWindowTitle("Contact Icon")
#     layout = QVBoxLayout()

#     button = QToolButton()
#     button.setIconSize(QtCore.QSize(64, 64))  # Set the size of the icon
#     button.setIcon(QIcon(icon))  # Set the icon
#     button.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)  # Set style to display only the icon

#     layout.addWidget(button)
#     window.setLayout(layout)
#     window.show()


#     sys.exit(app.exec_())

# from pynput import keyboard
# from ctypes import cast, POINTER
# from comtypes import CLSCTX_ALL
# from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
# import time

# # Function to increase the audio volume
# def increase_volume():
#     devices = AudioUtilities.GetSpeakers()
#     interface = devices.Activate(
#         IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
#     volume = cast(interface, POINTER(IAudioEndpointVolume))
#     current_volume = volume.GetMasterVolumeLevelScalar()
#     new_volume = min(current_volume + 0.1, 1.0)  # Increase by 10%
#     volume.SetMasterVolumeLevelScalar(new_volume, None)

# # Function to handle keypress events
# def on_key_release(key):
#     try:
#         if key.char == '4':
#             if any([keyboard.Controller().is_pressed(hotkey) for hotkey in ['ctrl', '4']]):
#                 increase_volume()
#     except AttributeError:
#         pass

# # Start listening for keypress events
# with keyboard.Listener(on_release=on_key_release) as listener:
#     listener.join()
# importing libraries
# from PyQt5.QtWidgets import *
# from PyQt5 import QtCore, QtGui
# from PyQt5.QtGui import *
# from PyQt5.QtCore import *
# import sys


# class Window(QMainWindow):

# 	def __init__(self):
# 		super().__init__()

# 		# setting title
# 		self.setWindowTitle("Python ")

# 		# setting geometry
# 		self.setGeometry(100, 100, 600, 400)

# 		# calling method
# 		# creating a radio button
# 		self.button1 = QRadioButton("Button1", self)

# 		# setting geometry of radio button
# 		self.button1.setGeometry(200, 150, 100, 40)

# 		# creating push button
# 		self.push = QPushButton("Change the text ", self)

# 		# setting geometry of push button
# 		self.push.setGeometry(200, 200, 100, 40)

# 		# connect push button to method
# 		self.push.clicked.connect(self.changeName)

# 		# showing all the widgets
# 		self.show()

# 	# method for widgets
# 	# def UiComponents(self):

		

# 	# creating changeName method
# 	def changeName(self):

# 		# setting new text to radio button
# 		self.button1.setText("New Name")



# # create pyqt5 app
# App = QApplication(sys.argv)

# # create the instance of our Window
# window = Window()

# # start the app
# sys.exit(App.exec())

# import sys
# import json
# import random
# from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton

# class ButtonMappingApp(QWidget):
#     def __init__(self):
#         super().__init__()

#         self.upper_buttons = []
#         self.lower_buttons = []
#         self.button_mapping = {}

#         self.init_ui()

#     def init_ui(self):
#         layout = QVBoxLayout()

#         for char in "ABCD":
#             upper_button = QPushButton(char)
#             upper_button.clicked.connect(self.upper_button_clicked)
#             layout.addWidget(upper_button)
#             self.upper_buttons.append(upper_button)

#         for num in "1234":
#             lower_button = QPushButton(num)
#             lower_button.clicked.connect(self.lower_button_clicked)
#             layout.addWidget(lower_button)
#             self.lower_buttons.append(lower_button)

#         self.load_button_mapping()

#         self.setLayout(layout)
#         self.setWindowTitle('Button Mapping App')
#         self.show()

#     def upper_button_clicked(self):
#         sender = self.sender()
#         if sender in self.upper_buttons and sender.text() in self.button_mapping:
#             lower_button_text = self.button_mapping[sender.text()]
#             sender.setText(lower_button_text)

#     def lower_button_clicked(self):
#         sender = self.sender()
#         if sender in self.lower_buttons:
#             upper_button_text = random.choice(["A", "B", "C", "D"])
#             self.button_mapping[upper_button_text] = sender.text()
#             self.save_button_mapping()
#             self.update_upper_buttons()

#     def update_upper_buttons(self):
#         for upper_button in self.upper_buttons:
#             if upper_button.text() in self.button_mapping:
#                 lower_button_text = self.button_mapping[upper_button.text()]
#                 upper_button.setText(lower_button_text)

#     def load_button_mapping(self):
#         try:
#             with open('button_mapping.json', 'r') as file:
#                 self.button_mapping = json.load(file)
#                 self.update_upper_buttons()
#         except FileNotFoundError:
#             pass

#     def save_button_mapping(self):
#         with open('button_mapping.json', 'w') as file:
#             json.dump(self.button_mapping, file)

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = ButtonMappingApp()
#     sys.exit(app.exec_())

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton
from PyQt5.QtGui import QIcon, QPixmap, QFont, QPainter, QColor
from PyQt5 import QtCore
import sqlite3
import random

class ButtonMappingApp(QWidget):
    def __init__(self):
        super().__init__()

        self.upper_buttons = []
        self.lower_buttons = []

        # Create the SQLite table
        self.create_table()

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        for char in "ABCD":
            upper_button = QPushButton(char)
            upper_button.setText(char)
            upper_button.setObjectName(char)
            upper_button.clicked.connect(self.upper_button_clicked)
            layout.addWidget(upper_button)
            self.upper_buttons.append(upper_button)

        for num in "1234":
            lower_button = QPushButton(num)
            lower_button.clicked.connect(self.lower_button_clicked)
            layout.addWidget(lower_button)
            self.lower_buttons.append(lower_button)

        self.update_upper_buttons()

        self.setLayout(layout)
        self.setWindowTitle('Button Mapping App')
        self.show()

    def upper_button_clicked(self):
        sender = self.sender()
        if sender in self.upper_buttons:
            button_id = sender.text()
            button_text = self.get_mapping(button_id)
            sender.setText(button_text)

    def lower_button_clicked(self):
        sender = self.sender()
        if sender in self.lower_buttons:
            upper_button = random.choice(self.upper_buttons)
            button_id = upper_button.objectName()
            button_text = sender.text()
            self.set_mapping(button_id, button_text)
            self.update_upper_buttons()

    def update_upper_buttons(self):
        for upper_button in self.upper_buttons:
            button_id = upper_button.text()
            button_text = self.get_mapping(button_id)
            upper_button.setText(button_text)

    def create_table(self):
        conn = sqlite3.connect('button_mapping.db')
        cursor = conn.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS button_mapping (
                button_id TEXT PRIMARY KEY,
                button_text TEXT
            )
        ''')

        conn.commit()
        conn.close()

    def set_mapping(self, button_id, button_text):
        conn = sqlite3.connect('button_mapping.db')
        cursor = conn.cursor()
        print(button_id)

        cursor.execute('''
            INSERT OR REPLACE INTO button_mapping (button_id, button_text)
            VALUES (?, ?)
        ''', (button_id, button_text,))

        conn.commit()
        conn.close()

    def get_mapping(self, button_id):
        conn = sqlite3.connect('button_mapping.db')
        cursor = conn.cursor()

        cursor.execute('SELECT button_text FROM button_mapping WHERE button_id=?', (button_id,))
        result = cursor.fetchone()

        conn.close()

        return result[0] if result else ''

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ButtonMappingApp()
    sys.exit(app.exec_())

