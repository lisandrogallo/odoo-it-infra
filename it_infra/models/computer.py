# -*- coding: utf-8 -*-

from odoo import fields, models


class Computer(models.Model):

    _name = 'it_infra.computer'
    _inherit = 'it_infra.equipment'

    # _identifier_ = [
    #     ('A', 'A'),
    #     ('B', 'B'),
    #     ('C', 'C'),
    #     ('D', 'D')
    # ]

    user_id = fields.Many2one(
        comodel_name='res.users',
        string='User',
        track_visibility='onchange'
    )

    username = fields.Char(
        required=True,
        track_visibility='onchange'
    )

    office = fields.Char(
        track_visibility='onchange'
    )

    os_id = fields.Many2one(
        comodel_name='it_infra.software',
        string='Operating System',
        domain=[('category_id.parent_id', 'ilike', 'Operating System')],
        track_visibility='onchange',
        required=True
    )

    hardware_data = fields.Html(
        track_visibility='onchange'
    )

    # switch = fields.Selection(
    #     selection=_identifier_
    # )

    # patch_panel = fields.Selection(
    #     selection=_identifier_
    # )

    # patch_panel_port = fields.Char()

    _sql_constraints = [
        ('name_unique',
         'unique(name)',
         'Computer name must be unique!'),
        ('ip_address_unique', 'unique(ip_address)',
         'Computer IP address must be unique!'),
        ('hostname_unique', 'unique(hostname)',
         'Computer hostname must be unique!')
    ]
