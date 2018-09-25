import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QMenu
from PyQt5.QtGui import QIcon
from views.main_window0 import Ui_MainWindow
from views.main_window import MainWindow


# class MainWindow(QMainWindow, Ui_MainWindow):
#     def __init__(self):
#         super(MainWindow, self).__init__()
#         self.setupUi(self)
#
#         self.m = QMenu(self.toolBar)
#         self.m.addAction(QAction('Import'))
#         self.m.addAction(QAction('Worksheet'))
#         self.actionVoters.setMenu(self.m)
#         self.actionVoters.triggered.connect(self.m.show)

    # def voter_menu(self):
    #     self.m.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec_())
