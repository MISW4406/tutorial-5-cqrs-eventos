from aeroalpes.modulos.vuelos.dominio.eventos import ReservaCreada, ReservaCancelada, ReservaAprobada, ReservaPagada
from aeroalpes.seedwork.aplicacion.handlers import Handler
from aeroalpes.seedwork.infraestructura.dispatchers import Dispatcher

class HandlerReserva(Handler):

    @Dispatcher.publicar.register(ReservaCreada)
    @classmethod
    def _(cls, evento):
        print('Reserva Creada')

    @Dispatcher.publicar.register(ReservaCancelada)
    @classmethod
    def _(cls, evento):
        print('Reserva Cancelada')

    @Dispatcher.publicar.register(ReservaAprobada)
    @classmethod
    def _(cls, evento):
        print('Reserva Aprobada')

    @Dispatcher.publicar.register(ReservaPagada)
    @classmethod
    def _(cls, evento):
        print('Reserva Pagada')


    