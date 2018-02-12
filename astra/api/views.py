from datetime import datetime
from flask import Blueprint, jsonify, abort, make_response, request, url_for
from flask import current_app as app

from . import api

@api.route('/')
def index():
    return app.config['ASTRA_MESSAGE']

@api.route('/time')
def current_time():
    return str(datetime.now())

@api.route('/tasks', methods=['GET'])
def all_tasks():
    return jsonify({'tasks': [urlify(task) for task in tasks]})

@api.route('/tasks/<int:task_id>', methods=['GET'])
def load_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    return jsonify({'task': task[0]})

@api.route('/tasks/', methods=['POST'])
def create_task():
    if not request.json:
        abort(400)
    newtask = {
        'id': tasks[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ''),
        'done': False
    }
    tasks.append(newtask)
    return jsonify({'task': newtask}), 201

@api.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)

    tasks.remove(task[0])
    return jsonify({'result': True})

@api.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not Found'}), 404)


def init_tasks():
    return [
        {
            'id': 1,
            'title': 'Improve',
            'description': 'Chase the horizon, follow the stars, choose the bigger life.',
            'done': False
        },
        {
            'id': 2,
            'title': 'Be present',
            'description': 'Gratitude, mindfulness, calm. Be. Look neither forward nor back.',
            'done': False
        },

        {
            'id': 3,
            'title': 'Hike the JMT',
            'description': 'July 5th to July 22nd. Hoping it is the trip of a lifetime. Again.',
            'done': False
        }
    ]

def urlify(task):
    newtask = {}
    for field in task:
        if field == 'id':
            newtask['id'] = task['id']
            newtask['uri'] = url_for('api.load_task', task_id=task['id'], _external=True)
        else:
            newtask[field] = task[field]

    return newtask

tasks = init_tasks()