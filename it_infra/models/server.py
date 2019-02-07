# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import except_orm, Warning


class Server(models.Model):

    _name = 'it_infra.server'
    _description = 'Server'
    _inherit = 'it_infra.computer'

    _server_type_ = [
        ('bare_metal', 'Bare Metal'),
        ('bare_metal_sa', 'Bare Metal (Standalone)'),
        ('cloud', 'Cloud')
        ('hypervisor', 'Hypervisor'),
        ('vm', 'Virtual Machine'),
        ('docker', 'Docker Stack'),
    ]

    password = fields.Char(
        track_visibility='onchange'
    )

    open_ports = fields.Char(
        track_visibility='onchange'
    )

    server_type = fields.Selection(
        selection=_server_type_
    )

    category_ids = fields.Many2many(
        comodel_name='it_infra.server_category',
        relation='server_category_rel',
        track_visibility='onchange',
        string='Categories'
    )

    location_id = fields.Many2one(
        comodel_name='it_infra.location',
        required=True
    )

    internal_location = fields.Boolean(
        related='location_id.internal'
    )

    webadmin = fields.Char(
        string='Web Admin'
    )

    hosted_in_id = fields.Many2one(
        comodel_name='it_infra.server',
        track_visibility='onchange'
    )

    hosted_server_ids = fields.One2many(
        comodel_name='it_infra.server',
        inverse_name='hosted_in_id',
        readonly=True
    )

    @api.multi
    def unlink(self):
        for server in self:
            if server.state not in ('draft', 'cancel'):
                raise Warning(_(
                    'You cannot delete a server \
                    which is not draft or cancelled.'))
            res = super(Server, self).unlink()
            return res

    @api.multi
    def show_passwd(self):
        for server in self:
            raise except_orm(
                _("Password for user '%s':") % server.username,
                _("%s") % server.password
            )
