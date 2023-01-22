from functools import singledispatch

class Comando:
    ...

class ComandoHandler:
    ...

@singledispatch
def ejecutar_commando(comando):
    raise NotImplementedError(f'No existe implementación para el comando de tipo {type(comando).__name__}')