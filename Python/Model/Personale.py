from Data.gestioneObject import gestObj


class Personale(object):
    gobj = gestObj()
    lista_staff = []

    def __init__(self, nome="", cognome="", codice_fiscale="", ore="", mansione="", password="1234"):
        if nome != "" or cognome != "":
            self.name = nome
            self.surname = cognome
            self.cf = codice_fiscale
            self.ore = ore
            self.mansione = mansione
            self.password = password

    def popolaLista(self):
        return self.gobj.popolaLista(self.lista_staff)

    def recuperaSalvataggio(self, path):
        self.lista_staff.clear()
        self.gobj.recuperaSalvataggio(path, self.lista_staff)

    def addToList(self, obj):
        self.gobj.addToList(obj, self.lista_staff)
        self.scriviLista("./Admin/gestione_personale/CredenzialiStaff.txt")

    def scriviLista(self, path):
        self.gobj.scriviLista(path, self.lista_staff)

    def getAttributi(self, id):
        return self.gobj.getAttributi(id, self.lista_staff)

    def rimuovi(self, stringa_da_eliminare):
        self.gobj.rimuovi(stringa_da_eliminare)
        self.scriviLista("./Admin/gestione_personale/CredenzialiStaff.txt")

    def reset(self, name):
        self.gobj.resetpassword(name, self.lista_staff)
        self.scriviLista("./Admin/gestione_personale/CredenzialiStaff.txt")

    def getClCred(self):
        return self.gobj.getUserPass(self.lista_staff)

    def getObject(self, id):
        return self.gobj.getObject(id, self.lista_staff)

    def get_lista(self):
        return self.gobj.get_lista(self.lista_staff)