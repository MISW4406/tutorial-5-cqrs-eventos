from aeroalpes.modulos.vuelos.dominio.eventos import ReservaCreada, ReservaCancelada, ReservaAprobada, ReservaPagada
from aeroalpes.seedwork.aplicacion.handlers import Handler
from aeroalpes.modulos.vuelos.infraestructura.despachadores import Despachador

class HandlerReserva(Handler):

    @staticmethod
    def handle_reserva_creada(evento):
        print(evento)

        despachador = Despachador()
        despachador.publicar(evento)        

        print('Reserva Creada en Reservas')

    @staticmethod
    def handle_reserva_cancelada(evento):
        print('Reserva Cancelada')

    @staticmethod
    def handle_reserva_aprobada(evento):
        print('Reserva Aprobada')

    @staticmethod
    def handle_reserva_pagada(evento):
        print('Reserva Pagada')


    