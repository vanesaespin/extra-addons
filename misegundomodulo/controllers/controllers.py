# -*- coding: utf-8 -*-
# from odoo import http


# class Misegundomodulo(http.Controller):
#     @http.route('/misegundomodulo/misegundomodulo', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/misegundomodulo/misegundomodulo/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('misegundomodulo.listing', {
#             'root': '/misegundomodulo/misegundomodulo',
#             'objects': http.request.env['misegundomodulo.misegundomodulo'].search([]),
#         })

#     @http.route('/misegundomodulo/misegundomodulo/objects/<model("misegundomodulo.misegundomodulo"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('misegundomodulo.object', {
#             'object': obj
#         })
