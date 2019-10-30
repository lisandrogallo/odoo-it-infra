from datetime import date

from odoo import models, fields


class WorkstationMaintenance(models.Model):

    _name = 'it_infra.workstation_maintenance'
    _order = "date desc"

    name = fields.Char(string='Description', required=True)

    date = fields.Date(default=date.today(), required=True)

    workstation_id = fields.Many2one(comodel_name='it_infra.workstation')
