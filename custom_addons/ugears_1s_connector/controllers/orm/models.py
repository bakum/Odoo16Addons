import pydantic

from . import utils


class Company(pydantic.BaseModel):
    id: int
    name: str
    display_name: str

    class Config:
        orm_mode = True
        getter_dict = utils.GenericOdooGetter


class User(pydantic.BaseModel):
    id: int
    login: str
    im_status: str
    company_id: Company

    class Config:
        orm_mode = True
        getter_dict = utils.GenericOdooGetter
