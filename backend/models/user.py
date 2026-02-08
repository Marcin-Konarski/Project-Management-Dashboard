from uuid import UUID
from sqlmodel import SQLModel, Field, Relationship


class User(SQLModel, table=True):
    uuid: UUID = Field(default=None, primary_key=True)
    username: str
    password: str
    # projects: list[Project] = Relationship(back_populates="project")
