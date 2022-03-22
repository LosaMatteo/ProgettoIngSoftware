from PyQt5 import QtCore, QtWidgets
from Data.casella_di_messaggi.casella_risposta import casella_risposta
from Model.Messaggio import Messaggio


class lettura_messaggio(object):
    username = ""
    messagger = Messaggio()

    def open_window_casella_di_messaggi(self):

        self.casella_risposta = QtWidgets.QMainWindow()
        self.ui = casella_risposta()
        self.ui.setupUi(self.casella_risposta, self.messagger)
        self.casella_risposta.show()

    def setupUi(self, MainWindow, obj, username):
        self.messagger = obj
        self.username = username
        self.finestra = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(690, 487)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(90, 110, 481, 241))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.plainTextEdit.setReadOnly(True)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(310, 370, 121, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(450, 370, 121, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 690, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        if self.messagger.mittente == self.username:
            self.pushButton.hide()
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton_2.clicked.connect(self.finestra.close)
        self.pushButton.clicked.connect(self.open_window_casella_di_messaggi)
        self.plainTextEdit.setPlainText(self.messagger.contenuto)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Rispondi"))
        self.pushButton_2.setText(_translate("MainWindow", "Indietro"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = lettura_messaggio()
    ui.setupUi(MainWindow, "")
    MainWindow.show()
    sys.exit(app.exec_())
