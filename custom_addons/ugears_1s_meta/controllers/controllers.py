# -*- coding: utf-8 -*-
# from odoo import http


# class Ugears1sMeta(http.Controller):
#     @http.route('/ugears_1s_meta/ugears_1s_meta', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ugears_1s_meta/ugears_1s_meta/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('ugears_1s_meta.listing', {
#             'root': '/ugears_1s_meta/ugears_1s_meta',
#             'objects': http.request.env['ugears_1s_meta.ugears_1s_meta'].search([]),
#         })

#     @http.route('/ugears_1s_meta/ugears_1s_meta/objects/<model("ugears_1s_meta.ugears_1s_meta"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ugears_1s_meta.object', {
#             'object': obj
#         })
