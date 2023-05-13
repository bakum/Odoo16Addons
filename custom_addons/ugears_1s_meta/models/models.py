# -*- coding: utf-8 -*-

from odoo import models, fields, api

class UgearsExchange1s(models.Model):
    _name = "ugears.exchange.settings"
    _order = "name"
    _description = "1S:Enterprise8.3 Exchange settings"

    name = fields.Char('Name', required=True)
    company_id = fields.Many2one('res.company', 'Company', required=True, default=lambda self: self.env.company)

class ResCompany(models.Model):
    _inherit = "res.company"

    company_1s_ref = fields.Char(string='Ref 1scode', size=40)


class ResUser(models.Model):
    _inherit = "res.users"

    user_1s_ref = fields.Char(string='Ref 1scode', size=40)