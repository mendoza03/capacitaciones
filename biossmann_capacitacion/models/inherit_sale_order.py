# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError

class InheritProductTemplate(models.Model):
    _inherit = 'product.template'

    campo_nuevo = fields.Char(string="campo para biossmann")

    @api.model_create_multi
    def create(self, vals_list):
        print('vals_list', vals_list)
        for vals in vals_list:
            print('name', vals.get('name', ''))
            vals['name'] = vals.get('name', '').upper()


        record = super().create(vals_list)

        return record

    # @api.constrains('campo_nuevo')
    # def funcion_test(self):
    #     if len(self.campo_nuevo) < 5:
    #         raise UserError('el campo no puede tener menos de 5 letras')


    @api.onchange('categ_id')
    def onchange_categ_id(self):
        if self.categ_id.name == 'Internal':
            print(self.campo_nuevo)

    def write(self, vals):
        print('vals write', vals)
        if 'list_price' in vals:
            if self.name == 'BIOSSMANN TEST':
                if not self.campo_nuevo:
                    if not 'campo_nuevo' in vals:
                        raise UserError('Debe asignar un valor a campo para biossmann')

        result = super().write(vals)

        return result






