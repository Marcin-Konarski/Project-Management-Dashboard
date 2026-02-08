from uuid import UUID, uuid4
from typing import Annotated

from pydantic import BaseModel, Field

class Project(BaseModel):
    uuid: UUID = Field(default_factory=uuid4) # Automatically generate random uuid
    name: Annotated[str, Field(min_length=3, max_length=50)]
    description: Annotated[str, Field(max_length=200)] | None = None
    documents: list[str] = Field(default_factory=lambda: list) # I assume the documents would be a list of strings constituting the path to object from S3?? dunno yet. TODO. # TODO 2: make it nullable. # ! Inconsisancy with model in db!!
    # owner: # TODO


# TODO: I need also one additional class in order to allow sharing projects with other users