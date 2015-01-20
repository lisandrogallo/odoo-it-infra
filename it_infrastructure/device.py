# -*- coding: utf-8 -*-

from openerp import fields, models


class device(models.Model):

    _name = 'it_infrastructure.device'
    _description = 'Device'
    _inherit = ['it_infrastructure.equipment']

    device_category_id = fields.Many2one(
        'it_infrastructure.device_category',
        string='Category',
        required=True
    )

    supply_ids = fields.Many2many(
        'it_infrastructure.supply',
        'it_infrastructure_supply_ids_device_ids_rel',
        'device_id',
        'supply_id',
        string='Supplies'
    )
