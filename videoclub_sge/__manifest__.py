# -*- coding: utf-8 -*-
{
    'name': "Videoclub",

    'summary': """
        Modulo creado con scaffolding para mi videoclub""",

    'description': """
        gestionaremos peliculas y categorias
    """,

    'author': "Vanesa Espín",
    'website': "https://www.ieshlanz.es",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Tools',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/videoclub_security.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
     "application": True,
    "installable": True,
}
