from odoo import fields, models


class SoftwareCategory(models.Model):

    _name = "it_infra.software_category"

    name = fields.Char(required=True)

    software_ids = fields.One2many(
        comodel_name="it_infra.software",
        inverse_name="category_id",
        string="Software",
    )

    parent_id = fields.Many2one(
        comodel_name="it_infra.software_category", string="Parent"
    )

    child_ids = fields.One2many(
        comodel_name="it_infra.software_category",
        inverse_name="parent_id",
        string="Childs",
    )
