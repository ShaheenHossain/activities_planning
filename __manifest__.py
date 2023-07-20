# -*- coding: utf-8 -*-
{
    'name': "Activities Planing",

    'summary': """
        Activities Planing""",

    'description': """
        Activities Planing
    """,

    'author': "Md. Shaheen Hossain",
    'website': "https://www.eagle-erp.com",
    'category': 'Planning',
    'version': '16.0.1.0.0',
    'depends': ['base'],

    'data': [
            "views/activities_planning.xml",
            'security/ir.model.access.csv',

    ],

    # 'demo': [
    #     'demo/demo.xml',
    # ],


    "auto_install": False,
    'application': True,
    'license': 'LGPL-3',
    "installable": True,
}
