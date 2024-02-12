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
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject
import shutil, os

class Ui_MainWindow(object):

    def drag_enter_event(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()  


    def drag_move_event(self, event):
        if event.mimeData().hasUrls():
            event.setDropAction(QtCore.Qt.CopyAction)
            event.accept()
        else:
            event.ignore()

    def drop_event(self, event):
            if event.mimeData().hasUrls():
                event.setDropAction(QtCore.Qt.CopyAction)
                event.accept()
                if len(os.listdir('./Drop folder')) > 0:
                    shutil.rmtree('./Drop folder')
                    os.mkdir('Drop folder')
                for url in event.mimeData().urls():
                    name = url.toLocalFile()
                    shutil.copy2(name,'./Drop folder')
                # self.listWidget.setViewMode(QtWidgets.QListWidget.IconMode)  # set the view mode to icon mode
                # self.listWidget.setIconSize(QtCore.QSize(100, 100))  # set the size of the icons
                # self.listWidget.setResizeMode(QtWidgets.QListWidget.Adjust)  # adjust the size of the items to the available space
                # self.listWidget.setWrapping(True)
    

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1006, 602)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.listWidget = QtWidgets.QListWidget(self.frame)
        self.listWidget.setGeometry(QtCore.QRect(0, 0, 261, 451))
        self.listWidget.setObjectName("listWidget")
        self.listWidget.setSelectionMode(
            QtWidgets.QAbstractItemView.ExtendedSelection
        )

        self.listWidget.setStyleSheet("QScrollBar:vertical {"
                               "    border: none;"
                               "    background: #f5f5f5;"
                               "    width: 10px;"
                               "    margin: 0px 0 0px 0;"
                               "}"
                               ""
                               "QScrollBar::handle:vertical {"
                               "    background: #555;"
                               "    min-height: 20px;"
                               "}"
                               ""
                               "QScrollBar::add-line:vertical {"
                               "    border: none;"
                               "    background: #f5f5f5;"
                               "    height: 0px;"
                               "    subcontrol-position: bottom;"
                               "    subcontrol-origin: margin;"
                               "}"
                               ""
                               "QScrollBar::sub-line:vertical {"
                               "    border: none;"
                               "    background: #f5f5f5;"
                               "    height: 0px;"
                               "    subcontrol-position: top;"
                               "    subcontrol-origin: margin;"
                               "}")

        self.listWidget.setObjectName("listWidget")

        # Enable drag and drop for the QListWidget
        self.listWidget.setAcceptDrops(True)

        # Connect signals for drag and drop events (IMAGES)
        self.listWidget.dragEnterEvent = self.drag_enter_event
        self.listWidget.dragMoveEvent = self.drag_move_event
        self.listWidget.dropEvent = self.drop_event


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())