from odoo import models, fields, api

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    # Campo para almacenar el descuento personalizado
    sol_discount = fields.Float(string='Descuento (%)', readonly=False)

    @api.onchange('product_id', 'order_id.partner_id')
    def _aplicar_descuento_personalizado(self):
        """
        Método que se activa cuando cambia el producto o el socio de la orden.
        Busca un registro de descuento personalizado para el producto y el socio actual,
        y aplica ese descuento a la línea de la orden de venta.
        """
        for line in self:
            descuento = 0.0  # Inicializa el descuento en 0.0

            # Verifica si hay un producto y un socio asociados a la línea de orden
            if line.product_id and line.order_id.partner_id:
                # Busca un registro de descuento personalizado específico para el producto y el socio
                registro_descuento = self.env['customer.product.discount'].search([
                    ('customer_id', '=', line.order_id.partner_id.id),
                    ('product_id', '=', line.product_id.id)
                ], limit=1)

                # Si se encuentra un registro de descuento, asigna el valor del descuento
                if registro_descuento:
                    descuento = registro_descuento.discount

            # Asigna el descuento personalizado a los campos 'sol_discount' y 'discount'
            line.sol_discount = descuento
            line.discount = descuento