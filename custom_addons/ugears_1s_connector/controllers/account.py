from .controllers import get_search_criterias_ext
from .orm.account_account import AccountAccount
from odoo import http


class Ugears1sAccount(http.Controller):
    @http.route('/api/1s_connector/accounts', auth='bearer_api_key', website=False, type='json', cors=True,
                methods=['GET', 'POST'])
    def index(self, **kw):
        search_criterias = get_search_criterias_ext(kw)

        accounts = http.request.env["account.account"].sudo().search(search_criterias)
        result = []
        mod = None
        for account in accounts:
            mod = AccountAccount.from_orm(account).dict()
            result.append(mod)
        count = len(result)
        # result.append('count': count)
        return result if len(result) > 1 else mod
