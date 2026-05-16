from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field, EmailStr
from typing import Optional, List
from datetime import date, datetime

app = FastAPI(
    title="Sistema de Gestión Odontológica - Proyecto SENA",
    description="API Completa con operaciones CRUD (GET, POST, PUT, DELETE) para la gestión clínica.",
    version="1.0.0"
)


class Paciente(BaseModel):
    id: int = Field(gt=0, description="ID interno mayor a 0")
    documento: str = Field(description="Cédula o TI")
    nombre: str = Field(min_length=3,max_length=50,  description="Nombres completos")
    apellido: str = Field(min_length=3,max_length=50,  description="Apellidos completos")
    email: EmailStr = Field(description="Correo electrónico")
    telefono: str = Field(min_length=7, max_length=15, description="Teléfono celular o fijo")
    fecha_nacimiento: date = Field(description="Fecha de nacimiento YYYY-MM-DD")
    tipo_sangre: str = Field(min_length=2, max_length=4, description="Ej: O+, A-")

class Odontologo(BaseModel):
    id: int = Field(gt=0, description="ID mayor a 0")
    tarjeta_profesional: str = Field(min_length=5, max_length=20, description="Registro médico")
    nombre: str = Field(min_length=3, max_length=50, description="Nombre del profesional")
    apellido: str = Field(min_length=3, max_length=50, description="Apellido del profesional")
    especialidad: str = Field(min_length=5, max_length=50, description="Ej: Ortodoncia, Endodoncia")
    email: EmailStr = Field(description="Correo institucional")
    telefono: str = Field(min_length=7, max_length=15, description="Teléfono de contacto")

class Cita(BaseModel):
    id: int = Field(gt=0, description="ID de la cita mayor a 0")
    paciente_id: int = Field(gt=0, description="ID del paciente asociado")
    odontologo_id: int = Field(gt=0, description="ID del odontólogo asignado")
    fecha_hora: datetime = Field(description="Fecha y hora (YYYY-MM-DD HH:MM:SS)")
    motivo: str = Field( max_length=250, description="Motivo de la consulta")
    estado: str = Field(default="Pendiente", description="Pendiente, Completada, Cancelada")

class Tratamiento(BaseModel):
    id: int = Field(gt=0, description="ID del tratamiento mayor a 0")
    nombre: str = Field( max_length=100, description="Nombre del tratamiento")
    costo: float = Field(gt=0, description="Precio mayor a 0")
    duracion_estimada_dias: int = Field(gt=0, description="Duración aproximada en días")

class HistoriaClinica(BaseModel):
    id: int = Field(gt=0, description="ID del registro clínico")
    paciente_id: int = Field(gt=0, description="ID del paciente")
    odontologo_id: int = Field(gt=0, description="ID del odontólogo")
    fecha_registro: date = Field(default_factory=date.today, description="Fecha de atención")
    diagnostico: str = Field(min_length=10, description="Diagnóstico médico")
    observaciones: Optional[str] = Field(None, description="Notas adicionales")

class ProveedorOdontologico(BaseModel):
    id: int = Field(gt=0, description="ID del proveedor")
    nit: str = Field(min_length=9, max_length=15, description="NIT de la empresa")
    razon_social: str = Field(min_length=3, max_length=100, description="Nombre de la empresa")
    telefono: str = Field(min_length=7, max_length=15, description="Teléfono de contacto")
    direccion: str = Field(min_length=5, description="Dirección de la empresa")
    insumo_principal: str = Field(min_length=3, description="Material que provee")


@app.get("/", tags=["Inicio"])
def inicio():
    return {
        "mensaje": "API de Gestión Odontológica funcionando con CRUD completo",
        "proyecto": "Evidencia SENA 2026",
        "documentacion_interactiva": "/docs"
    }


@app.post("/pacientes", status_code=status.HTTP_201_CREATED, tags=["Pacientes"])
def crear_paciente(paciente: Paciente):
    return {"mensaje": "POST: Paciente registrado exitosamente", "datos": paciente}

@app.get("/pacientes", tags=["Pacientes"])
def obtener_pacientes():
    return {"mensaje": "GET: Listado de todos los pacientes devuelto con éxito"}

@app.get("/pacientes/{paciente_id}", tags=["Pacientes"])
def obtener_paciente_por_id(paciente_id: int):
    return {"mensaje": f"GET: Buscando detalles del paciente con ID {paciente_id}"}

@app.put("/pacientes/{paciente_id}", tags=["Pacientes"])
def actualizar_paciente(paciente_id: int, paciente_actualizado: Paciente):
    return {"mensaje": f"PUT: Paciente con ID {paciente_id} actualizado por completo", "datos": paciente_actualizado}

@app.delete("/pacientes/{paciente_id}", tags=["Pacientes"])
def eliminar_paciente(paciente_id: int):
    return {"mensaje": f"DELETE: Paciente con ID {paciente_id} removido del sistema"}


@app.post("/odontologos", status_code=status.HTTP_201_CREATED, tags=["Odontólogos"])
def crear_odontologo(odontologo: Odontologo):
    return {"mensaje": "POST: Odontólogo registrado en el sistema", "datos": odontologo}

@app.get("/odontologos", tags=["Odontólogos"])
def obtener_odontologos():
    return {"mensaje": "GET: Lista del personal médico odontológico disponible"}

@app.get("/odontologos/{odontologo_id}", tags=["Odontólogos"])
def obtener_odontologo_por_id(odontologo_id: int):
    return {"mensaje": f"GET: Detalles del odontólogo con ID {odontologo_id}"}

@app.put("/odontologos/{odontologo_id}", tags=["Odontólogos"])
def actualizar_odontologo(odontologo_id: int, odontologo_actualizado: Odontologo):
    return {"mensaje": f"PUT: Perfil del odontólogo con ID {odontologo_id} actualizado", "datos": odontologo_actualizado}

@app.delete("/odontologos/{odontologo_id}", tags=["Odontólogos"])
def eliminar_odontologo(odontologo_id: int):
    return {"mensaje": f"DELETE: Odontólogo con ID {odontologo_id} dado de baja"}


@app.post("/citas", status_code=status.HTTP_201_CREATED, tags=["Citas Médicas"])
def agendar_cita(cita: Cita):
    return {"mensaje": "POST: Nueva cita odontológica agendada", "datos": cita}

@app.get("/citas", tags=["Citas Médicas"])
def obtener_citas():
    return {"mensaje": "GET: Calendario de citas médicas devuelto"}

@app.get("/citas/{cita_id}", tags=["Citas Médicas"])
def obtener_cita_por_id(cita_id: int):
    return {"mensaje": f"GET: Consultando información de la cita ID {cita_id}"}

@app.put("/citas/{cita_id}", tags=["Citas Médicas"])
def modificar_cita(cita_id: int, cita_actualizada: Cita):
    return {"mensaje": f"PUT: Datos o estado de la cita ID {cita_id} modificados", "datos": cita_actualizada}

@app.delete("/citas/{cita_id}", tags=["Citas Médicas"])
def cancelar_cita(cita_id: int):
    return {"mensaje": f"DELETE: Cita médica ID {cita_id} cancelada y eliminada"}


@app.post("/tratamientos", status_code=status.HTTP_201_CREATED, tags=["Tratamientos"])
def crear_tratamiento(tratamiento: Tratamiento):
    return {"mensaje": "POST: Nuevo servicio añadido al catálogo de tratamientos", "datos": tratamiento}

@app.get("/tratamientos", tags=["Tratamientos"])
def obtener_tratamientos():
    return {"mensaje": "GET: Catálogo de tratamientos y costos vigentes"}

@app.get("/tratamientos/{tratamiento_id}", tags=["Tratamientos"])
def obtener_tratamiento_por_id(tratamiento_id: int):
    return {"mensaje": f"GET: Información del tratamiento ID {tratamiento_id}"}

@app.put("/tratamientos/{tratamiento_id}", tags=["Tratamientos"])
def actualizar_tratamiento(tratamiento_id: int, tratamiento_actualizado: Tratamiento):
    return {"mensaje": f"PUT: Costo y parámetros del tratamiento ID {tratamiento_id} actualizados", "datos": tratamiento_actualizado}

@app.delete("/tratamientos/{tratamiento_id}", tags=["Tratamientos"])
def eliminar_tratamiento(tratamiento_id: int):
    return {"mensaje": f"DELETE: Tratamiento ID {tratamiento_id} retirado del portafolio"}


@app.post("/historias-clinicas", status_code=status.HTTP_201_CREATED, tags=["Historias Clínicas"])
def crear_registro_clinico(historia: HistoriaClinica):
    return {"mensaje": "POST: Nueva entrada registrada en la historia clínica", "datos": historia}

@app.get("/historias-clinicas", tags=["Historias Clínicas"])
def obtener_historias_clinicas():
    return {"mensaje": "GET: Listado global de registros clínicos"}

@app.get("/historias-clinicas/{historia_id}", tags=["Historias Clínicas"])
def obtener_historia_por_id(historia_id: int):
    return {"mensaje": f"GET: Viendo registro clínico ID {historia_id}"}

@app.put("/historias-clinicas/{historia_id}", tags=["Historias Clínicas"])
def actualizar_historia_clinica(historia_id: int, historia_actualizada: HistoriaClinica):
    return {"mensaje": f"PUT: Registro de evolución clínica ID {historia_id} editado", "datos": historia_actualizada}

@app.delete("/historias-clinicas/{historia_id}", tags=["Historias Clínicas"])
def eliminar_registro_clinico(historia_id: int):
    return {"mensaje": f"DELETE: Registro clínico ID {historia_id} eliminado"}


@app.post("/proveedores", status_code=status.HTTP_201_CREATED, tags=["Proveedores de Insumos"])
def crear_proveedor(proveedor: ProveedorOdontologico):
    return {"mensaje": "POST: Proveedor de insumos creado con éxito", "datos": proveedor}

@app.get("/proveedores", tags=["Proveedores de Insumos"])
def obtener_proveedores():
    return {"mensaje": "GET: Listado de empresas proveedoras de material clínico"}

@app.get("/proveedores/{proveedor_id}", tags=["Proveedores de Insumos"])
def obtener_proveedor_por_id(proveedor_id: int):
    return {"mensaje": f"GET: Mostrando datos del proveedor ID {proveedor_id}"}

@app.put("/proveedores/{proveedor_id}", tags=["Proveedores de Insumos"])
def actualizar_proveedor(proveedor_id: int, proveedor_actualizado: ProveedorOdontologico):
    return {"mensaje": f"PUT: Información comercial del proveedor ID {proveedor_id} actualizada", "datos": proveedor_actualizado}

@app.delete("/proveedores/{proveedor_id}", tags=["Proveedores de Insumos"])
def eliminar_proveedor(proveedor_id: int):
    return {"mensaje": f"DELETE: Proveedor ID {proveedor_id} removido del sistema"}
