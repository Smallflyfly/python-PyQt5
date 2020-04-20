from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("window class")
        self.resize(500,500)
    
    def setup_ui(self):
        label = QLabel(self)
        label.setText("标签")