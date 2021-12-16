
{
    'name': 'Countdown',
    'version': '1.0',
    'category': 'Website',
    'summary': 'Website Countdown Widget',
    'description': """Countdown""",
    'author': 'Turkesh Patel, Medma Infomatix',
    'depends': ['website', 'product', 'website_sale'],
    'website': 'http://turkeshpatel.odoo.com',
    'data': ['security/ir.model.access.csv',
             # 'views/countdown.xml',
             'views/templates.xml',
             'views/website_config.xml',
             'views/product.xml',
             ],
    'images': [
        'static/description/icon.png',
    ],
    'demo_xml': [],
    'installable': True,
    'active': True,
}

