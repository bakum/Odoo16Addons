import datetime
from typing import List

import pydantic
from . import utils
from .account_account import AccountAccount
from .models import Company, Product, Currency


class AccountJournal(pydantic.BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True
        getter_dict = utils.GenericOdooGetter


class AccountMoveLines(pydantic.BaseModel):
    id: int
    name: str
    account_id: AccountAccount
    display_type: str
    debit: float | None
    credit: float | None
    balance: float | None
    amount_currency: float | None
    tax_base_amount: float | None
    amount_residual: float | None
    amount_residual_currency: float | None
    product_id: Product | None
    quantity: float | None
    price_unit: float | None
    price_subtotal: float | None

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
    currency_id: Currency
    journal_id: AccountJournal
    amount_untaxed: float | None
    amount_tax: float | None
    amount_total: float | None
    line_ids: List[AccountMoveLines]

    class Config:
        orm_mode = True
        getter_dict = utils.GenericOdooGetter
