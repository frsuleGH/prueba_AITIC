from odoo import models, fields, api

# Clase que define el modelo de descuentos específicos para cada cliente y producto
class CustomerProductDiscount(models.Model):
    _name = 'customer.product.discount'  # Nombre del modelo
    _description = 'Descuento por Cliente y Producto'  # Descripción del modelo

    # Campo Many2one para relacionar el descuento con un cliente específico
    customer_id = fields.Many2one('res.partner', string='Cliente', required=True)
    # Campo Many2one para relacionar el descuento con un producto específico
    product_id = fields.Many2one('product.product', string='Producto', required=True)
    # Campo Float para almacenar el porcentaje de descuento
    discount = fields.Float(string='Descuento (%)', required=True)

    # Restricción SQL para asegurar que no se creen descuentos duplicados para el mismo cliente y producto
    _sql_constraints = [
        ('unique_discount', 'unique(customer_id, product_id)', '¡Ya existe un descuento para este cliente y producto!')
    ]