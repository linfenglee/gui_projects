import sys

from PyQt5.QtWidgets import QApplication, QWidget


if __name__ == "__main__":

    # create QApplication instance
    app = QApplication(sys.argv)

    # create a window
    w = QWidget()

    # set the size of the window
    w.resize(300, 150)
    w.move(300, 300)

    w.setWindowTitle("First PyQt5 App")

    w.show()

    sys.exit(app.exec_())