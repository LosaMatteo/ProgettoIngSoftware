from Data.casella_di_messaggi.Casella_di_messaggio import Casella_di_messaggio
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QDate, QRect, Qt, QMetaObject, QCoreApplication
from PyQt5.QtWidgets import QWidget, QCalendarWidget, QComboBox, QLabel, QDoubleSpinBox, QStatusBar, QPushButton, \
    QPlainTextEdit, QMessageBox
from Model.Orario import Orario
from Data.MessageBox import messageBox

class GestioneOrari(object):
    msg = messageBox()
    username = ""
    gestorario = Orario()
    notifica = Casella_di_messaggio()
    validitagiorno = False

    def fasciaOraria(self):
        tipo = self.cmbTipo.currentText()
        self.cmbInizio.clear()
        self.cmbFine.clear()
        if tipo == "Sala Pesi":
            self.cmbInizio.addItem("09:30")
            self.cmbInizio.addItem("11:00")
            self.cmbInizio.addItem("12:30")
            self.cmbInizio.addItem("14:00")
            self.cmbInizio.addItem("15:30")
            self.cmbInizio.addItem("17:00")
            self.cmbInizio.addItem("18:30")
            self.cmbInizio.addItem("20:00")
            self.cmbInizio.addItem("21:30")
            self.cmbFine.addItem("11:00")
            self.cmbFine.addItem("12:30")
            self.cmbFine.addItem("14:00")
            self.cmbFine.addItem("15:30")
            self.cmbFine.addItem("17:00")
            self.cmbFine.addItem("18:30")
            self.cmbFine.addItem("20:00")
            self.cmbFine.addItem("21:30")
            self.cmbFine.addItem("23:00")
        elif tipo == "Zumba":
            self.cmbInizio.addItem("18:00")
            self.cmbInizio.addItem("19:30")
            self.cmbFine.addItem("19:30")
            self.cmbFine.addItem("21:00")
        else:
            self.cmbInizio.addItem("15:30")
            self.cmbInizio.addItem("17:00")
            self.cmbFine.addItem("17:00")
            self.cmbFine.addItem("18:30")

    def controllaGiorno(self):
        self.ptxPreview.clear()
        tipo = self.cmbTipo.currentText()
        if tipo == "Sala Pesi":
            if self.calendarWidget.selectedDate().toString()[:3] == "dom":
                self.messaggioErrore("Selezionare un giorno corretto.")
                self.validitagiorno = False
        if tipo == "Zumba":
            if (self.calendarWidget.selectedDate().toString()[:3] != "gio" and
                    self.calendarWidget.selectedDate().toString()[:3] != "ven"):
                self.messaggioErrore("Selezionare un giorno corretto.")
                self.validitagiorno = False
        elif tipo == "Functional":
            if (self.calendarWidget.selectedDate().toString()[:3] != "mar" and
                    self.calendarWidget.selectedDate().toString()[:3] != "mer" and
                    self.calendarWidget.selectedDate().toString()[:3] != "ven"):
                self.messaggioErrore("Selezionare un giorno corretto.")
                self.validitagiorno = False
        self.controllaTurno()
        self.validitagiorno = True

    def controllaOrario(self, hinizio, hfine):
        if hinizio < hfine:
            return True
        return False

    def salva(self):
        if self.controllaOrario(self.cmbInizio.currentText(), self.cmbFine.currentText()):
            if self.calendarWidget.selectedDate().toString() != "" and self.validitagiorno:
                ora = Orario(self.calendarWidget.selectedDate().toString(), self.cmbInizio.currentText(),
                             self.cmbFine.currentText(),
                             self.username, self.spbPaga.text(), self.cmbTipo.currentText())
                self.gestorario.addToList(ora)
                self.notifica.notificaTurno("admin", self.username.replace(" ", ""), "In data " +
                                            self.calendarWidget.selectedDate().toString() + " ti occuperai di " +
                                            self.cmbTipo.currentText() + " dalle ore " + self.cmbInizio.currentText() + " alle ore " +
                                            self.cmbFine.currentText())
                self.controllaTurno()
            else:
                self.messaggioErrore("Selezionare una data.")
        else:
            self.messaggioErrore("Orario errato.")

    def controllaTurno(self):
        self.ptxPreview.clear()
        listaprenotati = self.gestorario.controlloGiorno(self.calendarWidget.selectedDate().toString())
        for elem in listaprenotati:
            self.ptxPreview.appendPlainText("In data "+elem.data+" dalle ore "+elem.ora_inizio+" alle ore "+elem.ora_fine+
                                    " nella sala "+elem.mansione+" è presente "+elem.staff)

    def restituisciListaControllaTurno(self):
        listaprenotati = self.gestorario.controlloGiorno(self.calendarWidget.selectedDate().toString())
        return listaprenotati


    def chiediConferma(self, testo1, testo2):
        msgBox = QMessageBox()
        msgBox.setText(testo1)
        msgBox.setInformativeText(testo2)
        msgBox.setStandardButtons(QMessageBox.Save | QMessageBox.Discard)
        msgBox.setDefaultButton(QMessageBox.Save)
        ret = msgBox.exec_()
        if ret == QMessageBox.Save:
            return True
        return False

    def rimuoviGiornata(self):
        for elem in self.restituisciListaControllaTurno():
            if elem.staff == self.username:
                if self.chiediConferma("Verrà rimosso il turno di " + self.username + " dalla giornata di " +
                                       self.calendarWidget.selectedDate().toString(), "Continuare?"):
                    self.gestorario.rimuoviTurno(self.username, self.calendarWidget.selectedDate().toString())
                    self.notifica.notificaTurno("admin", self.username.replace(" ", ""), "Il turno in data " +
                                                self.calendarWidget.selectedDate().toString() + " di " +
                                                self.cmbTipo.currentText() + " dalle ore " + self.cmbInizio.currentText() + " alle ore " +
                                                self.cmbFine.currentText() + " è stato cancellato.")
                self.controllaTurno()
                return
        self.messaggioErrore("Impossibile trovare "+self.username+" nella giornata di "
                             +self.calendarWidget.selectedDate().toString())
        self.controllaTurno()


    def messaggioErrore(self, testo):
        self.msg.show_popup_ok(testo)

    def setupUi(self, MainWindow, username):
        self.username = username
        MainWindow.resize(900, 700)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.calendarWidget = QCalendarWidget(self.centralwidget)
        self.calendarWidget.setObjectName(u"calendarWidget")
        self.calendarWidget.setGeometry(QRect(10, 30, 280, 240))
        self.calendarWidget.setGridVisible(True)
        self.calendarWidget.setVerticalHeaderFormat(QCalendarWidget.NoVerticalHeader)
        self.calendarWidget.setNavigationBarVisible(True)
        self.cmbTipo = QComboBox(self.centralwidget)
        self.cmbTipo.addItem("")
        self.cmbTipo.addItem("")
        self.cmbTipo.addItem("")
        self.cmbTipo.setObjectName(u"cmbTipo")
        self.cmbTipo.setGeometry(QRect(380, 90, 131, 22))
        self.cmbTipo.setEditable(True)
        self.ptxPreview = QPlainTextEdit(self.centralwidget)
        self.ptxPreview.setObjectName(u"ptxPreview")
        self.ptxPreview.setGeometry(QRect(40, 280, 701, 331))
        self.spbPaga = QDoubleSpinBox(self.centralwidget)
        self.spbPaga.setObjectName(u"spbPaga")
        self.spbPaga.setGeometry(QRect(410, 130, 62, 22))
        self.spbPaga.setDecimals(1)
        self.lblPagaOrario = QLabel(self.centralwidget)
        self.lblPagaOrario.setObjectName(u"lblPagaOrario")
        self.lblPagaOrario.setGeometry(QRect(330, 130, 61, 21))
        self.lblTitolo = QLabel(self.centralwidget)
        self.lblTitolo.setObjectName(u"lblTitolo")
        self.lblTitolo.setGeometry(QRect(40, 10, 251, 16))
        self.lblTitolo.setAlignment(Qt.AlignCenter)
        self.btnSalva = QPushButton(self.centralwidget)
        self.btnSalva.setObjectName(u"btnSalva")
        self.btnSalva.setGeometry(QRect(330, 170, 75, 24))
        self.btnRimuovi = QPushButton(self.centralwidget)
        self.btnRimuovi.setObjectName(u"btnRimuovi")
        self.btnRimuovi.setGeometry(QRect(330, 220, 75, 24))
        self.lblCompensi = QLabel(self.centralwidget)
        self.lblCompensi.setObjectName(u"lblCompensi")
        self.lblCompensi.setGeometry(QRect(500, 130, 231, 16))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(330, 20, 31, 20))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(330, 50, 20, 20))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(328, 90, 41, 20))
        self.cmbFine = QComboBox(self.centralwidget)
        self.cmbFine.addItem("")
        self.cmbFine.addItem("")
        self.cmbFine.addItem("")
        self.cmbFine.addItem("")
        self.cmbFine.addItem("")
        self.cmbFine.addItem("")
        self.cmbFine.addItem("")
        self.cmbFine.addItem("")
        self.cmbFine.addItem("")
        self.cmbFine.setObjectName(u"cmbFine")
        self.cmbFine.setGeometry(QRect(380, 50, 131, 22))
        self.cmbFine.setEditable(True)
        self.cmbInizio = QComboBox(self.centralwidget)
        self.cmbInizio.addItem("")
        self.cmbInizio.addItem("")
        self.cmbInizio.addItem("")
        self.cmbInizio.addItem("")
        self.cmbInizio.addItem("")
        self.cmbInizio.addItem("")
        self.cmbInizio.addItem("")
        self.cmbInizio.addItem("")
        self.cmbInizio.addItem("")
        self.cmbInizio.setObjectName(u"cmbInizio")
        self.cmbInizio.setGeometry(QRect(380, 20, 131, 22))
        self.cmbInizio.setEditable(True)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)
        self.lblTitolo.setText(self.username)
        self.cmbTipo.activated.connect(self.fasciaOraria)
        self.calendarWidget.setMinimumDate(QDate.currentDate())
        self.calendarWidget.setMaximumDate(QDate.currentDate().addMonths(3))
        self.calendarWidget.clicked.connect(self.controllaGiorno)
        self.btnSalva.clicked.connect(self.salva)
        self.gestorario.recuperaSalvataggio("./Admin/gestione_personale/TurniStaff.txt")
        self.btnRimuovi.clicked.connect(self.rimuoviGiornata)
        self.calendarWidget.setSelectedDate(QDate.currentDate())
        self.controllaTurno()


    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        _translate = QtCore.QCoreApplication.translate
        self.cmbTipo.setItemText(0, QCoreApplication.translate("MainWindow", u"Sala Pesi", None))
        self.cmbTipo.setItemText(1, QCoreApplication.translate("MainWindow", u"Zumba", None))
        self.cmbTipo.setItemText(2, QCoreApplication.translate("MainWindow", u"Functional", None))
        self.lblPagaOrario.setText(QCoreApplication.translate("MainWindow", u"Paga oraria", None))
        self.lblTitolo.setText("")
        self.btnSalva.setText(QCoreApplication.translate("MainWindow", u"Salva", None))
        self.btnRimuovi.setText(QCoreApplication.translate("MainWindow", u"Rimuovi", None))
        self.lblCompensi.setText("")
        self.ptxPreview.setPlainText(_translate("MainWindow", "Seleziona un giorno dal calendario."))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Da", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"A", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Sala", None))
        self.cmbFine.setItemText(0, QCoreApplication.translate("MainWindow", u"11:00", None))
        self.cmbFine.setItemText(1, QCoreApplication.translate("MainWindow", u"12:30", None))
        self.cmbFine.setItemText(2, QCoreApplication.translate("MainWindow", u"14:00", None))
        self.cmbFine.setItemText(3, QCoreApplication.translate("MainWindow", u"15:30", None))
        self.cmbFine.setItemText(4, QCoreApplication.translate("MainWindow", u"17:00", None))
        self.cmbFine.setItemText(5, QCoreApplication.translate("MainWindow", u"18:30", None))
        self.cmbFine.setItemText(6, QCoreApplication.translate("MainWindow", u"20:00", None))
        self.cmbFine.setItemText(7, QCoreApplication.translate("MainWindow", u"21:30", None))
        self.cmbFine.setItemText(8, QCoreApplication.translate("MainWindow", u"23:00", None))
        self.cmbInizio.setItemText(0, QCoreApplication.translate("MainWindow", u"09:30", None))
        self.cmbInizio.setItemText(1, QCoreApplication.translate("MainWindow", u"11:00", None))
        self.cmbInizio.setItemText(2, QCoreApplication.translate("MainWindow", u"12:30", None))
        self.cmbInizio.setItemText(3, QCoreApplication.translate("MainWindow", u"14:00", None))
        self.cmbInizio.setItemText(4, QCoreApplication.translate("MainWindow", u"15:30", None))
        self.cmbInizio.setItemText(5, QCoreApplication.translate("MainWindow", u"17:00", None))
        self.cmbInizio.setItemText(6, QCoreApplication.translate("MainWindow", u"18:30", None))
        self.cmbInizio.setItemText(7, QCoreApplication.translate("MainWindow", u"20:00", None))
        self.cmbInizio.setItemText(8, QCoreApplication.translate("MainWindow", u"21:30", None))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = GestioneOrari()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
