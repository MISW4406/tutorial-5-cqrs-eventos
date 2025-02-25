from saludtech.config.db import db
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, ForeignKey, Integer, Table

import uuid

Base = db.declarative_base()

# Tabla intermedia para tener la relación de muchos a muchos entre la tabla reservas e itinerarios
proceso_ingestion_imagen = db.Table(
    "proceso_ingestion_imagen",
    db.Model.metadata,
    db.Column("proceso_ingestion_id", db.String, db.ForeignKey("proceso_ingestion.id")),
    db.Column("tipo", db.String),
    db.Column("archivo", db.String),
    db.ForeignKeyConstraint(
        ["tipo", "archivo"],
        ["imagen.tipo", "imagen.archivo"]
    )
)

class Imagen(db.Model):
    __tablename__ = "imagen"
    tipo = db.Column(db.String, nullable=False, primary_key=True)
    archivo= db.Column(db.String, nullable=False, primary_key=True)


class ProcesoIngestion(db.Model):
    __tablename__ = "proceso_ingestion"
    id = db.Column(db.String, primary_key=True)
    fecha_creacion = db.Column(db.DateTime, nullable=False)
    fecha_actualizacion = db.Column(db.DateTime, nullable=False)
    imagenes = db.relationship('Imagen', secondary=proceso_ingestion_imagen, backref='proceso_ingestion')
