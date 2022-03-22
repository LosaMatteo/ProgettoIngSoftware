# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SalaPesiPrenot.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import os

from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtCore import QDate

from Data.MessageBox import messageBox
from Cliente.Prenotazioni.gestionePrenotazioni import GestionePrenotazioniCorsi


class prenotazioni_sala_pesi(object):
    gestpr = GestionePrenotazioniCorsi()
    username = ""
    msg = messageBox()
    path = ""

    def assegnaAttributi(self):
        if self.calendarWidget.selectedDate().toString()[:3] != "dom":
            self.path = self.gestpr.assegnaAttributi(self.calendarWidget.selectedDate().toString("dd.MM.yyyy"),
                                                     self.comboBox.currentText().split(":"),
                                                     "./Cliente/Prenotazioni/file_prenotazioni/salaPesi/")
            return True
        else:
            self.msg.show_popup_ok("Selezionare un giorno corretto.")
            return False

    def prenota(self):
        if self.assegnaAttributi() == True:
            self.gestpr.prenota(10,self.path, self.username, )
            self.finestra.close()

    def cmbActivated(self):
        self.assegnaAttributi()
        self.progressBar.setValue(self.gestpr.cmbActivated(self.path))

    def elimina(self):
        self.gestpr.elimina("./Cliente/Prenotazioni/file_prenotazioni/salaPesi/")

    def setupUi(self, Form, username):
        self.finestra = Form
        self.username = username
        Form.setObjectName("Form")
        Form.resize(758, 487)
        self.calendarWidget = QtWidgets.QCalendarWidget(Form)
        self.calendarWidget.setGeometry(QtCore.QRect(20, 120, 421, 251))
        self.calendarWidget.setFirstDayOfWeek(QtCore.Qt.Monday)
        self.calendarWidget.setGridVisible(True)
        self.calendarWidget.setObjectName("calendarWidget")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 20, 351, 71))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(160, 100, 101, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(580, 110, 81, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(580, 210, 111, 16))
        self.label_4.setObjectName("label_4")
        self.progressBar = QtWidgets.QProgressBar(Form)
        self.progressBar.setGeometry(QtCore.QRect(580, 250, 131, 23))
        self.progressBar.setMaximum(10)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(True)
        self.progressBar.setObjectName("progressBar")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(550, 400, 113, 32))
        self.pushButton.setObjectName("pushButton")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(400, 10, 61, 61))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("./Resources/images/pngPrenotazioni/IconaSalaPesi1.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(580, 140, 111, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.pushButton.clicked.connect(self.prenota)
        self.calendarWidget.setMinimumDate(QDate.currentDate())
        self.comboBox.activated[str].connect(self.cmbActivated)
        self.calendarWidget.clicked.connect(self.cmbActivated)
        self.calendarWidget.setMaximumDate(QDate.currentDate().addMonths(1))
        self.elimina()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form",
                                      "<html><head/><body><p>La Sala Pesi è aperta dal lunedì al sabato. <br/>La prenotazione è valida per 1 ora e 30 minuti dall\'ora selezionata.</p></body></html>"))
        self.label_2.setText(_translate("Form", "Scegli il giorno:"))
        self.label_3.setText(_translate("Form", "Scegli l\'ora"))
        self.label_4.setText(_translate("Form", "Posti disponibili:"))
        self.pushButton.setText(_translate("Form", "Prenota ora"))
        self.comboBox.setItemText(0, _translate("Form", "09:30-11:00"))
        self.comboBox.setItemText(1, _translate("Form", "11:00-12:30"))
        self.comboBox.setItemText(2, _translate("Form", "12:30-14:00"))
        self.comboBox.setItemText(3, _translate("Form", "14:00-15:30"))
        self.comboBox.setItemText(4, _translate("Form", "15:30-17:00"))
        self.comboBox.setItemText(5, _translate("Form", "17:00-18:30"))
        self.comboBox.setItemText(6, _translate("Form", "18:30-20:00"))
        self.comboBox.setItemText(7, _translate("Form", "20:00-21:30"))
        self.comboBox.setItemText(8, _translate("Form", "21:30-23:00"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = prenotazioni_sala_pesi()
    ui.setupUi(Form, username="")
    Form.show()
    sys.exit(app.exec_())