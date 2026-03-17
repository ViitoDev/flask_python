from wsgiref.simple_server import make_server

def web_application(environ, start_response):
    start_response("200 Ok", [('Content-Type', "text/html;charset=utf-8")])
    html = b'''
                <!DOCTYPE html>
                <html lang="en">
                <head>
                    <meta charset="UTF-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <title>Document</title>
                </head>
                <body>
                    Hello world!
                </body>
                </html>
            '''
    return [html]

make_server('', 5000, web_application).serve_forever()