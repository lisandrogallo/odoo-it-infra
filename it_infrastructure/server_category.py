# -*- coding: utf-8 -*-

from openerp import models, fields


class server_category(models.Model):

    _name = 'it_infrastructure.server_category'
    _description = 'server_category'

    name = fields.Char(
        string='Name',
        required=True
    )

    server_ids = fields.Many2many(
        'it_infrastructure.server',
        'category_ids',
        'server_category_rel',
        string='Server'
    )

    parent_id = fields.Many2one(
        'it_infrastructure.server_category',
        string='Parent'
    )

    child_ids = fields.One2many(
        'it_infrastructure.server_category',
        'parent_id',
        string='Childs'
    )

    _sql_constraints = [
        ('name_uniq', 'unique(name)',
            'Server tags must be unique!'),
    ]
