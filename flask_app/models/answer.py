from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Dojo:

    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, data):
        query = "INSERT INTO dojo (name , location, language, comment, created_at, updated_at ) VALUES ( %(name)s ,%(location)s ,%(language)s ,%(comment)s , NOW() , NOW());"
        return connectToMySQL('dojo_survey_schema').query_db( query, data)

        
    @classmethod
    def get_last_dojo(cls):
        query = "SELECT * FROM dojo order by id desc limit 1;"
        results = connectToMySQL('dojo_survey_schema').query_db(query)
        print(results)
        return Dojo(results[0])

    @staticmethod
    def is_valid(survey):
        is_valid = True
        if len(survey['name']) < 3:
            is_valid = False
            flash("Name must be at least 3 characters!", "name")
        if len(survey['location']) < 1:
            is_valid = False
            flash("Choose a dojo location!", "location")
        if len(survey['language']) < 1:
            is_valid = False
            flash("Choose a favorite language!", "language")
        if len(survey['comment']) < 5:
            is_valid = False
            flash("Comments must be at least 5 characters!", "comment")
        return is_valid