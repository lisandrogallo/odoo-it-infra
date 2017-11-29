# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import except_orm, Warning


class Server(models.Model):

    _name = 'it_infra.server'
    _inherit = 'it_infra.computer'

    password = fields.Char()

    open_ports = fields.Char()

    virtual_machine = fields.Boolean()

    category_ids = fields.Many2many(
        comodel_name='it_infra.server_category',
        relation='server_category_rel',
        string='Categories'
    )

    @api.multi
    def unlink(self):
        for server in self:
            if server.state not in ('draft', 'cancel'):
                raise Warning(_(
                    'You cannot delete a server \
                    which is not draft or cancelled.'))
            res = super(Server, self).unlink()
            self.clear_cache()
            return res

    @api.multi
    def show_passwd(self):
        for server in self:
            raise except_orm(
                _("Password for user '%s':") % server.username,
                _("%s") % server.password
            )
