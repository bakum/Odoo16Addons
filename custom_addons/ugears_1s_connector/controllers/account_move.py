from .controllers import get_search_criterias
from .orm.account_move import AccountMove
from odoo import http


class Ugears1sAccountMove(http.Controller):
    @http.route('/api/ugears/moves', auth='bearer_api_key', website=False, type='json', cors=True,
                methods=['GET', 'POST'])
    def index(self, **kw):
        search_criterias = get_search_criterias(kw)

        moves = http.request.env["account.move"].sudo().search(search_criterias)
        result = []
        mod = None
        for move in moves:
            mod = AccountMove.from_orm(move).dict()
            result.append(mod)
        return result if len(result) > 1 else mod