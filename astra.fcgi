#!/home/benjami8/virtualenv/projects_astra/3.5/bin/python
from flup.server.fcgi import WSGIServer
from astra import create_app

if __name__ == '__main__':
    app = create_app()
    WSGIServer(app).run()

