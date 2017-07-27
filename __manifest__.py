# -*- coding: utf-8 -*-
{
    'name': 'l10n_nc',
    'version': '1.0',
    'category': 'Localization',
    'description': """
This is the module to manage the accounting chart for New Caledonia in Odoo.
========================================================================

This module is a copy of the l10n_fr module.

All the charts of account is the same, with the following differences:

* None of the TVA tax are created

* TSS and TGC tax are created
""",
    'depends': ['base_iban', 'account', 'base_vat'],
    'data': [
        'data/l10n_nc_chart_data.xml',
        'data/decimal_price.xml',
        'data/account_chart_template_data.xml',
        'views/l10n_nc_view.xml',
        'data/account_tax_data.xml',
        'data/account_reconcile_model_template.xml',
        'data/account_chart_template_data.yml',
    ],
}
