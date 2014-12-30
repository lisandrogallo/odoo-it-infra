# -*- coding: utf-8 -*-

from openerp import models, fields


class device_category(models.Model):

    _name = 'it_infrastructure.device_category'
    _description = 'device_category'

    name = fields.Char(
        string='Name',
        required=True
    )

    device_ids = fields.One2many(
        'it_infrastructure.device',
        'device_category_id',
        string='Supplies'
    )

    parent_id = fields.Many2one(
        'it_infrastructure.device_category',
        string='Parent'
    )

    child_ids = fields.One2many(
        'it_infrastructure.device_category',
        'parent_id',
        string='Childs'
    )
