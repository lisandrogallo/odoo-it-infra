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
        string='User'
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
        string='Network Mask',
        default='255.255.255.0',
        required=True
    )

    os_id = fields.Many2one(
        'it_infrastructure.software',
        string='Operating System',
        required=True
    )

    hardware_data = fields.Html(
        string='Hardware Data'
    )

    hardware_specs = fields.Binary(
        string='Hardware Specifications'
    )

    note = fields.Html(
        string='Note'
    )

    change_ids = fields.One2many(
        'it_infrastructure.computer_change',
        'computer_id',
        string='Changes'
    )

    _sql_constraints = [
        ('name_uniq', 'unique(name)',
            'Computer name must be unique!'),
    ]
