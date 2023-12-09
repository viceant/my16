# -*- coding: utf-8 -*-
# from odoo import http


# class MyMaterial(http.Controller):
#     @http.route('/my_material/my_material', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/my_material/my_material/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('my_material.listing', {
#             'root': '/my_material/my_material',
#             'objects': http.request.env['my_material.my_material'].search([]),
#         })

#     @http.route('/my_material/my_material/objects/<model("my_material.my_material"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('my_material.object', {
#             'object': obj
#         })
