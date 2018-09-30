from PyQt5.QtWidgets import QDialog, QFrame, QLabel, QPushButton, QWidget, QVBoxLayout, QToolBar, QAction, QListWidget
from PyQt5.QtCore import QSize, Qt, QRect


class TurfPopup(QDialog):

    def __init__(self):
        super(TurfPopup, self).__init__()

        self.setObjectName('TurfPopup')
        self.resize(815, 540)
        self.setWindowTitle('Bluestreets Add Turf')

        panel = self.get_panel()

        # self.layoutWidget = QWidget(self)
        # self.layoutWidget.setGeometry(QRect(70, 110, 460, 380))
        # self.layout = QVBoxLayout(self.layoutWidget)
        # self.layout.setContentsMargins(0, 0, 0, 0)
        #
        # save_act = QAction('Save')
        # # noinspection PyUnresolvedReferences
        # save_act.triggered.connect(self.__save_triggered)
        #
        # self.toolbar = QToolBar(self.layoutWidget)
        # self.toolbar.setStyleSheet('background-color: #3fb0ac; color: white')
        # self.toolbar.setIconSize(QSize(48, 48))
        # self.toolbar.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        # # self.addToolBar(Qt.TopToolBarArea, self.toolbar)
        # self.toolbar.addAction(save_act)
        # self.toolbar.addAction('foo')
        #
        # self.layout.addWidget(self.toolbar)

        # layout = QVBoxLayout()
        # layout.addWidget(toolbar)
        # layout.setContentsMargins(0, 0, 0, 0)
        #
        # self.setLayout(layout)
        # self.setWindowIcon(images['small_donkey'])
        #
        # types_frame = QFrame(self)
        # types_frame.setGeometry(60, 90, 330, 330)
        # types_frame.setLayout(QVBoxLayout())

        # types_frame.addWidget(types_toolbar)

        # self.toolbar = QToolBar(self)
        # self.toolbar.setStyleSheet('background-color: #3fb0ac; color: white')
        # self.toolbar.setIconSize(QSize(48, 48))
        # self.toolbar.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        # self.addToolBar(Qt.TopToolBarArea, self.toolbar)
        #
        # save_act = QAction(images['save_icon'], 'Save', self)
        # # noinspection PyUnresolvedReferences
        # save_act.triggered.connect(self.__save_triggered)
        #
        # self.toolbar.addAction(save_act)
        #
        # self.lst = QListWidget(self)
        # self.lst.setGeometry(20, 90, 350, 200)
        # self.lst.setObjectName('lstTurf')
        #
        # self.__load()

    def get_panel(self):
        panel_frame = QFrame(self)
        panel_frame.setGeometry(QRect(30, 60, 640, 460))
        panel_frame.setStylesheet('background-color: gray')
        panel_frame.setFrameShape(QFrame.StyledPanel)
        panel_frame.setFrameShadow(QFrame.Raised)
        panel_frame.setObjectName('panel_frame')

        tb_frame = QFrame(panel_frame)
        tb_frame.setGeometry(QRect(10, 10, 610, 80))
        tb_frame.setStylesheet('background-color: skyblue')
        panel_frame.setFrameShape(QFrame.StyledPanel)
        panel_frame.setFrameShadow(QFrame.Raised)
        panel_frame.setObjectName('tb_frame')

        lbl = QLabel(tb_frame)
        lbl.setGeometry(QRect(30, 30, 68, 20))
        lbl.setText('the label')

        btn1 = QPushButton(tb_frame)
        btn1.setGeometry(QRect(130, 20, 112, 34))
        btn1.setObjectName("btn1")
        btn1.setText('btn1')

        btn2 = QPushButton(tb_frame)
        btn2.setGeometry(QRect(260, 20, 112, 34))
        btn2.setObjectName("btn2")
        btn2.setText('btn1')

        lst = QListWidget(panel_frame)
        lst.setGeometry(QRect(10, 100, 600, 340))
        lst.setStyleSheet('background-color: white')
        lst.setObjectName('the_list')

        return panel_frame


    def __save_triggered(self):
        print('save')
