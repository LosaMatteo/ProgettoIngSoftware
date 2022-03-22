from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDate
from Cliente.Prenotazioni.gestionePrenotazioni import GestionePrenotazioniCorsi
from Data.MessageBox import messageBox


class prenotazione_zumba(object):
    gestpr = GestionePrenotazioniCorsi()
    username = ""
    msg = messageBox()
    path = ""

    def assegnaAttributi(self):
        if (self.popupcalendar.selectedDate().toString()[:3] == "gio" or
                self.popupcalendar.selectedDate().toString()[:3] == "ven"):
            self.path = self.gestpr.assegnaAttributi(self.popupcalendar.selectedDate().toString("dd.MM.yyyy"),
                                                     self.comboBox.currentText().split(":"),
                                                     "./Cliente/Prenotazioni/file_prenotazioni/zumba/")
            return True
        else:
            self.msg.show_popup_ok("Selezionare un giorno corretto.")
            return False

    def prenota(self):
        if self.assegnaAttributi() == True:
            self.gestpr.prenota(20,self.path, self.username, )
            self.finestra.close()

    def cmbActivated(self):
        self.assegnaAttributi()
        self.progressBar.setValue(self.gestpr.cmbActivated(self.path))

    def elimina(self):
        self.gestpr.elimina("./Cliente/Prenotazioni/file_prenotazioni/zumba/")

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
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(19, 15, 291, 61))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(10, 110, 101, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(550, 80, 111, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(550, 180, 111, 20))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(390, 10, 81, 71))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap(".\\IconaZumba.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(550, 350, 113, 32))
        self.pushButton.setObjectName("pushButton")
        self.popupcalendar = QtWidgets.QCalendarWidget(Form)
        self.popupcalendar.setGeometry(QtCore.QRect(10, 130, 421, 251))
        self.popupcalendar.setFirstDayOfWeek(QtCore.Qt.Monday)
        self.popupcalendar.setGridVisible(True)
        self.popupcalendar.setObjectName("popupcalendar")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(550, 110, 111, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.pushButton.clicked.connect(self.prenota)
        self.popupcalendar.setMinimumDate(QDate.currentDate())
        self.comboBox.activated[str].connect(self.cmbActivated)
        self.popupcalendar.clicked.connect(self.cmbActivated)
        self.popupcalendar.setMaximumDate(QDate.currentDate().addMonths(1))
        self.elimina()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form",
                                      "<html><head/><body><p>Le lezioni si svolgono il giovedì e il venerdì</p><p>dalle ore 18:00 e dalle ore 19:30.</p></body></html>"))
        self.label_2.setText(_translate("Form", "Seleziona data:"))
        self.label_3.setText(_translate("Form", "Seleziona orario:"))
        self.label_4.setText(_translate("Form", "Posti disponibili:"))
        self.pushButton.setText(_translate("Form", "Prenota ora"))
        self.comboBox.setItemText(0, _translate("Form", "18:00-19:30"))
        self.comboBox.setItemText(1, _translate("Form", "19:30-21:00"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = prenotazione_zumba()
    ui.setupUi(Form, username="")
    Form.show()
    sys.exit(app.exec_())
