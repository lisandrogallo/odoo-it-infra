from odoo import models, fields


class Category(models.Model):

    _name = 'it_infra.category'

    name = fields.Char(required=True)

    def name_get(self):
        result = []
        for cat in self:
            prefix = None
            if cat.parent_id:
                prefix = cat.parent_id.name_get()[0][1] + ' / '
            result.append((cat.id, "%s %s" % (prefix or '', cat.name)))
        return result
