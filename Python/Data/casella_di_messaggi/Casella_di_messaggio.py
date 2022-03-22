from PyQt5 import QtCore, QtGui, QtWidgets
from Data.MessageBox import messageBox
from Model.Cliente import Client
from Model.Personale import Personale
from Model.Messaggio import Messaggio
from datetime import datetime


class Casella_di_messaggio(object):
    msg = messageBox()
    clsMessaggi = Messaggio()
    username = ""
    emittente = ""

    def popola_comboBox(self):
        cliente = Client()
        staff = Personale()
        self.label_4.setText(self.username)
        if self.username != "admin":
            self.comboBox_2.addItem("A-admin")
        vett = cliente.get_lista()
        for elem in vett:
            if elem != self.username:
             self.comboBox_2.addItem("C-" + elem)
        vett = staff.get_lista()
        for elem in vett:
            if elem != self.username:
             self.comboBox_2.addItem("P-" + elem)

    def scrittura_file_messaggi(self):
        cliente = Client()
        staff = Personale()
        if self.chkClienti.isChecked() == False and self.chkStaff.isChecked() == False:
            destinatario = self.comboBox_2.currentText().split("-")
            self.spedisciMessaggio(destinatario[1])
        if self.chkClienti.isChecked() == True:
            vett = cliente.get_lista()
            for elem in vett:
                self.spedisciMessaggio(elem)
        if self.chkStaff.isChecked() == True:
            vett = staff.get_lista()
            for elem in vett:
                self.spedisciMessaggio(elem)
        self.msg.show_popup_ok("il tuo contenuto è stato inviato correttamente")
        self.finestra.close()

    def spedisciMessaggio(self, destinatario):
        messaggi = Messaggio(self.username, destinatario, self.plainTextEdit.toPlainText(),
                             datetime.today().strftime('%Y-%m-%d-%H:%M'))
        messaggi.addToList(messaggi)
        #self.messaggi.scriviLista("./Data/casella_di_messaggi/messaggi.txt")

    def notificaTurno(self, mittente, destinatario, messaggio):
        messaggi = Messaggio(mittente, destinatario, messaggio,
                             datetime.today().strftime('%Y-%m-%d-%H:%M'))
        messaggi.addToList(messaggi)
        self.msg.show_popup_ok("il tuo contenuto è stato inviato correttamente")

    def selezioneDestinatario(self):
        if self.chkClienti.isChecked() or self.chkStaff.isChecked():
            self.comboBox_2.setDisabled(True)
        else:
            self.comboBox_2.setDisabled(False)


    def setupUi(self, MainWindow, username):
        self.finestra = MainWindow
        self.username = username
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(535, 450)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 60, 31, 20))
        font = QtGui.QFont()
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(360, 330, 141, 28))
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 30, 41, 20))
        font = QtGui.QFont()
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 90, 55, 31))
        font = QtGui.QFont()
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(90, 60, 151, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(90, 100, 421, 211))
        self.plainTextEdit.setPlainText("")
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(90, 30, 151, 21))
        font = QtGui.QFont()
        font.setBold(True)
        self.label_4.setFont(font)
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.chkClienti = QtWidgets.QCheckBox(self.centralwidget)
        self.chkClienti.setGeometry(QtCore.QRect(280, 60, 91, 20))
        self.chkClienti.setObjectName("chkClienti")
        self.chkStaff = QtWidgets.QCheckBox(self.centralwidget)
        self.chkStaff.setGeometry(QtCore.QRect(400, 60, 91, 20))
        self.chkStaff.setObjectName("chkStaff")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 535, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        if self.username != "admin":
            self.chkStaff.hide()
            self.chkClienti.hide()
        self.popola_comboBox()
        self.clsMessaggi.recuperaSalvataggio("./Data/casella_di_messaggi/messaggi.txt")
        self.pushButton.clicked.connect(self.scrittura_file_messaggi)
        self.chkStaff.clicked.connect(self.selezioneDestinatario)
        self.chkClienti.clicked.connect(self.selezioneDestinatario)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "A:"))
        self.pushButton.setText(_translate("MainWindow", "Invia Messaggio"))
        self.label_2.setText(_translate("MainWindow", "DA:"))
        self.label_3.setText(_translate("MainWindow", "Oggetto:"))
        self.chkClienti.setText(_translate("MainWindow", "Tutti i clienti"))
        self.chkStaff.setText(_translate("MainWindow", "Tutto lo staff"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Casella_di_messaggio()
    ui.setupUi(MainWindow, username="")
    MainWindow.show()
    sys.exit(app.exec_())
