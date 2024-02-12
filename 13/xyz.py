from PyQt5 import QtWidgets

class InputPopup(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        
    def init_ui(self):
        layout = QtWidgets.QVBoxLayout()
        self.open_popup_button = QtWidgets.QPushButton("Open Popup")
        self.open_popup_button.clicked.connect(self.show_input_popup)
        layout.addWidget(self.open_popup_button)
        self.setLayout(layout)
        
    def show_input_popup(self):
        user_input, ok_pressed = QtWidgets.QInputDialog.getText(self, "Input Popup", "Enter something:")
        if ok_pressed and user_input:
            print("User input:", user_input)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main_window = InputPopup()
    main_window.setWindowTitle("Main Window")
    main_window.setGeometry(200, 200, 400, 200)
    main_window.show()
    sys.exit(app.exec_())
