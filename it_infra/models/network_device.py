from odoo import fields, models


class NetworkDevice(models.Model):

    _name = 'it_infra.network_device'
    _inherit = 'it_infra.equipment'

    _network_device_types_ = [('router', 'Router'), ('switch', 'Switch'),
                              ('ap', 'Access Point')]

    mac_address = fields.Char(size=18)

    brand_id = fields.Many2one(comodel_name='it_infra.brand')

    model = fields.Char()

    network_device_type = fields.Selection(selection=_network_device_types_)

    username = fields.Char(required=True, tracking=True)

    password = fields.Char(tracking=True)

    location_id = fields.Many2one(comodel_name='it_infra.location',
                                  required=True)

    network_device_port_ids = fields.One2many(
        comodel_name='it_infra.network_device_port',
        inverse_name='network_device_id')

    notes = fields.Html()
