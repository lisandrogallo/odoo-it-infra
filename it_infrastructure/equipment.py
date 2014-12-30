# -*- coding: utf-8 -*-

from openerp import models, fields


class equipment(models.Model):

    _name = 'it_infrastructure.equipment'
    _description = 'Equipment'
    _inherit = ['mail.thread', 'ir.needaction_mixin']

    _states_ = [
        ('pending', 'Pending'),
        ('active', 'Active'),
        ('stored', 'Stored'),
        ('decommissioned', 'Decommissioned'),
    ]

    _track = {
        'state': {
            'it_infrastructure.equipment_pending':
            lambda self, cr, uid, obj, ctx=None: obj['state'] == 'pending',
            'it_infrastructure.equipment_active':
            lambda self, cr, uid, obj, ctx=None: obj['state'] == 'active',
            'it_infrastructure.equipment_stored':
            lambda self, cr, uid, obj, ctx=None: obj['state'] == 'stored',
            'it_infrastructure.equipment_decommissioned':
            lambda self, cr, uid, obj, ctx=None: obj['state'] == 'decommissioned',
        },
    }

    name = fields.Char(
        string='Name',
        required=True
    )

    stock_number = fields.Integer(
        string='Stock Number',
        required=True
    )

    input_date = fields.Date(
        string='Input Date'
    )

    warranty = fields.Integer(
        string='Warranty (months)',
        default=12
    )

    office_id = fields.Many2one(
        'hr.department',
        string='Office',
        required=True
    )
