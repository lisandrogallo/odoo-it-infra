# -*- coding: utf-8 -*-

from openerp import models, fields


class computer_change(models.Model):
    """"""

    _name = 'it_infrastructure.computer_change'
    _description = 'computer_change'

    name = fields.Char(
        string='Summary',
        required=True
    )

    date = fields.Date(
        string='Date',
        required=True,
        default=fields.Date.context_today
    )

    user_id = fields.Many2one(
        'res.users',
        string='User',
        required=True,
        default=lambda self, cr, uid, context: uid
    )

    description = fields.Text(
        string='Description',
        required=True
    )

    computer_id = fields.Many2one(
        'it_infrastructure.computer',
        string='Computer',
        ondelete='cascade',
        required=True
    )
