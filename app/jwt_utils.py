import jwt
from fastapi import HTTPException
from .config import JWT_SECRET

def verify_token(token: str):
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=["HS256"])
        if "email" not in payload or "role" not in payload:
            raise HTTPException(status_code=403, detail="Token sin información suficiente")
        return payload
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expirado")
    except jwt.DecodeError:
        raise HTTPException(status_code=401, detail="Token mal formado")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Token inválido")
