# -*- coding: utf-8 -*-
{
    'name': "Adarsh_Exam",

    'summary': """
        Here i have designed website where user can register it self and 
        that record will display in contacts.""",

    'description': """
        This module is designed for the new user where admin don't need to add 
        new records manually because it will auto updated on contacts.  
    """,

    'author': "Aktiv Software",
    'website': "https://www.aktivsoftware.com/",

    'category': 'website',
    'version': '15.0.1.0.0',
    'license': 'LGPL-3',

    # any module necessary for this one to work correctly
    'depends': ['base', 'website', 'contacts', 'mail'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/registration_form.xml',
        'views/controller.xml',
    ],
    'assets': {'web.assets_frontend': [
        '/Adarsh_Exam_02-06-2022/static/src/css/style.css',
    ]},
}
