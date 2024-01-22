# -*- coding: utf-8 -*-
from odoo import models, fields, api

class videoclub_pelis(models.Model):
    #atributos 
    _name = 'videoclub.pelis' 
    _description = 'Película'
    #campos
    titulo = fields.Char('Titulo', size=30, required=True, help='Nombre de la peli')
    director = fields.Char('Director', size=30, required=False, help='Director de la peli', default='')
    clasificacion = fields.Selection([('TP','Todos los Públicos'),('men12','Menores de 12 años'),('may18','Mayores 18 años')], string='Clasificación', default='TP')
    presupuesto = fields.Integer()
    fechaestreno = fields.Date()

# class videoclub_sge(models.Model):
#     _name = 'videoclub_sge.videoclub_sge'
#     _description = 'videoclub_sge.videoclub_sge'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
