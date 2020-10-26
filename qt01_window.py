from PyQt5.Qt import *
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QWidget()
    window.setWindowTitle("QT窗口")
    window.resize(400, 400)
    window.move(200, 200)

    label = QLabel(window)
    label.setText("标签")
    label.move(200,200)

    window.show()

    

    sys.exit(app.exec_())