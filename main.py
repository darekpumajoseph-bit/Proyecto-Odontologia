from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime

app = FastAPI()


# CORS


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# MIDDLEWARE


@app.middleware("http")
async def registrar_peticiones(request: Request, call_next):

    print(f"Ruta visitada: {request.url}")
    print(f"Método HTTP: {request.method}")
    print(f"Hora: {datetime.now()}")

    response = await call_next(request)

    return response


# EXCEPCIONES PERSONALIZADAS

class PacienteNoEncontrado(Exception):
    pass

class OdontologoNoEncontrado(Exception):
    pass

class CitaNoEncontrada(Exception):
    pass


# MANEJO GLOBAL DE ERRORES


@app.exception_handler(PacienteNoEncontrado)
async def paciente_error(request: Request, exc: PacienteNoEncontrado):

    return JSONResponse(
        status_code=404,
        content={
            "error": True,
            "mensaje": "Paciente no encontrado",
            "hora": str(datetime.now())
        }
    )

@app.exception_handler(OdontologoNoEncontrado)
async def odontologo_error(request: Request, exc: OdontologoNoEncontrado):

    return JSONResponse(
        status_code=404,
        content={
            "error": True,
            "mensaje": "Odontólogo no encontrado",
            "hora": str(datetime.now())
        }
    )

@app.exception_handler(CitaNoEncontrada)
async def cita_error(request: Request, exc: CitaNoEncontrada):

    return JSONResponse(
        status_code=404,
        content={
            "error": True,
            "mensaje": "Cita no encontrada",
            "hora": str(datetime.now())
        }
    )


# DATOS


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


# PACIENTES


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

    raise PacienteNoEncontrado()

@app.delete("/pacientes/{id}")
def delete_paciente(id: int):

    for p in pacientes:

        if p["id"] == id:

            pacientes.remove(p)

            return {"mensaje": "Paciente eliminado"}

    raise PacienteNoEncontrado()


# ODONTÓLOGOS


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

    raise OdontologoNoEncontrado()

@app.delete("/odontologos/{id}")
def delete_odontologo(id: int):

    for o in odontologos:

        if o["id"] == id:

            odontologos.remove(o)

            return {"mensaje": "Odontólogo eliminado"}

    raise OdontologoNoEncontrado()


# TRATAMIENTOS


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

    return {"error": "Tratamiento no encontrado"}

@app.delete("/tratamientos/{id}")
def delete_tratamiento(id: int):

    for t in tratamientos:

        if t["id"] == id:

            tratamientos.remove(t)

            return {"mensaje": "Tratamiento eliminado"}

    return {"error": "Tratamiento no encontrado"}


# CITAS


@app.get("/citas")
def get_citas():
    return citas

@app.post("/citas")
def post_cita(id: int, paciente: str, odontologo: str):

    nueva = {
        "id": id,
        "paciente": paciente,
        "odontologo": odontologo
    }

    citas.append(nueva)

    return nueva

@app.put("/citas/{id}")
def put_cita(id: int, paciente: str, odontologo: str):

    for c in citas:

        if c["id"] == id:

            c["paciente"] = paciente
            c["odontologo"] = odontologo

            return c

    raise CitaNoEncontrada()

@app.delete("/citas/{id}")
def delete_cita(id: int):

    for c in citas:

        if c["id"] == id:

            citas.remove(c)

            return {"mensaje": "Cita eliminada"}

    raise CitaNoEncontrada()