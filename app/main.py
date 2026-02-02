from fastapi import FastAPI

app = FastAPI(title="Checklist Digital para Oficinas")

@app.get("/")
def home():
    return {
        "status": "Sistema de Checklist da Oficina rodando com sucesso"
    }
