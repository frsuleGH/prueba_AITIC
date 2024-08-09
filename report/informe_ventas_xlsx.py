import io
import xlsxwriter
from odoo import models
from odoo.tools import date_utils

class InformeVentasMensualesXlsx(models.AbstractModel):
    _name = 'report.informe_ventas_mensuales.report_informe_ventas_xlsx'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, lines):
        worksheet = workbook.add_worksheet('Informe Ventas Mensuales')
        bold = workbook.add_format({'bold': True})
        date_format = workbook.add_format({'num_format': 'yyyy-mm-dd'})

        worksheet.write('A1', 'Producto', bold)
        worksheet.write('B1', 'Cliente', bold)
        worksheet.write('C1', 'Ingresos', bold)

        row = 1
        for line in lines:
            worksheet.write(row, 0, line.producto)
            worksheet.write(row, 1, line.cliente)
            worksheet.write(row, 2, line.ingresos)
            row += 1
