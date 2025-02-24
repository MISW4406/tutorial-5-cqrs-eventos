from saludtech.seedwork.dominio.excepciones import ExcepcionFabrica

class TipoObjetoNoExisteEnDominioPartnershipExcepcion(ExcepcionFabrica):
    def __init__(self, mensaje='No existe una fábrica para el tipo solicitado en el módulo de partnership'):
        self.__mensaje = mensaje
    def __str__(self):
        return str(self.__mensaje)