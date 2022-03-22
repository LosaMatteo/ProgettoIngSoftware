from Data.gestioneObject import gestObj


class Attrezzo(object):
    gobj = gestObj()
    lista_attrezzi = []

    def __init__(self, descr="", data_ac="", quantita="", pr_uni="", data_man=""):
        if descr != "":
            self.descr = descr
            self.data_ac = data_ac
            self.quantita = quantita
            self.pr_uni = pr_uni
            self.data_man = data_man

    def popolaLista(self):
        return self.gobj.popolaListaAttrezzi(self.lista_attrezzi)

    def recuperaSalvataggio(self, path):
        self.lista_attrezzi.clear()
        self.gobj.recuperaSalvataggio(path, self.lista_attrezzi)

    def addToList(self, obj):
        self.gobj.addToListAtt(obj, self.lista_attrezzi)
        self.gobj.scriviLista("./Admin/gestione_attrezzi/listaAttrezzi.txt", self.lista_attrezzi)

    def scriviLista(self, path):
        self.gobj.scriviLista(path, self.lista_attrezzi)

    def rimuovi(self, riga):
        self.gobj.rimuoviAttrezzo()
        self.scriviLista("./Admin/gestione_attrezzi/listaAttrezzi.txt")


