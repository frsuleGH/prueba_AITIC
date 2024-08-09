{
    'name': 'Ventas AITIC',
    'version': '1.0',
    'category': 'Custom',
    'description': """
        AITIC
    """,
    'depends': ['base', 'sale', 'sale_management'],
    'data': [
        'views/campos.xml',
        'views/discount_views.xml',
        'views/ir_actions_report_templates.xml',
        'views/informe_ventas_views.xml',
        'report/informe_ventas_report.xml',
            ],
    'installable': True,
    'application': True,
}
