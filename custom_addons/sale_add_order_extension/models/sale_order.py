from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    parent_order_id = fields.Many2one('sale.order', string='Parent Order')
    child_order_ids = fields.One2many('sale.order', 'parent_order_id', string='Related Orders')

    def action_create_related_order(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'New Quotation',
            'res_model': 'sale.order',
            'view_mode': 'form',
            'target': 'current',
            'context': {
                'default_partner_id': self.partner_id.id,
                'default_origin': self.name,
                'default_parent_order_id': self.id,
            }
        }