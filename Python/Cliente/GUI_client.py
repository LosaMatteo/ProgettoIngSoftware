import os
from os import listdir
from os.path import isfile, join
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDate
from Python.Cliente.Allenamento.scheda_allenamento import scheda_allenamento
from Python.Cliente.Dieta.dieta_cliente import dieta_cliente
from Python.Cliente.Prenotazioni.gestionePrenotazioni import GestionePrenotazioniCorsi
from Python.Data.MessageBox import messageBox
from Python.Data.casella_di_messaggi.Casella_di_messaggio import Casella_di_messaggio
from Python.Data.casella_di_messaggi.leggi_messaggio import lettura_messaggio
from Python.Data.interface_password import change_password
from Python.Cliente.Allenamento.Allenamenti import allenamento
from Python.Cliente.Prenotazioni.Prenotazioni1 import prenotazioni
from Python.Model.Cliente import Cliente
from Python.Model.Messaggio import Messaggio


class GUI_client(object):
    username = ""
    messanger = Messaggio()
    lista_files_utente = []
    objGestionePrenotazioneCorsi = GestionePrenotazioniCorsi()
    lista_messaggi = []
    messaggio = messageBox()
    lista_prenotazioni = []
    percorsi = {"./Cliente/Prenotazioni/file_prenotazioni/salaPesi/": "Sala Pesi",
                "./Cliente/Prenotazioni/file_prenotazioni/zumba/": "Zumba",
                "./Cliente/Prenotazioni/file_prenotazioni/functional/": "Functional"}

    def aggiungiPrenotazione(self):
        self.lista_prenotazioni.clear()
        self.listWidget_4.clear()
        for path in self.percorsi.keys():
            vettore = self.objGestionePrenotazioneCorsi.trovaCliente(path, self.username)
            for elem in vettore:
                self.lista_prenotazioni.append(path + "+" + elem)
                elem = elem[:-4]
                orario = elem[11:]
                data = elem[:10]
                self.listWidget_4.addItem("data: " + data + " orario: " + orario + " " + self.percorsi[path])
            vettore.clear()

    def apriDietaCliente(self):
        self.dieta_cliente = QtWidgets.QMainWindow()
        self.ui = dieta_cliente()
        self.ui.setupUi(self.dieta_cliente,self.username)
        self.dieta_cliente.show()

    def apriCasellaMessaggio(self):
        self.casella = QtWidgets.QMainWindow()
        self.ui = Casella_di_messaggio()
        self.ui.setupUi(self.casella, self.username)
        self.casella.show()

    def apriLetturaMessaggio(self):
        self.lettura_messaggio = QtWidgets.QMainWindow()
        self.ui = lettura_messaggio()
        self.ui.setupUi(self.lettura_messaggio, self.messanger, self.username)
        self.lettura_messaggio.show()

    def visualizzaMessaggi(self):
        self.listWidget_5.clear()
        self.lista_messaggi = self.messanger.getObject_message(self.username)
        self.lista_messaggi.sort(key=lambda x: x.data, reverse=True)  # ordina la lista messaggi in ordine temporale
        for elem in self.lista_messaggi:
            if elem.mittente == self.username:
                self.listWidget_5.addItem("messaggio inviato a: " + elem.destinatario + "  -  " + elem.data)
            elif elem.destinatario == self.username:
                self.listWidget_5.addItem("messaggio da: " + elem.mittente + "  -  " + elem.data)

    def restituisciMessaggio(self):
        riga = self.listWidget_5.currentRow()
        self.lista_messaggi = self.messanger.getObject_message(self.username)
        self.lista_messaggi.sort(key=lambda x: x.data, reverse=True)  # ordina la lista messaggi in ordine temporale
        self.messanger = self.lista_messaggi[riga]
        self.apriLetturaMessaggio()

    def eliminaMessaggio(self):

        try:
            objMessaggio = self.lista_messaggi[self.listWidget_5.currentRow()]
            self.messanger.rimuovi_messaggio(objMessaggio)
            self.listWidget_5.takeItem(self.listWidget_5.currentRow())
        except(Exception):
            self.messaggio.show_popup_exception("ERRORE")

    def apriFinestraAllenamento(self):
        self.allenamento = QtWidgets.QMainWindow()
        self.ui = allenamento()
        self.ui.setupUi(self.allenamento, self.username)
        self.allenamento.show()

    def apriPrenotazioni(self):
        self.password = QtWidgets.QMainWindow()
        self.ui = prenotazioni()
        self.ui.setupUi(self.password, self.username)
        self.password.show()

    def apriCambioPassword(self):
        self.password = QtWidgets.QMainWindow()
        self.ui = change_password()
        self.ui.setupUi(self.password, self.username)
        self.password.show()

    def scriviSuLista(self):
        for elem in self.lista_files_utente:
            nome2 = elem.split(".")
            nome2.pop()
            nome1 = ""
            for elems in nome2:
                nome1 += elems + " "
            temp = nome1.replace("_", " ")
            vett = temp.split(" ")
            vett.remove(vett[0])
            str = ""
            for elem in vett:
                str += elem + " "
            self.listWidget_3.addItem(str)

    def apriFileDieta(self):
        percorso = "./Cliente/Dieta/file_dieta"
        lista_files = [f for f in listdir(percorso) if isfile(join(percorso, f))]
        for elem in lista_files:
            if elem.startswith(self.username + "_dieta_personale_"):
                self.lista_files_utente.append(elem)
        self.scriviSuLista()

    def apri(self):
        file = self.lista_files_utente[self.listWidget_3.currentRow()]
        os.chdir("./Cliente/Dieta/file_dieta")
        os.system(file)
        os.chdir("..")
        os.chdir("..")
        os.chdir("..")

    def visualizza(self):
        self.mostra()
        self.messaggio = messageBox()
        data_odierna = QDate.currentDate()
        objCliente = Cliente()
        objCliente = objCliente.getObject(self.username)
        self.txt_nome.setText(objCliente.name)
        self.txt_cognome.setText(objCliente.surname)
        self.txt_username.setText(self.username)
        self.txt_password.setText(objCliente.password)
        self.txt_codice_fiscale.setText(objCliente.codice_fiscale)
        self.txt_luogo_nascita.setText(objCliente.luogo_nascita)
        self.txt_data_nascita.setText(objCliente.data_nascita.toString())
        self.dtdScadenzaCertMedico.setDate(objCliente.gestAll.data_iscrizione)
        if objCliente.gestAll.tipo_di_abbonamento.__contains__("mensile"):
            self.dtdScadenzaCertMedico_2.setDate(self.dtdScadenzaCertMedico.date().addMonths(1))
            if data_odierna > self.dtdScadenzaCertMedico_2.date():
                self.messaggio.show_popup_ok("abbonamento scaduto,si prega di rinnovarlo")
        elif objCliente.gestAll.tipo_di_abbonamento.__contains__("annuale"):
            self.dtdScadenzaCertMedico_2.setDate(self.dtdScadenzaCertMedico.date().addYears(1))
            if data_odierna > self.dtdScadenzaCertMedico_2.date():
                self.messaggio.show_popup_ok("abbonamento scaduto,si prega di rinnovarlo")
        self.dtdScadenzaCertMedico_3.setDate(objCliente.gestAll.data_certificato_medico)



    def apriSchedaAllenamento(self):
        self.scheda_allenamento = QtWidgets.QMainWindow()
        self.ui = scheda_allenamento()
        self.ui.setupUi(self.scheda_allenamento,self.username)
        self.scheda_allenamento.show()

    def nascondi(self):
        self.listWidget_2.hide()
        self.txt_nome.hide()
        self.txt_cognome.hide()
        self.txt_username.hide()
        self.txt_password.hide()
        self.txt_codice_fiscale.hide()
        self.txt_luogo_nascita.hide()
        self.txt_data_nascita.hide()
        self.dtdScadenzaCertMedico.hide()
        self.dtdScadenzaCertMedico_2.hide()
        self.dtdScadenzaCertMedico_3.hide()
        self.lbl_nome.hide()
        self.lbl_cognome.hide()
        self.lbl_username.hide()
        self.lbl_password.hide()
        self.lbl_codice_fiscale.hide()
        self.lbl_luogo_nascita.hide()
        self.lbl_data_nascita.hide()
        self.lbl_data_iscrizione.hide()
        self.lbl_data_fine_abbonamento.hide()
        self.lbl_data_certificato_medico.hide()
        self.pushButton_7.hide()

    def mostra(self):
        self.listWidget_2.show()
        self.txt_nome.show()
        self.txt_cognome.show()
        self.txt_username.show()
        self.txt_password.show()
        self.txt_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txt_codice_fiscale.show()
        self.txt_luogo_nascita.show()
        self.txt_data_nascita.show()
        self.dtdScadenzaCertMedico.show()
        self.dtdScadenzaCertMedico_2.show()
        self.dtdScadenzaCertMedico_3.show()
        self.lbl_nome.show()
        self.lbl_cognome.show()
        self.lbl_username.show()
        self.lbl_password.show()
        self.lbl_codice_fiscale.show()
        self.lbl_luogo_nascita.show()
        self.lbl_data_nascita.show()
        self.lbl_data_iscrizione.show()
        self.lbl_data_fine_abbonamento.show()
        self.lbl_data_certificato_medico.show()
        self.pushButton_7.show()

    def mostraPassword(self):
         self.txt_password.setEchoMode(QtWidgets.QLineEdit.Normal)

    def nascondiPassword(self):
        self.txt_password.setEchoMode(QtWidgets.QLineEdit.Password)

    def inserisciSuLista(self):
        objCLiente = Cliente()
        objCLiente = objCLiente.getObject(self.username)
        path = "Staff/Allenamento_staff/file_scheda_allenamento"
        lista_files = [f for f in listdir(path) if isfile(join(path, f))]
        for elem in lista_files:
            if objCLiente.name + " " + objCLiente.surname + ".txt" == elem:
                self.listWidget.addItem(elem)

    def annullaPrenotazione(self):
        try:
            if self.listWidget_4.currentItem().isSelected():
                da_annullare = self.lista_prenotazioni[self.listWidget_4.currentIndex().row()]
                percorso = da_annullare.split("+")
                self.objGestionePrenotazioneCorsi.annullaPrenotazione(self.username, percorso[0], percorso[1])
                self.listWidget_4.clear()
                self.aggiungiPrenotazione()
        except(AttributeError):
            self.messaggio.show_popup_exception("Non hai selezionato nulla dalla lista")
        except(Exception):
            self.messaggio.show_popup_exception("ERRORE")

    def setupUi(self, Form,username):
        self.username = username
        Form.setObjectName("Form")
        Form.resize(597, 647)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 10, 141, 31))
        font = QtGui.QFont()
        font.setBold(False)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(170, 10, 151, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.toolBox = QtWidgets.QToolBox(Form)
        self.toolBox.setGeometry(QtCore.QRect(30, 50, 471, 551))
        self.toolBox.setObjectName("toolBox")
        self.page = QtWidgets.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 471, 401))
        self.page.setObjectName("page")
        self.label_10 = QtWidgets.QLabel(self.page)
        self.label_10.setGeometry(QtCore.QRect(-1, 0, 461, 391))
        self.label_10.setText("")
        self.label_10.setPixmap(QtGui.QPixmap("./Resources/images/pngGUI_client/Sfondodecisivo.png"))
        self.label_10.setScaledContents(True)
        self.label_10.setObjectName("label_10")
        self.btnPassword = QtWidgets.QPushButton(self.page)
        self.btnPassword.setGeometry(QtCore.QRect(330, 290, 121, 24))
        self.btnPassword.setObjectName("btnPassword")
        self.pushButton_4 = QtWidgets.QPushButton(self.page)
        self.pushButton_4.setGeometry(QtCore.QRect(330, 270, 121, 21))
        self.pushButton_4.setObjectName("pushButton_4")
        self.listWidget_2 = QtWidgets.QListWidget(self.page)
        self.listWidget_2.setGeometry(QtCore.QRect(20, 20, 281, 361))
        self.listWidget_2.setObjectName("listWidget_2")
        self.txt_password = QtWidgets.QLineEdit(self.page)
        self.txt_password.setGeometry(QtCore.QRect(170, 140, 113, 22))
        self.txt_password.setText("")
        self.txt_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txt_password.setReadOnly(True)
        self.txt_password.setObjectName("txt_password")
        self.dtdScadenzaCertMedico = QtWidgets.QDateEdit(self.page)
        self.dtdScadenzaCertMedico.setGeometry(QtCore.QRect(170, 260, 111, 22))
        self.dtdScadenzaCertMedico.setReadOnly(True)
        self.dtdScadenzaCertMedico.setCalendarPopup(True)
        self.dtdScadenzaCertMedico.setObjectName("dtdScadenzaCertMedico")
        self.txt_luogo_nascita = QtWidgets.QLineEdit(self.page)
        self.txt_luogo_nascita.setGeometry(QtCore.QRect(170, 200, 113, 22))
        self.txt_luogo_nascita.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.txt_luogo_nascita.setReadOnly(True)
        self.txt_luogo_nascita.setObjectName("txt_luogo_nascita")
        self.lbl_data_iscrizione = QtWidgets.QLabel(self.page)
        self.lbl_data_iscrizione.setGeometry(QtCore.QRect(40, 260, 111, 21))
        self.lbl_data_iscrizione.setObjectName("lbl_data_iscrizione")
        self.dtdScadenzaCertMedico_3 = QtWidgets.QDateEdit(self.page)
        self.dtdScadenzaCertMedico_3.setGeometry(QtCore.QRect(170, 320, 111, 22))
        self.dtdScadenzaCertMedico_3.setReadOnly(True)
        self.dtdScadenzaCertMedico_3.setCalendarPopup(True)
        self.dtdScadenzaCertMedico_3.setObjectName("dtdScadenzaCertMedico_3")
        self.lbl_luogo_nascita = QtWidgets.QLabel(self.page)
        self.lbl_luogo_nascita.setGeometry(QtCore.QRect(40, 200, 111, 21))
        self.lbl_luogo_nascita.setObjectName("lbl_luogo_nascita")
        self.lbl_nome = QtWidgets.QLabel(self.page)
        self.lbl_nome.setGeometry(QtCore.QRect(40, 50, 111, 21))
        self.lbl_nome.setObjectName("lbl_nome")
        self.txt_nome = QtWidgets.QLineEdit(self.page)
        self.txt_nome.setGeometry(QtCore.QRect(170, 50, 113, 22))
        self.txt_nome.setReadOnly(True)
        self.txt_nome.setObjectName("txt_nome")
        self.lbl_data_fine_abbonamento = QtWidgets.QLabel(self.page)
        self.lbl_data_fine_abbonamento.setGeometry(QtCore.QRect(30, 290, 141, 21))
        self.lbl_data_fine_abbonamento.setObjectName("lbl_data_fine_abbonamento")
        self.lbl_data_certificato_medico = QtWidgets.QLabel(self.page)
        self.lbl_data_certificato_medico.setGeometry(QtCore.QRect(30, 320, 131, 21))
        self.lbl_data_certificato_medico.setObjectName("lbl_data_certificato_medico")
        self.txt_data_nascita = QtWidgets.QLineEdit(self.page)
        self.txt_data_nascita.setGeometry(QtCore.QRect(170, 230, 113, 22))
        self.txt_data_nascita.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.txt_data_nascita.setReadOnly(True)
        self.txt_data_nascita.setObjectName("txt_data_nascita")
        self.lbl_codice_fiscale = QtWidgets.QLabel(self.page)
        self.lbl_codice_fiscale.setGeometry(QtCore.QRect(40, 170, 111, 21))
        self.lbl_codice_fiscale.setObjectName("lbl_codice_fiscale")
        self.lbl_data_nascita = QtWidgets.QLabel(self.page)
        self.lbl_data_nascita.setGeometry(QtCore.QRect(40, 230, 111, 21))
        self.lbl_data_nascita.setObjectName("lbl_data_nascita")
        self.txt_codice_fiscale = QtWidgets.QLineEdit(self.page)
        self.txt_codice_fiscale.setGeometry(QtCore.QRect(170, 170, 113, 22))
        self.txt_codice_fiscale.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.txt_codice_fiscale.setReadOnly(True)
        self.txt_codice_fiscale.setObjectName("txt_codice_fiscale")
        self.lbl_username = QtWidgets.QLabel(self.page)
        self.lbl_username.setGeometry(QtCore.QRect(40, 110, 111, 21))
        self.lbl_username.setObjectName("lbl_username")
        self.txt_username = QtWidgets.QLineEdit(self.page)
        self.txt_username.setGeometry(QtCore.QRect(170, 110, 113, 22))
        self.txt_username.setReadOnly(True)
        self.txt_username.setObjectName("txt_username")
        self.txt_cognome = QtWidgets.QLineEdit(self.page)
        self.txt_cognome.setGeometry(QtCore.QRect(170, 80, 113, 22))
        self.txt_cognome.setReadOnly(True)
        self.txt_cognome.setObjectName("txt_cognome")
        self.lbl_password = QtWidgets.QLabel(self.page)
        self.lbl_password.setGeometry(QtCore.QRect(40, 140, 111, 21))
        self.lbl_password.setObjectName("lbl_password")
        self.lbl_cognome = QtWidgets.QLabel(self.page)
        self.lbl_cognome.setGeometry(QtCore.QRect(40, 80, 111, 21))
        self.lbl_cognome.setObjectName("lbl_cognome")
        self.dtdScadenzaCertMedico_2 = QtWidgets.QDateEdit(self.page)
        self.dtdScadenzaCertMedico_2.setGeometry(QtCore.QRect(170, 290, 111, 22))
        self.dtdScadenzaCertMedico_2.setReadOnly(True)
        self.dtdScadenzaCertMedico_2.setCalendarPopup(True)
        self.dtdScadenzaCertMedico_2.setObjectName("dtdScadenzaCertMedico_2")
        self.pushButton_7 = QtWidgets.QPushButton(self.page)
        self.pushButton_7.setGeometry(QtCore.QRect(260, 141, 21, 20))
        self.pushButton_7.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./Resources/images/download.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_7.setIcon(icon)
        self.pushButton_7.setObjectName("pushButton_7")
        self.toolBox.addItem(self.page, "")
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setGeometry(QtCore.QRect(0, 0, 471, 401))
        self.page_2.setObjectName("page_2")
        self.label_3 = QtWidgets.QLabel(self.page_2)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 171, 31))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.page_2)
        self.label_4.setGeometry(QtCore.QRect(10, 290, 240, 31))
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(self.page_2)
        self.pushButton.setGeometry(QtCore.QRect(260, 290, 113, 31))
        self.pushButton.setObjectName("pushButton")
        self.label_11 = QtWidgets.QLabel(self.page_2)
        self.label_11.setGeometry(QtCore.QRect(-1, 0, 451, 351))
        self.label_11.setText("")
        self.label_11.setPixmap(QtGui.QPixmap("./Resources/images/pngGUI_client/Sfondodecisivo.png"))
        self.label_11.setScaledContents(True)
        self.label_11.setObjectName("label_11")
        self.listWidget = QtWidgets.QListWidget(self.page_2)
        self.listWidget.setGeometry(QtCore.QRect(30, 50, 411, 192))
        self.listWidget.setObjectName("listWidget")
        self.label_11.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.pushButton.raise_()
        self.listWidget.raise_()
        self.toolBox.addItem(self.page_2, "")
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setGeometry(QtCore.QRect(0, 0, 98, 28))
        self.page_3.setObjectName("page_3")
        self.label_5 = QtWidgets.QLabel(self.page_3)
        self.label_5.setGeometry(QtCore.QRect(0, 0, 91, 21))
        self.label_5.setObjectName("label_5")
        self.pushButton_2 = QtWidgets.QPushButton(self.page_3)
        self.pushButton_2.setGeometry(QtCore.QRect(340, 290, 113, 32))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_6 = QtWidgets.QLabel(self.page_3)
        self.label_6.setGeometry(QtCore.QRect(10, 290, 330, 31))
        self.label_6.setObjectName("label_6")
        self.label_12 = QtWidgets.QLabel(self.page_3)
        self.label_12.setGeometry(QtCore.QRect(-1, 0, 471, 401))
        self.label_12.setText("")
        self.label_12.setPixmap(QtGui.QPixmap("./Resources/images/pngGUI_client/Sfondoverde.png"))
        self.label_12.setScaledContents(True)
        self.label_12.setObjectName("label_12")
        self.listWidget_3 = QtWidgets.QListWidget(self.page_3)
        self.listWidget_3.setGeometry(QtCore.QRect(20, 30, 271, 211))
        self.listWidget_3.setObjectName("listWidget_3")
        self.label_12.raise_()
        self.label_5.raise_()
        self.pushButton_2.raise_()
        self.label_6.raise_()
        self.listWidget_3.raise_()
        self.toolBox.addItem(self.page_3, "")
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setGeometry(QtCore.QRect(0, 0, 471, 401))
        self.page_4.setObjectName("page_4")
        self.label_7 = QtWidgets.QLabel(self.page_4)
        self.label_7.setGeometry(QtCore.QRect(10, 0, 131, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.page_4)
        self.label_8.setGeometry(QtCore.QRect(20, 270, 91, 31))
        self.label_8.setObjectName("label_8")
        self.pushButton_3 = QtWidgets.QPushButton(self.page_4)
        self.pushButton_3.setGeometry(QtCore.QRect(160, 270, 113, 32))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_13 = QtWidgets.QLabel(self.page_4)
        self.label_13.setGeometry(QtCore.QRect(0, 0, 471, 391))
        self.label_13.setText("")
        self.label_13.setPixmap(QtGui.QPixmap("./Resources/images/pngGUI_client/Sfoidnigiallo.png"))
        self.label_13.setScaledContents(True)
        self.label_13.setObjectName("label_13")
        self.listWidget_4 = QtWidgets.QListWidget(self.page_4)
        self.listWidget_4.setGeometry(QtCore.QRect(20, 30, 381, 211))
        self.listWidget_4.setAutoScroll(True)
        self.listWidget_4.setObjectName("listWidget_4")
        self.pushButton_8 = QtWidgets.QPushButton(self.page_4)
        self.pushButton_8.setGeometry(QtCore.QRect(350, 40, 31, 21))
        self.pushButton_8.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("./Resources/images/cancella.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_8.setIcon(icon1)
        self.pushButton_8.setIconSize(QtCore.QSize(30, 200))
        self.pushButton_8.setObjectName("pushButton_8")
        self.btn_aggiorna = QtWidgets.QPushButton(self.page_4)
        self.btn_aggiorna.setGeometry(QtCore.QRect(410, 30, 31, 31))
        self.btn_aggiorna.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("./Resources/images/aggiornamento.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_aggiorna.setIcon(icon2)
        self.btn_aggiorna.setIconSize(QtCore.QSize(50, 50))
        self.btn_aggiorna.setObjectName("btn_aggiorna")
        self.label_13.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.pushButton_3.raise_()
        self.listWidget_4.raise_()
        self.btn_aggiorna.raise_()
        self.pushButton_8.raise_()
        self.toolBox.addItem(self.page_4, "")
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setGeometry(QtCore.QRect(0, 0, 471, 401))
        self.page_5.setObjectName("page_5")
        self.label_9 = QtWidgets.QLabel(self.page_5)
        self.label_9.setGeometry(QtCore.QRect(50, 10, 191, 61))
        self.label_9.setObjectName("label_9")
        self.label_14 = QtWidgets.QLabel(self.page_5)
        self.label_14.setGeometry(QtCore.QRect(-1, 10, 471, 401))
        self.label_14.setText("")
        self.label_14.setPixmap(QtGui.QPixmap("./Resources/images/pngGUI_client/Sfondo1.png"))
        self.label_14.setObjectName("label_14")
        self.listWidget_5 = QtWidgets.QListWidget(self.page_5)
        self.listWidget_5.setGeometry(QtCore.QRect(20, 70, 300, 321))
        self.listWidget_5.setObjectName("listWidget_5")
        self.pushButton_5 = QtWidgets.QPushButton(self.page_5)
        self.pushButton_5.setGeometry(QtCore.QRect(325, 160, 141, 28))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.page_5)
        self.pushButton_6.setGeometry(QtCore.QRect(325, 200, 141, 28))
        self.pushButton_6.setObjectName("pushButton_6")
        self.btnAggiornaMex = QtWidgets.QPushButton(self.page_5)
        self.btnAggiornaMex.setGeometry(QtCore.QRect(330, 70, 31, 31))
        self.btnAggiornaMex.setText("")
        self.btnAggiornaMex.setIcon(icon2)
        self.btnAggiornaMex.setIconSize(QtCore.QSize(50, 50))
        self.btnAggiornaMex.setObjectName("btnAggiornaMex")
        self.label_14.raise_()
        self.label_9.raise_()
        self.listWidget_5.raise_()
        self.pushButton_5.raise_()
        self.pushButton_6.raise_()
        self.btnAggiornaMex.raise_()
        self.toolBox.addItem(self.page_5, "")

        self.retranslateUi(Form)
        self.toolBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

        for path in self.percorsi.keys():
            self.objGestionePrenotazioneCorsi.elimina(path)
        self.nascondi()
        self.messanger.recuperaSalvataggio("./Data/casella_di_messaggi/messaggi.txt")
        self.visualizzaMessaggi()
        self.label_2.setText(self.username)
        self.pushButton_4.clicked.connect(self.visualizza)
        self.btnPassword.clicked.connect(self.apriCambioPassword)
        self.pushButton.clicked.connect(self.apriFinestraAllenamento)
        self.pushButton_2.clicked.connect(self.apriDietaCliente)
        self.pushButton_3.clicked.connect(self.open_window_prenotazioni)
        self.listWidget.clicked.connect(self.apriSchedaAllenamento)
        self.listWidget_5.doubleClicked.connect(self.return_message)
        self.pushButton_5.clicked.connect(self.apriCasellaMessaggio)
        self.aggiungiPrenotazione()
        self.apriFileDieta()
        self.listWidget_3.doubleClicked.connect(self.apri)
        self.pushButton_7.pressed.connect(self.mostraPassword)
        self.pushButton_7.clicked.connect(self.nascondiPassword)
        self.pushButton_6.clicked.connect(self.eliminaMessaggio)
        self.inserisciSuLista()
        self.pushButton_8.clicked.connect(self.annullaPrenotazione)
        self.btn_aggiorna.clicked.connect(self.aggiungiPrenotazione)
        self.btnAggiornaMex.clicked.connect(self.visualizzaMessaggi)


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form",
                                      "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Bentornato </span></p></body></html>"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p><br/></p></body></html>"))
        self.btnPassword.setText(_translate("Form", "Cambia password"))
        self.pushButton_4.setText(_translate("Form", "Le tue info"))
        self.lbl_data_iscrizione.setText(_translate("Form", "Data iscrizione"))
        self.lbl_luogo_nascita.setText(_translate("Form", "Luogo di nascita:"))
        self.lbl_nome.setText(_translate("Form", "Nome:"))
        self.lbl_data_fine_abbonamento.setText(_translate("Form", "Data fine abbonamento"))
        self.lbl_data_certificato_medico.setText(_translate("Form", "Data certificato medico"))
        self.lbl_codice_fiscale.setText(_translate("Form", "Codice Fiscale:"))
        self.lbl_data_nascita.setText(_translate("Form", "Data di nascita:"))
        self.lbl_username.setText(_translate("Form", "Username:"))
        self.lbl_password.setText(_translate("Form", "Password:"))
        self.lbl_cognome.setText(_translate("Form", "Cognome:"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), _translate("Form", "Informazioni personali"))
        self.label_3.setText(_translate("Form", "<html><head/><body><p>La tua scheda allenamento:</p></body></html>"))
        self.label_4.setText(_translate("Form",
                                        "<html><head/><body><p><span style=\" color:#000000;\">Scopri gli esercizi e seleziona preferenze</span></p></body></html>"))
        self.pushButton.setText(_translate("Form", "Clicca qui!"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), _translate("Form", "Allenamento"))
        self.label_5.setText(_translate("Form", "<html><head/><body><p>La tua dieta: </p></body></html>"))
        self.pushButton_2.setText(_translate("Form", "Clicca qui!"))
        self.label_6.setText(
            _translate("Form", "<html><head/><body><p>Maggiori informazioni sulla tua forma fisica e sulle diete</p></body></html>"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_3), _translate("Form", "Dieta"))
        self.label_7.setText(_translate("Form", "<html><head/><body><p>Le tue Prenotazioni:</p></body></html>"))
        self.label_8.setText(_translate("Form", "<html><head/><body><p>Per prenotare</p></body></html>"))
        self.pushButton_3.setText(_translate("Form", "Clicca qui!"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_4), _translate("Form", "Prenotazioni"))
        self.label_9.setText(_translate("Form",
                                        "<html><head/><body><p align=\"center\">Qui riceverai le notifiche </p><p align=\"center\">riguardanti il tuo abbonamento!</p></body></html>"))
        self.pushButton_5.setText(_translate("Form", "Scrivi Messaggio"))
        self.pushButton_6.setText(_translate("Form", "Elimina Messaggio"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_5), _translate("Form", "Messaggi"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = GUI_client()
    ui.setupUi(Form, username="")
    Form.show()
    sys.exit(app.exec_())