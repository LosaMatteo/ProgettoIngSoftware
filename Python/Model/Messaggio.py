from Data.gestioneObject import gestObj


class Messaggio(object):

    lista_messaggi = []
    gobj = gestObj()

    def __init__(self,mittente = "",destinatario ="",contenuto = "", data = ""):
        self.mittente = mittente
        self.destinatario = destinatario
        self.contenuto = contenuto
        self.data = data

    def popolaLista(self):
        return self.gobj.popolaLista(self.lista_messaggi)

    def recuperaSalvataggio(self, path):
        self.lista_messaggi.clear()
        self.gobj.recuperaSalvataggio(path, self.lista_messaggi)

    def addToList(self, obj):
        self.gobj.addToList(obj, self.lista_messaggi)
        self.scriviLista("./Data/casella_di_messaggi/messaggi.txt")

    def scriviLista(self, path):
        self.gobj.scriviLista(path, self.lista_messaggi)

    def rimuovi_messaggio(self, obj):
        self.gobj.rimuovi_messaggio(obj, self.lista_messaggi)
        self.scriviLista("./Data/casella_di_messaggi/messaggi.txt")

    def getAttributi(self, id):
        return self.gobj.getAttributi(id, self.lista_messaggi)

    def getObject_message(self, id):
       return self.gobj.getObject_message(id, self.lista_messaggi)

    def modificaLista(self, vett, id):
        print("Questo metodo non esiste")
        self.gobj.modificaLista(vett, id, self.lista_messaggi)
        self.scriviLista("./Data/casella_di_messaggi/messaggi.txt")

    def getClCred(self):
        return self.gobj.getUserPass(self.lista_messaggi)

    def reset(self, name):
        self.gobj.resetpassword(name, self.lista_messaggi)
        self.scriviLista("./Data/casella_di_messaggi/messaggi.txt")

    def get_lista(self):
        return self.gobj.get_lista(self.lista_messaggi)
