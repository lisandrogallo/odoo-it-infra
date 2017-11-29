# -*- coding: utf-8 -*-

import re
from datetime import datetime

from dateutil.relativedelta import relativedelta

from odoo import _, api, fields, models
from odoo.exceptions import Warning


class Equipment(models.Model):

    _name = 'it_infra.equipment'
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
            'it_infra.equipment_draft':
            lambda self, cr, uid, obj, ctx=None: obj['state'] == 'draft',
            'it_infra.equipment_active':
            lambda self, cr, uid, obj, ctx=None: obj['state'] == 'active',
            'it_infra.equipment_stored':
            lambda self, cr, uid, obj, ctx=None: obj['state'] == 'stored',
            'it_infra.equipment_decommissioned':
            lambda self, cr, uid, obj, ctx=None: obj[
                'state'] == 'decommissioned',
        },
    }

    @api.multi
    @api.constrains('stock_number')
    def _check_stock_number(self):
        if len(str(self.stock_number)) != 4:
            return False
        return True

    __check_doc_number_re = re.compile(r'([0-9]{3}\-[A-z]{3}\-[0-9]{4})$')

    @api.onchange('source_doc_number')
    def onchange_source_doc_number(self):
        if self.source_doc_number:
            if self.__check_doc_number_re.match(self.source_doc_number):
                self.source_doc_number = self.source_doc_number.upper()

    @api.multi
    @api.constrains('source_doc_number')
    def _check_doc_number(self):
        if self.source_doc_number:
            if not self.__check_doc_number_re.match(self.source_doc_number):
                raise Warning(_('Invalid document format'))
            else:
                tmp = self.source_doc_number.split('-')[2]
                input_date = datetime.strptime(tmp, '%Y')
                year_limit = datetime.today() - relativedelta(years=20)
                if input_date < year_limit or input_date > datetime.today():
                    raise Warning(_('Invalid document year.'))

    @api.multi
    def action_draft(self):
        self.write({'state': 'draft'})

    @api.multi
    def action_active(self):
        self.write({'state': 'active'})

    @api.multi
    def action_stored(self):
        self.write({'state': 'stored'})

    @api.multi
    def action_decommissioned(self):
        self.write({'state': 'decommissioned'})

    name = fields.Char(
        required=True
    )

    description = fields.Text()

    stock_number = fields.Integer(
        help='Format: XXXX (For example: 1234)'
    )

    hostname = fields.Char()

    ip_address = fields.Char()

    netmask = fields.Char(
        string='Network Mask',
        default='255.255.255.0'
    )

    source_doc_number = fields.Char(
        string='Source Document',
        help='Format: XXX-AAA-YYYY (For example: 123-ABC-2014)',
    )

    purchase_date = fields.Date()

    office = fields.Char()

    warranty = fields.Integer(
        string='Warranty (months)',
        default=12
    )

    state = fields.Selection(
        selection=_states_,
        default='draft'
    )

    _sql_constraints = [
        ('stock_number_unique',
         'unique(stock_number)',
         'Stock number already exists')
    ]
