import os

from datetime import datetime
from flask import Flask, jsonify, abort, make_response, request, url_for
from . import config

def create_app(env_name=None):
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object(config.by_name[env_name or 'dev'])
    app.config.from_pyfile('config.py', silent=True)
    app.config.from_envvar('ASTRA_CONFIG_FILE', silent=True)

    @app.route('/')
    def index():
        return app.config['ASTRA_MESSAGE']

    @app.route('/time')
    def current_time():
        return str(datetime.now())

    @app.route('/tasks', methods=['GET'])
    def all_tasks():
        return jsonify({'tasks': [urlify(task) for task in tasks]})

    @app.route('/tasks/<int:task_id>', methods=['GET'])
    def load_task(task_id):
        task = [task for task in tasks if task['id'] == task_id]
        if len(task) == 0:
            abort(404)
        return jsonify({'task': task[0]})

    @app.route('/tasks/', methods=['POST'])
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

    @app.route('/tasks/<int:task_id>', methods=['DELETE'])
    def delete_task(task_id):
        task = [task for task in tasks if task['id'] == task_id]
        if len(task) == 0:
            abort(404)

        tasks.remove(task[0])
        return jsonify({'result': True})

    @app.errorhandler(404)
    def not_found(error):
        return make_response(jsonify({'error': 'Not Found'}), 404)

    return app


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
            newtask['uri'] = url_for('load_task', task_id=task['id'], _external=True)
        else:
            newtask[field] = task[field]

    return newtask

tasks = init_tasks()
