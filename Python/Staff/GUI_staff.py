import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDate
from os import listdir
from os.path import isfile, join
from Data.casella_di_messaggi.Casella_di_messaggio import Casella_di_messaggio
from Data.casella_di_messaggi.leggi_messaggio import lettura_messaggio
from Data.interface_password import change_password
from Model.Cliente import Client
from Data.MessageBox import messageBox
from Model.Messaggio import Messaggio
from Model.Orario import Orario
from Staff.Allenamento_staff.allenamento_staff import allenamento_staff
from Staff.Dieta_staff.dieta_personale import dieta_staff


class GUI_staff(object):

    gestOrario = Orario()
    obj = Client()
    username = ""
    usernameCl = ""
    messanger = Messaggio()
    msg = messageBox()
    lista_messaggi = []
    listafilesutente = []

    def carica(self):
        self.listWidget.clear()
        l = self.obj.popolaLista()
        if l is not None:
            for x in l:
                self.listWidget.addItem(x)
                self.listWidget_3.addItem(x)
        self.listWidget_2.hide()
        self.listWidget_5.hide()


    def open(self):
        try:
            path = "./Cliente/Dieta/file_dieta"
            listafiles = [f for f in listdir(path) if isfile(join(path, f))]
            for elem in listafiles:
                if elem.startswith(self.listWidget_3.currentItem().text().replace(" ", "") + "_dieta_personale_"):
                    os.chdir("./Cliente/Dieta/file_dieta")
                    os.system(elem)
                    os.chdir("..")
                    os.chdir("..")
                    os.chdir("..")
        except(Exception):
            self.msg.show_popup_exception("Errore nell'apertura della dieta.")

    def visualizza_esercizi(self):
        try:
            self.listWidget_2.show()
            self.listWidget_2.clear()
            name = self.listWidget.currentItem().text()
            name = name.replace(" ", "")
            if os.path.exists("./Cliente/Allenamento/file_allenamento/"+name+".txt"):
                with open("./Cliente/Allenamento/file_allenamento/"+name+".txt", "r") as openfile:
                    lettura = openfile.read()
                    self.listWidget_2.addItem(lettura)
            else:
                self.listWidget_2.addItem("Nessun esercizio selezionato dal cliente")
        except(Exception):
            self.msg.show_popup_listWidget('non hai selezionato nulla nella lista')

    def orario(self):
        self.ptxTestoOrario.clear()
        lavoro = self.gestOrario.controlloLavoro(self.calendarWidget.selectedDate().toString(), self.username)
        for elem in lavoro:
            self.ptxTestoOrario.appendPlainText(
                "In data " + elem.data + " ti occuperai di " + elem.mansione + " dalle " +
                elem.ora_inizio + " alle " + elem.ora_fine + "\n")

    def visualizza_messaggi(self):
        self.listWidget_4.clear()
        self.lista_messaggi = self.messanger.getObject_message(self.username)
        self.lista_messaggi.sort(key=lambda x: x.data, reverse=True)  # ordina la lista messaggi in ordine temporale
        for elem in self.lista_messaggi:
            if elem.mittente == self.username:
                self.listWidget_4.addItem("messaggio inviato a: " + elem.destinatario + "  -  " + elem.data)
            elif elem.destinatario == self.username:
                self.listWidget_4.addItem("messaggio da: " + elem.mittente + "  -  " + elem.data)

    def open_window_leggi_messaggio(self):

        self.lettura_messaggio = QtWidgets.QMainWindow()
        self.ui = lettura_messaggio()
        self.ui.setupUi(self.lettura_messaggio,self.messanger, self.username)
        self.lettura_messaggio.show()

    def open_window_allenamento_staff(self):
        try:
            self.usernameCl = self.listWidget.currentItem().text()
            self.allenamento_staff = QtWidgets.QMainWindow()
            self.ui = allenamento_staff()
            self.ui.setupUi(self.allenamento_staff,self.usernameCl)
            self.allenamento_staff.show()
        except(Exception):
            self.msg.show_popup_listWidget("non hai selezionato nulla nella lista!")

    def open_window_password(self):
        self.password = QtWidgets.QMainWindow()
        self.ui = change_password()
        self.ui.setupUi(self.password, self.username)
        self.password.show()

    def open_window_message(self):
        self.casella = QtWidgets.QMainWindow()
        self.ui = Casella_di_messaggio()
        self.ui.setupUi(self.casella,self.username)
        self.casella.show()

    def open_window_dieta_staff(self):
        self.dieta_staff = QtWidgets.QMainWindow()
        self.ui = dieta_staff()
        self.ui.setupUi(self.dieta_staff,self.listWidget_3.currentItem().text())
        self.dieta_staff.show()

    def return_message(self):
        row = self.listWidget_4.currentRow()
        lista_messaggi_destinatario = self.messanger.getObject_message(self.username)
        lista_messaggi_destinatario.sort(key=lambda x: x.data, reverse=True)  # ordina la lista messaggi in ordine temporale
        self.messanger = lista_messaggi_destinatario[row]
        self.open_window_leggi_messaggio()

    def elimina_messaggio(self):

        obj = self.lista_messaggi[self.listWidget_4.currentRow()]
        self.messanger.rimuovi_messaggio(obj)
        self.listWidget_4.takeItem(self.listWidget_4.currentRow())
        self.visualizza_messaggi()

    def nascondi_dieta(self):
        self.listWidget_5.hide()
        self.label_8.hide()
        self.label_7.hide()
        self.label_9.hide()
        self.lineEdit_5.hide()
        self.lineEdit_6.hide()
        self.lineEdit_7.hide()

    def appari_dieta(self):
        self.listWidget_5.show()
        self.label_8.show()
        self.label_7.show()
        self.label_9.show()
        self.lineEdit_5.show()
        self.lineEdit_6.show()
        self.lineEdit_7.show()

    def check_indici_fisiologici(self):
        cliente_name = self.listWidget_3.currentItem().text()
        cliente_name = cliente_name.replace(" ", "")
        self.lineEdit_6.clear()
        self.lineEdit_5.clear()
        self.lineEdit_7.clear()
        self.nascondi_dieta()
        if os.path.exists("./Cliente/Dieta/file_dieta/" + cliente_name + ".txt"):
            with open("./Cliente/Dieta/file_dieta/" + cliente_name + ".txt", "r") as openfile:
                lettura = openfile.read()
                lettura = lettura.split("-")
                self.appari_dieta()
                self.lineEdit_6.setText(lettura[0])
                self.lineEdit_5.setText(lettura[1])
                self.lineEdit_7.setText(lettura[2])
        else:
            return

    def setupUi(self, MainWindow,username):
        self.username = username
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(883, 632)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.toolBox = QtWidgets.QToolBox(self.centralwidget)
        self.toolBox.setGeometry(QtCore.QRect(90, 40, 701, 531))
        self.toolBox.setObjectName("toolBox")
        self.page = QtWidgets.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 701, 407))
        self.page.setObjectName("page")
        self.listWidget = QtWidgets.QListWidget(self.page)
        self.listWidget.setGeometry(QtCore.QRect(20, 10, 201, 391))
        self.listWidget.setObjectName("listWidget")
        self.listWidget_2 = QtWidgets.QListWidget(self.page)
        self.listWidget_2.setGeometry(QtCore.QRect(320, 70, 291, 171))
        self.listWidget_2.setAcceptDrops(False)
        self.listWidget_2.setObjectName("listWidget_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.page)
        self.pushButton_2.setGeometry(QtCore.QRect(412, 370, 251, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_12 = QtWidgets.QLabel(self.page)
        self.label_12.setGeometry(QtCore.QRect(0, 10, 701, 401))
        self.label_12.setText("")
        self.label_12.setPixmap(QtGui.QPixmap("./Resources/images/pngGUI_client/Sfondo1.png"))
        self.label_12.setScaledContents(True)
        self.label_12.setObjectName("label_12")
        self.label_12.raise_()
        self.listWidget.raise_()
        self.listWidget_2.raise_()
        self.pushButton_2.raise_()
        self.toolBox.addItem(self.page, "")
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setGeometry(QtCore.QRect(0, 0, 701, 407))
        self.page_2.setObjectName("page_2")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.page_2)
        self.calendarWidget.setGeometry(QtCore.QRect(10, 10, 451, 236))
        self.calendarWidget.setObjectName("calendarWidget")
        self.label = QtWidgets.QLabel(self.page_2)
        self.label.setGeometry(QtCore.QRect(20, 270, 211, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.page_2)
        self.label_2.setGeometry(QtCore.QRect(40, 310, 221, 31))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.ptxTestoOrario = QtWidgets.QPlainTextEdit(self.page_2)
        self.ptxTestoOrario.setGeometry(QtCore.QRect(180, 280, 281, 91))
        self.ptxTestoOrario.setObjectName("ptxTestoOrario")
        self.label_11 = QtWidgets.QLabel(self.page_2)
        self.label_11.setGeometry(QtCore.QRect(0, 10, 701, 401))
        self.label_11.setText("")
        self.label_11.setPixmap(QtGui.QPixmap("./Resources/images/pngGUI_client/Sfondo1.png"))
        self.label_11.setScaledContents(True)
        self.label_11.setObjectName("label_11")
        self.label_11.raise_()
        self.calendarWidget.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.ptxTestoOrario.raise_()
        self.toolBox.addItem(self.page_2, "")
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setGeometry(QtCore.QRect(0, 0, 701, 407))
        self.page_3.setObjectName("page_3")
        self.listWidget_3 = QtWidgets.QListWidget(self.page_3)
        self.listWidget_3.setGeometry(QtCore.QRect(10, 10, 201, 391))
        self.listWidget_3.setObjectName("listWidget_3")
        self.listWidget_5 = QtWidgets.QListWidget(self.page_3)
        self.listWidget_5.setGeometry(QtCore.QRect(290, 50, 256, 192))
        self.listWidget_5.setObjectName("listWidget_5")
        self.label_7 = QtWidgets.QLabel(self.page_3)
        self.label_7.setGeometry(QtCore.QRect(320, 190, 81, 20))
        self.label_7.setObjectName("label_7")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.page_3)
        self.lineEdit_5.setGeometry(QtCore.QRect(410, 150, 113, 21))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_5.setReadOnly(True)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.page_3)
        self.lineEdit_6.setGeometry(QtCore.QRect(410, 110, 113, 21))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_6.setReadOnly(True)
        self.label_8 = QtWidgets.QLabel(self.page_3)
        self.label_8.setGeometry(QtCore.QRect(320, 150, 81, 20))
        self.label_8.setObjectName("label_8")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.page_3)
        self.lineEdit_7.setGeometry(QtCore.QRect(410, 190, 113, 21))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_7.setReadOnly(True)
        self.label_9 = QtWidgets.QLabel(self.page_3)
        self.label_9.setGeometry(QtCore.QRect(320, 110, 61, 20))
        self.label_9.setObjectName("label_9")
        self.label_3 = QtWidgets.QLabel(self.page_3)
        self.label_3.setGeometry(QtCore.QRect(360, 70, 111, 20))
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.pushButton_5 = QtWidgets.QPushButton(self.page_3)
        self.pushButton_5.setGeometry(QtCore.QRect(470, 370, 121, 28))
        self.pushButton_5.setObjectName("pushButton_5")
        self.btnApriDieta = QtWidgets.QPushButton(self.page_3)
        self.btnApriDieta.setGeometry(QtCore.QRect(470, 330, 121, 28))
        self.btnApriDieta.setObjectName("btnApriDieta")
        self.label_10 = QtWidgets.QLabel(self.page_3)
        self.label_10.setGeometry(QtCore.QRect(0, 10, 701, 401))
        self.label_10.setText("")
        self.label_10.setPixmap(QtGui.QPixmap("./Resources/images/pngGUI_client/Sfondo1.png"))
        self.label_10.setScaledContents(True)
        self.label_10.setObjectName("label_10")
        self.label_10.raise_()
        self.listWidget_3.raise_()
        self.listWidget_5.raise_()
        self.label_7.raise_()
        self.lineEdit_5.raise_()
        self.lineEdit_6.raise_()
        self.label_8.raise_()
        self.lineEdit_7.raise_()
        self.label_9.raise_()
        self.label_3.raise_()
        self.pushButton_5.raise_()
        self.btnApriDieta.raise_()
        self.toolBox.addItem(self.page_3, "")
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setGeometry(QtCore.QRect(0, 0, 701, 407))
        self.page_4.setObjectName("page_4")
        self.listWidget_4 = QtWidgets.QListWidget(self.page_4)
        self.listWidget_4.setGeometry(QtCore.QRect(70, 90, 441, 251))
        self.listWidget_4.setObjectName("listWidget_4")
        self.btnAggiornaMex = QtWidgets.QPushButton(self.page_4)
        self.btnAggiornaMex.setGeometry(QtCore.QRect(475, 95, 31, 31))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./Resources/images/aggiornamento.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnAggiornaMex.setText("")
        self.btnAggiornaMex.setIcon(icon)
        self.btnAggiornaMex.setIconSize(QtCore.QSize(50, 50))
        self.btnAggiornaMex.setObjectName("btnAggiornaMex")
        self.pushButton_7 = QtWidgets.QPushButton(self.page_4)
        self.pushButton_7.setGeometry(QtCore.QRect(530, 210, 141, 28))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.page_4)
        self.pushButton_8.setGeometry(QtCore.QRect(530, 260, 141, 28))
        self.pushButton_8.setObjectName("pushButton_8")
        self.label_5 = QtWidgets.QLabel(self.page_4)
        self.label_5.setGeometry(QtCore.QRect(170, 30, 311, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.page_4)
        self.pushButton_6.setGeometry(QtCore.QRect(530, 300, 141, 28))
        self.pushButton_6.setObjectName("pushButton_6")
        self.label_6 = QtWidgets.QLabel(self.page_4)
        self.label_6.setGeometry(QtCore.QRect(0, 0, 701, 401))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("./Resources/images/pngGUI_client/Sfondo1.png"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.label_13 = QtWidgets.QLabel(self.page_4)
        self.label_13.setGeometry(QtCore.QRect(480, 0, 101, 71))
        self.label_13.setText("")
        self.label_13.setPixmap(QtGui.QPixmap("./Resources/images/images.jpg"))
        self.label_13.setScaledContents(True)
        self.label_13.setObjectName("label_13")
        self.label_6.raise_()
        self.listWidget_4.raise_()
        self.pushButton_7.raise_()
        self.pushButton_8.raise_()
        self.btnAggiornaMex.raise_()
        self.label_5.raise_()
        self.pushButton_6.raise_()
        self.label_13.raise_()
        self.toolBox.addItem(self.page_4, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 883, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.toolBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.messanger.recuperaSalvataggio("./Data/casella_di_messaggi/messaggi.txt")
        self.visualizza_messaggi()
        self.pushButton_5.hide()
        self.btnApriDieta.hide()
        self.carica()
        self.nascondi_dieta()
        self.listWidget_3.clicked.connect(self.check_indici_fisiologici)
        self.listWidget_3.clicked.connect(self.pushButton_5.show)
        self.listWidget_3.clicked.connect(self.btnApriDieta.show)
        self.listWidget.clicked.connect(self.visualizza_esercizi)
        self.pushButton_2.clicked.connect(self.open_window_allenamento_staff)
        self.pushButton_6.clicked.connect(self.open_window_password)
        self.pushButton_7.clicked.connect(self.open_window_message)
        self.listWidget_4.doubleClicked.connect(self.return_message)
        self.pushButton_8.clicked.connect(self.elimina_messaggio)
        self.pushButton_5.clicked.connect(self.open_window_dieta_staff)
        self.gestOrario.recuperaSalvataggio("./Admin/gestione_personale/TurniStaff.txt")
        self.calendarWidget.clicked.connect(self.orario)
        self.calendarWidget.setMinimumDate(QDate.currentDate())
        self.calendarWidget.setMaximumDate(QDate.currentDate().addMonths(3))
        self.calendarWidget.setSelectedDate(QDate.currentDate())
        self.orario()
        self.btnApriDieta.clicked.connect(self.open)
        self.btnAggiornaMex.clicked.connect(self.visualizza_messaggi)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_2.setText(_translate("MainWindow", "Crea scheda di allenamento"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), _translate("MainWindow", "Allenamento"))
        self.label.setText(_translate("MainWindow", "Il tuo orario lavorativo:"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), _translate("MainWindow", "Orario"))
        self.label_7.setText(_translate("MainWindow", "FABBISOGNO"))
        self.label_8.setText(_translate("MainWindow", "PESO FORMA:"))
        self.label_9.setText(_translate("MainWindow", "BMI:"))
        self.pushButton_5.setText(_translate("MainWindow", "Crea una dieta"))
        self.btnApriDieta.setText(_translate("MainWindow", "Apri dieta"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_3), _translate("MainWindow", "Dieta"))
        self.pushButton_7.setText(_translate("MainWindow", "Scrivi Messaggio"))
        self.pushButton_8.setText(_translate("MainWindow", "Elimina Messaggio"))
        self.label_5.setText(_translate("MainWindow",
                                        "<html><head/><body><p align=\"center\"><span style=\" color:#55aa00;\">BACHECA MESSAGGI</span></p><p align=\"center\"><span style=\" color:#55aa00;\"><br/></span></p></body></html>"))
        self.pushButton_6.setText(_translate("MainWindow", "Cambia password"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_4), _translate("MainWindow", "Bacheca"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = GUI_staff()
    ui.setupUi(MainWindow,username="")
    MainWindow.show()
    sys.exit(app.exec_())
