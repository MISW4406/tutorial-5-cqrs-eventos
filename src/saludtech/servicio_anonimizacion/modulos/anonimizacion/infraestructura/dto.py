from saludtech.servicio_anonimizacion.config.db import db
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, ForeignKey, Integer, Table

import uuid

Base = db.declarative_base()

# Tabla intermedia para la relación entre procesos de anonimización e imágenes
proceso_anonimizacion_imagen = db.Table(
    "proceso_anonimizacion_imagen",
    db.Model.metadata,
    db.Column("proceso_anonimizacion_id", db.String, db.ForeignKey("proceso_anonimizacion.id")),
    db.Column("tipo", db.String),
    db.Column("archivo", db.String),
    db.Column("archivo_original", db.String),
    db.ForeignKeyConstraint(
        ["tipo", "archivo", "archivo_original"],
        ["imagen_anonimizada.tipo", "imagen_anonimizada.archivo", "imagen_anonimizada.archivo_original"]
    )
)

class ImagenAnonimizada(db.Model):
    __tablename__ = "imagen_anonimizada"
    tipo = db.Column(db.String, nullable=False, primary_key=True)
    archivo = db.Column(db.String, nullable=False, primary_key=True)
    archivo_original = db.Column(db.String, nullable=False, primary_key=True)

class ProcesoAnonimizacion(db.Model):
    __tablename__ = "proceso_anonimizacion"
    id = db.Column(db.String, primary_key=True)
    fecha_creacion = db.Column(db.String, nullable=False)
    fecha_actualizacion = db.Column(db.String, nullable=False)
    id_proceso_original = db.Column(db.String, nullable=False)
    imagenes = db.relationship('ImagenAnonimizada', secondary=proceso_anonimizacion_imagen, backref='proceso_anonimizacion')