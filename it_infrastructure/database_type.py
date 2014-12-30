# -*- coding: utf-8 -*-

from openerp import models, fields


class database_type(models.Model):

    _name = 'it_infrastructure.database_type'
    _description = 'database_type'

    name = fields.Char(
        string='Name',
        required=True
    )

    prefix = fields.Char(
        string='Prefix',
        required=True,
        size=4
    )

    url_prefix = fields.Char(
        string='URL Prefix'
    )

    automatic_drop = fields.Boolean(
        string='Automatic Drop'
    )

    automatic_drop_days = fields.Integer(
        string='Automatic Drop Days'
    )

    protect_db = fields.Boolean(
        string='Protect Databases?'
    )

    color = fields.Integer(
        string='Color'
    )

    automatic_deactivation = fields.Boolean(
        string='Automatic Deactivation?'
    )

    auto_deactivation_days = fields.Integer(
        string='Automatic Deactivation Days'
    )

    url_example = fields.Char(
        string='URL Example'
    )

    database_name_example = fields.Char(
        string='Database Name Example'
    )

    database_backup_policy_ids = fields.Many2many(
        'it_infrastructure.database_backup_policy',
        'db_type_ids_database_backup_policy_ids_rel',
        'database_type_id',
        'database_backup_policy_id',
        string='Suggested Backup Policies'
    )
