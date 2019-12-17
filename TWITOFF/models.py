from flask_sqlachemy import SQLAlchemy

DB = SQLAlchemy()

class User(DB.Model):
    """Twitter users that we analyze"""
    id = DB.Column(DB.BigInteger, primary_key=True)
    name = DB
    
    
class tweet(DB.Model):
    id = 
    text = 