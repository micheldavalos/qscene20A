from mainwindow import MainWindow
from PySide2.QtWidgets import QApplication
import sys

app = QApplication()
window = MainWindow()
window.show()
sys.exit(app.exec_())