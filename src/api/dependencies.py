from typing import Annotated

from fastapi import Depends, Query
from pydantic import BaseModel

class PaginationParams(BaseModel):
    page: Annotated[int | None, Query(1, ge=1)]
    per_page: Annotated[int | None, Query(3, ge=1, lt=100)]

PaginationDep = Annotated[PaginationParams, Depends()]