# -*- coding: utf-8 -*-
# from odoo import http


# class Odoo9(http.Controller):
#     @http.route('/odoo9/odoo9/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/odoo9/odoo9/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('odoo9.listing', {
#             'root': '/odoo9/odoo9',
#             'objects': http.request.env['odoo9.odoo9'].search([]),
#         })

#     @http.route('/odoo9/odoo9/objects/<model("odoo9.odoo9"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('odoo9.object', {
#             'object': obj
#         })
