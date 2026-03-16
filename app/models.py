from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime
from .db import Base

class Cliente(Base):
    __tablename__ = "clientes"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    is_active = Column(Boolean, default=True)

    veiculos = relationship("Veiculo", back_populates="proprietario")

class Veiculo(Base):
    __tablename__ = "veiculos"

    id = Column(Integer, primary_key=True, index=True)
    marca = Column(String, index=True)
    modelo = Column(String, index=True)
    ano = Column(Integer)
    motorizacao = Column(String)
    categoria = Column(String)
    cliente_id = Column(Integer, ForeignKey("clientes.id"))

    proprietario = relationship("Cliente", back_populates="veiculos")
    registros_km = relationship("RegistroKM", back_populates="veiculo")
    pneus_instalados = relationship("RegistroPneuVeiculo", back_populates="veiculo")

class Pneu(Base):
    __tablename__ = "pneus"

    id = Column(Integer, primary_key=True, index=True)
    marca = Column(String, index=True)
    modelo = Column(String, index=True)
    largura = Column(Integer)
    perfil = Column(Integer)
    aro = Column(String)
    indice_carga = Column(Integer)
    velocidade = Column(String)

class RegistroPneuVeiculo(Base):
    __tablename__ = "registros_pneus_veiculos"

    id = Column(Integer, primary_key=True, index=True)
    veiculo_id = Column(Integer, ForeignKey("veiculos.id"))
    pneu_id = Column(Integer, ForeignKey("pneus.id"))
    data_instalacao = Column(DateTime, default=datetime.utcnow)
    km_instalacao = Column(Float)

    veiculo = relationship("Veiculo", back_populates="pneus_instalados")

class RegistroKM(Base):
    __tablename__ = "registros_km"

    id = Column(Integer, primary_key=True, index=True)
    veiculo_id = Column(Integer, ForeignKey("veiculos.id"))
    km = Column(Float)
    data_leitura = Column(DateTime, default=datetime.utcnow)

    veiculo = relationship("Veiculo", back_populates="registros_km")
