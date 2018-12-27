# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import except_orm, Warning


class Server(models.Model):

    _name = 'it_infra.server'
    _description = 'Server'
    _inherit = 'it_infra.computer'

    password = fields.Char(
        track_visibility='onchange'
    )

    open_ports = fields.Char(
        track_visibility='onchange'
    )

    virtual_machine = fields.Boolean()

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
