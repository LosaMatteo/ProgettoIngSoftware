import pickle

from Data.gestioneObject import gestObj

class Orario(object):
    lista_turni = []
    gobj = gestObj()
    path = "./Admin/gestione_personale/TurniStaff.txt"

    def __init__(self, data ="", ora_inizio="", ora_fine="", staff="", paga="", mansione=""):
        if data != "":
            self.data = data
            self.ora_inizio = ora_inizio
            self.ora_fine = ora_fine
            self.staff = staff
            self.paga = paga
            self.mansione = mansione

    def recuperaSalvataggio(self, path):
        self.lista_turni.clear()
        self.gobj.recuperaSalvataggio(path, self.lista_turni)

    def addToList(self, obj):
        self.gobj.addToList(obj, self.lista_turni)
        self.scriviLista(self.path)

    def scriviLista(self, path):
        self.gobj.scriviLista(path, self.lista_turni)

    def controlloGiorno(self, data):
        listaPrenotati = []
        for elem in self.lista_turni:
            if data == elem.data:
                listaPrenotati.append(elem)
        return listaPrenotati

    def controlloLavoro(self, data, staff):
        listaLavoro = []
        for elem in self.lista_turni:
            if data == elem.data and staff == self.getIndirizzo(elem.staff):
                listaLavoro.append(elem)
        return listaLavoro

    def getIndirizzo(self, username):
        indirizzo = ""
        tmp = username.split(" ")
        for elem in tmp:
            indirizzo += elem
        return indirizzo

    def rimuoviTurno(self, username, data):
        for elem in self.lista_turni:
            if elem.data == data and elem.staff == username:
                self.lista_turni.remove(elem)
        self.scriviLista(self.path)

    def rimuoviTurniStaff(self, username):
        filehandler = open(self.path, 'wb')
        for elem in self.lista_turni:
            if elem.staff != username:
                pickle.dump(elem, filehandler)



