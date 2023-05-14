import pydantic
from . import utils
from .models import Company, Currency


class AccountAccount(pydantic.BaseModel):
    code: str
    name: str
    company_id: Company
    currency_id: Currency | None
    is_off_ballance: bool | None
    account_type: str
    internal_group: str
    id: int

    class Config:
        orm_mode = True
        getter_dict = utils.GenericOdooGetter
