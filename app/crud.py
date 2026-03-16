from sqlalchemy.orm import Session
from . import models, schemas

# --- Cliente ---
def get_cliente(db: Session, cliente_id: int):
    return db.query(models.Cliente).filter(models.Cliente.id == cliente_id).first()

def get_cliente_by_email(db: Session, email: str):
    return db.query(models.Cliente).filter(models.Cliente.email == email).first()

def get_clientes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Cliente).offset(skip).limit(limit).all()

def create_cliente(db: Session, cliente: schemas.ClienteCreate):
    db_cliente = models.Cliente(nome=cliente.nome, email=cliente.email, is_active=cliente.is_active)
    db.add(db_cliente)
    db.commit()
    db.refresh(db_cliente)
    return db_cliente

# --- Veiculo ---
def create_veiculo(db: Session, veiculo: schemas.VeiculoCreate):
    db_veiculo = models.Veiculo(**veiculo.dict())
    db.add(db_veiculo)
    db.commit()
    db.refresh(db_veiculo)
    return db_veiculo

def get_veiculos_by_cliente(db: Session, cliente_id: int):
    return db.query(models.Veiculo).filter(models.Veiculo.cliente_id == cliente_id).all()

# --- Pneu ---
def get_pneus(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Pneu).offset(skip).limit(limit).all()

def create_pneu(db: Session, pneu: schemas.PneuCreate):
    db_pneu = models.Pneu(**pneu.dict())
    db.add(db_pneu)
    db.commit()
    db.refresh(db_pneu)
    return db_pneu

# --- KM ---
def create_registro_km(db: Session, registro: schemas.RegistroKMCreate):
    db_km = models.RegistroKM(**registro.dict())
    db.add(db_km)
    db.commit()
    db.refresh(db_km)
    return db_km
