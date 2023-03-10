"""
Python GUI Development with PyQt6 & Qt Designer.
02 - PyQt6 Widgets Introduction
031 QTableWidget in PyQt6
QTableWidget https://www.riverbankcomputing.com/static/Docs/PyQt6/api/qtwidgets/qtablewidget.html#
Пример корявый. Модифицировал без использования sys
"""

from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem
from PyQt6.QtGui import QIcon


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(200, 200, 700, 400)
        self.setWindowTitle('QTableWidget')
        self.setWindowIcon(QIcon('images/python.png'))
        vbox = QVBoxLayout()
        table = QTableWidget()
        table.setColumnCount(2)
        table.setRowCount(3)
        table.setItem(0, 0, QTableWidgetItem('Id'))
        table.setItem(0, 1, QTableWidgetItem('User'))
        vbox.addWidget(table)
        self.setLayout(vbox)


app = QApplication([])
window = Window()
window.show()
app.exec()
