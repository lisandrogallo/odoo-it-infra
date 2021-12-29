from odoo import fields, models


class Location(models.Model):

    _name = "it_infra.location"
    _description = "Location"

    name = fields.Char(required=True)

    internal = fields.Boolean()
