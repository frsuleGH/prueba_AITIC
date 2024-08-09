from odoo import models, fields

class InformeVentas(models.Model):
    _name = 'informe.ventas'
    _description = 'Informe de Ventas'

    fecha_inicio = fields.Date(string='Fecha de Inicio')
    fecha_fin = fields.Date(string='Fecha de Fin')

    def action_generate_report(self):
        self.ensure_one()
        fecha_inicio = self.fecha_inicio
        fecha_fin = self.fecha_fin

        # Buscar las órdenes de venta en el rango de fechas
        ventas = self.env['sale.order'].search([
            ('date_order', '>=', fecha_inicio),
            ('date_order', '<=', fecha_fin),
            ('state', 'in', ['sale', 'done'])
        ])

        ingresos_totales = sum(venta.amount_total for venta in ventas)
        desglose_producto = {}
        desglose_cliente = {}

        # Recolectar desglose por producto y cliente
        for venta in ventas:
            for linea in venta.order_line:
                producto = linea.product_id.name
                if producto in desglose_producto:
                    desglose_producto[producto] += linea.price_subtotal
                else:
                    desglose_producto[producto] = linea.price_subtotal

            cliente = venta.partner_id.name
            if cliente in desglose_cliente:
                desglose_cliente[cliente] += venta.amount_total
            else:
                desglose_cliente[cliente] = venta.amount_total

        # Convertir desglose a diccionario serializable
        desglose_producto = {k: v for k, v in desglose_producto.items()}
        desglose_cliente = {k: v for k, v in desglose_cliente.items()}

        # Generar el reporte
        return self.env.ref('ventas_aitic.informe_ventas_action').report_action(self, data={
            'doc_ids': self.ids,  # Usar self.ids en lugar de self.id para manejar múltiples registros
            'doc_model': 'informe.ventas',
            'docs': ventas,
            'ingresos_totales': ingresos_totales,
            'desglose_producto': desglose_producto,
            'desglose_cliente': desglose_cliente
        })
