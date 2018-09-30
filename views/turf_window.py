from PyQt5.QtWidgets import QMainWindow, QAction, QToolBar
from PyQt5.QtCore import QSize, Qt


class TurfWindow(QMainWindow):

    def __init__(self, images):
        super(TurfWindow, self).__init__()

        self.setObjectName('TurfWindow')
        self.resize(850, 560)
        self.setWindowTitle('Bluestreets Turf')
        self.setWindowIcon(images['small_donkey'])
        self.setStyleSheet('background-color: white;')

        self.toolbar = QToolBar(self)
        self.toolbar.setStyleSheet('background-color: #3fb0ac; color: white')
        self.toolbar.setIconSize(QSize(48, 48))
        self.toolbar.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.addToolBar(Qt.TopToolBarArea, self.toolbar)

        add_act = QAction(images['add_icon'], 'Add', self)
        # noinspection PyUnresolvedReferences
        add_act.triggered.connect(self.__add_triggered)

        drop_act = QAction(images['drop_icon'], 'Drop', self)
        # noinspection PyUnresolvedReferences
        drop_act.triggered.connect(self.__drop_triggered)

        close_act = QAction(images['close_icon'], 'Close', self)
        # noinspection PyUnresolvedReferences
        close_act.triggered.connect(self.__close_triggered)

        self.toolbar.addAction(add_act)
        self.toolbar.addAction(drop_act)
        self.toolbar.addAction(close_act)

    def __add_triggered(self):
        # self.turf_window = TurfWindow(self.images)
        # self.turf_window.show()
        # self.open_windows.append(self.turf_window)
        print('add')

    def __drop_triggered(self):
        print('drop')

    def __close_triggered(self):
        self.close()
