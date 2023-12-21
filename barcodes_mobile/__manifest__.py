# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Barcode in Mobile',
    'category': 'Hidden',
    'summary': 'Barcode scan in Mobile',
    'version': '1.0',
    'description': """ """,
    'depends': ['barcodes', 'web_mobile'],
    'data': ['views/barcodes_mobile_template.xml'],
    'qweb': ['static/src/xml/barcodes.xml'],
    'installable': True,
    'auto_install': False,
    'license': 'OEEL-1',
}
