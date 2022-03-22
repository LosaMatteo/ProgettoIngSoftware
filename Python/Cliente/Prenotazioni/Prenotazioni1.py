from PyQt5 import QtCore, QtGui, QtWidgets
from Python.Cliente.Prenotazioni.PrenotazioneZumba import prenotazione_zumba
from Python.Cliente.Prenotazioni.PrenotazioniAllenamentoFunzionale import prenotazioni_allenamento_functional
from Python.Cliente.Prenotazioni.SalaPesiPrenot import prenotazioni_sala_pesi


class prenotazioni(object):

    username = ""
    def apriPrenotazioniSalaPesi(self):
        self.sala_pesi = QtWidgets.QMainWindow()
        self.ui = prenotazioni_sala_pesi()
        self.ui.setupUi(self.sala_pesi, self.username)
        self.sala_pesi.show()

    def apriPrenotazioniFunctional(self):
        self.functional = QtWidgets.QMainWindow()
        self.ui = prenotazioni_allenamento_functional()
        self.ui.setupUi(self.functional, self.username)
        self.functional.show()

    def apriPrenotazioniZumba(self):
        self.zumba = QtWidgets.QMainWindow()
        self.ui = prenotazione_zumba()
        self.ui.setupUi(self.zumba, self.username)
        self.zumba.show()


    def setupUi(self, Form,username):
        self.username = username
        Form.setObjectName("Form")
        Form.resize(689, 576)
        self.lblTitolo = QtWidgets.QLabel(Form)
        self.lblTitolo.setGeometry(QtCore.QRect(200, 70, 261, 81))
        self.lblTitolo.setScaledContents(True)
        self.lblTitolo.setObjectName("lblTitolo")
        self.lblImmagineIntestazione = QtWidgets.QLabel(Form)
        self.lblImmagineIntestazione.setGeometry(QtCore.QRect(470, 80, 71, 71))
        self.lblImmagineIntestazione.setText("")
        self.lblImmagineIntestazione.setPixmap(QtGui.QPixmap("./Resources/images/pngPrenotazioni/Prenot1.png"))
        self.lblImmagineIntestazione.setScaledContents(True)
        self.lblImmagineIntestazione.setObjectName("lblImmagineIntestazione")
        self.btnApriSalaPesi = QtWidgets.QPushButton(Form)
        self.btnApriSalaPesi.setGeometry(QtCore.QRect(50, 420, 113, 32))
        self.btnApriSalaPesi.setObjectName("btnApriSalaPesi")
        self.btnApriFunzionale = QtWidgets.QPushButton(Form)
        self.btnApriFunzionale.setGeometry(QtCore.QRect(300, 420, 113, 32))
        self.btnApriFunzionale.setObjectName("btnApriFunzionale")
        self.btnApriZumba = QtWidgets.QPushButton(Form)
        self.btnApriZumba.setGeometry(QtCore.QRect(530, 420, 113, 32))
        self.btnApriZumba.setObjectName("btnApriZumba")
        self.lblImmagineSalaPesi = QtWidgets.QLabel(Form)
        self.lblImmagineSalaPesi.setGeometry(QtCore.QRect(20, 240, 181, 151))
        self.lblImmagineSalaPesi.setText("")
        self.lblImmagineSalaPesi.setPixmap(QtGui.QPixmap("./Resources/images/pngPrenotazioni/SalaPesi.png"))
        self.lblImmagineSalaPesi.setScaledContents(True)
        self.lblImmagineSalaPesi.setObjectName("lblImmagineSalaPesi")
        self.lblImmagineZumba = QtWidgets.QLabel(Form)
        self.lblImmagineZumba.setGeometry(QtCore.QRect(500, 240, 181, 151))
        self.lblImmagineZumba.setText("")
        self.lblImmagineZumba.setTextFormat(QtCore.Qt.RichText)
        self.lblImmagineZumba.setPixmap(QtGui.QPixmap("./Resources/images/pngPrenotazioni/zumba.png"))
        self.lblImmagineZumba.setScaledContents(True)
        self.lblImmagineZumba.setObjectName("lblImmagineZumba")
        self.lblImmagineFunctional = QtWidgets.QLabel(Form)
        self.lblImmagineFunctional.setGeometry(QtCore.QRect(270, 240, 171, 151))
        self.lblImmagineFunctional.setText("")
        self.lblImmagineFunctional.setPixmap(QtGui.QPixmap("./Resources/images/pngPrenotazioni/funzionale.png"))
        self.lblImmagineFunctional.setScaledContents(True)
        self.lblImmagineFunctional.setObjectName("lblImmagineFunctional")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.btnApriSalaPesi.clicked.connect(self.apriPrenotazioniSalaPesi)
        self.btnApriFunzionale.clicked.connect(self.apriPrenotazioniFunctional)
        self.btnApriZumba.clicked.connect(self.apriPrenotazioniZumba)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Prenotazioni"))
        self.lblTitolo.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:36pt;\">PRENOTAZIONI</span></p></body></html>"))
        self.btnApriSalaPesi.setText(_translate("Form", "Sala Pesi"))
        self.btnApriFunzionale.setText(_translate("Form", "Funzionale"))
        self.btnApriZumba.setText(_translate("Form", "Zumba"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = prenotazioni()
    ui.setupUi(Form,)
    Form.show()
    sys.exit(app.exec_())
