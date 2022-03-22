from PyQt5 import QtCore, QtGui, QtWidgets
from Python.Data.MessageBox import messageBox
from Python.Model.Cliente import Cliente
from Python.Admin.gestione_cliente.abbonamento_cliente import abbonamento_cliente
from Python.Model.Abbonamento import Abbonamento


class aggiungi_cliente(object):
    objAbb = Abbonamento()
    messaggio = messageBox()

    def collega_window_abbonamento(self):
        self.window_abbonamento = QtWidgets.QMainWindow()
        self.ui = abbonamento_cliente()
        self.ui.setupUi(self.window_abbonamento)
        self.window_abbonamento.show()
        self.btnSalva.show()

    def save(self):
        if self.txtNome.text() != "" and self.txtCognome.text() != "" and self.txtLuogoNascita.text() != "" \
                and self.txtCodiceFiscale.text() != "":
            oggetto_allenamento = self.objAbb.getObj()
            objCliente = Cliente(self.txtNome.text().replace(" ", ""), self.txtCognome.text().replace(" ", ""), self.cmbSesso.currentText(),
                                 self.dtdDataDiNascita.date(),
                                 self.txtLuogoNascita.text(), self.txtCodiceFiscale.text(), "1234", oggetto_allenamento)

            objCliente.addToList(objCliente)
            objCliente.scriviLista("./Admin/gestione_cliente/CredenzialiClienti.txt")
            self.saveWindow.close()
        else:
            self.messaggio.show_popup_listWidget("Uno o più campi risultano vuoti.")

    def setupUi(self, MainWindow):

        self.saveWindow = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(689, 495)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lblTitle = QtWidgets.QLabel(self.centralwidget)
        self.lblTitle.setGeometry(QtCore.QRect(100, 20, 501, 91))
        font = QtGui.QFont()
        font.setFamily("Papyrus")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.lblTitle.setFont(font)
        self.lblTitle.setObjectName("lblTitle")
        self.lblNome = QtWidgets.QLabel(self.centralwidget)
        self.lblNome.setGeometry(QtCore.QRect(180, 130, 61, 20))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.lblNome.setFont(font)
        self.lblNome.setObjectName("lblNome")
        self.txtNome = QtWidgets.QLineEdit(self.centralwidget)
        self.txtNome.setGeometry(QtCore.QRect(270, 130, 181, 21))
        self.txtNome.setObjectName("txtNome")
        self.lblCognome = QtWidgets.QLabel(self.centralwidget)
        self.lblCognome.setGeometry(QtCore.QRect(170, 170, 91, 20))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(13)
        self.lblCognome.setFont(font)
        self.lblCognome.setObjectName("lblCognome")
        self.txtCognome = QtWidgets.QLineEdit(self.centralwidget)
        self.txtCognome.setGeometry(QtCore.QRect(270, 170, 181, 21))
        self.txtCognome.setObjectName("txtCognome")
        self.lblSesso = QtWidgets.QLabel(self.centralwidget)
        self.lblSesso.setGeometry(QtCore.QRect(178, 210, 71, 20))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(13)
        self.lblSesso.setFont(font)
        self.lblSesso.setObjectName("lblSesso")
        self.lblLuogoNascita = QtWidgets.QLabel(self.centralwidget)
        self.lblLuogoNascita.setGeometry(QtCore.QRect(70, 290, 191, 20))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(13)
        self.lblLuogoNascita.setFont(font)
        self.lblLuogoNascita.setObjectName("lblLuogoNascita")
        self.txtLuogoNascita = QtWidgets.QLineEdit(self.centralwidget)
        self.txtLuogoNascita.setGeometry(QtCore.QRect(270, 290, 181, 21))
        self.txtLuogoNascita.setObjectName("txtLuogoNascita")
        self.btnSalva = QtWidgets.QPushButton(self.centralwidget)
        self.btnSalva.setGeometry(QtCore.QRect(460, 380, 75, 24))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setBold(True)
        font.setWeight(75)
        self.btnSalva.setFont(font)
        self.btnSalva.setObjectName("btnSalva")
        self.cmbSesso = QtWidgets.QComboBox(self.centralwidget)
        self.cmbSesso.setGeometry(QtCore.QRect(270, 210, 91, 22))
        self.cmbSesso.setObjectName("cmbSesso")
        self.cmbSesso.addItem("")
        self.cmbSesso.addItem("")
        self.lblDataNascita = QtWidgets.QLabel(self.centralwidget)
        self.lblDataNascita.setGeometry(QtCore.QRect(80, 250, 181, 20))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(13)
        self.lblDataNascita.setFont(font)
        self.lblDataNascita.setObjectName("lblDataNascita")
        self.lblCodiceFiscale = QtWidgets.QLabel(self.centralwidget)
        self.lblCodiceFiscale.setGeometry(QtCore.QRect(90, 330, 171, 20))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(13)
        self.lblCodiceFiscale.setFont(font)
        self.lblCodiceFiscale.setObjectName("lblCodiceFiscale")
        self.txtCodiceFiscale = QtWidgets.QLineEdit(self.centralwidget)
        self.txtCodiceFiscale.setGeometry(QtCore.QRect(270, 330, 181, 21))
        self.txtCodiceFiscale.setObjectName("txtCodiceFiscale")
        self.btnAvanti = QtWidgets.QPushButton(self.centralwidget)
        self.btnAvanti.setGeometry(QtCore.QRect(460, 410, 101, 31))
        self.btnAvanti.setIconSize(QtCore.QSize(200, 200))
        self.btnAvanti.setObjectName("btnAvanti")
        self.dtdDataDiNascita = QtWidgets.QDateEdit(self.centralwidget)
        self.dtdDataDiNascita.setGeometry(QtCore.QRect(270, 250, 110, 22))
        self.dtdDataDiNascita.setCalendarPopup(True)
        self.dtdDataDiNascita.setObjectName("dtdDataDiNascita")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 689, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.btnSalva.hide()
        self.btnAvanti.clicked.connect(self.collega_window_abbonamento)
        self.btnSalva.clicked.connect(self.save)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Nuova iscrizione"))
        self.btnAvanti.setText((_translate("MainWindow", "Abbonamenti")))
        self.lblTitle.setText(_translate("MainWindow", "Aggiungi i dati del cliente"))
        self.lblNome.setText(_translate("MainWindow", "Nome"))
        self.lblCognome.setText(_translate("MainWindow", "Cognome"))
        self.lblSesso.setText(_translate("MainWindow", "Sesso"))
        self.lblLuogoNascita.setText(_translate("MainWindow", "Luogo di nascita"))
        self.btnSalva.setText(_translate("MainWindow", "Salva"))
        self.cmbSesso.setItemText(0, _translate("MainWindow", "maschio"))
        self.cmbSesso.setItemText(1, _translate("MainWindow", "femmina"))
        self.lblDataNascita.setText(_translate("MainWindow", "Data di nascita"))
        self.lblCodiceFiscale.setText(_translate("MainWindow", "Codice Fiscale"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = aggiungi_cliente()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
