from aeroalpes.modulos.vuelos.dominio.eventos import ReservaCreada
from aeroalpes.seedwork.aplicacion.handlers import Handler

class HandlerReserva(Handler):

    @staticmethod
    def handle_reserva_creada(evento):
        print(evento)
        print('Reserva Creada en clientes')
        

    