from odoo import models, fields

class InformeVentas(models.Model):
    _name = 'informe.ventas'
    _description = 'Informe de Ventas'

    # Campo para el nombre del informe, requerido y con un valor predeterminado
    name = fields.Char(string='Nombre', required=True, default='Informe de Ventas')
    # Campo para la fecha de inicio del informe, requerido
    fecha_inicio = fields.Date(string='Fecha de Inicio', required=True)
    # Campo para la fecha de fin del informe, requerido
    fecha_fin = fields.Date(string='Fecha de Fin', required=True)
    # Campo para las órdenes de venta relacionadas
    sale_order_ids = fields.Many2many('sale.order', string='Órdenes de Venta')

    def action_generate_report(self):
        # Asegurarse de que solo se está trabajando con un registro
        self.ensure_one()

        # Buscar las órdenes de venta dentro del rango de fechas especificado
        # y que estén en estado de 'sale' o 'done'
        ventas = self.env['sale.order'].search([
            ('date_order', '>=', self.fecha_inicio),
            ('date_order', '<=', self.fecha_fin),
            ('state', 'in', ['sale', 'done'])
        ])

        # Asignar las órdenes de venta encontradas al campo sale_order_ids
        self.sale_order_ids = ventas

        # Generar el informe de ventas basado en las órdenes de venta encontradas
        return self.env.ref('ventas_aitic.informe_ventas_action').report_action(self)
