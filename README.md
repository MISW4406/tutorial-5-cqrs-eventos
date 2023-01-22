# Tutorial 5 - CQRS y manejo de eventos

Repositorio con código base para el uso de un sistema usando el patrón CQRS y usando eventos de dominio e integración para la comunicación asíncrona entre componentes internos parte del mismo contexto acotado y sistemas externos.

Este repositorio está basado en el repositorio de sidecars visto en el tutorial 4 del curso. Por tal motivo, puede usar ese mismo repositorio para entender algunos detalles que este README no cubre.

## Estructura del proyecto

Este repositorio sigue en general la misma estructura del repositorio de origen. Sin embargo, hay un par de adiciones importante mencionar:

- El directorio **src** ahora cuenta con un nuevo directorio llamado **notificaciones**, el cual representa un servicio de mensajería que recibe eventos de integración propagados del sistema de AeroAlpes, por medio de un broker de eventos.
- El directorio **src** ahora también cuenta cuenta con un nuevo directorio llamado **ui**, el cual representa nuestra interfaz gráfica la cual puede recibir por medio de un BFF desarrollado en Python usando websockets, las respuestas de nuestros comandos de forma asíncrona.
- Nuestro proyecto de AeroAlpes ha cambiado de forma considerable. Los siguientes son los cambios relevantes en cada módulo:
    - **api**: En este módulo se modificó el API de `vuelos.py` el cual cuenta con dos nuevos endpoints: `/reserva-commando` y `/reserva-query`, los cuales por detrás de escenas usan un patrón CQRS como la base de su comunicación.
    - **modulos/vuelos/aplicacion**: Este módulo ahora considera los sub-módulos: `queries` y `comandos`. En dichos directorios pdrá ver como se desacopló las diferentes operaciones lectura y escritura. Vea los archivos `obtener_reserva.py` y `crear_reserva.py` para ver como se logra dicho desacoplamiento.
    - 

## AeroAlpes
### Ejecutar Aplicación

Desde el directorio principal ejecute el siguiente comando.

```bash
flask --app src/aeroalpes/api run
```

Siempre puede ejecutarlo en modo DEBUG:

```bash
flask --app src/aeroalpes/api --debug run
```

### Ejecutar pruebas

```bash
coverage run -m pytest
```

### Ver reporte de covertura
```bash
coverage report
```

### Crear imagen Docker

Desde el directorio principal ejecute el siguiente comando.

```bash
docker build . -f aeroalpes.Dockerfile -t aeroalpes/flask
```

### Ejecutar contenedora (sin compose)

Desde el directorio principal ejecute el siguiente comando.

```bash
docker run -p 5000:5000 aeroalpes/flask
```

## Sidecar/Adaptador

### Instalar librerías

En el mundo real es probable que ambos proyectos estén en repositorios separados, pero por motivos pedagógicos y de simpleza, 
estamos dejando ambos proyectos en un mismo repositorio. Sin embargo, usted puede encontrar un archivo `sidecar-requirements.txt`, 
el cual puede usar para instalar las dependencias de Python para el servidor y cliente gRPC.

```bash
pip install -r sidecar-requirements.txt
```

### Ejecutar Servidor

Desde el directorio principal ejecute el siguiente comando.

```bash
python src/sidecar/main.py 
```

### Ejecutar Cliente

Desde el directorio principal ejecute el siguiente comando.

```bash
python src/sidecar/cliente.py 
```

### Compilación gRPC

Desde el directorio `src/sidecar` ejecute el siguiente comando.

```bash
python -m grpc_tools.protoc -Iprotos --python_out=./pb2py --pyi_out=./pb2py --grpc_python_out=./pb2py protos/vuelos.proto
```

### Crear imagen Docker

Desde el directorio principal ejecute el siguiente comando.

```bash
docker build . -f adaptador.Dockerfile -t aeroalpes/adaptador
```

### Ejecutar contenedora (sin compose)

Desde el directorio principal ejecute el siguiente comando.

```bash
docker run -p 50051:50051 aeroalpes/adaptador
```

## Docker-compose

Para desplegar toda la arquitectura en un solo comando, usamos `docker-compose`. Para ello, desde el directorio principal, ejecute el siguiente comando:

```bash
docker-compose up
```

Si desea detener el ambiente ejecute:

```bash
docker-compose stop
```

En caso de querer desplegar dicha topología en el background puede usar el parametro `-d`.

```bash
docker-compose up -d
```

## Comandos útiles

### Listar contenedoras en ejecución
```bash
docker ps
```

### Listar todas las contenedoras
```bash
docker ps -a
```

### Parar contenedora
```bash
docker stop <id_contenedora>
```

### Eliminar contenedora
```bash
docker rm <id_contenedora>
```

### Listar imágenes
```bash
docker images
```

### Eliminar imágenes
```bash
docker images rm <id_imagen>
```

### Acceder a una contendora
```bash
docker exec -it <id_contenedora> sh
```




docker-compose --profile pulsar up

# Servidor BFF (UI)
python src/ui/main.py


# Servidor notificaciones
python src/notificaciones/main.py

fuser -k 8080/tcp


Live Server librería a usar