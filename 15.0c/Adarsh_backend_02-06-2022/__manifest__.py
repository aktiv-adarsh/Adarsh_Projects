# -*- coding: utf-8 -*-
{
    'name': "Adarsh_Exam",

    'summary': """
        This module contains different action on buttons,
        changing state of statusbar and perform conditionally search.""",

    'description': """
        This module contains different types of fields and functions.
        Where the data will filter according to user given input. 
    """,

    'author': "Aktiv Software",
    'website': "https://www.aktivsoftware.com/",

    'category': 'Project',
    'version': '15.0.1.0.0',
    'license': 'LGPL-3',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale_management', 'contacts', 'mail', 'web_domain_field'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'wizards/wizard_batch_sale.xml',
        'views/batch_sale_workflow.xml',
    ],
}
