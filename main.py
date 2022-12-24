import json
from flask import Flask, jsonify, request, render_template
app = Flask(__name__)
data = [{'id': 0, 'name': 'Alex', 'surname': 'Turner'},
        {'id': 1, 'name': 'Thom', 'surname': 'Yorke'}]


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.route('/users', methods=['GET'])
def index():
    return jsonify(data)


@app.route('/users', methods=['POST'])
def add_user():
    #for num in range(len(data)):
    #    if request.get_json()['id'] == data[num]['id']:
    #        print("ID number is busy")
    #    else:
    data.append(request.get_json())
    return jsonify(data)


@app.route('/users', methods=['PUT'])
def update_user():
    data[request.get_json()['id']] = request.get_json()
    return jsonify(data)


@app.route('/users', methods=['DELETE'])
def del_user():
    data.pop(request.get_json()['id'])
    # data.append({'name': 'Matt'})
    # return jsonify(data)
    pass


if __name__ == '__main__':
    app.run(debug=True)


# Реализовать метод delete и put