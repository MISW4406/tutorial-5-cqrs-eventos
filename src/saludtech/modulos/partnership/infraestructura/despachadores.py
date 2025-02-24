import pulsar
from pulsar.schema import *

from saludtech.modulos.partnership.infraestructura.schema.v1.eventos import EventoProcesoIngestionPartnerAgregado, ProcesoIngestionPartnerAgregadoPayload
from saludtech.modulos.partnership.infraestructura.schema.v1.comandos import ComandoAgregarProcesoIngestionPartner, ComandoAgregarProcesoIngestionPartnerPayload
from saludtech.seedwork.infraestructura import utils

import datetime

epoch = datetime.datetime.utcfromtimestamp(0)

def unix_time_millis(dt):
    return (dt - epoch).total_seconds() * 1000.0

class Despachador:
    def _publicar_mensaje(self, mensaje, topico,schema):
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        publicador = cliente.create_producer(topico, schema=schema)
        publicador.send(mensaje)
        cliente.close()

    def publicar_evento(self, evento, topico):
        
        payload = EventoProcesoIngestionPartnerAgregadoPayload(
            id_proceso_ingestion=str(evento.id_proceso_ingestion), 
            id_partner=str(evento.id_partner), 
            fecha_creacion=int(unix_time_millis(evento.fecha_creacion))
        )
        evento_integracion = EventoProcesoIngestionPartnerAgregado(data=payload)
        self._publicar_mensaje(evento_integracion, topico,AvroSchema(EventoProcesoIngestionPartnerAgregado))

    def publicar_comando(self, comando, topico):
      
        payload = ComandoAgregarProcesoIngestionPartnerPayload(
            id_partner=str(comando.id_partner),
            fecha_creacion= str(comando.fecha_creacion),
            fecha_actualizacion= str(comando.fecha_actualizacion),
            id_proceso_ingestion= str(comando.id_proceso_ingestion)
            
        )
        comando_integracion = ComandoAgregarProcesoIngestionPartner(data=payload)
        self._publicar_mensaje(comando_integracion, topico,AvroSchema(ComandoAgregarProcesoIngestionPartner))
