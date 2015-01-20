# -*- coding: utf-8 -*-

from openerp import models, fields


class supply(models.Model):

    _name = 'it_infrastructure.supply'
    _description = 'supply'
    _inherit = ['ir.needaction_mixin', 'mail.thread']

    name = fields.Char(
        string='Name',
        required=True
    )

    description = fields.Html(
        string='Description'
    )

    supply_category_id = fields.Many2one(
        'it_infrastructure.supply_category',
        string='Category',
        required=True
    )

    quantity = fields.Integer(
        string='Quantity',
        default=0
    )

    partner_id = fields.Many2one(
        'res.partner',
        string='Partner'
    )

    device_ids = fields.Many2many(
        'it_infrastructure.device',
        'it_infrastructure_supply_ids_device_ids_rel',
        'supply_id',
        'device_id',
        string='Devices'
    )
