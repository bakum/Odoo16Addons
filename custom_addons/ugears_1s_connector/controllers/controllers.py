# -*- coding: utf-8 -*-
from odoo import http
from .orm.models import User, Company, Partner


def get_search_criterias(kw):
    search_criterias = []
    for key in kw:
        search_criterias.append((key, '=', kw[key]))
    return search_criterias


def get_search_criterias_ext(kw):
    search_criterias = []
    for key in kw:
        if key == 'operator':
            search_criterias.append(kw[key])
            continue
        sent = kw[key]
        search_criterias.append((key, sent['operator'], sent['arg']))
    return search_criterias


class Ugears1sConnector(http.Controller):
    @http.route('/api/1s_connector', auth='bearer_api_key', website=False, type='json', methods=['GET', 'POST'])
    def index(self, **kw):
        # search_criterias = self.get_search_criterias(kw)
        user = http.request.env["res.users"].sudo().search([('id', '=', http.request.uid), ('active', '=', True)])
        if user:
            return User.from_orm(user).dict()

        return "Hello, world"


class Ugears1sOrganization(http.Controller):
    @http.route('/api/1s_connector/organizations', auth='bearer_api_key', website=False, type='json', cors=True,
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
    @http.route('/api/1s_connector/partners', auth='bearer_api_key', website=False, type='json', cors=True,
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
