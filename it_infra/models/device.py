from odoo import fields, models


class Device(models.Model):

    _name = "it_infra.device"
    _inherit = "it_infra.equipment"
    _description = "Device"

    device_category_id = fields.Many2one(
        comodel_name="it_infra.device_category",
        string="Category",
        required=True,
    )

    supply_ids = fields.Many2many(
        comodel_name="it_infra.supply",
        relation="it_infra_supply_ids_device_ids_rel",
        column1="device_id",
        column2="supply_id",
        string="Supplies",
    )
