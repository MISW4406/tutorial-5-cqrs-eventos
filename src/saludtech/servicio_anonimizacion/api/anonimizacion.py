import saludtech.servicio_anonimizacion.seedwork.presentacion.api as api
import json
from flask import redirect, render_template, request, session, url_for
from flask import Response
from saludtech.servicio_anonimizacion.modulos.anonimizacion.aplicacion.mapeadores import MapeadorProcesoAnonimizacionDTOJson
from saludtech.servicio_anonimizacion.seedwork.aplicacion.comandos import ejecutar_commando
from saludtech.servicio_anonimizacion.modulos.anonimizacion.aplicacion.dto import ProcesoAnonimizacionDTO
from saludtech.servicio_anonimizacion.seedwork.dominio.excepciones import ExcepcionDominio

from saludtech.servicio_anonimizacion.modulos.anonimizacion.infraestructura.despachadores import Despachador
from saludtech.servicio_anonimizacion.modulos.anonimizacion.aplicacion.comandos.anonimizar_proceso import AnonimizarProceso
from saludtech.servicio_anonimizacion.modulos.anonimizacion.aplicacion.queries.obtener_proceso_anonimizado import ObtenerProcesoAnonimizado
from saludtech.servicio_anonimizacion.seedwork.aplicacion.queries import ejecutar_query

bp = api.crear_blueprint('anonimizacion', '/anonimizacion')

@bp.route('/anonimizacion-comando', methods=('POST',))
def proceso_anonimizacion_asincronica():
    try:
        proceso_anonimizacion_dict = request.json
        
        map_proceso_anonimizacion = MapeadorProcesoAnonimizacionDTOJson()
        proceso_anonimizacion_dto = map_proceso_anonimizacion.externo_a_dto(proceso_anonimizacion_dict)
        
        comando = AnonimizarProceso(
            proceso_anonimizacion_dto.fecha_creacion, 
            proceso_anonimizacion_dto.fecha_actualizacion, 
            proceso_anonimizacion_dto.id, 
            proceso_anonimizacion_dto.imagenes,
            proceso_anonimizacion_dto.id_proceso_original
        )
        
        # Publicar el comando para procesamiento asíncrono
        despachador = Despachador()
        despachador.publicar_comando(comando, 'comandos-proceso_anonimizacion')
        
        return Response('{}', status=202, mimetype='application/json')
    except ExcepcionDominio as e:
        return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')

@bp.route('/proceso-anonimizado-query', methods=('GET',))
@bp.route('/proceso-anonimizado-query/<id>', methods=('GET',))
def dar_proceso_anonimizado(id=None):
    if id:
        query_resultado = ejecutar_query(ObtenerProcesoAnonimizado(id))
        map_proceso_anonimizacion = MapeadorProcesoAnonimizacionDTOJson()
        
        return map_proceso_anonimizacion.dto_a_externo(query_resultado.resultado)
    else:
        return [{'message': 'GET!'}]