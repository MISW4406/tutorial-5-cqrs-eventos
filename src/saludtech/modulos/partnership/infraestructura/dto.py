from saludtech.config.db import db
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, ForeignKey, Integer, Table

import uuid

Base = db.declarative_base()

# Tabla intermedia para tener la relación de muchos a muchos entre la tabla reservas e itinerarios


class ProcesoIngestionPartner(db.Model):
    __tablename__ = "proceso_ingestion_partner"
    id_partner = db.Column(db.String, primary_key=True)
    id_proceso_ingestion=db.Column(db.String, primary_key=True)
    fecha_creacion = db.Column(db.String, nullable=False)
    fecha_actualizacion = db.Column(db.String, nullable=False)
