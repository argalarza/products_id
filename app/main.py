from fastapi import FastAPI
from ariadne import load_schema_from_path, make_executable_schema
from ariadne.asgi import GraphQL
from .resolvers import query

type_defs = load_schema_from_path("app/schema.graphql")
schema = make_executable_schema(type_defs, query)

app = FastAPI()
graphql_app = GraphQL(schema, context_value=lambda request: {"request": request})
app.mount("/", graphql_app)
