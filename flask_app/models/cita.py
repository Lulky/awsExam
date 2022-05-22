
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Cita:

    def __init__(self, data):
        self.id= data['id']
        self.tasks= data['tasks']
        self.date= data['date']
        self.status= data['status']
        self.user_id = data ['user_id']
        self.created_at= data['created_at']
        self.updated_at= data['updated_at']
        
    @staticmethod
    def valida_cita(formulario):
        es_valido = True

        if len(formulario['tasks'])<3:
            flash("El task de la receta debe tener al menos 3 caracteres", "cita")
            es_valido = False

        if formulario['date']=="":
            flash("Ingrese una fecha", "cita")
            es_valido = False

        return es_valido

    @classmethod
    def save(cls, data):
        query = "INSERT INTO citas (tasks, date, status, user_id) VALUES (%(tasks)s, %(date)s, %(status)s, %(user_id)s);"
        nuevo = connectToMySQL('esquema_citas').query_db(query, data)
        return nuevo

    #te todos los registros
    @classmethod
    def get_all(cls):#guardado, edicion, hacer un select de un regsitro en especifico o cuando quisiera hacer una validacion se usa data, osea que cumpla una condicional
        query = "SELECT * FROM citas"
        results= connectToMySQL('esquema_citas').query_db(query)
        citas = []
        for cita in results:
            citas.append(cls(cita))
        return citas

    #Solo te regresa un registro
    @classmethod
    def get_by_id(cls, data):
        query = "SELECT * FROM citas WHERE id = %(id)s"
        result = connectToMySQL('esquema_citas').query_db(query, data)
        cita = cls(result[0])
        return cita

    @classmethod
    def update(cls, data):
        query = "UPDATE citas SET tasks=%(tasks)s, date=%(date)s, status=%(status)s WHERE id=%(id)s;"
    
        result = connectToMySQL('esquema_citas').query_db(query, data)
        return result

    @classmethod
    def delete(cls,data):
        query = "DELETE FROM citas WHERE id = %(id)s"
        return connectToMySQL('esquema_citas').query_db(query, data)



