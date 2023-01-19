from functools import singledispatchmethod

class Dispatcher():
    @singledispatchmethod
    @classmethod
    def publicar(cls, evento):
        raise NotImplementedError(f"Tipo {type(evento)} no se sabe procesar")