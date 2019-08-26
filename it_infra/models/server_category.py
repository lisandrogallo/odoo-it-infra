
from odoo import models, fields


class ServerCategory(models.Model):

    _name = 'it_infra.server_category'

    name = fields.Char(
        required=True
    )

    server_ids = fields.Many2many(
        comodel_name='it_infra.server',
        relation='category_ids',
        column1='server_category_rel',
        string='Servers'
    )

    parent_id = fields.Many2one(
        comodel_name='it_infra.server_category',
        string='Parent'
    )

    child_ids = fields.One2many(
        comodel_name='it_infra.server_category',
        inverse_name='parent_id',
        string='Childs'
    )

    _sql_constraints = [
        ('name_uniq',
         'unique(name)',
         'Server tags must be unique!')
    ]
