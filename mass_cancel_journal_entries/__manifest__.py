# -*- coding: utf-8 -*-
{
    'name': "Mass Cancel Journal Entries",
    'summary': """ This module allows to cancel mass/bulk/multiple Journal Entries
            from the tree view.""", 
    'author': "AktivSoftware",
    'website': "http://www.aktivsoftware.com",
    'category': 'Invoicing',
    'version': '11.0.1.0.1',
    'license': 'AGPL-3',

    # any module necessary for this one to work correctly
    'depends': ['account_cancel', 'account_invoicing'],

    # always loaded
    'data': [
        'wizard/journal_entries_cancel_wizard.xml',
    ],
    'images': ['static/description/banner.png'],
    'installable': True,
    'auto_install': False,
}
