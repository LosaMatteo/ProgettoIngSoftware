from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QTableWidgetItem
from Admin.gestione_cliente.aggiungi_cliente import aggiungi_cliente
from Admin.gestione_cliente.gestionecliente import gestione_cliente
from Admin.gestione_attrezzi.agg_attrezzo import agg_attrezzo
from Admin.gestione_personale.agg_staff import agg_personale
from Admin.gestione_personale.gestionestaff import gestione_staff
from Data.MessageBox import messageBox
from Data.casella_di_messaggi.Casella_di_messaggio import Casella_di_messaggio
from Data.casella_di_messaggi.leggi_messaggio import lettura_messaggio
from Model.Cliente import Client
from Model.Attrezzo import Attrezzo
from Model.Messaggio import Messaggio
from Model.Personale import Personale


class GUI_Admin(object):
    username = ""
    objCli = Client()
    objAtt = Attrezzo()
    objStaff = Personale()
    messanger = Messaggio()
    msg = messageBox()
    lista_messaggi = []
    row = 0

    def open_windowDet(self):
        try:
            if self.listWidgetCli.currentItem().isSelected():
                name = self.listWidgetCli.currentItem().text()
                self.window = QtWidgets.QMainWindow()
                self.ui = gestione_cliente(name)
                self.ui.setupUi(self.window)
                self.window.show()
        except(Exception):
            self.msg.show_popup_exception("Seleziona un cliente!")

    def open_window_message(self):
        self.casella = QtWidgets.QMainWindow()
        self.ui = Casella_di_messaggio()
        self.ui.setupUi(self.casella, self.username)
        self.casella.show()

    def open_window_leggi_messaggio(self):

        self.lettura_messaggio = QtWidgets.QMainWindow()
        self.ui = lettura_messaggio()
        self.ui.setupUi(self.lettura_messaggio, self.messanger, self.username)
        self.lettura_messaggio.show()

    def visualizza_messaggi(self):
        self.listWidget_4.clear()
        self.lista_messaggi = self.messanger.getObject_message(self.username)
        self.lista_messaggi.sort(key=lambda x: x.data, reverse=True) # ordina la lista messaggi in ordine temporale
        for elem in self.lista_messaggi:
            if elem.mittente == self.username:
                self.listWidget_4.addItem("messaggio inviato a: " + elem.destinatario + "  -  " + elem.data)
            elif elem.destinatario == self.username:
                self.listWidget_4.addItem("messaggio da: " + elem.mittente + "  -  " + elem.data)

    def return_message(self):

        row = self.listWidget_4.currentRow()
        self.lista_messaggi = self.messanger.getObject_message(self.username)
        self.lista_messaggi.sort(key=lambda x: x.data, reverse=True)  # ordina la lista messaggi in ordine temporale
        self.messanger = self.lista_messaggi[row]
        self.open_window_leggi_messaggio()


    def elimina_messaggio(self):
        try:
            obj = self.lista_messaggi[self.listWidget_4.currentRow()]
            self.messanger.rimuovi_messaggio(obj)
            self.listWidget_4.takeItem(self.listWidget_4.currentRow())
            self.visualizza_messaggi()
        except(Exception):
            self.msg.show_popup_exception("NON hai selezionato nessun messaggio")

    def open_windowDetPer(self):
        try:
            if self.listWidget.currentItem().isSelected():
                name = self.listWidget.currentItem().text()
                self.window = QtWidgets.QMainWindow()
                self.ui = gestione_staff(name)
                self.ui.setupUi(self.window)
                self.window.show()
        except(Exception):
            self.msg.show_popup_exception("Seleziona un membro del personale!")

    def open_windowCli(self):
        self.window_aggiungi_cliente = QtWidgets.QMainWindow()
        self.ui = aggiungi_cliente()
        self.ui.setupUi(self.window_aggiungi_cliente)
        self.window_aggiungi_cliente.show()

    def open_windowPer(self):
        self.window_aggiungi_personale = QtWidgets.QMainWindow()
        self.ui = agg_personale()
        self.ui.setupUi(self.window_aggiungi_personale)
        self.window_aggiungi_personale.show()

    def open_windowAtt(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = agg_attrezzo()
        self.ui.setupUi(self.window)
        self.window.show()

    def rimuoviAtt(self):

        try:
            if self.tableWidgetAtt.currentItem().isSelected():
                obj = Attrezzo()
                obj.rimuovi(self.tableWidgetAtt.currentRow())
                self.caricaAtt()
        except(Exception):
                self.msg.show_popup_exception("Non hai selezionato nulla nella tabella")

    def caricaCli(self):
        self.listWidgetCli.clear()
        obj = Client()
        l = obj.popolaLista()
        if l is not None:
            for x in l:
                self.listWidgetCli.addItem(x)

    def caricaPer(self):
        self.listWidget.clear()
        obj = Personale()
        l = obj.popolaLista()
        if l is not None:
            for x in l:
                self.listWidget.addItem(x)

    def caricaAtt(self):
        object = Attrezzo()

        listaAtt = object.popolaLista()
        vett = []

        if listaAtt is not None:
            for x in listaAtt:
                for j in x:
                    vett.append(j)

        colonna = 0
        i = 0
        if self.row != 0:
            temp = self.row
            while temp != -1:
                self.tableWidgetAtt.removeRow(temp)
                temp -=1
                self.row = 0
        while len(vett) > i + 1:
                self.tableWidgetAtt.insertRow(self.row)
                self.tableWidgetAtt.setItem(self.row, colonna, QTableWidgetItem(vett[i]))
                self.tableWidgetAtt.setItem(self.row, colonna + 1, QTableWidgetItem(vett[i + 1]))
                self.tableWidgetAtt.setItem(self.row, colonna + 2, QTableWidgetItem(vett[i + 2]))
                self.tableWidgetAtt.setItem(self.row, colonna + 3, QTableWidgetItem(vett[i + 3]))
                self.tableWidgetAtt.setItem(self.row, colonna + 4, QTableWidgetItem(vett[i + 4]))
                self.row += 1
                i += 5

    def upload_attrezzo(self):
        self.objAtt.recuperaSalvataggio("./Admin/gestione_attrezzi/listaAttrezzi.txt")
        self.caricaAtt()

    def upload_client(self):
        self.objCli.recuperaSalvataggio("./Admin/gestione_cliente/CredenzialiClienti.txt")
        self.caricaCli()

    def upload_staff(self):
        self.objStaff.recuperaSalvataggio("./Admin/gestione_personale/CredenzialiStaff.txt")
        self.caricaPer()


    def setupUi(self, MainWindow, username):
        self.username = username
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 609)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 30, 731, 521))
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setObjectName("tabWidget")
        self.tabCli = QtWidgets.QWidget()
        self.tabCli.setObjectName("tabCli")
        self.listWidgetCli = QtWidgets.QListWidget(self.tabCli)
        self.listWidgetCli.setGeometry(QtCore.QRect(30, 70, 221, 381))
        self.listWidgetCli.setObjectName("listWidgetCli")
        self.btnnAggCli = QtWidgets.QPushButton(self.tabCli)
        self.btnnAggCli.setGeometry(QtCore.QRect(280, 340, 101, 31))
        self.btnnAggCli.setObjectName("btnnAggCli")
        self.btnModificaCli = QtWidgets.QPushButton(self.tabCli)
        self.btnModificaCli.setGeometry(QtCore.QRect(280, 400, 101, 31))
        self.btnModificaCli.setObjectName("btnModificaCli")
        self.btn_aggiorna = QtWidgets.QPushButton(self.tabCli)
        self.btn_aggiorna.setGeometry(QtCore.QRect(210, 80, 31, 31))
        self.btn_aggiorna.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./Resources/images/aggiornamento.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_aggiorna.setIcon(icon)
        self.btn_aggiorna.setIconSize(QtCore.QSize(50, 50))
        self.btn_aggiorna.setObjectName("btn_aggiorna")
        self.lbl_testo = QtWidgets.QLabel(self.tabCli)
        self.lbl_testo.setGeometry(QtCore.QRect(30, 40, 231, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lbl_testo.setFont(font)
        self.lbl_testo.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lbl_testo.setObjectName("lbl_testo")
        self.label_2 = QtWidgets.QLabel(self.tabCli)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 731, 491))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("./Resources/images/pngGUI_client/Sfondodecisivo.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_9 = QtWidgets.QLabel(self.tabCli)
        self.label_9.setGeometry(QtCore.QRect(350, 20, 341, 191))
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap("./Resources/images/download (1).jpg"))
        self.label_9.setScaledContents(True)
        self.label_9.setObjectName("label_9")
        self.label_2.raise_()
        self.listWidgetCli.raise_()
        self.btnnAggCli.raise_()
        self.btnModificaCli.raise_()
        self.btn_aggiorna.raise_()
        self.lbl_testo.raise_()
        self.label_9.raise_()
        self.tabWidget.addTab(self.tabCli, "")
        self.tabPer = QtWidgets.QWidget()
        self.tabPer.setObjectName("tabPer")
        self.listWidget = QtWidgets.QListWidget(self.tabPer)
        self.listWidget.setGeometry(QtCore.QRect(30, 70, 221, 381))
        self.listWidget.setObjectName("listWidget")
        self.btnAggPer = QtWidgets.QPushButton(self.tabPer)
        self.btnAggPer.setGeometry(QtCore.QRect(280, 340, 101, 31))
        self.btnAggPer.setObjectName("btnAggPer")
        self.btnViewPer = QtWidgets.QPushButton(self.tabPer)
        self.btnViewPer.setGeometry(QtCore.QRect(280, 400, 101, 31))
        self.btnViewPer.setObjectName("btnViewPer")
        self.lbl_testo_2 = QtWidgets.QLabel(self.tabPer)
        self.lbl_testo_2.setGeometry(QtCore.QRect(40, 40, 211, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lbl_testo_2.setFont(font)
        self.lbl_testo_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lbl_testo_2.setObjectName("lbl_testo_2")
        self.btn_aggiorna_2 = QtWidgets.QPushButton(self.tabPer)
        self.btn_aggiorna_2.setGeometry(QtCore.QRect(210, 80, 31, 31))
        self.btn_aggiorna_2.setText("")
        self.btn_aggiorna_2.setIcon(icon)
        self.btn_aggiorna_2.setIconSize(QtCore.QSize(50, 50))
        self.btn_aggiorna_2.setObjectName("btn_aggiorna_2")
        self.label_3 = QtWidgets.QLabel(self.tabPer)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 731, 491))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("./Resources/images/pngGUI_client/Sfondodecisivo.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_7 = QtWidgets.QLabel(self.tabPer)
        self.label_7.setGeometry(QtCore.QRect(350, 20, 341, 191))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("./Resources/images/download (1).jpg"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.label_3.raise_()
        self.listWidget.raise_()
        self.btnAggPer.raise_()
        self.btnViewPer.raise_()
        self.lbl_testo_2.raise_()
        self.btn_aggiorna_2.raise_()
        self.label_7.raise_()
        self.tabWidget.addTab(self.tabPer, "")
        self.tabAtt = QtWidgets.QWidget()
        self.tabAtt.setObjectName("tabAtt")
        self.btnAggAtt = QtWidgets.QPushButton(self.tabAtt)
        self.btnAggAtt.setGeometry(QtCore.QRect(390, 360, 91, 31))
        self.btnAggAtt.setObjectName("btnAggAtt")
        self.btnRimuoviAtt = QtWidgets.QPushButton(self.tabAtt)
        self.btnRimuoviAtt.setGeometry(QtCore.QRect(240, 360, 91, 31))
        self.btnRimuoviAtt.setObjectName("btnRimuoviAtt")
        self.label_4 = QtWidgets.QLabel(self.tabAtt)
        self.label_4.setGeometry(QtCore.QRect(0, 0, 731, 491))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("./Resources/images/pngGUI_client/Sfondodecisivo.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.tableWidgetAtt = QtWidgets.QTableWidget(self.tabAtt)
        self.tableWidgetAtt.setGeometry(QtCore.QRect(10, 80, 691, 261))
        self.tableWidgetAtt.setObjectName("tableWidgetAtt")
        self.tableWidgetAtt.setColumnCount(5)
        self.tableWidgetAtt.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetAtt.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetAtt.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetAtt.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetAtt.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetAtt.setHorizontalHeaderItem(4, item)
        self.btn_aggiorna_3 = QtWidgets.QPushButton(self.tabAtt)
        self.btn_aggiorna_3.setGeometry(QtCore.QRect(660, 90, 31, 31))
        self.btn_aggiorna_3.setText("")
        self.btn_aggiorna_3.setIcon(icon)
        self.btn_aggiorna_3.setIconSize(QtCore.QSize(50, 50))
        self.btn_aggiorna_3.setObjectName("btn_aggiorna_3")
        self.label_4.raise_()
        self.btnAggAtt.raise_()
        self.btnRimuoviAtt.raise_()
        self.tableWidgetAtt.raise_()
        self.btn_aggiorna_3.raise_()
        self.tabWidget.addTab(self.tabAtt, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.pushButton_8 = QtWidgets.QPushButton(self.tab)
        self.pushButton_8.setGeometry(QtCore.QRect(510, 220, 141, 28))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_7 = QtWidgets.QPushButton(self.tab)
        self.pushButton_7.setGeometry(QtCore.QRect(510, 170, 141, 28))
        self.pushButton_7.setObjectName("pushButton_7")
        self.listWidget_4 = QtWidgets.QListWidget(self.tab)
        self.listWidget_4.setGeometry(QtCore.QRect(50, 110, 441, 251))
        self.listWidget_4.setObjectName("listWidget_4")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(60, 30, 421, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(0, 0, 731, 491))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("./Resources/images/pngGUI_client/Sfondodecisivo.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.btnAggiornaMex = QtWidgets.QPushButton(self.tab)
        self.btnAggiornaMex.setGeometry(QtCore.QRect(450, 120, 31, 31))
        self.btnAggiornaMex.setText("")
        self.btnAggiornaMex.setIcon(icon)
        self.btnAggiornaMex.setIconSize(QtCore.QSize(50, 50))
        self.btnAggiornaMex.setObjectName("btnAggiornaMex")
        self.label_5.raise_()
        self.pushButton_8.raise_()
        self.pushButton_7.raise_()
        self.listWidget_4.raise_()
        self.label.raise_()
        self.btnAggiornaMex.raise_()
        self.tabWidget.addTab(self.tab, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.objCli.recuperaSalvataggio("./Admin/gestione_cliente/CredenzialiClienti.txt")
        self.objAtt.recuperaSalvataggio("./Admin/gestione_attrezzi/listaAttrezzi.txt")
        self.objStaff.recuperaSalvataggio("./Admin/gestione_personale/CredenzialiStaff.txt")
        self.messanger.recuperaSalvataggio("./Data/casella_di_messaggi/messaggi.txt")
        self.visualizza_messaggi()
        self.caricaAtt()
        self.caricaCli()
        self.caricaPer()
        self.btnRimuoviAtt.clicked.connect(self.rimuoviAtt)
        self.btnnAggCli.clicked.connect(self.open_windowCli)
        self.btnAggPer.clicked.connect(self.open_windowPer)
        self.btnAggAtt.clicked.connect(self.open_windowAtt)
        self.btnAggPer.clicked.connect(self.caricaPer)
        self.btnModificaCli.clicked.connect(self.open_windowDet)
        self.btnViewPer.clicked.connect(self.open_windowDetPer)
        self.listWidget_4.doubleClicked.connect(self.return_message)
        self.pushButton_7.clicked.connect(self.open_window_message)
        self.pushButton_8.clicked.connect(self.elimina_messaggio)
        self.btn_aggiorna.clicked.connect(self.upload_client)
        self.btn_aggiorna_2.clicked.connect(self.upload_staff)
        self.btn_aggiorna_3.clicked.connect(self.upload_attrezzo)
        self.btnAggiornaMex.clicked.connect(self.visualizza_messaggi)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnnAggCli.setText(_translate("MainWindow", "Aggiungi"))
        self.btnModificaCli.setText(_translate("MainWindow", "Visualizza"))
        self.lbl_testo.setText(
            _translate("MainWindow", "<html><head/><body><p align=\"center\">Lista clienti</p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabCli), _translate("MainWindow", "Clienti"))
        self.btnAggPer.setText(_translate("MainWindow", "Aggiungi"))
        self.btnViewPer.setText(_translate("MainWindow", "Visualizza"))
        self.lbl_testo_2.setText(
            _translate("MainWindow", "<html><head/><body><p align=\"center\">Lista personale</p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabPer), _translate("MainWindow", "Personale"))
        self.btnAggAtt.setText(_translate("MainWindow", "Aggiungi"))
        self.btnRimuoviAtt.setText(_translate("MainWindow", "Rimuovi"))
        item = self.tableWidgetAtt.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Descrizione"))
        item = self.tableWidgetAtt.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Data acquisto"))
        item = self.tableWidgetAtt.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Quantità"))
        item = self.tableWidgetAtt.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Costo unitario"))
        item = self.tableWidgetAtt.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Data manutenzione"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabAtt), _translate("MainWindow", "Attrezzi"))
        self.pushButton_8.setText(_translate("MainWindow", "Elimina Messaggio"))
        self.pushButton_7.setText(_translate("MainWindow", "Scrivi Messaggio"))
        self.label.setText(
            _translate("MainWindow", "<html><head/><body><p align=\"center\">Casella dei messaggi</p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Bacheca"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = GUI_Admin()
    ui.setupUi(MainWindow, username="")
    MainWindow.show()
    sys.exit(app.exec_())

