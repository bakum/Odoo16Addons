# -*- coding: utf-8 -*-
from odoo import http
from .orm.models import User, Company, Partner


def get_search_criterias(kw):
    search_criterias = []
    for key in kw:
        if key == 'operator':
            search_criterias.append(kw[key])
            continue
        sent = kw[key]
        operator = '='
        arg = kw[key]
        try:
            operator = sent['operator']
        except:
            pass
        try:
            arg = sent['arg']
        except:
            pass
        search_criterias.append((key, operator, arg))
    return search_criterias


class Ugears1sConnector(http.Controller):
    @http.route('/api/ugears', auth='bearer_api_key', website=False, type='json', methods=['GET', 'POST'])
    def index(self, **kw):
        # search_criterias = self.get_search_criterias(kw)
        # user = http.request.env["res.users"].sudo().search([('id', '=', http.request.uid), ('active', '=', True)])
        # if user:
        return User.from_orm(http.request.env.user).dict()

        # return "Hello, world"


class Ugears1sOrganization(http.Controller):
    @http.route('/api/ugears/organizations', auth='bearer_api_key', website=False, type='json', cors=True,
                methods=['GET', 'POST'])
    def index(self, **kw):
        search_criterias = get_search_criterias(kw)

        companys = http.request.env["res.company"].sudo().search(search_criterias)
        result = []
        mod = None
        for company in companys:
            mod = Company.from_orm(company).dict()
            result.append(mod)
        return result if len(result) > 1 else mod


class Ugears1sPartners(http.Controller):
    @http.route('/api/ugears/partners', auth='bearer_api_key', website=False, type='json', cors=True,
                methods=['GET', 'POST'])
    def index(self, **kw):
        search_criterias = get_search_criterias(kw)

        partners = http.request.env["res.partner"].sudo().search(search_criterias)
        result = []
        mod = None
        for partner in partners:
            mod = Partner.from_orm(partner).dict()
            result.append(mod)
        return result if len(result) > 1 else mod
