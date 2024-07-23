from odoo import models, fields, api

class ProductDate(models.Model):
    _inherit = 'product.template'

    expiration_date = fields.Date(string='Fecha de Expiración')
