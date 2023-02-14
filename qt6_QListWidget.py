"""
- QListWidget, исполльзование для создания списка addItems и insertItems
- QListWidget: clicked_item - обработка выбора элемента списка по клику мышки
- QListWidget: changed_item - индикация текущего элемента в StatusBar
- installEventFilter - локальный обработчик событий. Здесь - клавиатуры. [Помогло](https://www.youtube.com/watch?v=2Q8X3aRKPmY)
- keyPressEvent - закрыть окно, выйти из программы по Esc

Для справки ссылка
Старье, но подробно https://www.youtube.com/watch?v=mrBd2gFhVhk
TODO set current item in list to 0 on start
"""

from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QListWidget, QStatusBar, QLabel, QWidget, QLineEdit
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt, QEvent


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QListWidget...')
        self.setWindowIcon(QIcon('images/python.png'))

        self.lw = QListWidget()
        self.lw.addItems(['Java', 'C#', 'Python'])
        self.lw.insertItems(0, ['Prolog', 'Fortran', 'PL/1'])
        self.lw.clicked.connect(self.clicked_item)
        self.lw.currentItemChanged.connect(self.changed_item)
        # self.lw.setCurrentItem(1)
        # локальный, привязанный только к одному виджету, обработчик событий.
        self.lw.installEventFilter(self)
        self.le = QLineEdit()   # Заглушка для того, чтобы удостовериться,
                                # что в других полях не запускается обработчик клавиатуры
        self.text_info = QLabel("")     # динамически меняемое поле
        self.sb = QStatusBar(self)
        self.setStatusBar(self.sb)

        vbox = QVBoxLayout()
        vbox.addWidget(self.lw)
        vbox.addWidget(self.text_info)
        vbox.addWidget(self.le)
        widget = QWidget()
        widget.setLayout(vbox)
        self.setCentralWidget(widget)

    def clicked_item(self):
        item = self.lw.currentItem()
        self.text_info.setText(f"You select: {str(item.text())}")

    def changed_item(self):
        item = self.lw.currentItem()
        # self.sb.showMessage(item.text(), 2000)
        self.sb.showMessage(item.text())

    def eventFilter(self, source, event):
        if event.type() == QEvent.Type.KeyPress \
                and event.key() in (Qt.Key.Key_Space, Qt.Key.Key_Return, Qt.Key.Key_Enter) \
                and source == self.lw:
            # Последняя проверка не обязательна, т.к. eventFilter инсталлирован только для одного виджета
            print(f'Активирован пробелом или вводом элемент списка {self.lw.currentItem().text()}')
        return super().eventFilter(source, event)

    def keyPressEvent(self, e):
        # we reimplement the keyPressEvent event handler
        if e.key() == Qt.Key.Key_Escape.value:
            self.close()


app = QApplication([])
window = Window()
window.show()
app.exec()
