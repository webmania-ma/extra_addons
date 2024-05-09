# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Margins in Sales Orders',
    'version': '1.0',
    'category': 'Sales/Sales',
    'description': """ 
    This gives the profitability by calculating the difference between the Unit
    Price and Cost Price.
    """,
    'author': "Webmania",
    'website': "https://www.webmania.ma",
    'depends': ['sale_management', 'product'],
    'data': ['security/ir.model.access.csv',
             'views/sale_margin_view.xml',
             'views/view_product_price_list.xml',
             ],
    'license': 'LGPL-3',
}
