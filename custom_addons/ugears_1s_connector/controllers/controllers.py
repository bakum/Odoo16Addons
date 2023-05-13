# -*- coding: utf-8 -*-
from odoo import http
from .orm.models import User, Company


class Ugears1sConnector(http.Controller):
    @http.route('/api/1s_connector', auth='bearer_api_key', website=False, type='json', methods=['GET', 'POST'])
    def index(self, **kw):
        user = http.request.env["res.users"].sudo().search([('id', '=', http.request.uid), ('active', '=', True)])
        if user:
            return User.from_orm(user).dict()

        return "Hello, world"


class Ugears1sOrganization(http.Controller):
    @http.route('/api/1s_connector/organizations', auth='bearer_api_key', website=False, type='json', cors=True,
                methods=['GET', 'POST'])
    def index(self, **kw):
        search_criterias = []
        for key in kw:
            search_criterias.append((key, '=', kw[key]))

        companys = http.request.env["res.company"].sudo().search(search_criterias)
        result = []
        for company in companys:
            mod = Company.from_orm(company).dict()
            result.append(mod)
        return result if len(result) > 1 else mod
