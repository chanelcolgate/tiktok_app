# -*- coding: utf-8 -*-
{
    'name': "Tiktok Shop App",

    'summary': "Manage and send data to factory to print",

    'author': "chanelcolgate",
    'website': "https://www.github.com/chanelcolgate/library_app",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Services/Tiktok',
    'version': '15.0.1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        "security/tiktok_security.xml",
        'security/ir.model.access.csv',
        "views/tiktok_menu.xml",
        "views/product_view.xml",
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    "application": True,
}
