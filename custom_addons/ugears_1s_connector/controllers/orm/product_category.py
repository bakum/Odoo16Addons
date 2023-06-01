import pydantic

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
    complete_name: str | None
    parent_path: str

    class Config:
        orm_mode = True
        getter_dict = utils.GenericOdooGetter