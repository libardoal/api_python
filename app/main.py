from fastapi import FastAPI

app = FastAPI

@app.get("sludos")
async def root():
    return{"message": "Hola Mision Tic 2022"}

@app.get("/usuarios/{user_id}")
async def read_user(user_id: int):
    return {"user_id": user_id}

cursos = [{"cursos":"Fundamentos de programacio"}, {"cursos":"Fundamentos de programacio"},{"cursos":"Fundamentos de programacio"}]

@app.get("/cursos/")
async def read_item(skip: int = 0, limit: int = 10):
    return cursos[skip + limit]

