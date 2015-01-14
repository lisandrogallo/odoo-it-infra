# -*- coding: utf-8 -*-

from openerp import models, fields


class workstation(models.Model):

    _name = 'it_infrastructure.workstation'
    _description = 'workstation'
    _inherit = [
        'it_infrastructure.computer',
    ]

    office_suite_id = fields.Many2one(
        'it_infrastructure.software',
        string='Office Suite'
    )
