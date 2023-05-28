import datetime
from typing import List

import pydantic
from . import utils
from .account_account import AccountAccount
from .models import Company, Product, Currency, BankAcc, Partner


class AccountJournal(pydantic.BaseModel):
    id: int
    name: str
    bank_account_id: BankAcc | None

    class Config:
        orm_mode = True
        getter_dict = utils.GenericOdooGetter


class Payment(pydantic.BaseModel):
    id: int
    payment_type: str
    partner_type: str
    currency_id: Currency | None
    partner_bank_id: BankAcc | None
    amount: float

    class Config:
        orm_mode = True
        getter_dict = utils.GenericOdooGetter


class AccountMoveLines(pydantic.BaseModel):
    id: int
    date: datetime.date | None
    move_id: int
    move_name: str | None
    name: str | None
    account_id: AccountAccount
    journal_id: AccountJournal | None
    display_type: str
    debit: float | None
    credit: float | None
    balance: float | None
    amount_currency: float | None
    tax_base_amount: float | None
    amount_residual: float | None
    amount_residual_currency: float | None
    product_id: Product | None
    partner_id: Partner | None
    quantity: float | None
    price_unit: float | None
    price_subtotal: float | None
    payment_id: Payment | None
    currency_id: Currency | None
    company_currency_id: Currency | None

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
    line_ids: List[AccountMoveLines] | None

    class Config:
        orm_mode = True
        getter_dict = utils.GenericOdooGetter
