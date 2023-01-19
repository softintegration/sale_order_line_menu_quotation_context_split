# -*- coding: utf-8 -*-

{
    'name': 'Sale order line menu & view with split-up the Quotation in account',
    'version': '1.0.1',
    'author':'Soft-integration',
    'category': 'Sale',
    'description': "",
    'depends': [
        'sale_order_line_menu',
        'sale_order_quotation_context_split'
    ],
    'data': [
        'views/sale_views.xml'
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}
