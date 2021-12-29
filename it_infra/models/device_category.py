from odoo import fields, models


class DeviceCategory(models.Model):

    _name = "it_infra.device_category"
    _inherit = "it_infra.category"
    _description = "Device Category"

    device_ids = fields.One2many(
        comodel_name="it_infra.device",
        inverse_name="device_category_id",
        string="Devices",
    )

    parent_id = fields.Many2one(
        comodel_name="it_infra.device_category", string="Parent"
    )

    child_ids = fields.One2many(
        comodel_name="it_infra.device_category",
        inverse_name="parent_id",
        string="Childs",
    )
