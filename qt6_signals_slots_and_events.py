"""
<<<<<<< HEAD
=======
4
>>>>>>> origin/master
Хабр https://habr.com/ru/company/skillfactory/blog/599599/
Оигинал https://www.pythonguis.com/tutorials/pyqt6-signals-slots-events/
"""

from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

import sys
from random import choice

window_titles = [
    'My App',
    'My App',
    'Still My App',
    'Still My App',
    'What on earth',
    'What on earth',
    'This is surprising',
    'This is surprising',
    'Something went wrong'
]


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.n_times_clicked = 0

        self.setWindowTitle("My App")
<<<<<<< HEAD
        # self.showMaximized()
=======
>>>>>>> origin/master

        self.button = QPushButton("Press Me!")
        self.button.clicked.connect(self.the_button_was_clicked)

        self.windowTitleChanged.connect(self.the_window_title_changed)

        # Устанавливаем центральный виджет Window.
        self.setCentralWidget(self.button)

    def the_button_was_clicked(self):
        print("Clicked.")
        new_window_title = choice(window_titles)
        print("Setting title:  %s" % new_window_title)
        self.setWindowTitle(new_window_title)

    def the_window_title_changed(self, window_title):
        print("Window title changed: %s" % window_title)

        if window_title == 'Something went wrong':
            self.button.setDisabled(True)


app = QApplication(sys.argv)

window = MainWindow()
<<<<<<< HEAD
# window.show()
# window.showMaximized()
window.showFullScreen()
=======
window.show()
>>>>>>> origin/master

app.exec()
