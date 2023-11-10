# -*- coding: utf-8 -*-
{
    'name': "Ukrainian Gears - 1C: Enterprise8.3 Connector",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Bakum Viacheslav",
    'website': "https://www.yourcompany.com",
    'license': "LGPL-3",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '16.0.1.0',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    'data': [
        # 'security/ir.model.access.csv',
        'views/currency_views.xml',
    ],

    # always loaded

    # only loaded in demonstration mode

    "external_dependencies": {
        "python": ["pydantic", "contextvars", "typing-extensions"]
    },
    'installable': True,
    'application': False,
    'auto_install': False,
}
