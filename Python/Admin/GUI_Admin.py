from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QTableWidgetItem
from Python.Admin.gestione_cliente.aggiungi_cliente import aggiungi_cliente
from Python.Admin.gestione_cliente.gestionecliente import gestione_cliente
from Python.Admin.gestione_attrezzi.agg_attrezzo import agg_attrezzo
from Python.Admin.gestione_personale.agg_staff import agg_personale
from Python.Admin.gestione_personale.gestionestaff import gestione_staff
from Python.Data.MessageBox import messageBox
from Python.Data.casella_di_messaggi.Casella_di_messaggio import Casella_di_messaggio
from Python.Data.casella_di_messaggi.leggi_messaggio import lettura_messaggio
from Python.Model.Cliente import Cliente
from Python.Model.Attrezzo import Attrezzo
from Python.Model.Messaggio import Messaggio
from Python.Model.Personale import Personale


class GUI_Admin(object):
    username = ""
    objCliente = Cliente()
    objAttrezzo = Attrezzo()
    objStaff = Personale()
    messanger = Messaggio()
    msg = messageBox()
    lista_messaggi = []
    riga = 0

    def apriGesioneCliente(self):
        try:
            if self.lstClienti.currentItem().isSelected():
                nome = self.lstClienti.currentItem().text()
                self.window = QtWidgets.QMainWindow()
                self.ui = gestione_cliente(nome)
                self.ui.setupUi(self.window)
                self.window.show()
        except(Exception):
            self.msg.show_popup_exception("Seleziona un cliente!")

    def apriCasellaMessaggi(self):
        self.casella = QtWidgets.QMainWindow()
        self.ui = Casella_di_messaggio()
        self.ui.setupUi(self.casella, self.username)
        self.casella.show()

    def leggiMessaggio(self):

        self.lettura_messaggio = QtWidgets.QMainWindow()
        self.ui = lettura_messaggio()
        self.ui.setupUi(self.lettura_messaggio, self.messanger, self.username)
        self.lettura_messaggio.show()

    def visualizzaMessaggi(self):
        self.lstMessaggi.clear()
        self.lista_messaggi = self.messanger.getObject_message(self.username)
        self.lista_messaggi.sort(key=lambda x: x.data, reverse=True) # ordina la lista messaggi in ordine temporale
        for elem in self.lista_messaggi:
            if elem.mittente == self.username:
                self.lstMessaggi.addItem("messaggio inviato a: " + elem.destinatario + "  -  " + elem.data)
            elif elem.destinatario == self.username:
                self.lstMessaggi.addItem("messaggio da: " + elem.mittente + "  -  " + elem.data)

    def restituisciMessaggio(self):

        riga = self.lstMessaggi.currentRow()
        self.lista_messaggi = self.messanger.getObject_message(self.username)
        self.lista_messaggi.sort(key=lambda x: x.data, reverse=True)
        self.messanger = self.lista_messaggi[riga]
        self.leggiMessaggio()


    def eliminaMessaggio(self):
        try:
            objMessaggio = self.lista_messaggi[self.lstMessaggi.currentRow()]
            self.messanger.rimuovi_messaggio(objMessaggio)
            self.lstMessaggi.takeItem(self.lstMessaggi.currentRow())
            self.visualizzaMessaggi()
        except(Exception):
            self.msg.show_popup_exception("NON hai selezionato nessun messaggio")

    def apriGestioneStaff(self):
        try:
            if self.lstPersonale.currentItem().isSelected():
                nome = self.lstPersonale.currentItem().text()
                self.window = QtWidgets.QMainWindow()
                self.ui = gestione_staff(nome)
                self.ui.setupUi(self.window)
                self.window.show()
        except(Exception):
            self.msg.show_popup_exception("Seleziona un membro del personale!")

    def apriNuovaIscrizone(self):
        self.window_aggiungi_cliente = QtWidgets.QMainWindow()
        self.ui = aggiungi_cliente()
        self.ui.setupUi(self.window_aggiungi_cliente)
        self.window_aggiungi_cliente.show()

    def apriNuovaAssunzione(self):
        self.window_aggiungi_personale = QtWidgets.QMainWindow()
        self.ui = agg_personale()
        self.ui.setupUi(self.window_aggiungi_personale)
        self.window_aggiungi_personale.show()

    def apriAggiungiAttrezzo(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = agg_attrezzo()
        self.ui.setupUi(self.window)
        self.window.show()

    def rimuoviAttrezzo(self):

        try:
            if self.tblAttrezzi.currentItem().isSelected():
                objAttrezzo = Attrezzo()
                objAttrezzo.rimuovi(self.tblAttrezzi.currentRow())
                self.caricaAttrezzo()
        except(Exception):
                self.msg.show_popup_exception("Non hai selezionato nulla nella tabella")

    def caricaClienti(self):
        self.lstClienti.clear()
        objCliente = Cliente()
        lista_clienti = objCliente.popolaLista()
        if lista_clienti is not None:
            for x in lista_clienti:
                self.lstClienti.addItem(x)

    def caricaPersonale(self):
        self.lstPersonale.clear()
        objStaff = Personale()
        lista_personale = objStaff.popolaLista()
        if lista_personale is not None:
            for x in lista_personale:
                self.lstPersonale.addItem(x)

    def caricaAttrezzo(self):
        objAttrezzo = Attrezzo()
        lista_attrezzi = objAttrezzo.popolaLista()
        vettore = []
        if lista_attrezzi is not None:
            for x in lista_attrezzi:
                for j in x:
                    vettore.append(j)
        colonna = 0
        i = 0
        if self.riga != 0:
            temp = self.riga
            while temp != -1:
                self.tblAttrezzi.removeRow(temp)
                temp -=1
                self.riga = 0
        while len(vettore) > i + 1:
                self.tblAttrezzi.insertRow(self.riga)
                self.tblAttrezzi.setItem(self.riga, colonna, QTableWidgetItem(vettore[i]))
                self.tblAttrezzi.setItem(self.riga, colonna + 1, QTableWidgetItem(vettore[i + 1]))
                self.tblAttrezzi.setItem(self.riga, colonna + 2, QTableWidgetItem(vettore[i + 2]))
                self.tblAttrezzi.setItem(self.riga, colonna + 3, QTableWidgetItem(vettore[i + 3]))
                self.tblAttrezzi.setItem(self.riga, colonna + 4, QTableWidgetItem(vettore[i + 4]))
                self.riga += 1
                i += 5

    def aggiornaAttrezzo(self):
        self.objAttrezzo.recuperaSalvataggio("./Admin/gestione_attrezzi/listaAttrezzi.txt")
        self.caricaAttrezzo()

    def aggiornaCliente(self):
        self.objCliente.recuperaSalvataggio("./Admin/gestione_cliente/CredenzialiClienti.txt")
        self.caricaClienti()

    def aggiornaPersonale(self):
        self.objStaff.recuperaSalvataggio("./Admin/gestione_personale/CredenzialiStaff.txt")
        self.caricaPersonale()


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
        self.TabellaClienti = QtWidgets.QWidget()
        self.TabellaClienti.setObjectName("TabellaClienti")
        self.lstClienti = QtWidgets.QListWidget(self.TabellaClienti)
        self.lstClienti.setGeometry(QtCore.QRect(30, 70, 221, 381))
        self.lstClienti.setObjectName("lstClienti")
        self.btnAggiungiCliente = QtWidgets.QPushButton(self.TabellaClienti)
        self.btnAggiungiCliente.setGeometry(QtCore.QRect(280, 340, 101, 31))
        self.btnAggiungiCliente.setObjectName("btnAggiungiCliente")
        self.btnModificaCliente = QtWidgets.QPushButton(self.TabellaClienti)
        self.btnModificaCliente.setGeometry(QtCore.QRect(280, 400, 101, 31))
        self.btnModificaCliente.setObjectName("btnModificaCliente")
        self.btnAggiornaCliente = QtWidgets.QPushButton(self.TabellaClienti)
        self.btnAggiornaCliente.setGeometry(QtCore.QRect(210, 80, 31, 31))
        self.btnAggiornaCliente.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./Resources/images/aggiornamento.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnAggiornaCliente.setIcon(icon)
        self.btnAggiornaCliente.setIconSize(QtCore.QSize(50, 50))
        self.btnAggiornaCliente.setObjectName("btnAggiornaCliente")
        self.lblTitoloTabellaCliente = QtWidgets.QLabel(self.TabellaClienti)
        self.lblTitoloTabellaCliente.setGeometry(QtCore.QRect(30, 40, 231, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblTitoloTabellaCliente.setFont(font)
        self.lblTitoloTabellaCliente.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lblTitoloTabellaCliente.setObjectName("lblTitoloTabellaCliente")
        self.lblSfondoClienti = QtWidgets.QLabel(self.TabellaClienti)
        self.lblSfondoClienti.setGeometry(QtCore.QRect(0, 0, 731, 491))
        self.lblSfondoClienti.setText("")
        self.lblSfondoClienti.setPixmap(QtGui.QPixmap("./Resources/images/pngGUI_client/Sfondodecisivo.png"))
        self.lblSfondoClienti.setScaledContents(True)
        self.lblSfondoClienti.setObjectName("lblSfondoClienti")
        self.lblImmagineCliente = QtWidgets.QLabel(self.TabellaClienti)
        self.lblImmagineCliente.setGeometry(QtCore.QRect(350, 20, 341, 191))
        self.lblImmagineCliente.setText("")
        self.lblImmagineCliente.setPixmap(QtGui.QPixmap("./Resources/images/download (1).jpg"))
        self.lblImmagineCliente.setScaledContents(True)
        self.lblImmagineCliente.setObjectName("lblImmagineCliente")
        self.lblSfondoClienti.raise_()
        self.lstClienti.raise_()
        self.btnAggiungiCliente.raise_()
        self.btnModificaCliente.raise_()
        self.btnAggiornaCliente.raise_()
        self.lblTitoloTabellaCliente.raise_()
        self.lblImmagineCliente.raise_()
        self.tabWidget.addTab(self.TabellaClienti, "")
        self.TabellaPersonale = QtWidgets.QWidget()
        self.TabellaPersonale.setObjectName("tabPer")
        self.lstPersonale = QtWidgets.QListWidget(self.TabellaPersonale)
        self.lstPersonale.setGeometry(QtCore.QRect(30, 70, 221, 381))
        self.lstPersonale.setObjectName("lstPersonale")
        self.btnAggiornaPersonale = QtWidgets.QPushButton(self.TabellaPersonale)
        self.btnAggiornaPersonale.setGeometry(QtCore.QRect(280, 340, 101, 31))
        self.btnAggiornaPersonale.setObjectName("btnAggiornaPersonale")
        self.btnVisualizzaPersonale = QtWidgets.QPushButton(self.TabellaPersonale)
        self.btnVisualizzaPersonale.setGeometry(QtCore.QRect(280, 400, 101, 31))
        self.btnVisualizzaPersonale.setObjectName("btnVisualizzaPersonale")
        self.lblTitoloTabellaPersonale = QtWidgets.QLabel(self.TabellaPersonale)
        self.lblTitoloTabellaPersonale.setGeometry(QtCore.QRect(40, 40, 211, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblTitoloTabellaPersonale.setFont(font)
        self.lblTitoloTabellaPersonale.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lblTitoloTabellaPersonale.setObjectName("lblTitoloTabellaPersonale")
        self.btnAggiornaPersonale = QtWidgets.QPushButton(self.TabellaPersonale)
        self.btnAggiornaPersonale.setGeometry(QtCore.QRect(210, 80, 31, 31))
        self.btnAggiornaPersonale.setText("")
        self.btnAggiornaPersonale.setIcon(icon)
        self.btnAggiornaPersonale.setIconSize(QtCore.QSize(50, 50))
        self.btnAggiornaPersonale.setObjectName("btnAggiornaPersonale")
        self.lblSfondoPersonale = QtWidgets.QLabel(self.TabellaPersonale)
        self.lblSfondoPersonale.setGeometry(QtCore.QRect(0, 0, 731, 491))
        self.lblSfondoPersonale.setText("")
        self.lblSfondoPersonale.setPixmap(QtGui.QPixmap("./Resources/images/pngGUI_client/Sfondodecisivo.png"))
        self.lblSfondoPersonale.setScaledContents(True)
        self.lblSfondoPersonale.setObjectName("lblSfondoPersonale")
        self.lblImmaginePersonale = QtWidgets.QLabel(self.TabellaPersonale)
        self.lblImmaginePersonale.setGeometry(QtCore.QRect(350, 20, 341, 191))
        self.lblImmaginePersonale.setText("")
        self.lblImmaginePersonale.setPixmap(QtGui.QPixmap("./Resources/images/download (1).jpg"))
        self.lblImmaginePersonale.setScaledContents(True)
        self.lblImmaginePersonale.setObjectName("lblImmaginePersonale")
        self.lblSfondoPersonale.raise_()
        self.lstPersonale.raise_()
        self.btnAggiornaPersonale.raise_()
        self.btnVisualizzaPersonale.raise_()
        self.lblTitoloTabellaPersonale.raise_()
        self.btnAggiornaPersonale.raise_()
        self.lblImmaginePersonale.raise_()
        self.tabWidget.addTab(self.TabellaPersonale, "")
        self.TabellaAttrezzi = QtWidgets.QWidget()
        self.TabellaAttrezzi.setObjectName("TabellaAttrezzi")
        self.btnAggiornaAttrezzi = QtWidgets.QPushButton(self.TabellaAttrezzi)
        self.btnAggiornaAttrezzi.setGeometry(QtCore.QRect(390, 360, 91, 31))
        self.btnAggiornaAttrezzi.setObjectName("btnAggiornaAttrezzi")
        self.btnRimuoviAttrezzi = QtWidgets.QPushButton(self.TabellaAttrezzi)
        self.btnRimuoviAttrezzi.setGeometry(QtCore.QRect(240, 360, 91, 31))
        self.btnRimuoviAttrezzi.setObjectName("btnRimuoviAttrezzi")
        self.lblSfondoAttrezzi = QtWidgets.QLabel(self.TabellaAttrezzi)
        self.lblSfondoAttrezzi.setGeometry(QtCore.QRect(0, 0, 731, 491))
        self.lblSfondoAttrezzi.setText("")
        self.lblSfondoAttrezzi.setPixmap(QtGui.QPixmap("./Resources/images/pngGUI_client/Sfondodecisivo.png"))
        self.lblSfondoAttrezzi.setScaledContents(True)
        self.lblSfondoAttrezzi.setObjectName("lblSfondoAttrezzi")
        self.tblAttrezzi = QtWidgets.QTableWidget(self.TabellaAttrezzi)
        self.tblAttrezzi.setGeometry(QtCore.QRect(10, 80, 691, 261))
        self.tblAttrezzi.setObjectName("tblAttrezzi")
        self.tblAttrezzi.setColumnCount(5)
        self.tblAttrezzi.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tblAttrezzi.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblAttrezzi.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblAttrezzi.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblAttrezzi.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblAttrezzi.setHorizontalHeaderItem(4, item)
        self.btnAggiornaAttrezzi = QtWidgets.QPushButton(self.TabellaAttrezzi)
        self.btnAggiornaAttrezzi.setGeometry(QtCore.QRect(660, 90, 31, 31))
        self.btnAggiornaAttrezzi.setText("")
        self.btnAggiornaAttrezzi.setIcon(icon)
        self.btnAggiornaAttrezzi.setIconSize(QtCore.QSize(50, 50))
        self.btnAggiornaAttrezzi.setObjectName("btnAggiornaAttrezzi")
        self.lblSfondoAttrezzi.raise_()
        self.btnAggiornaAttrezzi.raise_()
        self.btnRimuoviAttrezzi.raise_()
        self.tblAttrezzi.raise_()
        self.btnAggiornaAttrezzi.raise_()
        self.tabWidget.addTab(self.TabellaAttrezzi, "")
        self.TabellaMessaggi = QtWidgets.QWidget()
        self.TabellaMessaggi.setObjectName("TabellaMessaggi")
        self.btnEliminaMessaggio = QtWidgets.QPushButton(self.TabellaMessaggi)
        self.btnEliminaMessaggio.setGeometry(QtCore.QRect(510, 220, 141, 28))
        self.btnEliminaMessaggio.setObjectName("btnEliminaMessaggio")
        self.btnScriviMessaggio = QtWidgets.QPushButton(self.TabellaMessaggi)
        self.btnScriviMessaggio.setGeometry(QtCore.QRect(510, 170, 141, 28))
        self.btnScriviMessaggio.setObjectName("btnScriviMessaggio")
        self.lstMessaggi = QtWidgets.QListWidget(self.TabellaMessaggi)
        self.lstMessaggi.setGeometry(QtCore.QRect(50, 110, 441, 251))
        self.lstMessaggi.setObjectName("lstMessaggi")
        self.lblTitoloMessaggi = QtWidgets.QLabel(self.TabellaMessaggi)
        self.lblTitoloMessaggi.setGeometry(QtCore.QRect(60, 30, 421, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lblTitoloMessaggi.setFont(font)
        self.lblTitoloMessaggi.setObjectName("label")
        self.lblSfondoMessaggi = QtWidgets.QLabel(self.TabellaMessaggi)
        self.lblSfondoMessaggi.setGeometry(QtCore.QRect(0, 0, 731, 491))
        self.lblSfondoMessaggi.setText("")
        self.lblSfondoMessaggi.setPixmap(QtGui.QPixmap("./Resources/images/pngGUI_client/Sfondodecisivo.png"))
        self.lblSfondoMessaggi.setScaledContents(True)
        self.lblSfondoMessaggi.setObjectName("label_5")
        self.btnAggiornaMessaggi = QtWidgets.QPushButton(self.TabellaMessaggi)
        self.btnAggiornaMessaggi.setGeometry(QtCore.QRect(450, 120, 31, 31))
        self.btnAggiornaMessaggi.setText("")
        self.btnAggiornaMessaggi.setIcon(icon)
        self.btnAggiornaMessaggi.setIconSize(QtCore.QSize(50, 50))
        self.btnAggiornaMessaggi.setObjectName("btnAggiornaMessaggi")
        self.lblSfondoMessaggi.raise_()
        self.btnEliminaMessaggio.raise_()
        self.btnScriviMessaggio.raise_()
        self.lstMessaggi.raise_()
        self.lblTitoloMessaggi.raise_()
        self.btnAggiornaMessaggi.raise_()
        self.tabWidget.addTab(self.TabellaMessaggi, "")
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
        self.objCliente.recuperaSalvataggio("./Admin/gestione_cliente/CredenzialiClienti.txt")
        self.objAttrezzo.recuperaSalvataggio("./Admin/gestione_attrezzi/listaAttrezzi.txt")
        self.objStaff.recuperaSalvataggio("./Admin/gestione_personale/CredenzialiStaff.txt")
        self.messanger.recuperaSalvataggio("./Data/casella_di_messaggi/messaggi.txt")
        self.visualizzaMessaggi()
        self.caricaAttrezzo()
        self.caricaClienti()
        self.caricaPersonale()
        self.btnRimuoviAttrezzi.clicked.connect(self.rimuoviAttrezzo)
        self.btnAggiungiCliente.clicked.connect(self.apriNuovaIscrizone)
        self.btnAggiornaPersonale.clicked.connect(self.apriNuovaAssunzione)
        self.btnAggiornaAttrezzi.clicked.connect(self.apriAggiungiAttrezzo)
        self.btnAggiornaPersonale.clicked.connect(self.caricaPersonale)
        self.btnModificaCliente.clicked.connect(self.apriGesioneCliente)
        self.btnVisualizzaPersonale.clicked.connect(self.apriGestioneStaff)
        self.lstMessaggi.doubleClicked.connect(self.restituisciMessaggio)
        self.btnScriviMessaggio.clicked.connect(self.apriCasellaMessaggi)
        self.btnEliminaMessaggio.clicked.connect(self.eliminaMessaggio)
        self.btnAggiornaCliente.clicked.connect(self.aggiornaCliente)
        self.btnAggiornaPersonale.clicked.connect(self.aggiornaPersonale)
        self.btnAggiornaAttrezzi.clicked.connect(self.aggiornaAttrezzo)
        self.btnAggiornaMessaggi.clicked.connect(self.visualizzaMessaggi)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Interfaccia admin"))
        self.btnAggiungiCliente.setText(_translate("MainWindow", "Aggiungi"))
        self.btnModificaCliente.setText(_translate("MainWindow", "Visualizza"))
        self.lblTitoloTabellaCliente.setText(
            _translate("MainWindow", "<html><head/><body><p align=\"center\">Lista clienti</p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.TabellaClienti), _translate("MainWindow", "Clienti"))
        self.btnAggiornaPersonale.setText(_translate("MainWindow", "Aggiungi"))
        self.btnVisualizzaPersonale.setText(_translate("MainWindow", "Visualizza"))
        self.lblTitoloTabellaPersonale.setText(
            _translate("MainWindow", "<html><head/><body><p align=\"center\">Lista personale</p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.TabellaPersonale), _translate("MainWindow", "Personale"))
        self.btnAggiornaAttrezzi.setText(_translate("MainWindow", "Aggiungi"))
        self.btnRimuoviAttrezzi.setText(_translate("MainWindow", "Rimuovi"))
        item = self.tblAttrezzi.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Descrizione"))
        item = self.tblAttrezzi.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Data acquisto"))
        item = self.tblAttrezzi.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Quantità"))
        item = self.tblAttrezzi.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Costo unitario"))
        item = self.tblAttrezzi.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Data manutenzione"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.TabellaAttrezzi), _translate("MainWindow", "Attrezzi"))
        self.btnEliminaMessaggio.setText(_translate("MainWindow", "Elimina Messaggio"))
        self.btnScriviMessaggio.setText(_translate("MainWindow", "Scrivi Messaggio"))
        self.lblTitoloMessaggi.setText(
            _translate("MainWindow", "<html><head/><body><p align=\"center\">Casella dei messaggi</p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.TabellaMessaggi), _translate("MainWindow", "Bacheca"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = GUI_Admin()
    ui.setupUi(MainWindow, username="")
    MainWindow.show()
    sys.exit(app.exec_())

