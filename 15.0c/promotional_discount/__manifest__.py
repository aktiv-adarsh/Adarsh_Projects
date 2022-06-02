# -*- coding: utf-8 -*-
{
    'name': "promotional_discount",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Vaghela Nilesh",
    'website': "http://www.aktivsoftware.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/
    # 14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Sale Order',
    'version': '15.0.1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/sale_views.xml',
        'views/views.xml',
        'views/res_config_setting_view.xml',
    ],
    'license': 'LGPL-3',
}
