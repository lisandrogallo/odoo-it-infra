# -*- coding: utf-8 -*-

from openerp import netsvc
from openerp import models, fields, api, _
from openerp.exceptions import Warning
import re
from datetime import datetime
from dateutil.relativedelta import relativedelta


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
    @api.constrains('stock_number')
    def _check_stock_number(self):
        if len(str(self.stock_number)) != 4:
            return False
        return True

    __check_document_number_re = re.compile(r'([0-9]{3}\-[A-z]{3}\-[0-9]{4})$')

    @api.onchange('source_document_number')
    def onchange_source_document_number(self):
        if self.source_document_number:
            if self.__check_document_number_re.match(self.source_document_number):
                self.source_document_number = self.source_document_number.upper()

    @api.multi
    @api.constrains('source_document_number')
    def _check_document_number(self):
        if self.source_document_number:
            if not self.__check_document_number_re.match(self.source_document_number):
                raise Warning(_('Invalid document format'))
            else:
                tmp = self.source_document_number.split('-')[2]
                input_date = datetime.strptime(tmp, '%Y')
                year_limit = datetime.today() - relativedelta(years=20)
                if input_date < year_limit or input_date > datetime.today():
                    raise Warning(_('Invalid document year.'))

    @api.one
    def action_draft(self):
        self.state = 'draft'

    @api.one
    def action_active(self):
        self.state = 'active'

    @api.one
    def action_stored(self):
        self.state = 'stored'

    @api.one
    def action_decommissioned(self):
        self.state = 'decommissioned'

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

    source_document_number = fields.Char(
        string='Source Document',
        help='Format: XXX-AAA-YYYY (For example: 123-ABC-2014)',
    )

    purchase_date = fields.Date(
        string='Purchase Date',
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
