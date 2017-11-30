# -*- coding: utf-8 -*-

from odoo import fields, models, api


class Software(models.Model):

    _name = 'it_infra.software'

    _architecture_ = [
        ('(x86)', '32 bits'),
        ('(x64)', '64 bits'),
    ]

    name = fields.Char(
        required=True
    )

    version = fields.Char()

    architecture = fields.Selection(
        selection=_architecture_,
    )

    category_id = fields.Many2one(
        comodel_name='it_infra.software_category',
        string='Category',
        required=True
    )

    @api.multi
    def name_get(self):
        result = []
        for soft in self:
            if soft.category_id.parent_id.name == 'Operating System':
                result.append((soft.id, "%s %s %s" % (
                    soft.name, soft.version or '', soft.architecture or '')))
            else:
                result.append((soft.id, "%s %s" %
                               (soft.name, soft.version or '')))
        return result
