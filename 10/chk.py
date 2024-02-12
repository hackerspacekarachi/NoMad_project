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
from PyQt5.QtWidgets import QApplication, QMainWindow, QHBoxLayout, QPushButton, QFrame, QWidget

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Button Example")
        self.setGeometry(100, 100, 300, 200)

        # Create a QHBoxLayout for the main widget
        layout = QHBoxLayout()

        # Create the left button
        self.left_button = QPushButton("Left Button")
        layout.addWidget(self.left_button)

        # Create the center QFrame
        self.center_frame = QFrame()
        self.center_frame_layout = QHBoxLayout(self.center_frame)
        layout.addWidget(self.center_frame)

        # Create the right button
        self.right_button = QPushButton("Right Button")
        layout.addWidget(self.right_button)

        # Set the layout to the main widget
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        # Create the button in the center frame
        self.center_button = QPushButton("Center Button")
        self.center_frame_layout.addWidget(self.center_button)

        # Connect the center button's clicked signal to the slot
        self.center_button.clicked.connect(self.add_button_to_center_frame)

    def add_button_to_center_frame(self):
        new_button = QPushButton("New Button")
        self.center_frame_layout.addWidget(new_button)

if __name__ == "__main__":
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec_()