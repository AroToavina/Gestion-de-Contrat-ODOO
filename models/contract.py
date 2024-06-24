from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Contract(models.Model):
    _name = 'contract.contract'
    _description = 'Contract'

    name = fields.Char('Contract Number', required=True)
    start_date = fields.Date('Start Date', required=True)
    end_date = fields.Date('End Date', required=True)
    amount = fields.Float('Contract Amount', required=True)
    customer_id = fields.Many2one('res.partner', string='Customer')

    def generate_invoice(self):
        invoice_vals = {
            'partner_id': self.customer_id.id,
            'move_type': 'out_invoice',
            'invoice_date': fields.Date.today(),
            'invoice_line_ids': [(0, 0, {
                'name': self.name,
                'quantity': 1,
                'price_unit': self.amount,
            })],
        }
        invoice = self.env['account.move'].create(invoice_vals)
        return invoice
