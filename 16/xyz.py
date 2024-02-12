# import sys
# import os
# from PyQt5 import QtWidgets, QtCore

# class MyWindow(QtWidgets.QMainWindow):
#     def __init__(self):
#         super().__init__()

#         self.central_widget = QtWidgets.QWidget()
#         self.setCentralWidget(self.central_widget)

#         self.layout = QtWidgets.QVBoxLayout(self.central_widget)

#         self.qframe = QtWidgets.QFrame()
#         self.qframe_layout = QtWidgets.QVBoxLayout(self.qframe)

#         self.layout.addWidget(self.qframe)

#         self.timer = QtCore.QTimer(self)
#         self.timer.timeout.connect(self.update_qframe)
#         self.timer.start(1000)  # Check for new files every second

#     def update_qframe(self):
#         json_files = [f for f in os.listdir("Actions/Profile1_demo/Action") if f.endswith(".json")]
#         json_file_count = len(json_files)

#         # Remove existing buttons
#         for i in reversed(range(self.qframe_layout.count())):
#             widget = self.qframe_layout.itemAt(i).widget()
#             if widget is not None:
#                 widget.deleteLater()

#         # Add new buttons
#         for i in range(json_file_count):
#             button = QtWidgets.QPushButton(f"Button {i+1}")
#             self.qframe_layout.addWidget(button)

# if __name__ == "__main__":
#     app = QtWidgets.QApplication(sys.argv)
#     window = MyWindow()
#     window.show()
#     sys.exit(app.exec_())
# importing the required libraries

from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5 import QtGui
import sys



class Window(QMainWindow):
	def __init__(self):
		super().__init__()

		# set the title
		self.setWindowTitle("Memory")

		# setting the geometry of window
		self.setGeometry(0, 0, 400, 300)

		# creating a label widget
		self.label_1 = QLabel("Label", self)

		# moving position
		self.label_1.move(100, 100)

		# setting up border
		self.label_1.setStyleSheet("border: 1px solid black;")

		# delete reference
		self.label_1.deleteLater()

		# show all the widgets
		self.show()



# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

# start the app
sys.exit(App.exec())

