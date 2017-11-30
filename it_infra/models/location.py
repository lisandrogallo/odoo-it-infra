# -*- coding: utf-8 -*-

from odoo import fields, models


class Location(models.Model):

    _name = 'it_infra.location'

    name = fields.Char(
        required=True
    )

    internal = fields.Boolean()
