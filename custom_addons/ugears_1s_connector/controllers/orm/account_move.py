import datetime
from typing import List

import pydantic
from . import utils
from .account_account import AccountAccount
from .models import Company


class AccountJournal(pydantic.BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True
        getter_dict = utils.GenericOdooGetter


class AccountMoveLines(pydantic.BaseModel):
    id: int
    account_id : AccountAccount

    class Config:
        orm_mode = True
        getter_dict = utils.GenericOdooGetter


class AccountMove(pydantic.BaseModel):
    id: int
    name: str
    ref: str | None
    date: datetime.date
    state: str
    move_type: str
    is_storno: bool
    company_id: Company
    journal_id: AccountJournal
    line_ids: List[AccountMoveLines]

    class Config:
        orm_mode = True
        getter_dict = utils.GenericOdooGetter
