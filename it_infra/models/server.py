from odoo import _, exceptions, fields, models


class Server(models.Model):

    _name = "it_infra.server"
    _inherit = "it_infra.computer"

    _server_type_ = [
        ("bare_metal", "Bare Metal"),
        ("bare_metal_sa", "Bare Metal (Standalone)"),
        ("cloud", "Cloud"),
        ("hypervisor", "Hypervisor"),
        ("vm", "Virtual Machine"),
        ("docker", "Docker Stack"),
    ]

    password = fields.Char()

    open_ports = fields.Char(tracking=True)

    server_type = fields.Selection(selection=_server_type_)

    category_ids = fields.Many2many(
        comodel_name="it_infra.server_category",
        relation="server_category_rel",
        tracking=True,
        string="Categories",
    )

    location_id = fields.Many2one(
        comodel_name="it_infra.location", required=True
    )

    internal_location = fields.Boolean(related="location_id.internal")

    webadmin = fields.Char(string="Web Admin")

    hosted_in_id = fields.Many2one(
        comodel_name="it_infra.server", tracking=True
    )

    hosted_server_ids = fields.One2many(
        comodel_name="it_infra.server",
        inverse_name="hosted_in_id",
        readonly=True,
    )

    def unlink(self):
        for server in self:
            if server.state not in ("draft", "cancel"):
                raise exceptions.UserError(
                    _(
                        "You cannot delete a server \
                    which is not draft or cancelled."
                    )
                )
            res = super(Server, self).unlink()
            return res

    def show_passwd(self):
        for server in self:
            raise exceptions.except_orm(
                _("Password for user '%s':") % server.username,
                _("%s") % server.password,
            )
