from pydantic import BaseModel, EmailStr
from typing import List, Optional
from datetime import datetime

# --- Pneu ---
class PneuBase(BaseModel):
    marca: str
    modelo: str
    largura: int
    perfil: int
    aro: str
    indice_carga: int
    velocidade: str

class PneuCreate(PneuBase):
    pass

class Pneu(PneuBase):
    id: int

    class Config:
        from_attributes = True

# --- Registro KM ---
class RegistroKMBase(BaseModel):
    km: float
    data_leitura: datetime = datetime.now()

class RegistroKMCreate(RegistroKMBase):
    veiculo_id: int

class RegistroKM(RegistroKMBase):
    id: int
    veiculo_id: int

    class Config:
        from_attributes = True

# --- Veiculo ---
class VeiculoBase(BaseModel):
    marca: str
    modelo: str
    ano: int
    motorizacao: str
    categoria: str

class VeiculoCreate(VeiculoBase):
    cliente_id: int

class Veiculo(VeiculoBase):
    id: int
    cliente_id: int
    registros_km: List[RegistroKM] = []

    class Config:
        from_attributes = True

# --- Cliente ---
class ClienteBase(BaseModel):
    nome: str
    email: EmailStr
    is_active: bool = True

class ClienteCreate(ClienteBase):
    pass

class Cliente(ClienteBase):
    id: int
    veiculos: List[Veiculo] = []

    class Config:
        from_attributes = True
