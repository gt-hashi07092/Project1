import sys
from votemenu import Ui_MainWindow
from PyQt6 import QtWidgets
import logic

if __name__ == "__main__":
   app = QtWidgets.QApplication(sys.argv)
   MainWindow = logic.VotingWindow()
   MainWindow.show()
   sys.exit(app.exec())