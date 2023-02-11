"""
Create file browser in python and Qt (PyQt5 or PySide2 QTreeView and QFileSystemModel)
[Youtube](https://www.youtube.com/watch?v=4PkPezdpO90)
"""

from PyQt6 import QtWidgets
from PyQt6 import QtGui
from PyQt6 import QtCore
from ui import main


class MyFileBrowser(main.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super(MyFileBrowser, self).__init__()
        self.setupUi(self)
        self.populate()

    def populate(self):
        # path = r"C:\Windows"
        path = r"s:\MyMedia"
        model = QtGui.QFileSystemModel()
        model.setRootPath(QtCore.QDir.rootPath())
        self.treeView.setModel(model)
        self.treeView.setRootIndex(model.index(path))
        self.treeView.setSortingEnabled(True)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    fb = MyFileBrowser()
    fb.show()
    app.exec()

