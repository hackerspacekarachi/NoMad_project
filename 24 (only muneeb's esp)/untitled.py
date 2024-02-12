from PyQt5.QtWidgets import QApplication, QFrame, QSlider, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        # Create a vertical QSlider
        self.vertical_slider = QSlider()
        self.vertical_slider.setOrientation(Qt.Vertical)
        self.vertical_slider.setMinimum(0)
        self.vertical_slider.setMaximum(100)

        # Connect the slider's valueChanged signal to a custom function
        self.vertical_slider.valueChanged.connect(self.adjust_frame_position)

        layout.addWidget(self.vertical_slider)

        # Create a QFrame
        self.my_frame = QFrame()
        self.my_frame.setFrameShape(QFrame.StyledPanel)

        # Add some content to the frame
        content_layout = QVBoxLayout(self.my_frame)
        for i in range(20):
            content_layout.addWidget(QFrame(self.my_frame))

        layout.addWidget(self.my_frame)

    def adjust_frame_position(self):
        # Adjust the position of the frame based on the slider value
        value = self.vertical_slider.value()
        self.my_frame.setGeometry(0, -value, self.my_frame.width(), self.my_frame.height())

if __name__ == '__main__':
    app = QApplication([])
    widget = MyWidget()
    widget.show()
    app.exec_()
