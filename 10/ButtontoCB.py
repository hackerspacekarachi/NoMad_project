import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QToolButton, QMenu
from PyQt5.QtGui import QFont

class AppDemo(QWidget):
    def __init__(self):
        super().__init__()

        menu = QMenu()
        menu.setStyleSheet("""
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

        menu.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint | QtCore.Qt.FramelessWindowHint)
        #menu.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        menu.setAttribute(QtCore.Qt.WA_TranslucentBackground)

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

 
        # create the 'Differentiate left/right modofiers' action and disable it
        action2 = menu.addAction("Differentiate left / right modifiers")
        action2.setEnabled(False)
        #bold_font = QFont()
        #bold_font.setBold(True)
        #action2.setFont(bold_font)

        self.binary = QToolButton(self)
        self.binary.setText("Keystroke 1")
        self.binary.setStyleSheet('''
                    font: 8pt "Work Sans";
                    background-color: white;
                    color: black;
                    border-radius: 8px;
                    text-align: left;
                   
                    ''')
        #self.binary.move(100, 100)
        #self.binary.resize(150, 150)
        self.binary.setGeometry(QtCore.QRect(50, 10, 221, 21))
        self.binary.setPopupMode(QToolButton.InstantPopup)
        #self.binary.setPopupMode(QToolButton.MenuButtonPopup)

        menu.triggered.connect(lambda x: self.menu_triggered(x.text()))

        self.binary.setMenu(menu)
        self.add_menu(K1, menu)

    def add_menu(self, data, menu_obj):
        if isinstance(data, dict):
            for k, v in data.items():
                sub_menu = QMenu(k, menu_obj)
                menu_obj.addMenu(sub_menu)
                self.add_menu(v, sub_menu)
        elif isinstance(data, list):
            for element in data:
                self.add_menu(element, menu_obj)

        else:
            action = menu_obj.addAction(data)
            action.setIconVisibleInMenu(False)


    def menu_triggered(self, text):
        self.binary.setText(text)
        menu_obj = self.binary.menu()
        menu_obj.close()  
    
    def mousePressEvent(self, event):
        # Hide the menu if the mouse press event occurred outside the menu
        if self.binary.menu().isVisible() and not self.binary.menu().rect().contains(event.pos()):
            self.binary.menu().hide()

        # Call the base class implementation of the event handler
        super().mousePressEvent(event)    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = AppDemo()
    demo.show()
    sys.exit(app.exec_())