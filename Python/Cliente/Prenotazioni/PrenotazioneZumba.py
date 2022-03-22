from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDate
from Python.Cliente.Prenotazioni.gestionePrenotazioni import GestionePrenotazioniCorsi
from Python.Data.MessageBox import messageBox


class prenotazione_zumba(object):
    objGestionePrenotazioneCorsi = GestionePrenotazioniCorsi()
    username = ""
    msg = messageBox()
    percorso = ""

    def assegnaAttributi(self):
        if (self.popupcalendar.selectedDate().toString()[:3] == "gio" or
                self.popupcalendar.selectedDate().toString()[:3] == "ven"):
            self.percorso = self.objGestionePrenotazioneCorsi.assegnaAttributi(self.popupcalendar.selectedDate().toString("dd.MM.yyyy"),
                                                                               self.cmbOrario.currentText().split(":"),
                                                     "./Cliente/Prenotazioni/file_prenotazioni/zumba/")
            return True
        else:
            self.msg.show_popup_ok("Selezionare un giorno corretto.")
            return False

    def prenota(self):
        if self.assegnaAttributi() == True:
            self.objGestionePrenotazioneCorsi.prenota(20, self.percorso, self.username, )
            self.finestra.close()

    def cmbAttive(self):
        self.assegnaAttributi()
        self.progressBar.setValue(self.objGestionePrenotazioneCorsi.cmbAttive(self.percorso))

    def elimina(self):
        self.objGestionePrenotazioneCorsi.elimina("./Cliente/Prenotazioni/file_prenotazioni/zumba/")

    def setupUi(self, Form, username):
        self.finestra = Form
        self.username = username
        Form.setObjectName("Form")
        Form.resize(754, 433)
        Form.setMouseTracking(False)
        self.progressBar = QtWidgets.QProgressBar(Form)
        self.progressBar.setGeometry(QtCore.QRect(550, 220, 118, 23))
        self.progressBar.setMaximum(20)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.lblInfo = QtWidgets.QLabel(Form)
        self.lblInfo.setGeometry(QtCore.QRect(19, 15, 291, 61))
        self.lblInfo.setObjectName("lblInfo")
        self.lblTesto_1 = QtWidgets.QLabel(Form)
        self.lblTesto_1.setGeometry(QtCore.QRect(10, 110, 101, 16))
        self.lblTesto_1.setObjectName("lblTesto_1")
        self.lblTesto_2 = QtWidgets.QLabel(Form)
        self.lblTesto_2.setGeometry(QtCore.QRect(550, 80, 111, 16))
        self.lblTesto_2.setObjectName("lblTesto_2")
        self.lblTesto_3 = QtWidgets.QLabel(Form)
        self.lblTesto_3.setGeometry(QtCore.QRect(550, 180, 111, 20))
        self.lblTesto_3.setObjectName("lblTesto_3")
        self.lblImmagineZumba = QtWidgets.QLabel(Form)
        self.lblImmagineZumba.setGeometry(QtCore.QRect(390, 10, 81, 71))
        self.lblImmagineZumba.setText("")
        self.lblImmagineZumba.setPixmap(QtGui.QPixmap(".\\IconaZumba.png"))
        self.lblImmagineZumba.setScaledContents(True)
        self.lblImmagineZumba.setObjectName("lblImmagineZumba")
        self.btnPrenota = QtWidgets.QPushButton(Form)
        self.btnPrenota.setGeometry(QtCore.QRect(550, 350, 113, 32))
        self.btnPrenota.setObjectName("btnPrenota")
        self.popupcalendar = QtWidgets.QCalendarWidget(Form)
        self.popupcalendar.setGeometry(QtCore.QRect(10, 130, 421, 251))
        self.popupcalendar.setFirstDayOfWeek(QtCore.Qt.Monday)
        self.popupcalendar.setGridVisible(True)
        self.popupcalendar.setObjectName("popupcalendar")
        self.cmbOrario = QtWidgets.QComboBox(Form)
        self.cmbOrario.setGeometry(QtCore.QRect(550, 110, 111, 22))
        self.cmbOrario.setObjectName("cmbOrario")
        self.cmbOrario.addItem("")
        self.cmbOrario.addItem("")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.btnPrenota.clicked.connect(self.prenota)
        self.popupcalendar.setMinimumDate(QDate.currentDate())
        self.cmbOrario.activated[str].connect(self.cmbAttive)
        self.popupcalendar.clicked.connect(self.cmbAttive)
        self.popupcalendar.setMaximumDate(QDate.currentDate().addMonths(1))
        self.elimina()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Zumba"))
        self.lblInfo.setText(_translate("Form",
                                      "<html><head/><body><p>Le lezioni si svolgono il giovedì e il venerdì</p><p>dalle ore 18:00 e dalle ore 19:30.</p></body></html>"))
        self.lblTesto_1.setText(_translate("Form", "Seleziona data:"))
        self.lblTesto_2.setText(_translate("Form", "Seleziona orario:"))
        self.lblTesto_3.setText(_translate("Form", "Posti disponibili:"))
        self.btnPrenota.setText(_translate("Form", "Prenota ora"))
        self.cmbOrario.setItemText(0, _translate("Form", "18:00-19:30"))
        self.cmbOrario.setItemText(1, _translate("Form", "19:30-21:00"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = prenotazione_zumba()
    ui.setupUi(Form, username="")
    Form.show()
    sys.exit(app.exec_())
