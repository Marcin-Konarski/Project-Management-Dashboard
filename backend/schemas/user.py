from uuid import UUID, uuid4
from typing import Annotated

from pydantic import BaseModel, SecretStr, Field

class User(BaseModel):
    uuid: UUID = Field(default_factory=uuid4)
    username: Annotated[str, Field(min_length=3, max_length=50)]
    password: Annotated[SecretStr, Field(min_length=8, max_length=50)] # TODO: Deal with hasing passwords in some way

