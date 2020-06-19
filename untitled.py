# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 560)
        MainWindow.setStyleSheet("QPushButton:hover {    background-color: gold;}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.sort_but = QtWidgets.QPushButton(self.centralwidget)
        self.sort_but.setGeometry(QtCore.QRect(275, 60, 100, 50))
        self.sort_but.setObjectName("sort_but")
        self.show_progres = QtWidgets.QListWidget(self.centralwidget)
        self.show_progres.setGeometry(QtCore.QRect(25, 120, 350, 399))
        self.show_progres.setStyleSheet("QPushButton {\n"
"    border-radius: 50px 0 0 50px;\n"
"}")
        self.show_progres.setObjectName("show_progres")
        self.background = QtWidgets.QLabel(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(0, 0, 400, 600))
        self.background.setText("")
        self.background.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.background.setObjectName("background")
        self.add = QtWidgets.QLineEdit(self.centralwidget)
        self.add.setGeometry(QtCore.QRect(25, 20, 350, 30))
        self.add.setObjectName("add")
        self.add_but = QtWidgets.QPushButton(self.centralwidget)
        self.add_but.setGeometry(QtCore.QRect(25, 60, 100, 50))
        self.add_but.setObjectName("add_but")
        self.del_but = QtWidgets.QPushButton(self.centralwidget)
        self.del_but.setGeometry(QtCore.QRect(150, 60, 100, 50))
        self.del_but.setObjectName("del_but")
        self.background.raise_()
        self.sort_but.raise_()
        self.show_progres.raise_()
        self.add.raise_()
        self.add_but.raise_()
        self.del_but.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Dictionary"))
        self.sort_but.setText(_translate("MainWindow", "Сортировка"))
        self.add_but.setText(_translate("MainWindow", "Добавить"))
        self.del_but.setText(_translate("MainWindow", "Удалить"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
