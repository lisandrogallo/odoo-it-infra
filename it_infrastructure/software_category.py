# -*- coding: utf-8 -*-

from openerp import models, fields


class software_category(models.Model):

    _name = 'it_infrastructure.software_category'
    _description = 'software_category'

    name = fields.Char(
        string='Name',
        required=True
    )

    software_ids = fields.One2many(
        'it_infrastructure.software',
        'category_id',
        string='Supplies'
    )

    parent_id = fields.Many2one(
        'it_infrastructure.software_category',
        string='Parent'
    )

    child_ids = fields.One2many(
        'it_infrastructure.software_category',
        'parent_id',
        string='Childs'
    )
