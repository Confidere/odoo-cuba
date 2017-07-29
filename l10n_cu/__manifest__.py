# -*- coding: utf-8 -*-

# Copyright (c) 2017 Confidere CU (http://confidere.brazzisoft.com).

{
    'name': "Cuba - Accounting",
    'description': """
Cuban accounting chart localization.
==================================================
        
Plan contable cubano de acuerdo a disposiciones vigentes.

    """,
    'author': "Confidere",
    'website': "http://confidere.brazzisoft.com",
    'category': 'Localization',
    'version': '0.1',
    'depends': [
        'account'
    ],
    'data': [
        "data/l10n_cu_chart_data.xml",
        "data/account_tax_data.xml",
        "data/account_chart_template_data.yml",
    ],
    # 'test': [
    #     'test/account_bank_statement.yml',
    #     'test/account_invoice_state.yml',
    # ],
    # 'demo': [
    #     'demo/account_bank_statement.yml',
    #     'demo/account_invoice_demo.yml',
    # ],
}