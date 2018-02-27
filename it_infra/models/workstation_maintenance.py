# -*- coding: utf-8 -*-

from odoo import models, fields
from datetime import datetime


class WorkstationMaintenance(models.Model):

    _name = 'it_infra.workstation_maintenance'

    name = fields.Char(
        string='Description'
    )

    date = fields.Date(
        default=datetime.today()
    )

    workstation_id = fields.Many2one(
        comodel_name='it_infra.workstation'
    )
