# -*- coding: utf-8 -*-

from openerp import models, fields


class computer(models.Model):

    _name = 'it_infrastructure.computer'
    _description = 'Computer'
    _inherit = [
        'it_infrastructure.equipment',
    ]

    hostname = fields.Char(
        string='Hostname',
        required=True
    )

    user_id = fields.Many2one(
        'res.partner',
        string='User',
        required=True
    )

    username = fields.Char(
        string='Username',
        required=True
    )

    ip_address = fields.Char(
        string='IP Address',
        required=True
    )

    netmask = fields.Char(
        string='Network Mask'
    )

    os = fields.Many2one(
        'it_infrastructure.software',
        string='Operating System',
        required=True
    )
