# -*- coding: utf-8 -*-
# from odoo import http


# class VideoclubSge(http.Controller):
#     @http.route('/videoclub_sge/videoclub_sge', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/videoclub_sge/videoclub_sge/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('videoclub_sge.listing', {
#             'root': '/videoclub_sge/videoclub_sge',
#             'objects': http.request.env['videoclub_sge.videoclub_sge'].search([]),
#         })

#     @http.route('/videoclub_sge/videoclub_sge/objects/<model("videoclub_sge.videoclub_sge"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('videoclub_sge.object', {
#             'object': obj
#         })
