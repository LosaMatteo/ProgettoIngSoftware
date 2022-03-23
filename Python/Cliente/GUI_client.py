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
        self.lstPrenotazioni.clear()
        for percorso in self.percorsi.keys():
            vettore = self.objGestionePrenotazioneCorsi.trovaCliente(percorso, self.username)
            for elem in vettore:
                self.lista_prenotazioni.append(percorso + "+" + elem)
                elem = elem[:-4]
                orario = elem[11:]
                data = elem[:10]
                self.lstPrenotazioni.addItem("data: " + data + " orario: " + orario + " " + self.percorsi[percorso])
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
        self.lstMessaggi.clear()
        self.lista_messaggi = self.messanger.getObject_message(self.username)
        self.lista_messaggi.sort(key=lambda x: x.data, reverse=True)  # ordina la lista messaggi in ordine temporale
        for elem in self.lista_messaggi:
            if elem.mittente == self.username:
                self.lstMessaggi.addItem("Messaggio inviato a: " + elem.destinatario + "  -  " + elem.data)
            elif elem.destinatario == self.username:
                self.lstMessaggi.addItem("Messaggio da: " + elem.mittente + "  -  " + elem.data)

    def restituisciMessaggio(self):
        riga = self.lstMessaggi.currentRow()
        self.lista_messaggi = self.messanger.getObject_message(self.username)
        self.lista_messaggi.sort(key=lambda x: x.data, reverse=True)  # ordina la lista messaggi in ordine temporale
        self.messanger = self.lista_messaggi[riga]
        self.apriLetturaMessaggio()

    def eliminaMessaggio(self):
        try:
            objMessaggio = self.lista_messaggi[self.lstMessaggi.currentRow()]
            self.messanger.rimuovi_messaggio(objMessaggio)
            self.lstMessaggi.takeItem(self.lstMessaggi.currentRow())
        except(Exception):
            self.messaggio.show_popup_exception("Errore")

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
            self.lstDieta.addItem(str)

    def apriFileDieta(self):
        percorso = "./Cliente/Dieta/file_dieta"
        lista_files = [f for f in listdir(percorso) if isfile(join(percorso, f))]
        for elem in lista_files:
            if elem.startswith(self.username + "_dieta_personale_"):
                self.lista_files_utente.append(elem)
        self.scriviSuLista()

    def apri(self):
        file = self.lista_files_utente[self.lstDieta.currentRow()]
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
        self.txtNome.setText(objCliente.name)
        self.txtCognome.setText(objCliente.surname)
        self.txtUsername.setText(self.username)
        self.txtPassword.setText(objCliente.password)
        self.txtCodiceFiscale.setText(objCliente.codice_fiscale)
        self.txtLuogoNascita.setText(objCliente.luogo_nascita)
        self.txtDataNascita.setText(objCliente.data_nascita.toString())
        self.dtdDataIscrizione.setDate(objCliente.gestAll.data_iscrizione)
        if objCliente.gestAll.tipo_di_abbonamento.__contains__("mensile"):
            self.dtdScadenzaAbbonamento.setDate(self.dtdDataIscrizione.date().addMonths(1))
            if data_odierna > self.dtdScadenzaAbbonamento.date():
                self.messaggio.show_popup_ok("abbonamento scaduto,si prega di rinnovarlo")
        elif objCliente.gestAll.tipo_di_abbonamento.__contains__("annuale"):
            self.dtdScadenzaAbbonamento.setDate(self.dtdDataIscrizione.date().addYears(1))
            if data_odierna > self.dtdScadenzaAbbonamento.date():
                self.messaggio.show_popup_ok("abbonamento scaduto,si prega di rinnovarlo")
        self.dtdScadenzaCertificatoMedico.setDate(objCliente.gestAll.data_certificato_medico)



    def apriSchedaAllenamento(self):
        self.scheda_allenamento = QtWidgets.QMainWindow()
        self.ui = scheda_allenamento()
        self.ui.setupUi(self.scheda_allenamento,self.username)
        self.scheda_allenamento.show()

    def nascondi(self):
        self.lstInformazioniPersonali.hide()
        self.txtNome.hide()
        self.txtCognome.hide()
        self.txtUsername.hide()
        self.txtPassword.hide()
        self.txtCodiceFiscale.hide()
        self.txtLuogoNascita.hide()
        self.txtDataNascita.hide()
        self.dtdDataIscrizione.hide()
        self.dtdScadenzaAbbonamento.hide()
        self.dtdScadenzaCertificatoMedico.hide()
        self.lblNome.hide()
        self.lblCognome.hide()
        self.lblUsername.hide()
        self.lblPassword.hide()
        self.lblCodiceFiscale.hide()
        self.lblLuogoNascita.hide()
        self.lblDataNascita.hide()
        self.lblDataIscrizione.hide()
        self.lblDataFineAbbonamento.hide()
        self.lblDataCertificatoMedico.hide()
        self.btnMostraPassword.hide()

    def mostra(self):
        self.lstInformazioniPersonali.show()
        self.txtNome.show()
        self.txtCognome.show()
        self.txtUsername.show()
        self.txtPassword.show()
        self.txtPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txtCodiceFiscale.show()
        self.txtLuogoNascita.show()
        self.txtDataNascita.show()
        self.dtdDataIscrizione.show()
        self.dtdScadenzaAbbonamento.show()
        self.dtdScadenzaCertificatoMedico.show()
        self.lblNome.show()
        self.lblCognome.show()
        self.lblUsername.show()
        self.lblPassword.show()
        self.lblCodiceFiscale.show()
        self.lblLuogoNascita.show()
        self.lblDataNascita.show()
        self.lblDataIscrizione.show()
        self.lblDataFineAbbonamento.show()
        self.lblDataCertificatoMedico.show()
        self.btnMostraPassword.show()

    def mostraPassword(self):
         self.txtPassword.setEchoMode(QtWidgets.QLineEdit.Normal)

    def nascondiPassword(self):
        self.txtPassword.setEchoMode(QtWidgets.QLineEdit.Password)

    def inserisciSuLista(self):
        objCliente = Cliente()
        objCliente = objCliente.getObject(self.username)
        percorso = "Staff/Allenamento_staff/file_scheda_allenamento"
        lista_files = [f for f in listdir(percorso) if isfile(join(percorso, f))]
        for elem in lista_files:
            if objCliente.name + " " + objCliente.surname + ".txt" == elem:
                self.lstSchedaAllenamento.addItem(elem)

    def annullaPrenotazione(self):
        try:
            if self.lstPrenotazioni.currentItem().isSelected():
                da_annullare = self.lista_prenotazioni[self.lstPrenotazioni.currentIndex().row()]
                percorso = da_annullare.split("+")
                self.objGestionePrenotazioneCorsi.annullaPrenotazione(self.username, percorso[0], percorso[1])
                self.lstPrenotazioni.clear()
                self.aggiungiPrenotazione()
        except(AttributeError):
            self.messaggio.show_popup_exception("Non hai selezionato nulla dalla lista")
        except(Exception):
            self.messaggio.show_popup_exception("ERRORE")

    def setupUi(self, Form,username):
        self.username = username
        Form.setObjectName("Form")
        Form.resize(597, 647)
        self.lblMsgDiBenvenuto = QtWidgets.QLabel(Form)
        self.lblMsgDiBenvenuto.setGeometry(QtCore.QRect(10, 10, 141, 31))
        font = QtGui.QFont()
        font.setBold(False)
        self.lblMsgDiBenvenuto.setFont(font)
        self.lblMsgDiBenvenuto.setObjectName("lblMsgDiBenvenuto")
        self.lblNomeUtente = QtWidgets.QLabel(Form)
        self.lblNomeUtente.setGeometry(QtCore.QRect(170, 10, 151, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        font.setBold(True)
        self.lblNomeUtente.setFont(font)
        self.lblNomeUtente.setObjectName("lblNomeUtente")
        self.toolBox = QtWidgets.QToolBox(Form)
        self.toolBox.setGeometry(QtCore.QRect(30, 50, 471, 551))
        self.toolBox.setObjectName("toolBox")
        self.Pagina_1 = QtWidgets.QWidget()
        self.Pagina_1.setGeometry(QtCore.QRect(0, 0, 471, 401))
        self.Pagina_1.setObjectName("Pagina_1")
        self.lblSfondo = QtWidgets.QLabel(self.Pagina_1)
        self.lblSfondo.setGeometry(QtCore.QRect(-1, 0, 461, 391))
        self.lblSfondo.setText("")
        self.lblSfondo.setPixmap(QtGui.QPixmap("./Resources/images/pngGUI_client/Sfondodecisivo.png"))
        self.lblSfondo.setScaledContents(True)
        self.lblSfondo.setObjectName("lblSfondo")
        self.btnCambioPassword = QtWidgets.QPushButton(self.Pagina_1)
        self.btnCambioPassword.setGeometry(QtCore.QRect(330, 290, 121, 24))
        self.btnCambioPassword.setObjectName("btnCambioPassword")
        self.btnLeTueInfo = QtWidgets.QPushButton(self.Pagina_1)
        self.btnLeTueInfo.setGeometry(QtCore.QRect(330, 270, 121, 21))
        self.btnLeTueInfo.setObjectName("btnLeTueInfo")
        self.lstInformazioniPersonali = QtWidgets.QListWidget(self.Pagina_1)
        self.lstInformazioniPersonali.setGeometry(QtCore.QRect(20, 20, 281, 361))
        self.lstInformazioniPersonali.setObjectName("lstInformazioniPersonali")
        self.txtPassword = QtWidgets.QLineEdit(self.Pagina_1)
        self.txtPassword.setGeometry(QtCore.QRect(170, 140, 113, 22))
        self.txtPassword.setText("")
        self.txtPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txtPassword.setReadOnly(True)
        self.txtPassword.setObjectName("txtPassword")
        self.dtdDataIscrizione = QtWidgets.QDateEdit(self.Pagina_1)
        self.dtdDataIscrizione.setGeometry(QtCore.QRect(170, 260, 111, 22))
        self.dtdDataIscrizione.setReadOnly(True)
        self.dtdDataIscrizione.setCalendarPopup(True)
        self.dtdDataIscrizione.setObjectName("dtdDataIscrizione")
        self.txtLuogoNascita = QtWidgets.QLineEdit(self.Pagina_1)
        self.txtLuogoNascita.setGeometry(QtCore.QRect(170, 200, 113, 22))
        self.txtLuogoNascita.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.txtLuogoNascita.setReadOnly(True)
        self.txtLuogoNascita.setObjectName("txtLuogoNascita")
        self.lblDataIscrizione = QtWidgets.QLabel(self.Pagina_1)
        self.lblDataIscrizione.setGeometry(QtCore.QRect(40, 260, 111, 21))
        self.lblDataIscrizione.setObjectName("lblDataIscrizione")
        self.dtdScadenzaCertificatoMedico = QtWidgets.QDateEdit(self.Pagina_1)
        self.dtdScadenzaCertificatoMedico.setGeometry(QtCore.QRect(170, 320, 111, 22))
        self.dtdScadenzaCertificatoMedico.setReadOnly(True)
        self.dtdScadenzaCertificatoMedico.setCalendarPopup(True)
        self.dtdScadenzaCertificatoMedico.setObjectName("dtdScadenzaCertificatoMedico")
        self.lblLuogoNascita = QtWidgets.QLabel(self.Pagina_1)
        self.lblLuogoNascita.setGeometry(QtCore.QRect(40, 200, 111, 21))
        self.lblLuogoNascita.setObjectName("lblLuogoNascita")
        self.lblNome = QtWidgets.QLabel(self.Pagina_1)
        self.lblNome.setGeometry(QtCore.QRect(40, 50, 111, 21))
        self.lblNome.setObjectName("lblNome")
        self.txtNome = QtWidgets.QLineEdit(self.Pagina_1)
        self.txtNome.setGeometry(QtCore.QRect(170, 50, 113, 22))
        self.txtNome.setReadOnly(True)
        self.txtNome.setObjectName("txtNome")
        self.lblDataFineAbbonamento = QtWidgets.QLabel(self.Pagina_1)
        self.lblDataFineAbbonamento.setGeometry(QtCore.QRect(30, 290, 141, 21))
        self.lblDataFineAbbonamento.setObjectName("lblDataFineAbbonamento")
        self.lblDataCertificatoMedico = QtWidgets.QLabel(self.Pagina_1)
        self.lblDataCertificatoMedico.setGeometry(QtCore.QRect(30, 320, 131, 21))
        self.lblDataCertificatoMedico.setObjectName("lblDataCertificatoMedico")
        self.txtDataNascita = QtWidgets.QLineEdit(self.Pagina_1)
        self.txtDataNascita.setGeometry(QtCore.QRect(170, 230, 113, 22))
        self.txtDataNascita.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.txtDataNascita.setReadOnly(True)
        self.txtDataNascita.setObjectName("txtDataNascita")
        self.lblCodiceFiscale = QtWidgets.QLabel(self.Pagina_1)
        self.lblCodiceFiscale.setGeometry(QtCore.QRect(40, 170, 111, 21))
        self.lblCodiceFiscale.setObjectName("lblCodiceFiscale")
        self.lblDataNascita = QtWidgets.QLabel(self.Pagina_1)
        self.lblDataNascita.setGeometry(QtCore.QRect(40, 230, 111, 21))
        self.lblDataNascita.setObjectName("lblDataNascita")
        self.txtCodiceFiscale = QtWidgets.QLineEdit(self.Pagina_1)
        self.txtCodiceFiscale.setGeometry(QtCore.QRect(170, 170, 113, 22))
        self.txtCodiceFiscale.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.txtCodiceFiscale.setReadOnly(True)
        self.txtCodiceFiscale.setObjectName("txtCodiceFiscale")
        self.lblUsername = QtWidgets.QLabel(self.Pagina_1)
        self.lblUsername.setGeometry(QtCore.QRect(40, 110, 111, 21))
        self.lblUsername.setObjectName("lblUsername")
        self.txtUsername = QtWidgets.QLineEdit(self.Pagina_1)
        self.txtUsername.setGeometry(QtCore.QRect(170, 110, 113, 22))
        self.txtUsername.setReadOnly(True)
        self.txtUsername.setObjectName("txtUsername")
        self.txtCognome = QtWidgets.QLineEdit(self.Pagina_1)
        self.txtCognome.setGeometry(QtCore.QRect(170, 80, 113, 22))
        self.txtCognome.setReadOnly(True)
        self.txtCognome.setObjectName("txtCognome")
        self.lblPassword = QtWidgets.QLabel(self.Pagina_1)
        self.lblPassword.setGeometry(QtCore.QRect(40, 140, 111, 21))
        self.lblPassword.setObjectName("lblPassword")
        self.lblCognome = QtWidgets.QLabel(self.Pagina_1)
        self.lblCognome.setGeometry(QtCore.QRect(40, 80, 111, 21))
        self.lblCognome.setObjectName("lblCognome")
        self.dtdScadenzaAbbonamento = QtWidgets.QDateEdit(self.Pagina_1)
        self.dtdScadenzaAbbonamento.setGeometry(QtCore.QRect(170, 290, 111, 22))
        self.dtdScadenzaAbbonamento.setReadOnly(True)
        self.dtdScadenzaAbbonamento.setCalendarPopup(True)
        self.dtdScadenzaAbbonamento.setObjectName("dtdScadenzaAbbonamento")
        self.btnMostraPassword = QtWidgets.QPushButton(self.Pagina_1)
        self.btnMostraPassword.setGeometry(QtCore.QRect(260, 141, 21, 20))
        self.btnMostraPassword.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./Resources/images/download.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnMostraPassword.setIcon(icon)
        self.btnMostraPassword.setObjectName("btnMostraPassword")
        self.toolBox.addItem(self.Pagina_1, "")
        self.Pagina_2 = QtWidgets.QWidget()
        self.Pagina_2.setGeometry(QtCore.QRect(0, 0, 471, 401))
        self.Pagina_2.setObjectName("Pagina_2")
        self.lblTitolo = QtWidgets.QLabel(self.Pagina_2)
        self.lblTitolo.setGeometry(QtCore.QRect(10, 10, 171, 31))
        self.lblTitolo.setObjectName("lblTitolo")
        self.lblTesto_2 = QtWidgets.QLabel(self.Pagina_2)
        self.lblTesto_2.setGeometry(QtCore.QRect(10, 290, 240, 31))
        self.lblTesto_2.setObjectName("lblTesto_2")
        self.btnEserciziCorsi = QtWidgets.QPushButton(self.Pagina_2)
        self.btnEserciziCorsi.setGeometry(QtCore.QRect(260, 290, 113, 31))
        self.btnEserciziCorsi.setObjectName("btnEserciziCorsi")
        self.lblSfondo_2 = QtWidgets.QLabel(self.Pagina_2)
        self.lblSfondo_2.setGeometry(QtCore.QRect(-1, 0, 451, 351))
        self.lblSfondo_2.setText("")
        self.lblSfondo_2.setPixmap(QtGui.QPixmap("./Resources/images/pngGUI_client/Sfondodecisivo.png"))
        self.lblSfondo_2.setScaledContents(True)
        self.lblSfondo_2.setObjectName("lblSfondo_2")
        self.lstSchedaAllenamento = QtWidgets.QListWidget(self.Pagina_2)
        self.lstSchedaAllenamento.setGeometry(QtCore.QRect(30, 50, 411, 192))
        self.lstSchedaAllenamento.setObjectName("lstSchedaAllenamento")
        self.lblSfondo_2.raise_()
        self.lblTitolo.raise_()
        self.lblTesto_2.raise_()
        self.btnEserciziCorsi.raise_()
        self.lstSchedaAllenamento.raise_()
        self.toolBox.addItem(self.Pagina_2, "")
        self.Pagina_3 = QtWidgets.QWidget()
        self.Pagina_3.setGeometry(QtCore.QRect(0, 0, 98, 28))
        self.Pagina_3.setObjectName("Pagina_3")
        self.lblTitolo_2 = QtWidgets.QLabel(self.Pagina_3)
        self.lblTitolo_2.setGeometry(QtCore.QRect(0, 0, 91, 21))
        self.lblTitolo_2.setObjectName("lblTitolo_2")
        self.btnFabbisogno = QtWidgets.QPushButton(self.Pagina_3)
        self.btnFabbisogno.setGeometry(QtCore.QRect(340, 290, 113, 32))
        self.btnFabbisogno.setObjectName("btnFabbisogno")
        self.lblTesto_3 = QtWidgets.QLabel(self.Pagina_3)
        self.lblTesto_3.setGeometry(QtCore.QRect(10, 290, 330, 31))
        self.lblTesto_3.setObjectName("lblTesto_3")
        self.lblSfondo_3 = QtWidgets.QLabel(self.Pagina_3)
        self.lblSfondo_3.setGeometry(QtCore.QRect(-1, 0, 471, 401))
        self.lblSfondo_3.setText("")
        self.lblSfondo_3.setPixmap(QtGui.QPixmap("./Resources/images/pngGUI_client/Sfondoverde.png"))
        self.lblSfondo_3.setScaledContents(True)
        self.lblSfondo_3.setObjectName("lblSfondo_3")
        self.lstDieta = QtWidgets.QListWidget(self.Pagina_3)
        self.lstDieta.setGeometry(QtCore.QRect(20, 30, 271, 211))
        self.lstDieta.setObjectName("lstDieta")
        self.lblSfondo_3.raise_()
        self.lblTitolo_2.raise_()
        self.btnFabbisogno.raise_()
        self.lblTesto_3.raise_()
        self.lstDieta.raise_()
        self.toolBox.addItem(self.Pagina_3, "")
        self.Pagina_4 = QtWidgets.QWidget()
        self.Pagina_4.setGeometry(QtCore.QRect(0, 0, 471, 401))
        self.Pagina_4.setObjectName("Pagina_4")
        self.lblTitolo_3 = QtWidgets.QLabel(self.Pagina_4)
        self.lblTitolo_3.setGeometry(QtCore.QRect(10, 0, 131, 16))
        self.lblTitolo_3.setObjectName("lblTitolo_3")
        self.lblTesto_4 = QtWidgets.QLabel(self.Pagina_4)
        self.lblTesto_4.setGeometry(QtCore.QRect(20, 270, 91, 31))
        self.lblTesto_4.setObjectName("lblTesto_4")
        self.btnPrenotazioni = QtWidgets.QPushButton(self.Pagina_4)
        self.btnPrenotazioni.setGeometry(QtCore.QRect(160, 270, 113, 32))
        self.btnPrenotazioni.setObjectName("btnPrenotazioni")
        self.lblSfondo_4 = QtWidgets.QLabel(self.Pagina_4)
        self.lblSfondo_4.setGeometry(QtCore.QRect(0, 0, 471, 391))
        self.lblSfondo_4.setText("")
        self.lblSfondo_4.setPixmap(QtGui.QPixmap("./Resources/images/pngGUI_client/Sfoidnigiallo.png"))
        self.lblSfondo_4.setScaledContents(True)
        self.lblSfondo_4.setObjectName("lblSfondo_4")
        self.lstPrenotazioni = QtWidgets.QListWidget(self.Pagina_4)
        self.lstPrenotazioni.setGeometry(QtCore.QRect(20, 30, 381, 211))
        self.lstPrenotazioni.setAutoScroll(True)
        self.lstPrenotazioni.setObjectName("lstPrenotazioni")
        self.btnCancella = QtWidgets.QPushButton(self.Pagina_4)
        self.btnCancella.setGeometry(QtCore.QRect(350, 40, 31, 21))
        self.btnCancella.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("./Resources/images/cancella.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnCancella.setIcon(icon1)
        self.btnCancella.setIconSize(QtCore.QSize(30, 200))
        self.btnCancella.setObjectName("btnCancella")
        self.btnAggiorna = QtWidgets.QPushButton(self.Pagina_4)
        self.btnAggiorna.setGeometry(QtCore.QRect(410, 30, 31, 31))
        self.btnAggiorna.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("./Resources/images/aggiornamento.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnAggiorna.setIcon(icon2)
        self.btnAggiorna.setIconSize(QtCore.QSize(50, 50))
        self.btnAggiorna.setObjectName("btnAggiorna")
        self.lblSfondo_4.raise_()
        self.lblTitolo_3.raise_()
        self.lblTesto_4.raise_()
        self.btnPrenotazioni.raise_()
        self.lstPrenotazioni.raise_()
        self.btnAggiorna.raise_()
        self.btnCancella.raise_()
        self.toolBox.addItem(self.Pagina_4, "")
        self.Pagina_5 = QtWidgets.QWidget()
        self.Pagina_5.setGeometry(QtCore.QRect(0, 0, 471, 401))
        self.Pagina_5.setObjectName("page_5")
        self.lblTitolo_4 = QtWidgets.QLabel(self.Pagina_5)
        self.lblTitolo_4.setGeometry(QtCore.QRect(50, 10, 191, 61))
        self.lblTitolo_4.setObjectName("lblTitolo_4")
        self.lblSfondo_5 = QtWidgets.QLabel(self.Pagina_5)
        self.lblSfondo_5.setGeometry(QtCore.QRect(-1, 10, 471, 401))
        self.lblSfondo_5.setText("")
        self.lblSfondo_5.setPixmap(QtGui.QPixmap("./Resources/images/pngGUI_client/Sfondo1.png"))
        self.lblSfondo_5.setObjectName("lblSfondo_5")
        self.lstMessaggi = QtWidgets.QListWidget(self.Pagina_5)
        self.lstMessaggi.setGeometry(QtCore.QRect(20, 70, 300, 321))
        self.lstMessaggi.setObjectName("lstMessaggi")
        self.btnNuovoMessaggio = QtWidgets.QPushButton(self.Pagina_5)
        self.btnNuovoMessaggio.setGeometry(QtCore.QRect(325, 160, 141, 28))
        self.btnNuovoMessaggio.setObjectName("btnNuovoMessaggio")
        self.btnEliminaMessaggio = QtWidgets.QPushButton(self.Pagina_5)
        self.btnEliminaMessaggio.setGeometry(QtCore.QRect(325, 200, 141, 28))
        self.btnEliminaMessaggio.setObjectName("btnEliminaMessaggio")
        self.btnAggiornaMessaggi = QtWidgets.QPushButton(self.Pagina_5)
        self.btnAggiornaMessaggi.setGeometry(QtCore.QRect(330, 70, 31, 31))
        self.btnAggiornaMessaggi.setText("")
        self.btnAggiornaMessaggi.setIcon(icon2)
        self.btnAggiornaMessaggi.setIconSize(QtCore.QSize(50, 50))
        self.btnAggiornaMessaggi.setObjectName("btnAggiornaMessaggi")
        self.lblSfondo_5.raise_()
        self.lblTitolo_4.raise_()
        self.lstMessaggi.raise_()
        self.btnNuovoMessaggio.raise_()
        self.btnEliminaMessaggio.raise_()
        self.btnAggiornaMessaggi.raise_()
        self.toolBox.addItem(self.Pagina_5, "")
        self.retranslateUi(Form)
        self.toolBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)
        for percorso in self.percorsi.keys():
            self.objGestionePrenotazioneCorsi.elimina(percorso)
        self.nascondi()
        self.messanger.recuperaSalvataggio("./Data/casella_di_messaggi/messaggi.txt")
        self.visualizzaMessaggi()
        self.lblNomeUtente.setText(self.username)
        self.btnLeTueInfo.clicked.connect(self.visualizza)
        self.btnCambioPassword.clicked.connect(self.apriCambioPassword)
        self.btnEserciziCorsi.clicked.connect(self.apriFinestraAllenamento)
        self.btnFabbisogno.clicked.connect(self.apriDietaCliente)
        self.btnPrenotazioni.clicked.connect(self.apriPrenotazioni)
        self.lstSchedaAllenamento.clicked.connect(self.apriSchedaAllenamento)
        self.lstMessaggi.doubleClicked.connect(self.restituisciMessaggio)
        self.btnNuovoMessaggio.clicked.connect(self.apriCasellaMessaggio)
        self.aggiungiPrenotazione()
        self.apriFileDieta()
        self.lstDieta.doubleClicked.connect(self.apri)
        self.btnMostraPassword.pressed.connect(self.mostraPassword)
        self.btnMostraPassword.clicked.connect(self.nascondiPassword)
        self.btnEliminaMessaggio.clicked.connect(self.eliminaMessaggio)
        self.inserisciSuLista()
        self.btnCancella.clicked.connect(self.annullaPrenotazione)
        self.btnAggiorna.clicked.connect(self.aggiungiPrenotazione)
        self.btnAggiornaMessaggi.clicked.connect(self.visualizzaMessaggi)


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Bentornato, "+self.username))
        self.lblMsgDiBenvenuto.setText(_translate("Form",
                                      "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Bentornato </span></p></body></html>"))
        self.lblNomeUtente.setText(_translate("Form", "<html><head/><body><p><br/></p></body></html>"))
        self.btnCambioPassword.setText(_translate("Form", "Cambia password"))
        self.btnLeTueInfo.setText(_translate("Form", "Le tue info"))
        self.lblDataIscrizione.setText(_translate("Form", "Data iscrizione"))
        self.lblLuogoNascita.setText(_translate("Form", "Luogo di nascita:"))
        self.lblNome.setText(_translate("Form", "Nome:"))
        self.lblDataFineAbbonamento.setText(_translate("Form", "Data fine abbonamento"))
        self.lblDataCertificatoMedico.setText(_translate("Form", "Data certificato medico"))
        self.lblCodiceFiscale.setText(_translate("Form", "Codice Fiscale:"))
        self.lblDataNascita.setText(_translate("Form", "Data di nascita:"))
        self.lblUsername.setText(_translate("Form", "Username:"))
        self.lblPassword.setText(_translate("Form", "Password:"))
        self.lblCognome.setText(_translate("Form", "Cognome:"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.Pagina_1), _translate("Form", "Informazioni personali"))
        self.lblTitolo.setText(_translate("Form", "<html><head/><body><p>La tua scheda allenamento:</p></body></html>"))
        self.lblTesto_2.setText(_translate("Form",
                                        "<html><head/><body><p><span style=\" color:#000000;\">Scopri gli esercizi e seleziona preferenze</span></p></body></html>"))
        self.btnEserciziCorsi.setText(_translate("Form", "Clicca qui!"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.Pagina_2), _translate("Form", "Allenamento"))
        self.lblTitolo_2.setText(_translate("Form", "<html><head/><body><p>La tua dieta: </p></body></html>"))
        self.btnFabbisogno.setText(_translate("Form", "Clicca qui!"))
        self.lblTesto_3.setText(
            _translate("Form", "<html><head/><body><p>Maggiori informazioni sulla tua forma fisica e sulle diete</p></body></html>"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.Pagina_3), _translate("Form", "Dieta"))
        self.lblTitolo_3.setText(_translate("Form", "<html><head/><body><p>Le tue Prenotazioni:</p></body></html>"))
        self.lblTesto_4.setText(_translate("Form", "<html><head/><body><p>Per prenotare</p></body></html>"))
        self.btnPrenotazioni.setText(_translate("Form", "Clicca qui!"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.Pagina_4), _translate("Form", "Prenotazioni"))
        self.lblTitolo_4.setText(_translate("Form",
                                        "<html><head/><body><p align=\"center\">Qui riceverai le notifiche </p><p align=\"center\">riguardanti il tuo abbonamento!</p></body></html>"))
        self.btnNuovoMessaggio.setText(_translate("Form", "Scrivi Messaggio"))
        self.btnEliminaMessaggio.setText(_translate("Form", "Elimina Messaggio"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.Pagina_5), _translate("Form", "Messaggi"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = GUI_client()
    ui.setupUi(Form, username="")
    Form.show()
    sys.exit(app.exec_())