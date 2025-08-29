from fastapi import FastAPI, Depends, HTTPException, Query
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, Session
from sqlalchemy.exc import IntegrityError
from fastapi_pagination import Page, add_pagination, paginate

DATABASE_URL = "sqlite:///./test.db"

# Configuração banco
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Modelo
class Atleta(Base):
    __tablename__ = "atletas"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    cpf = Column(String, unique=True, nullable=False)
    centro_treinamento = Column(String, nullable=False)
    categoria = Column(String, nullable=False)

Base.metadata.create_all(bind=engine)

# Dependência de sessão
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app = FastAPI(title="API de Atletas")

# Schemas
from pydantic import BaseModel

class AtletaCreate(BaseModel):
    nome: str
    cpf: str
    centro_treinamento: str
    categoria: str

class AtletaResponse(BaseModel):
    nome: str
    centro_treinamento: str
    categoria: str

# POST - criar atlet
@app.post("/atletas/", response_model=AtletaResponse)
def criar_atleta(atleta: AtletaCreate, db: Session = Depends(get_db)):
    novo = Atleta(**atleta.dict())
    db.add(novo)
    try:
        db.commit()
        db.refresh(novo)
        return novo
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=303,
            detail=f"Já existe um atleta cadastrado com o cpf: {atleta.cpf}"
        )

# GET - listar todos 
@app.get("/atletas/", response_model=Page[AtletaResponse])
def listar_atletas(db: Session = Depends(get_db)):
    atletas = db.query(Atleta).all()
    return paginate(atletas)

# GET - buscar atleta 
@app.get("/atletas/search", response_model=list[AtletaResponse])
def buscar_atleta(
    nome: str = Query(None),
    cpf: str = Query(None),
    db: Session = Depends(get_db)
):
    query = db.query(Atleta)
    if nome:
        query = query.filter(Atleta.nome.ilike(f"%{nome}%"))
    if cpf:
        query = query.filter(Atleta.cpf == cpf)
    return query.all()

# Habilitar paginação
add_pagination(app)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("api_atleta:app", host="127.0.0.1", port=8000, reload=True)
