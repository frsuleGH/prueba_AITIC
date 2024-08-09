from odoo import models, fields, api
from odoo.exceptions import UserError

class InformeVentasMensuales(models.TransientModel):
    _name = 'informe.ventas.mensuales'
    _description = 'Informe de Ventas Mensuales'

    fecha_inicio = fields.Date(string="Fecha de Inicio", required=True)
    fecha_fin = fields.Date(string="Fecha de Fin", required=True)

    def action_generar_informe(self):
        if not self.fecha_inicio or not self.fecha_fin:
            raise UserError("Por favor, complete el rango de fechas.")
        
        # Lógica para obtener datos de ventas
        venta_obj = self.env['sale.order']
        ventas = venta_obj.search([
            ('date_order', '>=', self.fecha_inicio),
            ('date_order', '<=', self.fecha_fin)
        ])
       
        # Aquí podrías agregar la lógica para generar y devolver el informe
        return True
