import pydantic
from typing import Any, List

from pydantic import Json

from . import utils


class Category(pydantic.BaseModel):
    id: int
    name: str
    complete_name: str | None
    parent_path: str

    class Config:
        orm_mode = True
        getter_dict = utils.GenericOdooGetter

class PublicCategory(pydantic.BaseModel):
    id: int
    name: str
    parent_id: int | None
    sequence: int | None
    parent_path: str
    seo_name: Json[Any] | None

    class Config:
        orm_mode = True
        getter_dict = utils.GenericOdooGetter