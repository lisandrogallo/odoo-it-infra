# -*- coding: utf-8 -*-

from openerp import fields, models, api


class software(models.Model):

    _name = 'it_infrastructure.software'
    _description = 'Software'

    name = fields.Char(
        string='Name',
        required=True
    )

    version = fields.Char(
        string='Version'
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
            result.append((soft.id, "%s %s" % (soft.name, soft.version or '')))
        return result
