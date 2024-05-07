# -*- coding: utf-8 -*-
from odoo import models, fields, api

#class director (models.Model):
    #_name = 'res.partner' --no hace falta
 #   _inherit = 'res.partner'
"""     _description = 'Director'
    _rec_name = 'Director' """

""" class cine (models.Model):
    #_name = 'res.company' --no hace falta
    _inherit = 'res.company'
    _description = 'Director'
    _rec_name = 'Director'  """

class compania_cinematografica(models.Model):
#      #_name = 'res.partner' --no hace falta
     _inherit = 'res.partner'
     is_cine=fields.Boolean()
     premiada = fields.Boolean('Premiada', default=False)

class videoclub_pelis(models.Model):
    #atributos 
    _name = 'videoclub.pelis' 
    _description = 'Película'
    _rec_name = 'titulo'
    #campos
    titulo = fields.Char('Titulo', size=30, required=True, help='Nombre de la peli') 
    director = fields.Char('Director', size=30, required=False, help='Director de la peli', default='')
    #director = fields.Many2one('director', help='Aun no se ha creado ningun director')
    clasificacion = fields.Selection([('TP','Todos los Públicos'),('men12','Menores de 12 años'),('may18','Mayores 18 años')], string='Clasificación', default='TP')
    presupuesto = fields.Integer()
    recaudado = fields.Integer()
    fechaestreno = fields.Date()
    
    #Campos calculados Supongamos que se subvenciona el 30% de la película
    subvencionado = fields.Integer(compute='_valor_subvencion') #no inmediato, solo al guardar
    invertido = fields.Integer(compute='_valor_inversion') #queremos verlo de modo inmediato
    mas_de_millon_euros = fields.Boolean('Más de un millon de euros', compute='_is_millonario', help='Este valor es verdadero si la peli ha costado más de un millon de euros')

    #Nueva relación Relacion
    compania = fields.Many2one('res.partner')

    def _valor_subvencion(self):
        self.subvencionado=self.presupuesto*0.3
        
    @api.depends('presupuesto')
    def _valor_inversion(self):
        self.invertido=self.presupuesto*0.7

    @api.depends('presupuesto')
    def _is_millonario(self):
        self.mas_de_millon_euros=(self.presupuesto > 1000000)

#FALTAN POR METER LAS CATEGORÍAS

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
