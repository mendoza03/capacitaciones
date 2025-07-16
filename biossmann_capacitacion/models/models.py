# -*- coding: utf-8 -*-
from odoo import models, fields, api


class biossmann_capacitacion(models.Model):
     _name = 'biossmann.capacitacion'
     _description = 'descripcion del modelo'

     name = fields.Char()
     value = fields.Integer()
     age = fields.Integer()
     display_name = fields.Char()



#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

