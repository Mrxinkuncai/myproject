def test_sqlalchemy():
    from flask import Flask
    from flask_sqlalchemy import SQLAlchemy

    app=Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"]="mysql+pymysql://root:123456@192.168.150.135/myproject?charset=utf8mb4"

    db=SQLAlchemy(app)

    class User(db.Model):
        id=db.Column(db.Integer,primary_key=True)
        username=db.Column(db.String(80),unique=True,nullable=False)
        email=db.Column(db.String(120),unique=True,nullable=False)

        def __repr__(self):
            return '<User %r>'%self.username
    # db.create_all()
    db.session.add(User(id=123,username="xiaohong",email="abc@163.com"))
    db.session.commit()