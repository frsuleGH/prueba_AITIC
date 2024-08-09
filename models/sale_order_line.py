from odoo import models, fields, api
import logging

_logger = logging.getLogger(__name__)

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    sol_discount = fields.Float(string='Discount (%)', readonly=False)

    @api.onchange('product_id', 'order_id.partner_id')
    def _apply_custom_discount(self):
        for line in self:
            discount = 0.0

            if line.product_id and line.order_id.partner_id:
                discount_record = self.env['customer.product.discount'].search([
                    ('customer_id', '=', line.order_id.partner_id.id),
                    ('product_id', '=', line.product_id.id)
                ], limit=1)

                if discount_record:
                    discount = discount_record.discount

            # Asigna el descuento personalizado y actualiza ambos campos
            line.sol_discount = discount
            line.discount = discount
