# -*- coding: utf-8 -*-

{ 
   'name': 'Multiuser To-Do', 
   'description': 'Extend the To-Do app to multiuser.', 
   'author': 'Mariocgo', 
   'depends': [
      'todo_app2',
      'mail',
   ], 
   'data': [
      'views/todo_task.xml',
      'security/todo_access_rules.xml',
   ],
}