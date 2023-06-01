from .controllers import get_search_criterias
from odoo import http
from .orm.product_category import Category


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
            return result