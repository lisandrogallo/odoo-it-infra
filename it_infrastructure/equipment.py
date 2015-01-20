# -*- coding: utf-8 -*-

from openerp import models, fields, api


class equipment(models.Model):

    _name = 'it_infrastructure.equipment'
    _description = 'Equipment'
    _inherit = ['mail.thread', 'ir.needaction_mixin']
    _order = "purchase_date desc"

    _states_ = [
        ('draft', 'Draft'),
        ('active', 'Active'),
        ('stored', 'Stored'),
        ('decommissioned', 'Decommissioned'),
    ]

    _track = {
        'state': {
            'it_infrastructure.equipment_draft':
            lambda self, cr, uid, obj, ctx=None: obj['state'] == 'draft',
            'it_infrastructure.equipment_active':
            lambda self, cr, uid, obj, ctx=None: obj['state'] == 'active',
            'it_infrastructure.equipment_stored':
            lambda self, cr, uid, obj, ctx=None: obj['state'] == 'stored',
            'it_infrastructure.equipment_decommissioned':
            lambda self, cr, uid, obj, ctx=None: obj['state'] == 'decommissioned',
        },
    }

    @api.multi
    def _check_stock_number(self):
        if len(str(self.stock_number)) != 4:
            return False
        return True

    _constraints = [
        (_check_stock_number, 'Error: Invalid stock number', ['stock_number'])
    ]

    name = fields.Char(
        string='Name',
        required=True
    )

    description = fields.Html(
        string='Description'
    )

    stock_number = fields.Integer(
        string='Stock Number',
        required=True,
        help='Format: XXXX (For example: 1234)'
    )

    purchase_date = fields.Date(
        string='Purchase Date',
        required=True
    )

    warranty = fields.Integer(
        string='Warranty (months)',
        default=12
    )

    office_id = fields.Many2one(
        'hr.department',
        string='Office'
    )

    state = fields.Selection(
        selection=_states_,
        string='State',
        default='draft'
    )

    _sql_constraints = [
        ('stock_number_unique', 'unique(stock_number)', 'Stock number already exists')
    ]
