from wsgiref.simple_server import make_server

def web_application(environ, start_response):
    products = [
        {'name' : "Notebook", 'value' : 300},
        {'name' : "Smartphone", 'value' : 350},
        {'name' : "Tv", 'value' : 500},
        {'name' : "Computer", 'value' : 800}
    ]

    html_lines = ""
    for product in products:
        html_lines += "<li> {} - {} </li>".format(product['name'], product['value'])

    start_response("200 Ok", [('Content-Type', "text/html;charset=utf-8")])
    
    with open("index.html", "r", encoding="utf-8") as file:
        tamplate_html = file.read()

    html_final = tamplate_html.replace("{{PRODUCTS}}", html_lines)
    return [html_final.encode("utf-8")]

make_server('', 5000, web_application).serve_forever()