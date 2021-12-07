# -*- coding: utf-8 -*- 
from odoo import models, fields, api 
from odoo.exceptions import ValidationError

class TodoTask(models.Model): 
# La siguiente línea establece el atributo _name que define el identificador que se utilizará en
#  Odoo para referirse a este modelo. Toma en cuenta que el nombre real de la clase Python, TodoTask en 
#  este caso, carece de significado para otros módulos Odoo. El valor _name es lo que se utilizará como 
#  identificador.

# Para extender un modelo existente, usamos una clase Python con un atributo _inherit. 
# Esto identifica el modelo a ser extendido. La nueva clase hereda todas las características del 
# modelo Odoo padre, y solo necesitamos declarar las modificaciones que queremos introducir.
# TodoTask es local para este archivo de Python y, en general, es irrelevante para otros módulos. 
# _inherit es la clave aquí: le dice a Odoo que esta clase está heredando y modificando así el modelo 
# todo.task.
# Observa que el atributo _name está ausente. No es necesario porque ya está heredado del modelo padre.

# Punto 2: Con respecto al segundo punto, la herencia en mail.thread se hace usando el atributo _inherit 
# que utilizamos antes. Pero nuestra extensión de tareas pendientes ya está usando el atributo _inherit. 
# Afortunadamente, puede aceptar una lista de modelos de los que heredar, por lo que podemos usar esto
# para que también incluya la herencia en mail.thread:

# El módulo de red social (nombre técnico mail) proporciona el panel de mensajes que se encuentra en la 
# parte inferior de muchos formularios y la función Seguidores, así como la lógica de los mensajes y las 
# notificaciones
    _name = 'todo.task'
    _inherit = ['todo.task', 'mail.thread']
# El campo user_id representa un usuario del modelo de usuarios res.users. 
# con instalar el addon, se añadiran los 2 campos a la tabla "todo.task"
# Es un campo Many2one, que es equivalente a una clave extranjera en la jerga de la base de dato
    user_id = fields.Many2one('res.users', 'Responsible') 
# El date_deadline es un simple campo de fecha.    
    date_deadline = fields.Date('Deadline')
# es posible modificar los atributos en los campos heredados existentes. Se hace agregando un 
# campo con el mismo nombre y estableciendo valores sólo para los atributos que se van a cambiar.    
    name = fields.Char(help="What needs to be done?")

# Para extender o cambiar la lógica existente, el método correspondiente puede anularse declarando un
# método con el mismo nombre. El nuevo método reemplazará al anterior, y también puede extender el código 
# de la clase heredada, utilizando el método super () de Python para llamar al método padre. Puede entonces
# agregar nueva lógica alrededor de la lógica original antes y después de que el método super ()
# sea llamado.    


# domain: que es una lista de condiciones, donde cada condición es una tupla.
# Estas condiciones se unen implícitamente con el operador AND (&). Para la operación OR, una tubería, | 

# El dominio utilizado aquí filtra todas las tareas hechas ('is_done', '=', True) 
# que tienen el usuario actual como responsable ('user_id', '=', self.env.uid) o no
#  tienen un set de usuario actual ('user_id', '=', False).     
    @api.multi 
    def do_clear_done(self):       
        domain = [('is_done', '=', True), 
                '|', ('user_id', '=', self.env.uid), 
                        ('user_id', '=', False)] 
        dones = self.search(domain) 
        dones.write({'active': False}) 
        return True 


# El método en la clase heredada comienza con un bucle for para comprobar que ninguna de las tareas a 
# activar pertenece a otro usuario. Si estos chequeos pasan, entonces continúa llamando al método de clase 
# padre, usando super(). Si no se plantea un error, y debemos utilizar para ello las excepciones
# incorporadas de Odoo. Los más relevantes son ValidationError, utilizado aquí y UserError.


    @api.multi 
    def do_toggle_done(self): 
        for task in self: 
            if task.user_id != self.env.user: 
                raise ValidationError(
                    'Only the responsible can do this!') 
        return super(TodoTask, self).do_toggle_done()
