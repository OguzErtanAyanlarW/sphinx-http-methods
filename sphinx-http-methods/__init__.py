from docutils import nodes
from docutils.parsers.rst import Directive

class HTTPMethod(nodes.Admonition, nodes.Element):
    pass

class HelloWorld(Directive):
    has_content = True
    required_arguments = 1

    def run(self):
        http_method = HTTPMethod(text=self.arguments[0])
        return [http_method]

def setup(app):
    app.add_directive("helloworld", HelloWorld)

    return {
        'version': '1.2.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }