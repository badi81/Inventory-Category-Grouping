{
    'name': 'Inventory Category Grouping',
    'version': '17.0.1.0.0',
    'category': 'Inventory',
    'summary': 'Add "Group by Product Category" to the Locations Report in the Inventory module.',
    'description': '''
        This module enhances the Inventory module in Odoo 17 by adding a "Group by Product Category" feature to the Locations Report.
        It helps businesses better analyze and manage their stock by categorizing products efficiently within inventory locations.
    ''',
    'author': 'Mohamed Badi',
    'company': 'iTech Solutions & Innovations',
    'website': 'https://www.itech-libya.com',
    'license': 'LGPL-3',
    'depends': ['stock'],
    'data': [
        'views/stock_quant_views.xml',
    ],
    'installable': True,
    'application': False,
    'support': 'mohamed.badi@gmail.com',  # Add your support email here
    'price': 14.00,
    'currency': 'USD',

}
