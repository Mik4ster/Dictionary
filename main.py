from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
from untitled import *

#Create application
class MyMain(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


        self.progres_file_add = 'dict'

        self.progres_file_show = 'dict'
        file = open('media/'+self.progres_file_show+'.txt')

        self.list = []

        self.ui.add_but.clicked.connect(self.add_in_progres)
        self.ui.del_but.clicked.connect(self.del_in_progres)
        self.ui.sort_but.clicked.connect(self.sortirovOchka)

    def add_in_progres(self):
        item = self.ui.add.text()
        self.list.append(item)
        self.ui.show_progres.clear()
        for i in self.list:
            self.ui.show_progres.addItem(i)

    def del_in_progres(self):
        text = self.ui.add.text()
        for i in range(len(self.list)):
            if self.list[i]==text:
                self.list.pop(i)
                break
        self.ui.show_progres.clear()
        for i in self.list:
            self.ui.show_progres.addItem(i)
    def sortirovOchka(self):
        self.list = sorted(self.list)
        self.ui.show_progres.clear()
        for i in self.list:
            self.ui.show_progres.addItem(i)
#Run main loop
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyMain()
    myapp.show()
    sys.exit(app.exec_())
