from odoo import fields, models


class Brand(models.Model):

    _name = 'it_infra.brand'

    name = fields.Char(required=True)
