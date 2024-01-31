{
    'name': 'propiedades',
    'summary': 'Módulo de gestión de propiedades inmobiliarias',
    'description': "Propiedades Inmobiliarias",
    'license': 'LGPL-3',
    'depends': [
        'base',
    ],
    'data': [
        'views/svrc_propiedades_inmuebles_views.xml',
        'views/svrc_inmuebles_tipos_views.xml',
        'views/svrc_inmuebles_etiquetas_views.xml',
        'views/svrc_inmuebles_ofertas_views.xml',
        'views/svrc_propiedades_menus.xml',
        'security/ir.model.access.csv',
    ],
    'application': True
}

