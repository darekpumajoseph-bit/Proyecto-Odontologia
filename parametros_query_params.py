from fastapi import FastAPI, Path, Query

app = FastAPI()

# PACIENTES
@app.get("/pacientes/{id}/{documento}")
def pacientes(
    id: int = Path(gt=0),
    documento: str = Path(min_length=5),
    nombre: str = Query(default=None, min_length=3),
    ciudad: str = Query(default=None, min_length=3)
):
    return {
        "id": id,
        "documento": documento,
        "nombre": nombre,
        "ciudad": ciudad
    }

# ODONTOLOGOS
@app.get("/odontologos/{id}/{especialidad}")
def odontologos(
    id: int = Path(gt=0),
    especialidad: str = Path(min_length=3),
    nombre: str = Query(default=None, min_length=3),
    experiencia: int = Query(default=1, gt=0)
):
    return {
        "id": id,
        "especialidad": especialidad,
        "nombre": nombre,
        "experiencia": experiencia
    }