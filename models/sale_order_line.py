from odoo import models, fields, api

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    sol_discount = fields.Float(string='Descuento (%)', readonly=False)

    @api.onchange('product_id', 'order_id.partner_id')
    def _aplicar_descuento_personalizado(self):
        for line in self:
            descuento = 0.0

            if line.product_id and line.order_id.partner_id:
                registro_descuento = self.env['customer.product.discount'].search([
                    ('customer_id', '=', line.order_id.partner_id.id),
                    ('product_id', '=', line.product_id.id)
                ], limit=1)

                if registro_descuento:
                    descuento = registro_descuento.discount

            # Asigna el descuento personalizado y actualiza ambos campos
            line.sol_discount = descuento
            line.discount = descuento