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

     line_ids = fields.One2many('biossmann.capacitacion.lineas', 'capacitacion_ids', string='lineas')

     doctor_ids = fields.Many2many('biossmann.capacitacion.doctores', string='Doctors')

     def send_product(self):
          self.city = 'mexico'


     def _show_name(self):
          if self.country:
               self.country_name = self.country.name
          else:
               self.country_name = 'sin pais'


class biossmann_capacitacionLineas(models.Model):
     _name = 'biossmann.capacitacion.lineas'

     name = fields.Char()
     value = fields.Integer()
     capacitacion_ids = fields.Many2one('biossmann.capacitacion', string='Capacitacion')



class biossmann_capacitacionDoctores(models.Model):
     _name = 'biossmann.capacitacion.doctores'

     name = fields.Char()
     value = fields.Integer()