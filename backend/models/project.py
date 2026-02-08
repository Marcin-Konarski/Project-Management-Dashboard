from uuid import UUID
from sqlmodel import SQLModel, Field


class Project(SQLModel, table=True):
    uuid: UUID = Field(default=None, primary_key=True)
    name: str
    description: str | None = None
    # documents: list[str] | None = None
    owner_id: UUID = Field(foreign_key="user.uuid")

