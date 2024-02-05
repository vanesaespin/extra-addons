# -*- coding: utf-8 -*-
from odoo import models, fields, api

class videoclub_pelis(models.Model):
    #atributos 
    _name = 'videoclub.pelis' 
    _description = 'Película'
    #campos
    titulo = fields.Char('Titulo', size=30, required=True, help='Nombre de la peli')
    _rec_name = 'titulo'
    director = fields.Char('Director', size=30, required=False, help='Director de la peli', default='')
    clasificacion = fields.Selection([('TP','Todos los Públicos'),('men12','Menores de 12 años'),('may18','Mayores 18 años')], string='Clasificación', default='TP')
    presupuesto = fields.Integer()
    recaudado = fields.Integer()
    fechaestreno = fields.Date()
    #Supongamos que se subvenciona el 30% de la película
    subvencionado = fields.Integer(compute='_valor_subvencion') #no inmediato, solo al guardar
    invertido = fields.Integer(compute='_valor_inversion') #queremos verlo de modo inmediato
    mas_de_millon_euros = fields.Boolean('Más de un millon de euros', compute='_is_millonario', help='Este valor es verdadero si la peli ha costado más de un millon de euros')

    def _valor_subvencion(self):
        self.subvencionado=self.presupuesto*0.3
        
    @api.depends('presupuesto')
    def _valor_inversion(self):
        self.invertido=self.presupuesto*0.7

    @api.depends('presupuesto')
    def _is_millonario(self):
        self.mas_de_millon_euros=(self.presupuesto > 1000000)


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
