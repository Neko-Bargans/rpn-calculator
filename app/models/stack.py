from random import randint
from typing import List
from sqlmodel import (
    Field,
    SQLModel,
)  # Use sqlmodel to be compliant with both pydantic and sqlalchemy
from sqlalchemy import JSON


class Stack(SQLModel, table=True):
    id: int | None = Field(default=randint(0, 10000), primary_key=True)
    stack: List[int] = Field(default=[], sa_type=JSON)

    def __init__(self):
        super().__init__()
        self.stack = []

    def to_json(self):
        return {"id": self.id, "stack": self.stack}
