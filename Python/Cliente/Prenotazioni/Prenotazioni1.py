from PyQt5 import QtCore, QtGui, QtWidgets
from Cliente.Prenotazioni.PrenotazioneZumba import prenotazione_zumba
from Cliente.Prenotazioni.PrenotazioniAllenamentoFunzionale import prenotazioni_allenamento_functional
from Cliente.Prenotazioni.SalaPesiPrenot import prenotazioni_sala_pesi


class prenotazioni(object):

    username = ""
    def open_window_prenotazione_sala_pesi(self):
        self.sala_pesi = QtWidgets.QMainWindow()
        self.ui = prenotazioni_sala_pesi()
        self.ui.setupUi(self.sala_pesi, self.username)
        self.sala_pesi.show()

    def open_window_prenotazioni_functional(self):
        self.functional = QtWidgets.QMainWindow()
        self.ui = prenotazioni_allenamento_functional()
        self.ui.setupUi(self.functional, self.username)
        self.functional.show()

    def open_window_prenotazioni_zumba(self):
        self.zumba = QtWidgets.QMainWindow()
        self.ui = prenotazione_zumba()
        self.ui.setupUi(self.zumba, self.username)
        self.zumba.show()


    def setupUi(self, Form,username):
        self.username = username
        Form.setObjectName("Form")
        Form.resize(689, 576)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(200, 70, 261, 81))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(470, 80, 71, 71))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("./Resources/images/pngPrenotazioni/Prenot1.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(50, 420, 113, 32))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(300, 420, 113, 32))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(530, 420, 113, 32))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(20, 240, 181, 151))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("./Resources/images/pngPrenotazioni/SalaPesi.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(500, 240, 181, 151))
        self.label_4.setText("")
        self.label_4.setTextFormat(QtCore.Qt.RichText)
        self.label_4.setPixmap(QtGui.QPixmap("./Resources/images/pngPrenotazioni/zumba.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(270, 240, 171, 151))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("./Resources/images/pngPrenotazioni/funzionale.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.pushButton.clicked.connect(self.open_window_prenotazione_sala_pesi)
        self.pushButton_2.clicked.connect(self.open_window_prenotazioni_functional)
        self.pushButton_3.clicked.connect(self.open_window_prenotazioni_zumba)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:36pt;\">PRENOTAZIONI</span></p></body></html>"))
        self.pushButton.setText(_translate("Form", "Sala Pesi"))
        self.pushButton_2.setText(_translate("Form", "Funzionale"))
        self.pushButton_3.setText(_translate("Form", "Zumba"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = prenotazioni()
    ui.setupUi(Form,)
    Form.show()
    sys.exit(app.exec_())
