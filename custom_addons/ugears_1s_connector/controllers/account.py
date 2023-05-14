from .controllers import get_search_criterias
from .orm.account_account import AccountAccount
from odoo import http


class Ugears1sAccount(http.Controller):
    @http.route('/api/ugears/accounts', auth='bearer_api_key', website=False, type='json', cors=True,
                methods=['GET', 'POST'])
    def index(self, **kw):
        search_criterias = get_search_criterias(kw)
        # if http.request.httprequest.method == 'GET':
        #     pass
        accounts = http.request.env["account.account"].sudo().search(search_criterias)
        result = []
        mod = None
        for account in accounts:
            mod = AccountAccount.from_orm(account).dict()
            result.append(mod)
        count = len(result)
        # result.append('count': count)
        return result if len(result) > 1 else mod
