import saludtech.seedwork.presentacion.api as api
import json
from flask import redirect, render_template, request, session, url_for
from flask import Response
from saludtech.modulos.ingestion.aplicacion.mapeadores import MapeadorProcesoIngestionDTOJson
from saludtech.seedwork.aplicacion.comandos import ejecutar_commando
from saludtech.modulos.ingestion.aplicacion.dto import ProcesoIngestionDTO
from saludtech.seedwork.dominio.excepciones import ExcepcionDominio
from multiprocessing import Process
from saludtech.modulos.ingestion.infraestructura.despachadores import Despachador
from saludtech.modulos.ingestion.aplicacion.comandos.crear_proceso_ingestion import CrearProcesoIngestion
from saludtech.modulos.ingestion.aplicacion.queries.obtener_proceso_ingestion import ObtenerProcesoIngestion
from saludtech.seedwork.aplicacion.queries import ejecutar_query
import saludtech.modulos.ingestion.infraestructura.consumidores as ingestion
import saludtech.modulos.partnership.infraestructura.consumidores as partnership
#from saludtech.modulos.ingestion.infraestructura.despachadores import Despachador

bp = api.crear_blueprint('ingestion', '/ingestion')


@bp.route('/ingestion-comando', methods=('POST',))
def proceso_ingestion_asincronica():
    try:
        proceso_ingestion_dict = request.json

        map_proceso_ingestion = MapeadorProcesoIngestionDTOJson()
        proceso_ingestion_dto = map_proceso_ingestion.externo_a_dto(proceso_ingestion_dict)

        comando = CrearProcesoIngestion(proceso_ingestion_dto.fecha_creacion, proceso_ingestion_dto.fecha_actualizacion, proceso_ingestion_dto.id, proceso_ingestion_dto.imagenes,proceso_ingestion_dto.id_partner)
        hp1=Process(target=ingestion.suscribirse_a_eventos,daemon=True).start()
        hp2=Process(target=partnership.suscribirse_a_comandos,daemon=True).start()
        hp3=Process(target=partnership.suscribirse_a_eventos,daemon=True).start()
        hp4=Process(target=ingestion.suscribirse_a_comandos,daemon=True).start()

        despachador = Despachador()
        despachador.publicar_comando(comando,'comandos-proceso_ingestion')
        
        
        
        return Response('{}', status=202, mimetype='application/json')
    except ExcepcionDominio as e:
        return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')

@bp.route('/proceso-ingestion-query', methods=('GET',))
@bp.route('/proceso-ingestion-query/<id>', methods=('GET',))
def dar_proceso_ingestion(id=None):
    if id:
        query_resultado = ejecutar_query(ObtenerProcesoIngestion(id))
        map_proceso_ingestion = MapeadorProcesoIngestionDTOJson()
        
        return map_proceso_ingestion.dto_a_externo(query_resultado.resultado)
    else:
        return [{'message': 'GET!'}]