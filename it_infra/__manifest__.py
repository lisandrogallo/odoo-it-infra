# -*- coding: utf-8 -*-

{
    'name': u'IT Infrastructure',
    'version': '10.0.2.0.0',
    'category': u'base.module_category_knowledge_management',
    'author': u'Liso Gallo',
    'license': 'AGPL-3',
    'depends': [u'mail'],
    'data': [
        u'data/software_category.xml',
        u'data/equipment_track.xml',
        u'data/software.xml',
        u'security/groups.xml',
        u'security/ir.model.access.csv',
        u'views/device.xml',
        u'views/server_category.xml',
        u'views/server.xml',
        u'views/software_category.xml',
        u'views/software.xml',
        u'views/supply.xml',
        u'views/workstation.xml',
        u'views/location.xml',
        u'views/menu.xml'
    ],
    'installable': True,
    'auto_install': False,
    'demo': [],
}
