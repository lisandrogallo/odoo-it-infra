# -*- coding: utf-8 -*-

from odoo import fields, models


class NetworkDevicePort(models.Model):

    _name = 'it_infra.network_device_port'
    _description = 'Network Device Port'

    _cable_colors_ = [
        ('blue', 'Blue'),
        ('yellow', 'Yellow'),
        ('white', 'White'),
        ('gray', 'Gray'),
        ('black', 'Black')
    ]

    name = fields.Char()

    mac_address = fields.Char(
        size=18
    )

    ip_address = fields.Char(
        track_visibility='onchange'
    )

    netmask = fields.Char(
        default='/24'
    )
    
    state = fields.Boolean(
        string='Active'
    )

    vlan = fields.Char()

    inter_vlan_routing = fields.Char()

    connected_to = fields.Many2one(
        comodel_name='it_infra.equipment'
    )

    cable_color = fields.Selection(
        selection=_cable_colors_
    )

    network_device_id = fields.Many2one(
        comodel_name='it_infra.network_device'
    )
