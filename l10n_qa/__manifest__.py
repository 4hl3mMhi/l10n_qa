# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Qatar - Accounting',
    'version': '15.0.1',
    'author': 'Ahlem Mehri',
    'category': 'Accounting/Localizations/Account Charts',
    'description': """
Qatar accounting chart and localization.
=======================================================
This module is a migration of l10n_qa version 14 from:
https://apps.odoo.com/apps/modules/14.0/l10n_qa/
    """,
    'depends': ['account', 'l10n_multilang'],
    'data': [
        'data/l10n_qa_chart_data.xml',
        'data/account.account.template.csv',
        'data/account_tax_group_data.xml',
        'data/l10n_qa_chart_post_data.xml',
        'data/account_tax_report_data.xml',
        'data/account_tax_template_data.xml',
        'data/fiscal_templates_data.xml',
        'data/account_chart_template_configure_data.xml',
    ],
    'images': ['static/description/banner.png'],
    'demo': [
        'demo/demo_company.xml',
    ],
    'post_init_hook': 'load_translations',
    'license': 'LGPL-3',
}
