from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from ariadne import load_schema_from_path, make_executable_schema
from ariadne.asgi import GraphQL
from .resolvers import query  # ajusta esto a tu archivo de resolvers

type_defs = load_schema_from_path("app/schema.graphql")
schema = make_executable_schema(type_defs, query)

app = FastAPI()

# ✅ Habilita CORS para todas las fuentes
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # O reemplaza "*" por ["http://54.175.97.19"] si quieres restringir
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Monta GraphQL en la raíz
graphql_app = GraphQL(schema, context_value=lambda request: {"request": request})
app.mount("/", graphql_app)
