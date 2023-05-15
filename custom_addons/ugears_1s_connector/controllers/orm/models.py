import pydantic

from . import utils


class Currency(pydantic.BaseModel):
    id: int
    name: str
    full_name: str
    symbol: str

    class Config:
        orm_mode = True
        getter_dict = utils.GenericOdooGetter


class Company(pydantic.BaseModel):
    id: int
    name: str
    display_name: str
    vat: str | None

    class Config:
        orm_mode = True
        getter_dict = utils.GenericOdooGetter


class Partner(pydantic.BaseModel):
    id: int
    name: str
    title: str | None
    display_name: str
    vat: str | None
    company_id: Company | None
    is_company: bool

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


class Product(pydantic.BaseModel):
    id: int
    name: str
    active: bool

    class Config:
        orm_mode = True
        getter_dict = utils.GenericOdooGetter
