import sys
import sqlite3

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QMessageBox
from PyQt5 import uic


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.connect = sqlite3.connect('coffee.sqlite')
        self.add_btn.clicked.connect(self.add_coffee)
        self.edit_btn.clicked.connect(self.edit_coffee)
        self.delete_btn.clicked.connect(self.delete_coffee)
        self.change_table()

    def change_table(self):
        cursor = self.connect.cursor()
        command = f'select c.id, c.name, d.title, k.title, c.description, c.price, c.size ' \
                  f'from coffee c ' \
                  f'left join degree d on c.degree = d.id ' \
                  f'left join kind k on c.kind = k.id'
        res = cursor.execute(command).fetchall()
        title = ['ID', 'Название сорта', 'Степень обжарки', 'Молотый/В зернах', 'Описание вкуса',
                 'Цена', 'Объем порции']
        self.tableWidget.setColumnCount(len(title))
        self.tableWidget.setHorizontalHeaderLabels(title)
        self.tableWidget.setRowCount(len(res))
        for i, row in enumerate(res):
            for j, elem in enumerate(row):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(elem)))
        self.tableWidget.resizeColumnsToContents()

    def add_coffee(self):
        class AddCoffee(QMainWindow):
            def __init__(self, connect, main):
                super().__init__()
                uic.loadUi('addEditCoffeeForm.ui', self)
                self.connect = connect
                self.main = main
                self.pushButton.clicked.connect(self.check)
                cursor = self.connect.cursor()
                command = f'select title ' \
                          f'from degree ' \
                          f'order by id'
                res = cursor.execute(command).fetchall()
                for elem in res:
                    self.degree_box.addItem(elem[0])
                command = f'select title ' \
                          f'from kind ' \
                          f'order by id'
                res = cursor.execute(command).fetchall()
                for elem in res:
                    self.kind_box.addItem(elem[0])

            def check(self):
                try:
                    name = self.name_edit.text()
                    degree = self.degree_box.currentIndex() + 1
                    kind = self.kind_box.currentIndex() + 1
                    description = self.description_edit.text()
                    price = int(self.price_edit.text())
                    size = int(self.size_edit.text())
                except ValueError:
                    QMessageBox.critical(self, 'Ошибка', 'Некорректные данные', QMessageBox.Ok)
                    return
                cursor = self.connect.cursor()
                command = f'insert into coffee(name, degree, kind, description, price, size) ' \
                          f'values(\'{name}\', {degree}, {kind}, \'{description}\', {price}, {size})'
                cursor.execute(command)
                self.connect.commit()
                self.main.change_table()
                self.close()

        self.add_coffee_ = AddCoffee(self.connect, self)
        self.add_coffee_.setWindowModality(Qt.ApplicationModal)
        self.add_coffee_.show()

    def edit_coffee(self):
        class EditCoffee(QMainWindow):
            def __init__(self, connect, main, id_):
                super().__init__()
                uic.loadUi('addEditCoffeeForm.ui', self)
                self.connect = connect
                self.main = main
                self.id_ = id_
                self.pushButton.clicked.connect(self.check)
                cursor = self.connect.cursor()
                command = f'select title ' \
                          f'from degree ' \
                          f'order by id'
                res = cursor.execute(command).fetchall()
                for elem in res:
                    self.degree_box.addItem(elem[0])
                command = f'select title ' \
                          f'from kind ' \
                          f'order by id'
                res = cursor.execute(command).fetchall()
                for elem in res:
                    self.kind_box.addItem(elem[0])
                command = f'select name, description, price, size ' \
                          f'from coffee ' \
                          f'where id = {self.id_}'
                res = cursor.execute(command).fetchone()
                self.name_edit.setText(res[0])
                self.description_edit.setText(res[1])
                self.price_edit.setText(str(res[2]))
                self.size_edit.setText(str(res[3]))

            def check(self):
                try:
                    name = self.name_edit.text()
                    degree = self.degree_box.currentIndex() + 1
                    kind = self.kind_box.currentIndex() + 1
                    description = self.description_edit.text()
                    price = int(self.price_edit.text())
                    size = int(self.size_edit.text())
                except ValueError:
                    QMessageBox.critical(self, 'Ошибка', 'Некорректные данные', QMessageBox.Ok)
                    return
                cursor = self.connect.cursor()
                command = f'update coffee ' \
                          f'set name = \'{name}\', ' \
                          f'degree =  {degree}, ' \
                          f'kind = {kind}, ' \
                          f'description = \'{description}\', ' \
                          f'price = {price}, ' \
                          f'size = {size} ' \
                          f'where id = {self.id_}'
                cursor.execute(command)
                self.connect.commit()
                self.main.change_table()
                self.close()

        if self.tableWidget.currentRow() != -1:
            id_ = self.tableWidget.item(self.tableWidget.currentRow(), 0).text()
        else:
            QMessageBox.critical(self, 'Ошибка', 'Выберите нужную строку', QMessageBox.Ok)
            return

        self.edit_coffee_ = EditCoffee(self.connect, self, id_)
        self.edit_coffee_.setWindowModality(Qt.ApplicationModal)
        self.edit_coffee_.show()

    def delete_coffee(self):
        if self.tableWidget.currentRow() != -1:
            id_ = self.tableWidget.item(self.tableWidget.currentRow(), 0).text()
        else:
            QMessageBox.critical(self, 'Ошибка', 'Выберите нужную строку', QMessageBox.Ok)
            return
        cursor = self.connect.cursor()
        command = f'delete from coffee ' \
                  f'where id = {id_}'
        cursor.execute(command)
        self.connect.commit()
        self.change_table()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyWindow()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
