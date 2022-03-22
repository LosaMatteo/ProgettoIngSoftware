from Data.gestioneObject import gestObj


class Abbonamento(object):
    listaAbb = []
    gobj = gestObj()
    def __init__(self, data_iscrizione="", data_certificato_medico="", tipo_di_abbonamento=""):
        if data_iscrizione != "":
            self.data_iscrizione = data_iscrizione
            self.data_certificato_medico = data_certificato_medico
            self.tipo_di_abbonamento = tipo_di_abbonamento

    def addToList(self, obj):
        self.gobj.addToList(obj, self.listaAbb)


    def getObj(self):
        tempvar = self.listaAbb[0]
        self.listaAbb.pop()
        return tempvar