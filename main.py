from fastapi import FastAPI
app = FastAPI()
pacientes = [
    {"id": 1, "nombre": "Laura"},
    {"id": 2, "nombre": "Andres"}
]
odontologos = [
    {"id": 1, "nombre": "Dr. Gomez"},
    {"id": 2, "nombre": "Dra. Ruiz"}
]
tratamientos = [
    {"id": 1, "nombre": "Limpieza"},
    {"id": 2, "nombre": "Ortodoncia"}
]
citas = []

@app.get("/pacientes")
def get_pacientes():
    return pacientes
@app.post("/pacientes")
def post_paciente(id: int, nombre: str):
    nuevo = {"id": id, "nombre": nombre}
    pacientes.append(nuevo)
    return nuevo
@app.put("/pacientes/{id}")
def put_paciente(id: int, nombre: str):
    for p in pacientes:
        if p["id"] == id:
            p["nombre"] = nombre
            return p
    return {"error": "No encontrado"}
@app.delete("/pacientes/{id}")
def delete_paciente(id: int):
    for p in pacientes:
        if p["id"] == id:
            pacientes.remove(p)
            return {"mensaje": "Eliminado"}
    return {"error": "No encontrado"}
@app.get("/odontologos")
def get_odontologos():
    return odontologos
@app.post("/odontologos")
def post_odontologo(id: int, nombre: str):
    nuevo = {"id": id, "nombre": nombre}
    odontologos.append(nuevo)
    return nuevo
@app.put("/odontologos/{id}")
def put_odontologo(id: int, nombre: str):
    for o in odontologos:
        if o["id"] == id:
            o["nombre"] = nombre
            return o
    return {"error": "No encontrado"}
@app.delete("/odontologos/{id}")
def delete_odontologo(id: int):
    for o in odontologos:
        if o["id"] == id:
            odontologos.remove(o)
            return {"mensaje": "Eliminado"}
    return {"error": "No encontrado"}
@app.get("/tratamientos")
def get_tratamientos():
    return tratamientos

@app.post("/tratamientos")
def post_tratamiento(id: int, nombre: str):
    nuevo = {"id": id, "nombre": nombre}
    tratamientos.append(nuevo)
    return nuevo
@app.put("/tratamientos/{id}")
def put_tratamiento(id: int, nombre: str):
    for t in tratamientos:
        if t["id"] == id:
            t["nombre"] = nombre
            return t
    return {"error": "No encontrado"}
@app.delete("/tratamientos/{id}")
def delete_tratamiento(id: int):
    for t in tratamientos:
        if t["id"] == id:
            tratamientos.remove(t)
            return {"mensaje": "Eliminado"}
    return {"error": "No encontrado"}
@app.get("/citas")
def get_citas():
    return citas

@app.post("/citas")
def post_cita(id: int, paciente: str, odontologo: str):
    nueva = {"id": id, "paciente": paciente, "odontologo": odontologo}
    citas.append(nueva)
    return nueva

@app.put("/citas/{id}")
def put_cita(id: int, paciente: str, odontologo: str):
    for c in citas:
        if c["id"] == id:
            c["paciente"] = paciente
            c["odontologo"] = odontologo
            return c
    return {"error": "No encontrado"}

@app.delete("/citas/{id}")
def delete_cita(id: int):
    for c in citas:
        if c["id"] == id:
            citas.remove(c)
            return {"mensaje": "Eliminado"}
    return {"error": "No encontrado"}

