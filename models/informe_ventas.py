from odoo import models, fields

class InformeVentas(models.Model):
    _name = 'informe.ventas'
    _description = 'Informe de Ventas'

    name = fields.Char(string='Nombre', required=True, default='Informe de Ventas')
    fecha_inicio = fields.Date(string='Fecha de Inicio', required=True)
    fecha_fin = fields.Date(string='Fecha de Fin', required=True)
    sale_order_ids = fields.Many2many('sale.order', string='Órdenes de Venta')


    def action_generate_report(self):
        self.ensure_one()

        # Buscar las órdenes de venta en el rango de fechas
        ventas = self.env['sale.order'].search([
            ('date_order', '>=', self.fecha_inicio),
            ('date_order', '<=', self.fecha_fin),
            ('state', 'in', ['sale', 'done'])
        ])

        # Asignar las órdenes encontradas al campo sale_order_ids
        self.sale_order_ids = ventas

        # Generar el reporte
        return self.env.ref('ventas_aitic.informe_ventas_action').report_action(self)

