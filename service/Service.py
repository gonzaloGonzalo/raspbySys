from dao import Base
from flask import Flask, jsonify, request
from dao import PositionDAO
from model.Position import Position

app = Base.app

@app.route('/')
def alive():
    return jsonify(message=str("HELLO")), 200

@app.route('/positions')
def getAllPositions():
    return jsonify(str(PositionDAO.findAllPosition())),200

@app.route('/position/<int:posID>')
def getPositionById(posID):
    return jsonify(str(PositionDAO.findPositionById(posID))),200

@app.route('/position', methods=['POST'])
def createPosition():
    name = request.args["name"]
    lat = request.args["lat"]
    long = request.args["long"]

    position = Position(name=name, latitude=lat, longitude=long)
    PositionDAO.createPosition(position)

    return jsonify(message=str("Position created")), 201

@app.route('/position', methods=['PATCH'])
def updatePosition():
    id = request.args["id"]
    name = request.args["name"]
    lat = request.args["lat"]
    long = request.args["long"]

    PositionDAO.updatePositionById(id=id, name=name, latitude=lat, longitude=long)

    return jsonify(message=str("Position updated")), 200

@app.route('/position', methods=['DELETE'])
def deletePosition():
    id = request.args["id"]
    PositionDAO.deletePositionById(id)
    return jsonify(message=str("Position deleted")), 200