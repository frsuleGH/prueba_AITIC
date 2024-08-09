from odoo import models, fields, api

class CustomerProductDiscount(models.Model):
    _name = 'customer.product.discount'
    _description = 'Discount by Customer and Product'

    customer_id = fields.Many2one('res.partner', string='Customer', required=True)
    product_id = fields.Many2one('product.product', string='Product', required=True)
    discount = fields.Float(string='Discount (%)', required=True)

    _sql_constraints = [
        ('unique_discount', 'unique(customer_id, product_id)', 'A discount for this customer and product already exists!')
    ]