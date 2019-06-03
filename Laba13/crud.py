from flask import Flask, request, jsonify
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
import os


app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'crud.sqlite')
db = SQLAlchemy(app)
ma = Marshmallow(app)


class Armament(db.Model):

    id = db.Column(db.Integer,  nullable=False,  primary_key=True, autoincrement=True)
    user = db.Column(db.String(70), nullable=False, unique=False)
    price = db.Column(db.Integer, nullable=False, unique=False)
    amount = db.Column(db.Integer, nullable=False, unique=False)

    def __init__(self,
                 price=0.0,
                 user="NoUser",
                 amount=0):
        self.price = price
        self.user = user
        self.amount = amount


class ArmamentSchema(ma.Schema):

    class Meta:

        fields = ('price', 'user', 'amount')


armament_schema = ArmamentSchema()

armaments_schema = ArmamentSchema(many=True)

db.create_all()


@app.route("/armament", methods=["POST"])
def add_armament():

    user = request.json['user']

    price = request.json['price']

    amount = request.json['amount']

    new_armament = Armament(price, user, amount)

    db.session.add(new_armament)

    db.session.commit()

    return armament_schema.jsonify(new_armament)


@app.route("/armament", methods=["GET"])
def get_armament():
    all_armaments = Armament.query.all()
    result = armaments_schema.dump(all_armaments)
    return jsonify(result.data)


@app.route("/armament/<id>", methods=["GET"])
def armament_detail(id):

    armament = Armament.query.get(id)

    return armament_schema.jsonify(armament)


@app.route("/armament/<id>", methods=["PUT"])
def armament_update(id):

    armament = Armament.query.get(id)

    user = request.json['user']

    price = request.json['price']

    amount = request.json['amount']

    armament.user = user

    armament.price = price

    armament.amount = amount

    db.session.commit()

    return armament_schema.jsonify(armament)


@app.route("/armament/<id>", methods=["DELETE"])
def armament_delete(id):
    armament = Armament.query.get(id)
    db.session.delete(armament)
    db.session.commit()

    return armament_schema.jsonify(armament)


if __name__ == '__main__':
    app.debug = True
    app.run()
