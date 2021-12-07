# -*- coding: utf-8 -*- 
from odoo.tests.common import TransactionCase 
# También debemos añadir un caso de prueba para asegurarnos de que los
# usuarios sólo pueden ver sus propias tareas. 
from odoo.exceptions import AccessError 

 
class TestTodo(TransactionCase): 
 
    def test_create(self): 
        "Create a simple Todo" 
        Todo = self.env['todo.task'] 
        task = Todo.create({'name': 'Test Task'}) 
        self.assertEqual(task.is_done, False)

    # Test Toggle Done 
        task.do_toggle_done() 
        self.assertTrue(task.is_done) 
        # Test Clear Done 
        Todo.do_clear_done() 
        self.assertFalse(task.active)

    # Metodo para que sea aplicado a los usuarios demo
     def setUp(self, *args, **kwargs): 
        result = super(TestTodo, self).setUp(*args, \ 
        **kwargs) 
        user_demo = self.env.ref('base.user_demo') 
        self.env= self.env(user=user_demo) 
        return result 

    # Dado que nuestro método env ahora está utilizando el usuario de Demo, 
    # usamos el método sudo () para cambiar el contexto al usuario admin. 
    def test_record_rule(self): 
        "Test per user record rules" 
        Todo = self.env['todo.task'] 
        task = Todo.sudo().create({'name': 'Admin Task'}) 
        with self.assertRaises(AccessError): 
            Todo.browse([task.id]).name 
