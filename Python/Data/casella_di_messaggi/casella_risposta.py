from PyQt5 import QtCore, QtGui, QtWidgets
from Data.MessageBox import messageBox
from Model.Messaggio import Messaggio
from datetime import datetime


class casella_risposta(object):

    username = ""
    messanger = Messaggio()
    msg = messageBox()

    def scrivi_messaggio(self):

        risposta = Messaggio()
        risposta.mittente = self.messanger.destinatario
        risposta.destinatario = self.messanger.mittente
        risposta.contenuto = self.plainTextEdit.toPlainText()
        risposta.data = datetime.today().strftime('%Y-%m-%d-%H:%M')

        self.messanger.addToList(risposta)
        self.messanger.scriviLista("./Data/casella_di_messaggi/messaggi.txt")
        self.msg.show_popup_ok("il tuo messaggio è stato inviato correttamente")
        self.finestra.close()

    def setupUi(self, MainWindow, obj):
        self.messanger = obj
        self.finestra = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(682, 450)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(70, 80, 55, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(140, 90, 421, 211))
        self.plainTextEdit.setPlainText("")
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(410, 320, 141, 28))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 682, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.messanger.recuperaSalvataggio("./Data/casella_di_messaggi/messaggi.txt")
        self.pushButton.clicked.connect(self.scrivi_messaggio)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "Oggetto:"))
        self.pushButton.setText(_translate("MainWindow", "Invia Messaggio"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = casella_risposta()
    ui.setupUi(MainWindow, "")
    MainWindow.show()
    sys.exit(app.exec_())
