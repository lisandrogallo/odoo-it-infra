# -*- coding: utf-8 -*-

from openerp import models, fields


class supply_category(models.Model):

    _name = 'it_infrastructure.supply_category'
    _description = 'supply_category'
    _inherit = 'it_infrastructure.category'

    supply_ids = fields.One2many(
        'it_infrastructure.supply',
        'supply_category_id',
        string='Supplies'
    )

    parent_id = fields.Many2one(
        'it_infrastructure.supply_category',
        string='Parent'
    )

    child_ids = fields.One2many(
        'it_infrastructure.supply_category',
        'parent_id',
        string='Childs'
    )
