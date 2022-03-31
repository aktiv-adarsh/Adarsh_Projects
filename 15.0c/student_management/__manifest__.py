# -*- coding: utf-8 -*-
{
    'name': "students_management",

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
    'depends': ['base', 'contacts', 'sale', 'mail', 'project'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'wizards/sale_2wizards_order.xml',
        # 'wizards/wizards_2sale.xml',
        'views/student_management.xml',
        'views/contacts_soperator_script.xml',
        'views/sale_soperator_script.xml',
        'data/tag_data_file.xml',
    ]
}
