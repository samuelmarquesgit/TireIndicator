from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from . import crud, models, schemas, db, services

models.Base.metadata.create_all(bind=db.engine)

app = FastAPI(title="Tirindicator API")

@app.get("/")
def read_root():
    return {"message": "Bem-vindo à API do Tirindicator"}

# --- FIPE ---
@app.get("/fipe/marcas")
def list_marcas():
    return services.FipeService.get_marcas()

@app.get("/fipe/marcas/{marca_id}/modelos")
def list_modelos(marca_id: str):
    return services.FipeService.get_modelos(marca_id)

@app.get("/fipe/marcas/{marca_id}/modelos/{modelo_id}/anos")
def list_anos(marca_id: str, modelo_id: str):
    return services.FipeService.get_anos(marca_id, modelo_id)

# --- Recomendação ---
@app.get("/recomendação/{veiculo_id}")
def recommend_tires(veiculo_id: int, database: Session = Depends(db.get_db)):
    # Busca info do veículo no banco para pegar a categoria
    veiculos = database.query(models.Veiculo).filter(models.Veiculo.id == veiculo_id).first()
    if not veiculos:
        raise HTTPException(status_code=404, detail="Veículo não encontrado")
    
    veiculo_info = {
        "marca": veiculos.marca,
        "modelo": veiculos.modelo,
        "categoria": veiculos.categoria
    }
    return services.RecommendationEngine.recommend_tires(veiculo_info)

# --- Clientes ---
@app.post("/clientes/", response_model=schemas.Cliente)
def create_cliente(cliente: schemas.ClienteCreate, database: Session = Depends(db.get_db)):
    db_cliente = crud.get_cliente_by_email(database, email=cliente.email)
    if db_cliente:
        raise HTTPException(status_code=400, detail="Email já cadastrado")
    return crud.create_cliente(database, cliente=cliente)

@app.get("/clientes/", response_model=List[schemas.Cliente])
def read_clientes(skip: int = 0, limit: int = 100, database: Session = Depends(db.get_db)):
    clientes = crud.get_clientes(database, skip=skip, limit=limit)
    return clientes

@app.get("/clientes/{cliente_id}", response_model=schemas.Cliente)
def read_cliente(cliente_id: int, database: Session = Depends(db.get_db)):
    db_cliente = crud.get_cliente(database, cliente_id=cliente_id)
    if db_cliente is None:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")
    return db_cliente

# --- Veículos ---
@app.post("/veiculos/", response_model=schemas.Veiculo)
def create_veiculo(veiculo: schemas.VeiculoCreate, database: Session = Depends(db.get_db)):
    return crud.create_veiculo(database, veiculo=veiculo)

@app.get("/clientes/{cliente_id}/veiculos", response_model=List[schemas.Veiculo])
def read_veiculos(cliente_id: int, database: Session = Depends(db.get_db)):
    return crud.get_veiculos_by_cliente(database, cliente_id=cliente_id)

# --- Pneus ---
@app.get("/pneus/", response_model=List[schemas.Pneu])
def read_pneus(skip: int = 0, limit: int = 100, database: Session = Depends(db.get_db)):
    return crud.get_pneus(database, skip=skip, limit=limit)

@app.post("/pneus/", response_model=schemas.Pneu)
def create_pneu(pneu: schemas.PneuCreate, database: Session = Depends(db.get_db)):
    return crud.create_pneu(database, pneu=pneu)
