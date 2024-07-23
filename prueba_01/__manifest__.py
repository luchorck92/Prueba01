{
    'name': 'Prueba01',
    'version': '1.0',
    'summary': 'este modulo agrega un campo personalizado en product.template',
    'description': 'Prueba',
    'category': 'sale',
    'author': 'Guillermo Parera',
    'depends': ['base','sale'],
    'data': [
        'views/sale_form_date.xml',
    ],
    'images': ['static/description/banner.png'],
    'installable': True,
    'application': False,
}