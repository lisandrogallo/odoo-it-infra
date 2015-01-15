# -*- coding: utf-8 -*-

from openerp import models, fields, api


class supply_category(models.Model):

    _name = 'it_infrastructure.supply_category'
    _description = 'supply_category'

    name = fields.Char(
        string='Name',
        required=True
    )

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

    @api.multi
    def name_get(self):
        result = []
        for cat in self:
            prefix = None
            if cat.parent_id:
                prefix = cat.parent_id.name + ' / '
            result.append((cat.id, "%s %s" % (prefix or '', cat.name)))
        return result
