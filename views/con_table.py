from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QHeaderView


class ContactsTable(QTableWidget):

    flds = [
        'id', 'name', 'nickname',
        'addr', 'city', 'zipcode',
        'email', 'phone1', 'phone2',
        'gender', 'birth_year', 'reg_date'
    ]

    def __init__(self, contacts, *__args):
        super().__init__(*__args)
        nrows = len(contacts)
        ncols = len(self.flds)
        self.setRowCount(nrows)
        self.setColumnCount(ncols)
        self.setHorizontalHeaderLabels([
            'ID', 'Name', 'Nickname',
            'Address', 'City', 'Zip',
            'Email', 'Phone 1', 'Phone 2',
            'Gender', 'BYr', 'Reg Date'
        ])
        for colnum in range(0, ncols):
            self.horizontalHeader().setSectionResizeMode(colnum, QHeaderView.ResizeToContents)
        for rownum in range(0, nrows):
            for colnum in range(0, ncols):
                item = QTableWidgetItem(contacts[rownum][self.flds[colnum]])
                self.setItem(rownum, colnum, item)

        self.setColumnHidden(0, True)
        self.setSortingEnabled(True)
