from fastapi import FastAPI

app = FastAPI(title="Checklist Digital para Oficinas")

@app.get("/")
def home():
    return {
        "status": "Sistema de Checklist da Oficina rodando com sucesso"
    }
python3 -m uvicorn app.main:app --host 0.0.0.0 --port 8000

from fastapi import FastAPI

app = FastAPI(title="Checklist Digital para Oficinas")

@app.get("/")
def home():
    return {
        "status": "Sistema de Checklist da Oficina rodando com sucesso"
    }
from fastapi import FastAPI

app = FastAPI(title="Checklist Digital para Oficinas")

@app.get("/")
def home():
    return {
        "status": "Sistema de Checklist da Oficina rodando com sucesso"
    }
python3 -m uvicorn app.main:app --host 0.0.0.0 --port 8000

git add app/main.py
git commit -m "Corrige endpoint inicial"
git push
^
