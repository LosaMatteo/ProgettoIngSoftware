from PyQt5 import QtCore, QtGui, QtWidgets
from Python.Data.MessageBox import messageBox
from Python.Model.Personale import Personale


class agg_personale(object):

    messaggio = messageBox()

    def salva(self):
        if self.txtNome.text() != "" and self.txtCognome.text() != "" and self.txtCodiceFiscale.text() != "" \
                and self.txtOre.text() != "" and self.txtTitolo.text() != "":
            staff = Personale(self.txtNome.text(), self.txtCognome.text(), self.txtCodiceFiscale.text(), self.txtOre.text(),
                              self.txtTitolo.text())
            staff.addToList(staff)
            staff.scriviLista("./Admin/gestione_personale/CredenzialiStaff.txt")
            self.saveWindow.close()
        else: self.messaggio.show_popup_listWidget("Uno o più campi risultano vuoti.")

    def cancella(self):
        self.txtNome.setText("")
        self.txtCognome.setText("")
        self.txtCodiceFiscale.setText("")
        self.txtOre.setText("")
        self.txtTitolo.setText("")

    def setupUi(self, MainWindow):
        self.saveWindow = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(670, 514)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lblTitle = QtWidgets.QLabel(self.centralwidget)
        self.lblTitle.setGeometry(QtCore.QRect(30, 30, 601, 91))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(21)
        self.lblTitle.setFont(font)
        self.lblTitle.setObjectName("lblTitle")
        self.txtNome = QtWidgets.QLineEdit(self.centralwidget)
        self.txtNome.setGeometry(QtCore.QRect(280, 150, 151, 31))
        self.txtNome.setObjectName("txtNome")
        self.lblNome = QtWidgets.QLabel(self.centralwidget)
        self.lblNome.setGeometry(QtCore.QRect(180, 150, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lblNome.setFont(font)
        self.lblNome.setObjectName("lblNome")
        self.lblCognome = QtWidgets.QLabel(self.centralwidget)
        self.lblCognome.setGeometry(QtCore.QRect(160, 190, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lblCognome.setFont(font)
        self.lblCognome.setObjectName("lblCognome")
        self.lblCodiceFiscale = QtWidgets.QLabel(self.centralwidget)
        self.lblCodiceFiscale.setGeometry(QtCore.QRect(130, 230, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lblCodiceFiscale.setFont(font)
        self.lblCodiceFiscale.setObjectName("lblCodiceFiscale")
        self.txtCodiceFiscale = QtWidgets.QLineEdit(self.centralwidget)
        self.txtCodiceFiscale.setGeometry(QtCore.QRect(280, 230, 151, 31))
        self.txtCodiceFiscale.setObjectName("txtCodiceFiscale")
        self.lblOre = QtWidgets.QLabel(self.centralwidget)
        self.lblOre.setGeometry(QtCore.QRect(120, 270, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lblOre.setFont(font)
        self.lblOre.setObjectName("lblOre")
        self.txtOre = QtWidgets.QLineEdit(self.centralwidget)
        self.txtOre.setGeometry(QtCore.QRect(280, 270, 151, 31))
        self.txtOre.setObjectName("txtOre")
        self.lblTitolo = QtWidgets.QLabel(self.centralwidget)
        self.lblTitolo.setGeometry(QtCore.QRect(120, 310, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lblTitolo.setFont(font)
        self.lblTitolo.setObjectName("lblTitolo")
        self.btnAnnulla = QtWidgets.QPushButton(self.centralwidget)
        self.btnAnnulla.setGeometry(QtCore.QRect(260, 370, 131, 31))
        self.btnAnnulla.setObjectName("btnAnnulla")
        self.btnSalva = QtWidgets.QPushButton(self.centralwidget)
        self.btnSalva.setGeometry(QtCore.QRect(400, 370, 121, 31))
        self.btnSalva.setObjectName("btnSalva")
        self.txtCognome = QtWidgets.QLineEdit(self.centralwidget)
        self.txtCognome.setGeometry(QtCore.QRect(280, 190, 151, 31))
        self.txtCognome.setObjectName("txtCognome")
        self.txtTitolo = QtWidgets.QLineEdit(self.centralwidget)
        self.txtTitolo.setGeometry(QtCore.QRect(280, 310, 151, 31))
        self.txtTitolo.setObjectName("txtTitolo")
        self.btnIndietro = QtWidgets.QPushButton(self.centralwidget)
        self.btnIndietro.setGeometry(QtCore.QRect(530, 370, 131, 31))
        self.btnIndietro.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 670, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.btnSalva.clicked.connect(self.salva)
        self.btnAnnulla.clicked.connect(self.cancella)
        self.btnIndietro.clicked.connect(self.saveWindow.close)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Assunzione"))
        self.lblTitle.setText(_translate("MainWindow",
                                         "<html><head/><body><p align=\"center\">Aggiungi un membro dello staff</p></body></html>"))
        self.lblNome.setText(_translate("MainWindow", "Nome"))
        self.lblCognome.setText(_translate("MainWindow", "Cognome"))
        self.lblCodiceFiscale.setText(_translate("MainWindow", "Codice fiscale"))
        self.lblOre.setText(_translate("MainWindow", "Ore settimanali"))
        self.lblTitolo.setText(_translate("MainWindow", "<html><head/><body><p>Mansione</p></body></html>"))
        self.btnAnnulla.setText(_translate("MainWindow", "Cancella"))
        self.btnSalva.setText(_translate("MainWindow", "Salva"))
        self.btnIndietro.setText(_translate("MainWindow", "Indietro"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = agg_personale()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
