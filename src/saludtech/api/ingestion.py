import json
from flask import redirect, render_template, request, session, url_for
from flask import Response
from saludtech.modulos.ingestion.aplicacion.mapeadores import MapeadorIngestionDTOJson
from saludtech.seedwork.aplicacion.comandos import ejecutar_commando
from saludtech.seedwork.aplicacion.queries import ejecutar_query
from saludtech.seedwork.dominio.excepciones import ExcepcionDominio
from saludtech.modulos.vuelos.aplicacion.comandos.crear_reserva import CrearReserva
from saludtech.modulos.vuelos.aplicacion.queries.obtener_reserva import ObtenerReserva

@bp.route('/ingestion-comando', methods=('POST',))
def proceso_ingestion_asincronica():
    try:
        proceso_ingestion_dict = request.json

        map_proceso_ingestion = MapeadorProcesoIngestionDTOJson()
        proceso_ingestion_dto = map_proceso_ingestion.externo_a_dto(proceso_ingestion_dict)

        comando = CrearProcesoIngestion(proceso_ingestion_dto.fecha_creacion, proceso_ingestion_dto.fecha_actualizacion, proceso_ingestion_dto.id, proceso_ingestion_dto.imagenes)
        
        # TODO Reemplaze es todo código sincrono y use el broker de eventos para propagar este comando de forma asíncrona
        # Revise la clase Despachador de la capa de infraestructura
        ejecutar_commando(comando)
        
        return Response('{}', status=202, mimetype='application/json')
    except ExcepcionDominio as e:
        return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')

@bp.route('/reserva-query', methods=('GET',))
@bp.route('/reserva-query/<id>', methods=('GET',))
def dar_proceso_ingestion(id=None):
    if id:
        query_resultado = ejecutar_query(ObtenerProcesoIngestion(id))
        map_proceso_ingestion = MapeadorProcesoIngestionDTOJson()
        
        return map_proceso_ingestion.dto_a_externo(query_resultado.resultado)
    else:
        return [{'message': 'GET!'}]