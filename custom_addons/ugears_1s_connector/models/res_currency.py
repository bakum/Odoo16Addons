from odoo import models, fields


class ResCurrency(models.Model):
    _inherit = "res.currency"
    code = fields.Char(string='Code of currency', size=3)