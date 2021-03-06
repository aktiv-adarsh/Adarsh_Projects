# -*- coding: utf-8 -*-
{
    'name': "orm_methods",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',
    'license': 'LGPL-3',

    # any module necessary for this one to work correctly
    'depends': ['base','sale'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/wizards_sale.xml',
        'views/sale_wizard_button.xml',
        'views/customer_name_get.xml',
        'views/get_val_setting.xml',
	    # 'relational_fld/relational.xml',
        # 'views/department.xml'
    ],
}



