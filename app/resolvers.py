from ariadne import QueryType
from fastapi import Request
from .models import product_collection
from .jwt_utils import verify_token
from bson import ObjectId

query = QueryType()

@query.field("getProductById")
def resolve_get_product_by_id(_, info, id):
    request: Request = info.context["request"]
    auth_header = request.headers.get("Authorization")

    if not auth_header or not auth_header.startswith("Bearer "):
        raise Exception("Falta el token")

    token = auth_header.split(" ")[1]
    user = verify_token(token)

    try:
        product = product_collection.find_one({"_id": ObjectId(id)})
    except:
        raise Exception("ID inválido")

    if not product:
        raise Exception("Producto no encontrado")

    product["_id"] = str(product["_id"])
    return product
