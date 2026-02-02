from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime
from typing import List

app = FastAPI(title="Checklist Digital para Oficinas")

# modelo do checklist
class Checklist(BaseModel):
    placa: str
    veiculo: str
    km: int
    motor: bool
    freios: bool
    eletrica: bool
    observacoes: str | None = None

# “banco” em memória (vai zerar quando reiniciar)
checklists: List[dict] = []

@app.get("/")
def home():
    return {
        "status": "Sistema de Checklist da Oficina rodando com sucesso"
    }

# criar checklist
@app.post("/checklist")
def criar_checklist(dados: Checklist):
    registro = dados.dict()
    registro["data"] = datetime.now().isoformat()
    checklists.append(registro)
    return {"mensagem": "Checklist salvo com sucesso", "dados": registro}

# listar todos
@app.get("/checklist")
def listar_checklists():
    return checklists
