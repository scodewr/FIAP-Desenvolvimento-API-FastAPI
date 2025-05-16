from fastapi import FastAPI
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from my_basemodel import Item

app = FastAPI(
    title="My FastAPI API",
    version="1.0.0",
    description="API de Exemplo com FastAPI"
)

# Banco de dados de usuários em memória para autenticação
users = {
    "user1": "password1",  # Usuário 1
    "user2": "password2",  # Usuário 2
}

security = HTTPBasic()

def verify_password(credentials: HTTPBasicCredentials = Depends(security)):
    username = credentials.username
    password = credentials.password
    if username in users and users[username] == password:
        return username
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Credenciais inválidas",
        headers={"WWW-Authenticate": "Basic"},
    )

@app.get("/")
async def home():
    return "Hello, FastAPI!"

@app.get("/secure-data")
async def secure_data(username: str = Depends(verify_password)):
    return {"message": f"Hello, {username}!"}

items = []

@app.get("/items")
async def get_items():
    return items

@app.post("/items", status_code=201)
async def create_item(item: Item):
    items.append(item.model_dump())
    return item

@app.put("/items/{item_id}", status_code=200)
async def update_item(item_id: int, item: Item):
    if 0 <= item_id < len(items):
        items[item_id].update(item.model_dump())
        return items[item_id]
    raise HTTPException(status_code=404, detail="Item not found")

@app.delete("/items/{item_id}", status_code=204)
async def delete_item(item_id: int):
    if 0 <= item_id < len(items):
        removed_item = items.pop(item_id)
        return removed_item
    raise HTTPException(status_code=404, detail="Item not found")