from pydantic import BaseModel
from typing import Optional, List
from enum import Enum
from uuid import UUID, uuid4

class Gender(str, Enum):
    male="male"
    female="female"

class Role(str, Enum):
    admin="admin"
    user="user"
    student="student"

class Position(str, Enum):
    operacional="Operacional"
    gestao="Gestao"
    executivo="Executivo"

class User (BaseModel):
    id: Optional[UUID] = uuid4() 
    first_name: str
    last_name: str
    middle_name: str
    gender: Gender
    roles:list[Role]

class Police(BaseModel):
    id: Optional[UUID] = uuid4()
    posicao: Optional[Position]
    name: Optional[str]

    
def update_existing_police(existing_police: Police, new_data: Police):
    # Utiliza o método `dict()` para converter a instância em um dicionário
    existing_data = existing_police.dict()
    # Atualiza o dicionário com os valores não nulos da nova instância
    existing_data.update({k: v for k, v in new_data.dict().items() if v is not None})
