from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDate
from Cliente.Prenotazioni.gestionePrenotazioni import GestionePrenotazioniCorsi
from Data.MessageBox import messageBox


class prenotazioni_allenamento_functional(object):
    gestpr = GestionePrenotazioniCorsi()
    username = ""
    msg = messageBox()
    path = ""

    def assegnaAttributi(self):
        if (self.popupcalendar.selectedDate().toString()[:3] == "mar" or
                self.popupcalendar.selectedDate().toString()[:3] == "mer" or
                self.popupcalendar.selectedDate().toString()[:3] == "ven"):
            self.path = self.gestpr.assegnaAttributi(self.popupcalendar.selectedDate().toString("dd.MM.yyyy"),
                                                     self.comboBox.currentText().split(":"),
                                                     "./Cliente/Prenotazioni/file_prenotazioni/functional/")
            return True
        else:
            self.msg.show_popup_ok("Selezionare un giorno corretto.")
            return False

    def prenota(self):
        if self.assegnaAttributi() == True:
            self.gestpr.prenota(15,self.path, self.username, )
            self.finestra.close()

    def cmbActivated(self):
        self.assegnaAttributi()
        self.progressBar.setValue(self.gestpr.cmbActivated(self.path))

    def elimina(self):
        self.gestpr.elimina("./Cliente/Prenotazioni/file_prenotazioni/functional/")

    def setupUi(self, Form, username):
        self.finestra = Form
        self.username = username
        Form.setObjectName("Form")
        Form.resize(756, 411)
        self.progressBar = QtWidgets.QProgressBar(Form)
        self.progressBar.setGeometry(QtCore.QRect(560, 230, 121, 23))
        self.progressBar.setMaximum(15)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(560, 340, 113, 32))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 100, 111, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(550, 80, 111, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(560, 200, 81, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(19, 15, 311, 61))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(370, 10, 91, 71))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap(".\\IconaAllFunzionale.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.popupcalendar = QtWidgets.QCalendarWidget(Form)
        self.popupcalendar.setGeometry(QtCore.QRect(10, 120, 421, 251))
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
        self.pushButton.setText(_translate("Form", "Prenota ora"))
        self.label.setText(_translate("Form", "Seleziona data:"))
        self.label_2.setText(_translate("Form", "Seleziona orario:"))
        self.label_3.setText(_translate("Form", "Posti liberi:"))
        self.label_4.setText(_translate("Form",
                                        "<html><head/><body><p>Le lezioni di Allenamento Funzionale si svolgono<br/>martedì, mercoledì e venerdì.<br/>Dalle ore 15:30 e dalle 17:00. <br/></p></body></html>"))
        self.comboBox.setItemText(0, _translate("Form", "15:30-17:00"))
        self.comboBox.setItemText(1, _translate("Form", "17:00-18:30"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = prenotazioni_allenamento_functional()
    ui.setupUi(Form, username="")
    Form.show()
    sys.exit(app.exec_())
