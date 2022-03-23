from PyQt5 import QtCore, QtGui, QtWidgets
from Python.Data.MessageBox import messageBox
from Python.Model.Messaggio import Messaggio
from datetime import datetime


class casella_risposta(object):

    username = ""
    objMessaggio = Messaggio()
    msg = messageBox()

    def scrivi_messaggio(self):
        risposta = Messaggio()
        risposta.mittente = self.objMessaggio.destinatario
        risposta.destinatario = self.objMessaggio.mittente
        risposta.contenuto = self.ptxTesto.toPlainText()
        risposta.data = datetime.today().strftime('%Y-%m-%d-%H:%M')
        self.objMessaggio.addToList(risposta)
        self.objMessaggio.scriviLista("./Data/casella_di_messaggi/messaggi.txt")
        self.msg.show_popup_ok("il tuo messaggio è stato inviato correttamente")
        self.finestra.close()

    def setupUi(self, MainWindow, obj):
        self.objMessaggio = obj
        self.finestra = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(682, 450)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lblTesto_1 = QtWidgets.QLabel(self.centralwidget)
        self.lblTesto_1.setGeometry(QtCore.QRect(70, 80, 55, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblTesto_1.setFont(font)
        self.lblTesto_1.setObjectName("lblTesto_1")
        self.ptxTesto = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.ptxTesto.setGeometry(QtCore.QRect(140, 90, 421, 211))
        self.ptxTesto.setPlainText("")
        self.ptxTesto.setObjectName("ptxTesto")
        self.btnInviaMessaggio = QtWidgets.QPushButton(self.centralwidget)
        self.btnInviaMessaggio.setGeometry(QtCore.QRect(410, 320, 141, 28))
        self.btnInviaMessaggio.setObjectName("pushButton")
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
        self.objMessaggio.recuperaSalvataggio("./Data/casella_di_messaggi/messaggi.txt")
        self.btnInviaMessaggio.clicked.connect(self.scrivi_messaggio)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Rispondi"))
        self.lblTesto_1.setText(_translate("MainWindow", "Oggetto:"))
        self.btnInviaMessaggio.setText(_translate("MainWindow", "Invia Messaggio"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = casella_risposta()
    ui.setupUi(MainWindow, "")
    MainWindow.show()
    sys.exit(app.exec_())
