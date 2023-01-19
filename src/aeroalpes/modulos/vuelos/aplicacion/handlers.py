from aeroalpes.modulos.vuelos.dominio.eventos import ReservaCreada, ReservaCancelada, ReservaAprobada, ReservaPagada
from aeroalpes.seedwork.aplicacion.handlers import Handler

class HandlerReserva(Handler):

    @staticmethod
    def handle_reserva_creada(evento):
        print(evento)
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


    