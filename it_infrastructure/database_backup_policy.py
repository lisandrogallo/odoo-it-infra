# -*- coding: utf-8 -*-

from openerp import models, fields


class database_backup_policy(models.Model):
    """"""

    _name = 'it_infrastructure.database_backup_policy'
    _description = 'database_backup_policy'

    name = fields.Char(
        string='Name',
        required=True
    )

    backup_prefix = fields.Char(
        string='Back Up Prefix',
        required=True
    )

    cron_id = fields.Many2one(
        'ir.cron',
        string='Cron',
        required=True
    )

    database_ids = fields.Many2many(
        'it_infrastructure.database',
        'it_infrastructure_db_ids_db_backup_policy_ids_rel',
        'database_backup_policy_id',
        'database_id',
        string='database_ids'
    )

    database_type_ids = fields.Many2many(
        'it_infrastructure.database_type',
        'it_infrastructure_db_type_ids_db_backup_policy_ids',
        'database_backup_policy_id',
        'database_type_id',
        string='database_type_ids'
    )
