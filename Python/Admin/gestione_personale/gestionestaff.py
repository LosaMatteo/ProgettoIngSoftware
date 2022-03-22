from Python.Admin.gestione_personale.gestioneorari import GestioneOrari
from PyQt5 import QtCore, QtGui, QtWidgets
from Python.Data.MessageBox import messageBox
from Python.Model.Personale import Personale


class gestione_staff(object):
    def __init__(self, name):
        self.name = name

    objPersonale = Personale()
    messaggio = messageBox()

    def visualizza(self):
        objPersonale = self.objPersonale.getAttributi(self.name)
        self.txtNome.setText(objPersonale.name)
        self.txtCognome.setText(objPersonale.surname)
        self.txtCodiceFiscale.setText(objPersonale.cf)
        self.txtMansione.setText(objPersonale.mansione)

    def salvaModifiche(self):
        if self.txtNome.text() != "" and self.txtCognome.text() != "" and self.txtCodiceFiscale.text() != "" \
                and self.txtMansione.text() != "":
            try:
                oggPer = self.objPersonale.getAttributi(self.name)
                if oggPer.name == self.txtNome.text() and oggPer.surname == self.txtCognome.text() and \
                        oggPer.cf == self.txtCodiceFiscale.text() and oggPer.mansione == self.txtMansione.text():
                    self.messaggio.show_popup_listWidget("Nessun campo modificato.")
                else:
                    self.objPersonale.rimuovi(self.name)
                    oggPer.name = self.txtNome.text()
                    oggPer.surname = self.txtCognome.text()
                    oggPer.cf = self.txtCodiceFiscale.text()
                    oggPer.mansione = self.txtMansione.text()
                    self.objPersonale.addToList(oggPer)
                    self.messaggio.show_popup_ok("Modifiche salvate con successo!")
            except(Exception):
                self.messaggio.show_popup_listWidget("non hai selezionato nulla nella lista!")
        else:
            self.messaggio.show_popup_listWidget("Uno o più campi risultano vuoti.")


    def pulisciCaselle(self):
        self.txtNome.clear()
        self.txtCognome.clear()
        self.txtCodiceFiscale.clear()
        self.txtMansione.clear()

    def rimuovi(self):
        try:
            if self.messaggio.show_popup_question("Sei sicuro di voler eliminare il membro dello staff?"):
                self.objPersonale.rimuovi(self.name)
                self.pulisciCaselle()
            else:
                return
        except(Exception):
            self.messaggio.show_popup_exception("Errore!")

    def reset(self):
        name = self.name
        self.objPersonale.reset(name)

    def apriGestioneOrario(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = GestioneOrari()
        self.ui.setupUi(self.window, self.name)
        self.window.show()

    def setupUi(self, MainWindow):
        self.finestra = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(509, 274)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lblTitolo = QtWidgets.QLabel(self.centralwidget)
        self.lblTitolo.setGeometry(QtCore.QRect(80, 40, 121, 41))
        self.lblTitolo.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.lblTitolo.setObjectName("lblTitolo")
        self.txtNome = QtWidgets.QLineEdit(self.centralwidget)
        self.txtNome.setGeometry(QtCore.QRect(340, 40, 113, 21))
        self.txtNome.setObjectName("txtNome")
        self.txtCognome = QtWidgets.QLineEdit(self.centralwidget)
        self.txtCognome.setGeometry(QtCore.QRect(340, 70, 113, 21))
        self.txtCognome.setObjectName("txtCognome")
        self.txtMansione = QtWidgets.QLineEdit(self.centralwidget)
        self.txtMansione.setGeometry(QtCore.QRect(340, 130, 113, 21))
        self.txtMansione.setObjectName("txtMansione")
        self.txtCodiceFiscale = QtWidgets.QLineEdit(self.centralwidget)
        self.txtCodiceFiscale.setGeometry(QtCore.QRect(340, 100, 113, 21))
        self.txtCodiceFiscale.setObjectName("txtCodiceFiscale")
        self.btnReset = QtWidgets.QPushButton(self.centralwidget)
        self.btnReset.setGeometry(QtCore.QRect(100, 190, 101, 24))
        self.btnReset.setObjectName("btnReset")
        self.lblNome = QtWidgets.QLabel(self.centralwidget)
        self.lblNome.setGeometry(QtCore.QRect(250, 40, 41, 21))
        self.lblNome.setObjectName("lblNome")
        self.lblCognome = QtWidgets.QLabel(self.centralwidget)
        self.lblCognome.setGeometry(QtCore.QRect(250, 70, 51, 21))
        self.lblCognome.setObjectName("lblCognome")
        self.lblMansione = QtWidgets.QLabel(self.centralwidget)
        self.lblMansione.setGeometry(QtCore.QRect(250, 130, 51, 21))
        self.lblMansione.setObjectName("lblMansione")
        self.lblCodiceFiscale = QtWidgets.QLabel(self.centralwidget)
        self.lblCodiceFiscale.setGeometry(QtCore.QRect(250, 100, 81, 21))
        self.lblCodiceFiscale.setObjectName("lblCodiceFiscale")
        self.btnSalva = QtWidgets.QPushButton(self.centralwidget)
        self.btnSalva.setGeometry(QtCore.QRect(20, 190, 61, 24))
        self.btnSalva.setObjectName("btnSalva")
        self.btnIndietro = QtWidgets.QPushButton(self.centralwidget)
        self.btnIndietro.setGeometry(QtCore.QRect(390, 190, 71, 24))
        self.btnIndietro.setObjectName("btnIndietro")
        self.lblNomeStaff = QtWidgets.QLabel(self.centralwidget)
        self.lblNomeStaff.setGeometry(QtCore.QRect(60, 80, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.lblNomeStaff.setFont(font)
        self.lblNomeStaff.setAlignment(QtCore.Qt.AlignCenter)
        self.lblNomeStaff.setObjectName("lblNomeStaff")
        self.btnOrario = QtWidgets.QPushButton(self.centralwidget)
        self.btnOrario.setGeometry(QtCore.QRect(300, 190, 75, 24))
        self.btnOrario.setObjectName("btnOrario")
        self.btnRimuovi = QtWidgets.QPushButton(self.centralwidget)
        self.btnRimuovi.setGeometry(QtCore.QRect(210, 190, 75, 24))
        self.btnRimuovi.setObjectName("btnRimuovi")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.txtNome.setReadOnly(True)
        self.txtCognome.setReadOnly(True)
        self.txtCodiceFiscale.setReadOnly(True)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.btnSalva.clicked.connect(self.salvaModifiche)
        self.btnRimuovi.clicked.connect(self.rimuovi)
        self.visualizza()
        self.btnOrario.clicked.connect(self.apriGestioneOrario)
        self.btnIndietro.clicked.connect(self.finestra.close)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Informazioni - " + self.name))
        self.lblTitolo.setText(_translate("MainWindow", "Informazioni di "))
        self.btnReset.setText(_translate("MainWindow", "Reset password"))
        self.lblNome.setText(_translate("MainWindow", "Nome"))
        self.lblCognome.setText(_translate("MainWindow", "Cognome"))
        self.lblMansione.setText(_translate("MainWindow", "Mansione"))
        self.lblCodiceFiscale.setText(_translate("MainWindow", "Codice fiscale"))
        self.btnSalva.setText(_translate("MainWindow", "Salva"))
        self.btnIndietro.setText(_translate("MainWindow", "Indietro"))
        self.lblNomeStaff.setText(_translate("MainWindow", self.name))
        self.btnOrario.setText(_translate("MainWindow", "Orario"))
        self.btnRimuovi.setText(_translate("MainWindow", "Rimuovi"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = gestione_staff("")
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
