from PyQt5.QtWidgets import QMainWindow, QAction, QToolBar, QToolButton, QMenu, QLabel
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import QSize, Qt, QRect


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.images = {}
        self.__build_icons()

        self.setObjectName('MainWindow')
        self.resize(850, 560)
        self.setWindowTitle('Bluestreets')
        self.setWindowIcon(self.images['small_donkey'])
        self.setStyleSheet('background-color: white;')

        self.toolbar = QToolBar(self)
        self.toolbar.setStyleSheet('background-color: #3fb0ac; color: white')
        self.toolbar.setIconSize(QSize(48, 48))
        self.toolbar.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.addToolBar(Qt.TopToolBarArea, self.toolbar)

        turf_act = QAction(self.images['turf'], 'Turf', self)
        # noinspection PyUnresolvedReferences
        turf_act.triggered.connect(self.__turf_triggered)

        vtr_btn = self.__make_toolbutton('Voters', self.images['voters'])
        vtr_btn.setMenu(self.__make_menu(vtr_btn, [
            {'text': 'Import County', 'func': self.__vtr_import_county},
            {'text': 'Import Spreadsheet', 'func': self.__vtr_import_spreadsheet},
            {'text': 'Worksheet', 'func': self.__vtr_worksheet},
            {'text': 'Export', 'func': self.__vtr_export}
        ]))

        con_btn = self.__make_toolbutton('Contacts', self.images['contacts'])
        con_btn.setMenu(self.__make_menu(con_btn, [
            {'text': 'Import County', 'func': self.__con_import_county},
            {'text': 'Import Spreadsheet', 'func': self.__con_import_spreadsheet},
            {'text': 'Entry Form', 'func': self.__con_entry_form},
            {'text': 'Battle Stations', 'func': self.__con_battle_stations},
            {'text': 'Export', 'func': self.__con_export}
        ]))

        grp_act = QAction(self.images['groups'], 'Groups', self)
        # noinspection PyUnresolvedReferences
        grp_act.triggered.connect(self.__grp_triggered)

        dta_btn = self.__make_toolbutton('Clean Data', self.images['soap'])
        dta_btn.setMenu(self.__make_menu(dta_btn, [
            {'text': 'Email Duplicates', 'func': self.__email_dups},
            {'text': 'Phone Duplicates', 'func': self.__phone_dups},
            {'text': 'Name + Address Duplicates', 'func': self.__name_addr_dups},
            {'text': 'Name Only Duplicates', 'func': self.__name_dups},
            {'text': 'Voter Sync', 'func': self.__voter_sync}
        ]))

        self.toolbar.addAction(turf_act)
        self.toolbar.addWidget(vtr_btn)
        self.toolbar.addWidget(con_btn)
        self.toolbar.addAction(grp_act)
        self.toolbar.addWidget(dta_btn)

        self.__build_images()
        self.__add_labels()

    def __build_icons(self):
        self.images['small_donkey'] = QIcon(QPixmap(":/small_donkey.png"))
        self.images['turf'] = QIcon(QPixmap(":/map.png"))
        self.images['voters'] = QIcon(QPixmap(":/voters.png"))
        self.images['contacts'] = QIcon(QPixmap(":/contacts.png"))
        self.images['groups'] = QIcon(QPixmap(":/groups.png"))
        self.images['soap'] = QIcon(QPixmap(":/soap.png"))

    def __build_images(self):
        self.images['adlai'] = QPixmap(":/adlai_button.jpg")
        self.images['blue_streets'] = QPixmap(":/blue_streets.png")
        self.images['ragtime_cowboy'] = QPixmap(":/ragtime_cowboy.png")
        self.images['cowboy_large'] = QPixmap(":/cowboy_large.jpg")

    def __make_toolbutton(self, text, icon):
        btn = QToolButton(self)
        btn.setText(text)
        btn.setIcon(icon)
        btn.setPopupMode(QToolButton.InstantPopup)
        btn.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        return btn

    def __make_menu(self, btn, entries):
        mnu = QMenu(btn)
        for entry in entries:
            act = QAction(entry['text'], mnu)
            act.setData(entry['func'])
            # noinspection PyUnresolvedReferences
            act.triggered.connect(self.menu_triggered)
            mnu.addAction(act)
        return mnu

    def __add_labels(self):
        lbl = QLabel(self)
        lbl.setGeometry(QRect(20, 70, 190, 290))
        lbl.setPixmap(self.images['blue_streets'])

        lbl = QLabel(self)
        lbl.setGeometry(QRect(220, 70, 270, 310))
        lbl.setPixmap(self.images['adlai'])

        lbl = QLabel(self)
        lbl.setGeometry(QRect(520, 90, 110, 20))
        lbl.setText("A product of")

        lbl = QLabel(self)
        lbl.setGeometry(QRect(520, 110, 180, 50))
        lbl.setPixmap(self.images['ragtime_cowboy'])

        lbl = QLabel(self)
        lbl.setGeometry(QRect(520, 170, 80, 120))
        lbl.setPixmap(self.images['cowboy_large'])

        lbl = QLabel(self)
        lbl.setGeometry(QRect(520, 310, 140, 20))
        lbl.setText('All rights reserved')

    def menu_triggered(self):
        self.sender().data()()

    def __turf_triggered(self):
        print('turf')

    def __vtr_import_county(self):
        print('voter import county')

    def __vtr_import_spreadsheet(self):
        print('voter import spreadsheet')

    def __vtr_worksheet(self):
        print('voter worksheet')

    def __vtr_export(self):
        print('voter export')

    def __con_import_county(self):
        print('contact import county')

    def __con_import_spreadsheet(self):
        print('contact import spreadsheet')

    def __con_entry_form(self):
        print('contact entry form')

    def __con_battle_stations(self):
        print('battle stations')

    def __con_export(self):
        print('con export')

    def __grp_triggered(self):
        print('groups')

    def __email_dups(self):
        print('email dups')

    def __phone_dups(self):
        print('phone dups')

    def __name_addr_dups(self):
        print('name + address dups')

    def __name_dups(self):
        print('name only dups')

    def __voter_sync(self):
        print('voter sync')