from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.blueprints.todo_bp import router as todo_router 

app = FastAPI()

# configure CORS to enable request from frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # starts in port 3000
    allow_credentials=True,
    allow_methods=["*"],  # allow all methods (GET, POST, etc.)
    allow_headers=["*"],  # allow all headers
)

@app.get("/")
async def root():
    return {"message": "Bienvenido a la API de TODO LISTA DE BASF"}

# include router of todo_bp without prefix
app.include_router(todo_router, tags=["todos"])
