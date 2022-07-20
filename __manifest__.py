# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name': 'Material Keda Tech',
    'version': '1.0',
    'category': 'Sales/Sales',
    'summary': 'Material Management Tools',
    'description': """
This module allows you to manage all operations for managing material.
=========================================================================

It supports different kind of features:
--------------------------------------
    * Insert new material
    * Edit material
    * Delete material

    """,
    'category': 'Extra Tools',
    'author': 'Muhammad Yusran',
    'maintainer':'Muhammad Yusran',
    'depends': ['base'],
    'data': [
        'views/material_view.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'application': True,
    'sequence': '1',
    'auto_install': False,
    'website': 'https://www.odoo.com/app/forum',
    'license': 'LGPL-3',
}
