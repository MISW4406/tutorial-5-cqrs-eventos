from pydispatch import dispatcher

from .handlers import HandlerReserva

from aeroalpes.modulos.vuelos.dominio.eventos import ReservaCreada, ReservaCancelada, ReservaAprobada, ReservaPagada

dispatcher.connect(HandlerReserva.handle_reserva_creada, signal=ReservaCreada.__name__)
dispatcher.connect(HandlerReserva.handle_reserva_cancelada, signal=ReservaCancelada.__name__)
dispatcher.connect(HandlerReserva.handle_reserva_pagada, signal=ReservaPagada.__name__)
dispatcher.connect(HandlerReserva.handle_reserva_aprobada, signal=ReservaAprobada.__name__)