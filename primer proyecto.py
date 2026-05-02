from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def bienvenida():
    return{"mensaje":"Bienvenidos a nuestra empresa"}
@app.get("/empresa")
def empresa():
    return{"nombre": "Software code S.A."}


@app.get("/")
def informacion():
    return{"mensaje":"Nuestro proposito es:"}
@app.get("/proposito")
def proposito():
    return{"nombre": "Llegar a ser los mas grandes del mundo"}


@app.get("/")
def usuarios():
    return{"mensaje": "bienvenidos a los datos de usuario"}
@app.get("/datos")
def datos_usuarios():
    return {
        "nombre": "Cesar Vega",
        "edad": 18,
        "ciudad de origen": "Bogotá D.C.",


        "nombre": "Jose Benitez",
        "edad": 16,
        "ciudad de origen": "Bogotá D.C.",


        "nombre": "Darek Puerto",
        "edad": 16,
        "ciudad de origen": "Bogotá D.C.",
       
    }


@app.get("/")
def doctores():
    return{"mensaje": "bienvenidos a los datos de dostores"}
@app.get("/datos")
def datos_doctores():
    return {
        "nombre": "Daniela Cuervo",
        "edad": 198,
        "ciudad de origen": "Bogotá D.C.",


        "nombre": "Allison Ibañez",
        "edad": 169,
        "ciudad de origen": "Bogotá D.C.",
       
    }


@app.get("/")
def isumos():
    return{"mensaje": "Cantidad de insumos"}
@app.get("/datos")
def datos_insumos():
    return {
        "nombre": "protesis",
        "cantidad": 50,
       


        "nombre": "cajas de dientes",
        "cantidad": 16,
       
    }
