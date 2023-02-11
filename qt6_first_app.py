"""
Первый пример использования pyqt6
Рекламная статья на Хабре PyQt6 — полное руководство для новичков. Дословный перевод, неполный
Хабр https://habr.com/ru/company/skillfactory/blog/599599/
Оригинал https://www.pythonguis.com/tutorials/pyqt6-creating-your-first-window
"""

import sys
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton


# Подкласс QMainWindow для настройки главного окна приложения
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Заголовок окна на кириллице отображается нормально")
        self.setFixedSize(QSize(400, 300))
        self.setMinimumSize(QSize(200, 150))
        self.setMaximumSize(QSize(800, 600))
        button = QPushButton("Press Me!")

        # Устанавливаем центральный виджет Window. Совершенно бестолковый комментарий. Зачем он здесь?
        self.setCentralWidget(button)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
