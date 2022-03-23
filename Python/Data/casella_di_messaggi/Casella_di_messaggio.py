from PyQt5 import QtCore, QtGui, QtWidgets
from Python.Data.MessageBox import messageBox
from Python.Model.Cliente import Cliente
from Python.Model.Personale import Personale
from Python.Model.Messaggio import Messaggio
from datetime import datetime


class Casella_di_messaggio(object):
    msg = messageBox()
    objMessaggio = Messaggio()
    username = ""
    mittente = ""

    def popola_comboBox(self):
        objCliente = Cliente()
        objPersonale = Personale()
        self.lblMittente.setText(self.username)
        if self.username != "admin":
            self.cmbDestinatari.addItem("A-admin")
        vett = objCliente.get_lista()
        for elem in vett:
            if elem != self.username:
             self.cmbDestinatari.addItem("C-" + elem)
        vett = objPersonale.get_lista()
        for elem in vett:
            if elem != self.username:
             self.cmbDestinatari.addItem("P-" + elem)

    def scrittura_file_messaggi(self):
        objCliente = Cliente()
        objPersonale = Personale()
        if self.chkClienti.isChecked() == False and self.chkStaff.isChecked() == False:
            destinatario = self.cmbDestinatari.currentText().split("-")
            self.spedisciMessaggio(destinatario[1])
        if self.chkClienti.isChecked() == True:
            vett = objCliente.get_lista()
            for elem in vett:
                self.spedisciMessaggio(elem)
        if self.chkStaff.isChecked() == True:
            vett = objPersonale.get_lista()
            for elem in vett:
                self.spedisciMessaggio(elem)
        self.msg.show_popup_ok("il tuo contenuto è stato inviato correttamente")
        self.finestra.close()

    def spedisciMessaggio(self, destinatario):
        messaggi = Messaggio(self.username, destinatario, self.ptxTesto.toPlainText(),
                             datetime.today().strftime('%Y-%m-%d-%H:%M'))
        messaggi.addToList(messaggi)
        #self.messaggi.scriviLista("./Data/casella_di_messaggi/messaggi.txt")

    def notificaTurno(self, mittente, destinatario, messaggio):
        notifica = Messaggio(mittente, destinatario, messaggio,
                             datetime.today().strftime('%Y-%m-%d-%H:%M'))
        notifica.addToList(notifica)
        self.msg.show_popup_ok("il tuo contenuto è stato inviato correttamente")

    def selezioneDestinatario(self):
        if self.chkClienti.isChecked() or self.chkStaff.isChecked():
            self.cmbDestinatari.setDisabled(True)
        else:
            self.cmbDestinatari.setDisabled(False)


    def setupUi(self, MainWindow, username):
        self.finestra = MainWindow
        self.username = username
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(535, 450)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lblTesto_2 = QtWidgets.QLabel(self.centralwidget)
        self.lblTesto_2.setGeometry(QtCore.QRect(40, 60, 31, 20))
        font = QtGui.QFont()
        font.setBold(True)
        self.lblTesto_2.setFont(font)
        self.lblTesto_2.setObjectName("lblTesto_2")
        self.btnInviaMessaggio = QtWidgets.QPushButton(self.centralwidget)
        self.btnInviaMessaggio.setGeometry(QtCore.QRect(360, 330, 141, 28))
        self.btnInviaMessaggio.setObjectName("btnInviaMessaggio")
        self.lblTesto_1 = QtWidgets.QLabel(self.centralwidget)
        self.lblTesto_1.setGeometry(QtCore.QRect(30, 30, 41, 20))
        font = QtGui.QFont()
        font.setBold(True)
        self.lblTesto_1.setFont(font)
        self.lblTesto_1.setObjectName("lblTesto_1")
        self.lblTesto_3 = QtWidgets.QLabel(self.centralwidget)
        self.lblTesto_3.setGeometry(QtCore.QRect(20, 90, 55, 31))
        font = QtGui.QFont()
        font.setBold(True)
        self.lblTesto_3.setFont(font)
        self.lblTesto_3.setObjectName("lblTesto_3")
        self.cmbDestinatari = QtWidgets.QComboBox(self.centralwidget)
        self.cmbDestinatari.setGeometry(QtCore.QRect(90, 60, 151, 22))
        self.cmbDestinatari.setObjectName("cmbDestinatari")
        self.ptxTesto = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.ptxTesto.setGeometry(QtCore.QRect(90, 100, 421, 211))
        self.ptxTesto.setPlainText("")
        self.ptxTesto.setObjectName("ptxTesto")
        self.lblMittente = QtWidgets.QLabel(self.centralwidget)
        self.lblMittente.setGeometry(QtCore.QRect(90, 30, 151, 21))
        font = QtGui.QFont()
        font.setBold(True)
        self.lblMittente.setFont(font)
        self.lblMittente.setText("")
        self.lblMittente.setObjectName("lblMittente")
        self.chkClienti = QtWidgets.QCheckBox(self.centralwidget)
        self.chkClienti.setGeometry(QtCore.QRect(280, 60, 91, 20))
        self.chkClienti.setObjectName("chkClienti")
        self.chkStaff = QtWidgets.QCheckBox(self.centralwidget)
        self.chkStaff.setGeometry(QtCore.QRect(400, 60, 91, 20))
        self.chkStaff.setObjectName("chkStaff")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 535, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        if self.username != "admin":
            self.chkStaff.hide()
            self.chkClienti.hide()
        self.popola_comboBox()
        self.objMessaggio.recuperaSalvataggio("./Data/casella_di_messaggi/messaggi.txt")
        self.btnInviaMessaggio.clicked.connect(self.scrittura_file_messaggi)
        self.chkStaff.clicked.connect(self.selezioneDestinatario)
        self.chkClienti.clicked.connect(self.selezioneDestinatario)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Scrivi messaggio"))
        self.lblTesto_2.setText(_translate("MainWindow", "A:"))
        self.btnInviaMessaggio.setText(_translate("MainWindow", "Invia Messaggio"))
        self.lblTesto_1.setText(_translate("MainWindow", "DA:"))
        self.lblTesto_3.setText(_translate("MainWindow", "Oggetto:"))
        self.chkClienti.setText(_translate("MainWindow", "Tutti i clienti"))
        self.chkStaff.setText(_translate("MainWindow", "Tutto lo staff"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Casella_di_messaggio()
    ui.setupUi(MainWindow, username="")
    MainWindow.show()
    sys.exit(app.exec_())
