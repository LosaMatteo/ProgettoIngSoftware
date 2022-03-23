from Python.Data.gestioneObject import gestObj


class Abbonamento(object):
    lista_abbonamento = []
    gobj = gestObj()
    def __init__(self, data_iscrizione="", data_certificato_medico="", tipo_di_abbonamento=""):
        if data_iscrizione != "":
            self.data_iscrizione = data_iscrizione
            self.data_certificato_medico = data_certificato_medico
            self.tipo_di_abbonamento = tipo_di_abbonamento

    def addToList(self, obj):
        self.gobj.addToList(obj, self.lista_abbonamento)


    def getObj(self):
        oggetto = self.lista_abbonamento[0]
        self.lista_abbonamento.pop()
        return oggetto