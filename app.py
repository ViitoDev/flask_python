from wsgiref.simple_server import make_server

def web_application(environ, start_response):
    start_response("200 Ok", [('Content-Type', "text/html;charset=utf-8")])
    with open("index.html", "r", encoding="utf-8") as file:
        html = file.read()
    return [html.encode("utf-8")]

make_server('', 5000, web_application).serve_forever()