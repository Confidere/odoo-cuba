# -*- coding: utf-8 -*-
{
    'name': "l10_cu",
    'author': "Carlos Fonseca",
    'website': "https://www.fonse.net",
    'category': 'Localization/Account Charts',
    'version': '0.1',

    'description': """
        Cuban Accounting and Tax Preconfiguration
    """,

    'depends': [
        'account',
        'account_chart',
    ],

    'data': [
        'data/account.account.type.csv',
        'data/account.account.template.csv',
        'data/account.tax.code.template.csv',
        'data/account_chart_template.xml',
        'data/account.tax.template.csv',
        'wizard/account_wizard.xml',    
    ],
    'demo': [
    ],
    'installable': True,
    'images': [],    
}
