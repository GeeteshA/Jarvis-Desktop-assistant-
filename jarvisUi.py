# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'jarvisUi.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_JarvisUi(object):
    def setupUi(self, JarvisUi):
        JarvisUi.setObjectName("JarvisUi")
        JarvisUi.resize(831, 555)
        self.centralwidget = QtWidgets.QWidget(JarvisUi)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 831, 621))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Ui/7LP8.gif"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(610, 480, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(85, 170, 127)")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(680, 480, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(14)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 0, 0)")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, -30, 331, 181))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("Ui/Jarvis_Loading_Screen.gif"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(655, 20, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(14)
        self.textBrowser.setFont(font)
        self.textBrowser.setStyleSheet("background: transparent;\n"
                                       "border-radius:none;\n"
                                       "color:white;\n"
                                       "font-size:20px;")
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(510, 20, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(14)
        self.textBrowser_2.setFont(font)
        self.textBrowser_2.setStyleSheet("background: transparent;\n"
                                         "border-radius:none;"
                                         "color:white;\n"
                                         "font-size:20px;")
        self.textBrowser_2.setObjectName("textBrowser_2")
        JarvisUi.setCentralWidget(self.centralwidget)

        self.retranslateUi(JarvisUi)
        QtCore.QMetaObject.connectSlotsByName(JarvisUi)

    def retranslateUi(self, JarvisUi):
        _translate = QtCore.QCoreApplication.translate
        JarvisUi.setWindowTitle(_translate("JarvisUi", "MainWindow"))
        self.pushButton.setText(_translate("JarvisUi", "Start"))
        self.pushButton_2.setText(_translate("JarvisUi", "Exit"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    JarvisUi = QtWidgets.QMainWindow()
    ui = Ui_JarvisUi()
    ui.setupUi(JarvisUi)
    JarvisUi.show()
    sys.exit(app.exec_())
