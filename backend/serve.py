import os

from flask import Flask,request
from flask_restful import Resource, Api, abort
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config["SQLALCHEMY_DATABASE_URI"]="mysql+pymysql://root:123456@192.168.150.136/myproject?charset=utf8mb4"
db=SQLAlchemy(app)
app.config['testcase']=[]


class TestCase(db.Model):
    name = db.Column(db.String(80), primary_key=True)
    description = db.Column(db.String(80), unique=False, nullable=True)
    content = db.Column(db.String(1000), unique=False, nullable=False)
    filename = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<TestCase %r>' % self.name


# db.create_all()
# db.session.add(User(id=123, username="xiaohong", email="abc@163.com"))
# db.session.commit()


class TestCaseStore(Resource):
    def get(self):
        print(request.args)
        if "id" in request.args:
            # 从用例库中找对应的用例
            for i in app.config['testcase']:
                if i['id']==int(request.args['id']):
                    return i
        else:
            return app.config['testcase']

    def post(self):
        """
        每条testcase要有ID，description,steps
        :return:
        """
        print("123")
        if "file" in request.files and "name" in request.form:
            name=request.form['name']
            f=request.files["file"]
            content=f.read()

            file_name=f.filename
            testcase=TestCase(name=name,filename=file_name,content=content)
            db.session.add(testcase)
            db.session.commit()
            # f.save(os.path.join('./',file_name))

            state={"message":"ok"}
            return state
        abort(404)


@app.route("/run",methods=['get'])
def get_testcase():
    if "name" in request.args:
        name=request.args['name']
        testcase=TestCase.query.filter_by(name=name).first()
        return testcase.content
    abort(404)


api.add_resource(TestCaseStore, '/store')


if __name__ == '__main__':
    # db.drop_all()
    # db.create_all()
    app.run(debug=True,port=5000,host="0.0.0.0")