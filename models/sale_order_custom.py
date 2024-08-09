from odoo import models, fields

# Clase que hereda de 'sale.order' para agregar campos personalizados
class SaleOrder(models.Model):
    _inherit = 'sale.order'

    # Campo de texto para información adicional
    campo_personalizado_1 = fields.Char(
        string="Información Adicional (campo_personalizado_1)",
        help="Este campo debe contener información adicional relevante para la orden de venta. Puede ser utilizado para incluir datos específicos que el cliente considere importante visualizar en el informe."
    )

    # Campo numérico para datos adicionales
    campo_personalizado_2 = fields.Float(
        string="Datos Numéricos (campo_personalizado_2)",
        help="Se trata de un campo numérico que puede almacenar valores como cantidades adicionales o datos numéricos relacionados con la orden de venta."
    )

    # Campo de fecha para eventos importantes
    campo_personalizado_3 = fields.Date(
        string="Fecha de Evento (campo_personalizado_3)",
        help="Este campo debe contener fechas relacionadas con la orden de venta. Puede ser útil para rastrear eventos importantes o plazos asociados con la transacción."
    )
