from .controllers import get_search_criterias
from odoo import http
from .orm.product_category import Category, PublicCategory


class Ugears1sCategory(http.Controller):
    @http.route('/api/ugears/category', auth='bearer_api_key', website=False, type='json', cors=True,
                methods=['GET', 'POST'])
    def index(self, **kw):
        search_criterias = get_search_criterias(kw)
        result = []
        mod = None

        if http.request.httprequest.method == 'GET':
            moves = http.request.env["product.category"].sudo().search(search_criterias)
            for move in moves:
                mod = Category.from_orm(move).dict()
                result.append(mod)
            return result if len(result) > 1 else mod

        if http.request.httprequest.method == 'POST':
            res = http.request.env["product.category"].sudo().create(kw)
            return Category.from_orm(res).dict()


class Ugears1sPublicCategory(http.Controller):
    @http.route('/api/ugears/public_category', auth='bearer_api_key', website=False, type='json', cors=True,
                methods=['GET', 'POST'])
    def index(self, **kw):
        search_criterias = get_search_criterias(kw)
        result = []
        mod = None

        if http.request.httprequest.method == 'GET':
            try:
                moves = http.request.env["product.public.category"].sudo().search(search_criterias)
            except:
                return result

            for move in moves:
                mod = PublicCategory.from_orm(move).dict()
                result.append(mod)
            return result if len(result) > 1 else mod

        if http.request.httprequest.method == 'POST':
            try:
                found = http.request.env["product.public.category"].sudo().search(search_criterias)
            except:
                return result
            if found is not None:
                return Category.from_orm(found).dict()
            res = http.request.env["product.public.category"].sudo().create(kw)
            return Category.from_orm(res).dict()
