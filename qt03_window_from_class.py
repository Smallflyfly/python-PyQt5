import qt02_window_class as win
import sys
from PyQt5.Qt import *

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = win.Window()

    window.show()

    sys.exit(app._exec())