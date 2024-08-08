{
    'name': 'Ventas AITIC',
    'version': '1.0',
    'category': 'Custom',
    'description': """
        AITIC
    """,
    'depends': ['base', 'sale'],
    'data': [
        'views/sale_order_views.xml',
        'views/ir_actions_report_templates.xml'
            ],
    'installable': True,
    'application': True,
}
