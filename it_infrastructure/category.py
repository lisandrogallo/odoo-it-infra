# -*- coding: utf-8 -*-

from openerp import models, fields, api


class category(models.Model):

    _name = 'it_infrastructure.category'
    _description = 'category'

    name = fields.Char(
        string='Name',
        required=True
    )

    @api.multi
    def name_get(self):
        result = []
        for cat in self:
            prefix = None
            if cat.parent_id:
                prefix = cat.parent_id.name_get()[0][1] + ' / '
            result.append((cat.id, "%s %s" % (prefix or '', cat.name)))
        return result
