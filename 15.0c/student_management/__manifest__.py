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
        'wizards/Wizards_stu_man_smart_btn.xml',
        'views/student_management.xml',
        'views/student_fees.xml',
        'views/student_courses.xml',
        'views/student_email.xml',
        'report/student_paper_format.xml',
        'report/student_template.xml',
        'report/student_report.xml',
        # 'xml_report/student_server_action.xml',
        'views/controller.xml',
        'views/controller_2link.xml',
    ]
}
