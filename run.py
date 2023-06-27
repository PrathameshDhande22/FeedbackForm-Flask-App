from gevent.pywsgi import WSGIServer
from feedback import create_app

app = create_app()
http_server = WSGIServer(("127.0.0.1", 8000), app)
http_server.serve_forever()