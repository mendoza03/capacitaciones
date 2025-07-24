# -*- coding: utf-8 -*-
from email.policy import default

from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError

class InheritProductTemplate(models.Model):
    _inherit = 'product.template'

    campo_nuevo = fields.Char(string="campo para biossmann")

    state_biossman = fields.Selection([('new', 'Draft product'), ('send', 'Send'), ('done', 'Done')], default='new')

    conteo_factura = fields.Integer(string="conteo")

    def send_product(self):
        #campo base de datos
        contactos = self.env['res.partner'].search([('is_company','=', True), ('web_site', '=', self.web_site)])
        #campo relacion, busca el id directo
        facturas = self.env['account.move'].search_count([('partner_id', '=', self.partner_id.id)])
        # campo base de datos, por medio de id
        contacto = self.env['res.partner'].browse(self.partnert_id.id)

        if facturas:
            facturas.partner_id.country_id.id

        facturas = self.env['account.move'].create({
            'name': 'test',
            'partner_id': 5,
            'product_id': self.env.ref('biossmann_capacitacion.grupo_biossmann') # 'product_id': 8
        })

        self.env['account.move'].post()



        for contacto in contactos:
            print('contacto', contacto)
        self.write({
            'state_biossman': 'send',
            'campo_nuevo': 'se envio a gerente',
            'conteo_factura': facturas,
        })

    def validate_product(self):
        self.write({
            'state_biossman': 'done',
            'campo_nuevo': 'lo valido el gerente',
        })


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






