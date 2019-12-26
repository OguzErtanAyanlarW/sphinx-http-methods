from docutils import nodes
from docutils.parsers.rst import Directive

FILES = [
    'sphinx-http-methods.css',
]

class HTTPMethod(Directive):
    has_content = True
    required_arguments = 1

    def run(self):
        method_type = self.arguments[0]
        paragraph_node = nodes.paragraph(text=method_type)

        if (method_type == 'POST'):
          paragraph_node['classes'].append("api-method-post api-method-text")
        elif (method_type == 'GET'):
          paragraph_node['classes'].append("api-method-get api-method-text")
        else:
          paragraph_node['classes'].append("unknown method type")

        return [paragraph_node]

def setup(app):
    app.add_directive("httpmethod", HTTPMethod)

    for path in ['sphinx-http-methods/' + f for f in FILES]:
        if path.endswith('.css'):
            if 'add_css_file' in dir(app):
                app.add_css_file(path)
            else:
                app.add_stylesheet(path)

    return {
        'version': '1.4.2',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }