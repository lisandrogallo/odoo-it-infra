# -*- coding: utf-8 -*-

from openerp import fields, models


class software(models.Model):

    _name = 'it_infrastructure.software'
    _description = 'Software'
    _inherit = [
        'mail.thread',
        'ir.needaction_mixin'
    ]

    name = fields.Char(
        string='Name',
        required=True
    )

    description = fields.Text(
        string='Description'
    )

    version = fields.Char(
        string='Version',
        required=True
    )

    software_category_id = fields.Many2one(
        'it_infrastructure.software_category',
        string='Category',
        required=True
    )
