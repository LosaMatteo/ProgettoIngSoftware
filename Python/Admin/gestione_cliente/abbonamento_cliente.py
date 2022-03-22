from PyQt5 import QtCore, QtGui, QtWidgets
from Model.Abbonamento import Abbonamento
from Data.MessageBox import messageBox


class abbonamento_cliente(object):
    clsAbbonamento = Abbonamento()
    messaggio = messageBox()

    def create_object_abbonamento(self):
        try:
            tipo_abbonamento = ""
            data_iscrizione = self.dtdDataIscrizione.date()
            data_certificato_medico = self.dtdCertificatoMedico.date()
            if self.rdbSalaPesiMensile.isChecked():
                tipo_abbonamento += "Abbonamento mensile sala pesi €30 - "
            elif self.rdbSalaPesiAnnuale.isChecked():
                tipo_abbonamento += "Abbonamento annuale sala pesi €300 - "
            if self.rdbFunctionalMensile.isChecked():
                tipo_abbonamento += "Abbonamento mensile functional €40 - "
            elif self.rdbFunctionalAnnuale.isChecked():
                tipo_abbonamento += "Abbonamento annuale functional €360 - "
            if self.rdbZumbaMensile.isChecked():
                tipo_abbonamento += "Abbonamento mensile zumba €35 - "
            elif self.rdbZumbaAnnuale.isChecked():
                tipo_abbonamento += "Abbonamento annuale zumba €340 - "
            if self.rdbAllInclusiveAnnuale.isChecked():
                tipo_abbonamento += "Abbonamento mensile all inclusive €42 - "
            elif self.rdbAllInclusiveMensile.isChecked():
                tipo_abbonamento += "Abbonamento annuale all inclusive €420 - "
            if tipo_abbonamento != "":
                objAll = Abbonamento(data_iscrizione, data_certificato_medico, tipo_abbonamento)
                self.clsAbbonamento.addToList(objAll)
                self.messaggio.show_popup_ok("Salvataggio effettuato!")
            else:
                self.messaggio.show_popup_exception("Non è stato selezionato nessun abbonamento!")
        except(Exception):
            self.messaggio.show_popup_exception("Errore durante il salvataggio!")

    def setupUi(self, MainWindow):
        self.AbbonamentoWindow = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(812, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lblDataIscrizione = QtWidgets.QLabel(self.centralwidget)
        self.lblDataIscrizione.setGeometry(QtCore.QRect(130, 20, 231, 31))
        font = QtGui.QFont()
        font.setFamily("MS UI Gothic")
        font.setPointSize(13)
        self.lblDataIscrizione.setFont(font)
        self.lblDataIscrizione.setObjectName("lblDataIscrizione")
        self.lblDataCertificato = QtWidgets.QLabel(self.centralwidget)
        self.lblDataCertificato.setGeometry(QtCore.QRect(130, 60, 241, 31))
        font = QtGui.QFont()
        font.setFamily("MS UI Gothic")
        font.setPointSize(13)
        self.lblDataCertificato.setFont(font)
        self.lblDataCertificato.setObjectName("lblDataCertificato")
        self.lblPicPesi = QtWidgets.QLabel(self.centralwidget)
        self.lblPicPesi.setGeometry(QtCore.QRect(60, 140, 161, 121))
        self.lblPicPesi.setText("")
        self.lblPicPesi.setPixmap(QtGui.QPixmap("./Resources/images/abbonamento palestra.jpg"))
        self.lblPicPesi.setScaledContents(True)
        self.lblPicPesi.setObjectName("lblPicPesi")
        self.lblPicAllInclusive = QtWidgets.QLabel(self.centralwidget)
        self.lblPicAllInclusive.setGeometry(QtCore.QRect(450, 140, 151, 121))
        self.lblPicAllInclusive.setText("")
        self.lblPicAllInclusive.setPixmap(QtGui.QPixmap("./Resources/images/abbonamento palestra2.jpg"))
        self.lblPicAllInclusive.setScaledContents(True)
        self.lblPicAllInclusive.setObjectName("lblPicAllInclusive")
        self.lblPicFunctional = QtWidgets.QLabel(self.centralwidget)
        self.lblPicFunctional.setGeometry(QtCore.QRect(60, 310, 161, 131))
        self.lblPicFunctional.setText("")
        self.lblPicFunctional.setPixmap(QtGui.QPixmap("./Resources/images/abbonamento functional.jpg"))
        self.lblPicFunctional.setScaledContents(True)
        self.lblPicFunctional.setObjectName("lblPicFunctional")
        self.lblPicZumba = QtWidgets.QLabel(self.centralwidget)
        self.lblPicZumba.setGeometry(QtCore.QRect(450, 310, 151, 131))
        self.lblPicZumba.setText("")
        self.lblPicZumba.setPixmap(QtGui.QPixmap("./Resources/images/zumba.jpg"))
        self.lblPicZumba.setScaledContents(True)
        self.lblPicZumba.setObjectName("lblPicZumba")
        self.lblSalaPesi = QtWidgets.QLabel(self.centralwidget)
        self.lblSalaPesi.setGeometry(QtCore.QRect(240, 140, 171, 71))
        self.lblSalaPesi.setObjectName("lblSalaPesi")
        self.lblAllInclusive = QtWidgets.QLabel(self.centralwidget)
        self.lblAllInclusive.setGeometry(QtCore.QRect(610, 140, 171, 71))
        self.lblAllInclusive.setObjectName("lblAllInclusive")
        self.lblFunctional = QtWidgets.QLabel(self.centralwidget)
        self.lblFunctional.setGeometry(QtCore.QRect(240, 320, 171, 71))
        self.lblFunctional.setObjectName("lblFunctional")
        self.lblZumba = QtWidgets.QLabel(self.centralwidget)
        self.lblZumba.setGeometry(QtCore.QRect(590, 310, 171, 71))
        self.lblZumba.setObjectName("lblZumba")
        self.btnAggiungi = QtWidgets.QPushButton(self.centralwidget)
        self.btnAggiungi.setGeometry(QtCore.QRect(300, 490, 121, 31))
        self.btnAggiungi.setIconSize(QtCore.QSize(150, 150))
        self.btnAggiungi.setObjectName("btnAggiungi")
        self.btnAnnulla = QtWidgets.QPushButton(self.centralwidget)
        self.btnAnnulla.setGeometry(QtCore.QRect(480, 490, 121, 31))
        self.btnAnnulla.setIconSize(QtCore.QSize(150, 150))
        self.btnAnnulla.setObjectName("btnAnnulla")
        self.dtdDataIscrizione = QtWidgets.QDateEdit(self.centralwidget)
        self.dtdDataIscrizione.setGeometry(QtCore.QRect(380, 30, 110, 22))
        self.dtdDataIscrizione.setMaximumDateTime(
            QtCore.QDateTime(QtCore.QDate(2050, 12, 31), QtCore.QTime(23, 59, 59)))
        self.dtdDataIscrizione.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(2020, 9, 14), QtCore.QTime(0, 0, 0)))
        self.dtdDataIscrizione.setCalendarPopup(True)
        self.dtdDataIscrizione.setObjectName("dtdDataIscrizione")
        self.dtdCertificatoMedico = QtWidgets.QDateEdit(self.centralwidget)
        self.dtdCertificatoMedico.setGeometry(QtCore.QRect(380, 70, 110, 22))
        self.dtdCertificatoMedico.setMaximumDateTime(
            QtCore.QDateTime(QtCore.QDate(2050, 12, 31), QtCore.QTime(23, 59, 59)))
        self.dtdCertificatoMedico.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(2020, 9, 14), QtCore.QTime(0, 0, 0)))
        self.dtdCertificatoMedico.setCalendarPopup(True)
        self.dtdCertificatoMedico.setObjectName("dtdCertificatoMedico")
        self.rdbSalaPesiMensile = QtWidgets.QRadioButton(self.centralwidget)
        self.rdbSalaPesiMensile.setGeometry(QtCore.QRect(260, 220, 141, 20))
        self.rdbSalaPesiMensile.setObjectName("rdbSalaPesiMensile")
        self.rdbSalaPesiAnnuale = QtWidgets.QRadioButton(self.centralwidget)
        self.rdbSalaPesiAnnuale.setGeometry(QtCore.QRect(260, 250, 141, 20))
        self.rdbSalaPesiAnnuale.setObjectName("rdbSalaPesiAnnuale")
        self.rdbAllInclusiveMensile = QtWidgets.QRadioButton(self.centralwidget)
        self.rdbAllInclusiveMensile.setGeometry(QtCore.QRect(620, 220, 141, 20))
        self.rdbAllInclusiveMensile.setObjectName("rdbAllInclusiveMensile")
        self.rdbAllInclusiveAnnuale = QtWidgets.QRadioButton(self.centralwidget)
        self.rdbAllInclusiveAnnuale.setGeometry(QtCore.QRect(620, 250, 131, 20))
        self.rdbAllInclusiveAnnuale.setObjectName("rdbAllInclusiveAnnuale")
        self.rdbFunctionalMensile = QtWidgets.QRadioButton(self.centralwidget)
        self.rdbFunctionalMensile.setGeometry(QtCore.QRect(260, 410, 141, 20))
        self.rdbFunctionalMensile.setObjectName("rdbFunctionalMensile")
        self.rdbFunctionalAnnuale = QtWidgets.QRadioButton(self.centralwidget)
        self.rdbFunctionalAnnuale.setGeometry(QtCore.QRect(260, 440, 141, 20))
        self.rdbFunctionalAnnuale.setObjectName("rdbFunctionalAnnuale")
        self.rdbZumbaMensile = QtWidgets.QRadioButton(self.centralwidget)
        self.rdbZumbaMensile.setGeometry(QtCore.QRect(620, 400, 141, 20))
        self.rdbZumbaMensile.setObjectName("rdbZumbaMensile")
        self.rdbZumbaAnnuale = QtWidgets.QRadioButton(self.centralwidget)
        self.rdbZumbaAnnuale.setGeometry(QtCore.QRect(620, 430, 141, 20))
        self.rdbZumbaAnnuale.setObjectName("rdbZumbaAnnuale")
        self.btnAggiungi.raise_()
        self.lblDataIscrizione.raise_()
        self.lblDataCertificato.raise_()
        self.lblPicPesi.raise_()
        self.lblPicAllInclusive.raise_()
        self.lblPicFunctional.raise_()
        self.lblPicZumba.raise_()
        self.lblSalaPesi.raise_()
        self.lblAllInclusive.raise_()
        self.lblFunctional.raise_()
        self.lblZumba.raise_()
        self.dtdDataIscrizione.raise_()
        self.dtdCertificatoMedico.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 812, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.btnAggiungi.clicked.connect(self.create_object_abbonamento)
        self.btnAnnulla.clicked.connect(self.AbbonamentoWindow.close)
        self.dtdCertificatoMedico.setDate(self.dtdCertificatoMedico.date().currentDate())
        self.dtdDataIscrizione.setDate(self.dtdDataIscrizione.date().currentDate())


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnAggiungi.setText(_translate("MainWindow", "Aggiungi"))
        self.btnAnnulla.setText(_translate("MainWindow", "Indietro"))
        self.lblDataIscrizione.setText(_translate("MainWindow", "Data di iscrizione"))
        self.lblDataCertificato.setText(_translate("MainWindow", "Data certificato medico"))
        self.lblSalaPesi.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Abbonamento sala pesi</p><p align=\"center\">30 euro/mese</p><p align=\"center\">300/anno</p><p><br/></p></body></html>"))
        self.lblAllInclusive.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Abbonamento tutto incluso</p><p align=\"center\">42 euro/mese</p><p align=\"center\">420 euro/anno</p><p><br/></p></body></html>"))
        self.lblFunctional.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Abbonamento functional</p><p align=\"center\">40 euro/mese</p><p align=\"center\">360 euro/anno</p><p><br/></p></body></html>"))
        self.lblZumba.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Abbonamento zumba </p><p align=\"center\">35 euro/mese</p><p align=\"center\">340/anno</p><p><br/></p></body></html>"))
        self.rdbSalaPesiMensile.setText(_translate("MainWindow", "Pacchetto mensile"))
        self.rdbSalaPesiAnnuale.setText(_translate("MainWindow", "Pacchetto annuale"))
        self.rdbFunctionalAnnuale.setText(_translate("MainWindow", "Pacchetto annuale"))
        self.rdbFunctionalMensile.setText(_translate("MainWindow", "Pacchetto mensile"))
        self.rdbZumbaAnnuale.setText(_translate("MainWindow", "Pacchetto annuale"))
        self.rdbZumbaMensile.setText(_translate("MainWindow", "Pacchetto mensile"))
        self.rdbAllInclusiveAnnuale.setText(_translate("MainWindow", "Pacchetto annuale"))
        self.rdbAllInclusiveMensile.setText(_translate("MainWindow", "Pacchetto mensile"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = abbonamento_cliente()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
