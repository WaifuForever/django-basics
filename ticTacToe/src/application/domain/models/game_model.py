from typing import List, TypeVar
from pydantic import BaseModel, Field, StrictStr

T = TypeVar("T")

class GameModel(BaseModel):
    board: List[T] = Field(min_items=9, max_items=9)
    values: List[T] = Field(min_items=3, max_items=3)