# -*- coding: utf-8 -*-

from openerp import models, fields, api, _
from openerp.exceptions import except_orm
import os
from fabric.api import cd, sudo
from fabric.contrib.files import exists


class repository(models.Model):

    """"""

    _name = 'it_infrastructure.repository'
    _description = 'repository'

    sequence = fields.Integer(
        string='Sequence'
    )

    name = fields.Char(
        string='Name',
        required=True
    )

    directory = fields.Char(
        string='Directory',
        required=True
    )

    type = fields.Selection(
        [(u'git', 'git')],
        string='Type',
        required=True
    )

    addons_subdirectory = fields.Char(
        string='Addons Subdirectory'
    )

    url = fields.Char(
        string='URL',
        required=True
    )

    pip_packages = fields.Char(
        string='PIP Packages'
    )

    is_server = fields.Boolean(
        string='Is Server?'
    )

    install_server_command = fields.Char(
        string='Install Server Command',
        default='python setup.py install'
    )

    branch_ids = fields.Many2many(
        'it_infrastructure.repository_branch',
        'infrastructure_repository_ids_branch_ids_rel',
        'repository_id',
        'repository_branch_id',
        string='Branches'
    )

    _order = "sequence"

    @api.one
    def get_repository(self, server):
        server.get_env()
        if not exists(server.sources_path, use_sudo=True):
            raise except_orm(
                _('No Source Directory!'),
                _("Please first create the source directory '%s'!")
                % (server.sources_path,))
        with cd(server.sources_path):
            path = False
            if self.type == 'git':
                command = 'git clone '
                command += self.url
                command += ' ' + self.directory
                sudo(command)
                path = os.path.join(server.sources_path, self.directory)
                # TODO implementar otros tipos de repos
        return path
