# -*- coding: utf-8 -*-
# from odoo import http


# class TiktokApp(http.Controller):
#     @http.route('/tiktok_app/tiktok_app', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/tiktok_app/tiktok_app/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('tiktok_app.listing', {
#             'root': '/tiktok_app/tiktok_app',
#             'objects': http.request.env['tiktok_app.tiktok_app'].search([]),
#         })

#     @http.route('/tiktok_app/tiktok_app/objects/<model("tiktok_app.tiktok_app"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('tiktok_app.object', {
#             'object': obj
#         })
