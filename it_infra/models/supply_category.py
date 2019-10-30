from odoo import models, fields


class SupplyCategory(models.Model):

    _name = 'it_infra.supply_category'
    _inherit = 'it_infra.category'

    supply_ids = fields.One2many(comodel_name='it_infra.supply',
                                 inverse_name='supply_category_id',
                                 string='Supplies')

    parent_id = fields.Many2one(comodel_name='it_infra.supply_category',
                                string='Parent')

    child_ids = fields.One2many(comodel_name='it_infra.supply_category',
                                inverse_name='parent_id',
                                string='Childs')
