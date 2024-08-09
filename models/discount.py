from odoo import models, fields, api

class CustomerProductDiscount(models.Model):
    _name = 'customer.product.discount'
    _description = 'Descuento por Cliente y Producto'

    customer_id = fields.Many2one('res.partner', string='Cliente', required=True)
    product_id = fields.Many2one('product.product', string='Producto', required=True)
    discount = fields.Float(string='Descuento (%)', required=True)

    _sql_constraints = [
        ('unique_discount', 'unique(customer_id, product_id)', '¡Ya existe un descuento para este cliente y producto!')
    ]