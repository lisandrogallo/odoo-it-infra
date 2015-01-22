# -*- coding: utf-8 -*-

from openerp import fields, models, api


class software(models.Model):

    _name = 'it_infrastructure.software'
    _description = 'Software'

    _architecture_ = [
        ('x86', '32 bits'),
        ('x64', '64 bits'),
    ]

    name = fields.Char(
        string='Name',
        required=True
    )

    version = fields.Char(
        string='Version'
    )

    architecture = fields.Selection(
        selection=_architecture_,
        string='Architecture'
    )

    category_id = fields.Many2one(
        'it_infrastructure.software_category',
        string='Category',
        required=True
    )

    @api.multi
    def name_get(self):
        result = []
        for soft in self:
            if soft.category_id.parent_id.name == 'Operating System':
                result.append((soft.id, "%s %s (%s)" % (soft.name, soft.version, soft.architecture or '')))
            else:
                result.append((soft.id, "%s %s" % (soft.name, soft.version or '')))
        return result
