from Python.Data.gestioneObject import gestObj
from Python.Model.Abbonamento import Abbonamento


class Cliente(object):
    gestAll = Abbonamento()
    lista_clienti = []
    gobj = gestObj()

    def __init__(self, nome="", cognome="", gender="", data_di_nascita="", luogo_di_nascita="", codice_fiscale="",
                 password="1234", Abbonamento="", altezza="", peso="", eta=""):
        if nome != "" or cognome != "":
            self.name = nome
            self.surname = cognome
            self.gender = gender
            self.data_nascita = data_di_nascita
            self.luogo_nascita = luogo_di_nascita
            self.codice_fiscale = codice_fiscale
            self.password = password
            self.gestAll = Abbonamento
            self.altezza = altezza
            self.peso = peso
            self.eta = eta

    def popolaLista(self):
        return self.gobj.popolaLista(self.lista_clienti)

    def recuperaSalvataggio(self, path):
        self.lista_clienti.clear()
        self.gobj.recuperaSalvataggio(path, self.lista_clienti)

    def addToList(self, obj):
        self.gobj.addToList(obj, self.lista_clienti)
        self.scriviLista("./Admin/gestione_cliente/CredenzialiClienti.txt")

    def scriviLista(self, path):
        self.gobj.scriviLista(path, self.lista_clienti)

    def rimuovi(self, stringa_da_eliminare):
        self.gobj.rimuovi(stringa_da_eliminare)
        self.scriviLista("./Admin/gestione_cliente/CredenzialiClienti.txt")
        self.gobj.rimuoviPrenotazioni(stringa_da_eliminare.replace(" ", ""),
                                      "./Cliente/Prenotazioni/file_prenotazioni/salaPesi/")
        self.gobj.rimuoviPrenotazioni(stringa_da_eliminare.replace(" ", ""),
                                      "./Cliente/Prenotazioni/file_prenotazioni/functional/")
        self.gobj.rimuoviPrenotazioni(stringa_da_eliminare.replace(" ", ""),
                                      "./Cliente/Prenotazioni/file_prenotazioni/zumba/")
        self.gobj.rimuoviFiles("./Cliente/Dieta/file_dieta/", stringa_da_eliminare.replace(" ", ""))
        self.gobj.rimuoviFiles("./Cliente/Allenamento/file_allenamento/", stringa_da_eliminare.replace(" ", ""))

    def getAttributi(self, id):
        return self.gobj.getAttributi(id, self.lista_clienti)

    def getObject(self, id):
        return self.gobj.getObject(id, self.lista_clienti)

    def modificaLista(self, vett, id):
        self.gobj.modificaLista(vett, id, self.lista_clienti)
        self.scriviLista("./Admin/gestione_cliente/CredenzialiClienti.txt")

    def getClCred(self):
        return self.gobj.getUserPass(self.lista_clienti)

    def return_object(self):
        return self.gestAll.data_iscrizione

    def reset(self, name):
        self.gobj.resetpassword(name, self.lista_clienti)
        self.scriviLista("./Admin/gestione_cliente/CredenzialiClienti.txt")

    def get_lista(self):
        return self.gobj.get_lista(self.lista_clienti)
