# -*- coding: utf-8 -*-
import typing

from odoo import models, fields, api
from odoo.api import ValuesType, Self


class biossmann_capacitacion(models.Model):
     _name = 'biossmann.capacitacion'
     _description = 'descripcion del modelo'

     name = fields.Char()
     value = fields.Integer()
     age = fields.Integer()
     country = fields.Many2one('res.country')
     country_name = fields.Char(compute='_show_name')
     city = fields.Char()
     display_name = fields.Char()


     def _show_name(self):
          if self.country:
               self.country_name = self.country.name
          else:
               self.country_name = 'sin pais'



#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

