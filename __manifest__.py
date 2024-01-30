{
    'name': 'propiedades',
    'summary': 'Módulo de gestión de propiedades inmobiliarias',
    'description': "Propiedades Inmobiliarias",
    'license': 'LGPL-3',
    'depends': [
        'base',
    ],
    'data': [
        'views/propiedades_inmuebles_views.xml',
        'views/inmuebles_tipos_views.xml'
        'views/inmuebles_etiquetas_views.xml'
        'views/propiedades_menus.xml',
        'security/ir.model.access.csv',
    ],
    'application': True
}

