# -*- coding: utf-8 -*-
{ 
    'name': 'To-Do Application', 
    'version': '1.0',
    'website' : 'https://www.odoo.com/page/accounting',
    'description': 'Pruebo',
    'author': 'Mariocgo', 
    'depends': [
        'base'
    ], 
    'application': True, 
    'data': [
        'security/ir.model.access.csv', 
        'security/todo_access_rules.xml', 
        'views/todo_menu.xml',
        'views/todo_view.xml',
     ],
    
}
