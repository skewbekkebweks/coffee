import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from PyQt5 import uic


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.connect = sqlite3.connect('coffee.sqlite')
        self.loadTable()

    def loadTable(self):
        cursor = self.connect.cursor()
        command = f'select c.id, c.name, d.title, k.title, c.description, c.price, c.size ' \
                  f'from coffee c ' \
                  f'left join degree d on c.degree = d.id ' \
                  f'left join kind k on c.kind = k.id'
        res = cursor.execute(command).fetchall()
        title = ['ID', 'Название сорта', 'Степень обжарки', 'Молотый/в зернах', 'Описание вкуса',
                 'Цена', 'Объем порции']
        self.tableWidget.setColumnCount(len(title))
        self.tableWidget.setHorizontalHeaderLabels(title)
        self.tableWidget.setRowCount(len(res))
        for i, row in enumerate(res):
            for j, elem in enumerate(row):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(elem)))
        self.tableWidget.resizeColumnsToContents()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyWindow()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
