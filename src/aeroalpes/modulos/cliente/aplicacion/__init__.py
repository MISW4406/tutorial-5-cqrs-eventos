from pydispatch import dispatcher
from .handlers import HandlerReserva

dispatcher.connect(HandlerReserva.handle_reserva_creada, signal='ReservaCreada')
