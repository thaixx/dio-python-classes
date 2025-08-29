import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from api_atleta import app, Base, get_db, Atleta

# Banco de teste
SQLALCHEMY_DATABASE_URL = "sqlite:///./test_test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Recriar tabelas
Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

# Sobrescrever a dependência de DB
def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

# --- TESTES ---
def test_criar_atleta():
    response = client.post("/atletas/", json={
        "nome": "João",
        "cpf": "12345678901",
        "centro_treinamento": "Centro A",
        "categoria": "Adulto"
    })
    assert response.status_code == 200
    data = response.json()
    assert data["nome"] == "João"
    assert data["centro_treinamento"] == "Centro A"

def test_criar_atleta_duplicado():
    response = client.post("/atletas/", json={
        "nome": "Maria",
        "cpf": "12345678901",
        "centro_treinamento": "Centro B",
        "categoria": "Adulto"
    })
    assert response.status_code == 303
    assert "Já existe um atleta" in response.json()["detail"]

def test_listar_atletas():
    response = client.get("/atletas/")
    assert response.status_code == 200
    data = response.json()
    assert data["total"] == 1  

def test_buscar_atleta_por_nome():
    response = client.get("/atletas/search", params={"nome": "João"})
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]["nome"] == "João"
