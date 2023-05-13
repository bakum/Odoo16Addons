# -*- coding: utf-8 -*-
# from odoo import http


# class UgearsConsolidation(http.Controller):
#     @http.route('/ugears_consolidation/ugears_consolidation', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ugears_consolidation/ugears_consolidation/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('ugears_consolidation.listing', {
#             'root': '/ugears_consolidation/ugears_consolidation',
#             'objects': http.request.env['ugears_consolidation.ugears_consolidation'].search([]),
#         })

#     @http.route('/ugears_consolidation/ugears_consolidation/objects/<model("ugears_consolidation.ugears_consolidation"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ugears_consolidation.object', {
#             'object': obj
#         })
