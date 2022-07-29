from typing import List, TypeVar
from pydantic import BaseModel, Field, StrictStr

class GameModel(BaseModel):
    board: List[int] = Field(min_items=9, max_items=9)
    values: List[int] = Field(min_items=3, max_items=3)