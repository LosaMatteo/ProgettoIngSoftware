from Data.gestioneObject import gestObj
from Model.Abbonamento import Abbonamento


class Cliente(object):
    gestAll = Abbonamento()
    listaclienti = []
    gobj = gestObj()

    def __init__(self, name="", surname="", gender="", data_di_nascita="", luogo_nascita="", codice_fiscale="",
                 password="1234", Abbonamento="", altezza="", peso="", eta=""):
        if name != "" or surname != "":
            self.name = name
            self.surname = surname
            self.gender = gender
            self.data_nascita = data_di_nascita
            self.luogo_nascita = luogo_nascita
            self.codice_fiscale = codice_fiscale
            self.password = password
            self.gestAll = Abbonamento
            self.altezza = altezza
            self.peso = peso
            self.eta = eta

    def popolaLista(self):
        return self.gobj.popolaLista(self.listaclienti)

    def recuperaSalvataggio(self, path):
        self.listaclienti.clear()
        self.gobj.recuperaSalvataggio(path, self.listaclienti)

    def addToList(self, obj):
        self.gobj.addToList(obj, self.listaclienti)
        self.scriviLista("./Admin/gestione_cliente/CredenzialiClienti.txt")

    def scriviLista(self, path):
        self.gobj.scriviLista(path, self.listaclienti)

    def rimuovi(self, strdaeliminare):
        self.gobj.rimuovi(strdaeliminare, self.listaclienti)
        self.scriviLista("./Admin/gestione_cliente/CredenzialiClienti.txt")
        self.gobj.rimuoviPrenotazioni(strdaeliminare.replace(" ", ""),
                                      "./Cliente/Prenotazioni/file_prenotazioni/salaPesi/")
        self.gobj.rimuoviPrenotazioni(strdaeliminare.replace(" ", ""),
                                      "./Cliente/Prenotazioni/file_prenotazioni/functional/")
        self.gobj.rimuoviPrenotazioni(strdaeliminare.replace(" ", ""),
                                      "./Cliente/Prenotazioni/file_prenotazioni/zumba/")
        self.gobj.rimuoviFiles("./Cliente/Dieta/file_dieta/", strdaeliminare.replace(" ", ""))
        self.gobj.rimuoviFiles("./Cliente/Allenamento/file_allenamento/", strdaeliminare.replace(" ", ""))

    def getAttributi(self, id):
        return self.gobj.getAttributi(id, self.listaclienti)

    def getObject(self, id):
        return self.gobj.getObject(id, self.listaclienti)

    def modificaLista(self, vett, id):
        self.gobj.modificaLista(vett, id, self.listaclienti)
        self.scriviLista("./Admin/gestione_cliente/CredenzialiClienti.txt")

    def getClCred(self):
        return self.gobj.getUserPass(self.listaclienti)

    def return_object(self):
        return self.gestAll.data_iscrizione

    def reset(self, name):
        self.gobj.resetpassword(name, self.listaclienti)
        self.scriviLista("./Admin/gestione_cliente/CredenzialiClienti.txt")

    def get_lista(self):
        return self.gobj.get_lista(self.listaclienti)
