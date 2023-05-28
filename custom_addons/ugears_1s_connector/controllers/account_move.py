from .controllers import get_search_criterias
from .orm.account_move import AccountMove, AccountMoveLines
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

class Ugears1sAccountMoveLines(http.Controller):
    @http.route('/api/ugears/movelines', auth='bearer_api_key', website=False, type='json', cors=True,
                methods=['GET', 'POST'])
    def index(self, **kw):
        search_criterias = get_search_criterias(kw)

        moves = http.request.env["account.move.line"].sudo().search(search_criterias)
        result = []
        mod = None
        for move in moves:
            mod = AccountMoveLines.from_orm(move).dict()
            result.append(mod)
        return result if len(result) > 1 else mod


class Ugears1sAccounBallans(http.Controller):
    @http.route('/api/ugears/ballans', auth='bearer_api_key', website=False, type='json', cors=True,
                methods=['GET'])
    def index(self, **kw):
        # search_criterias = get_search_criterias(kw)
        account_result = []
        sql = """select rc.id as company_id, rc.name as company_name, account_move_line.date as date,
            account_move_line.company_currency_id as company_currency_id, rcuc.name as company_currency,rcuc.code as company_currency_code,
            account_move_line.currency_id as currenc_id, rcu.name as currency, rcu.code as currency_id,
            rp.id as partner_id, rp.name as partner_name, rp.vat as vat,
            prod.id as product_id, ptmp.name as product_name,
            journal_id as journal, aj.name as journal_name, aj.type as journal_type,
            aa.code, aa.name acc_name, SUM(debit) as debit, SUM(credit) as credit, SUM(quantity) as quantity,
            (SUM(debit) - SUM(credit)) AS balance, SUM(amount_currency) as amount_currency from account_move_line
        right join account_account aa on aa.id = account_move_line.account_id
        right join res_company rc on rc.id = account_move_line.company_id
        left join account_journal aj on account_move_line.journal_id = aj.id
        left join res_partner rp on account_move_line.partner_id = rp.id
        left join res_currency rcu on account_move_line.currency_id = rcu.id
        left join res_currency rcuc on account_move_line.company_currency_id = rcuc.id
        left join product_product prod on account_move_line.product_id = prod.id
        left join product_template ptmp on prod.product_tmpl_id = ptmp.id
            where account_move_line.date <= %(date)s and account_move_line.company_id = %(company_id)s
        group by aa.code, aa.name, rc.name, rc.id, journal_id, account_move_line.date,
            aj.name, aj.type, rp.id, rp.name, rp.vat, account_move_line.currency_id, rcu.name, rcu.code,
            account_move_line.company_currency_id, rcuc.name, rcuc.code, prod.id, ptmp.name
        order by aa.code, aj.name"""
        http.request.env.cr.execute(sql,kw)
        for row in http.request.env.cr.dictfetchall():
            #account_result[row.pop('code')] = row
            account_result.append(row)

        return account_result
