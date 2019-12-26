from docutils import nodes
from docutils.parsers.rst import Directive

class httpmethod(nodes.Admonition, nodes.Element):
    pass

def visit_httpmethod_node(self, node):
    self.visit_admonition(node)

def depart_httpmethod_node(self, node):
    self.depart_admonition(node)

class HelloWorld(Directive):
    has_content = True
    required_arguments = 1

    def run(self):
        http_method = httpmethod(text=self.arguments[0])
        return [http_method]

def setup(app):
    app.add_node(httpmethod,
                 html=(visit_httpmethod_node, depart_httpmethod_node),
                 latex=(visit_httpmethod_node, depart_httpmethod_node),
                 text=(visit_httpmethod_node, depart_httpmethod_node))
    app.add_directive("helloworld", HelloWorld)

    return {
        'version': '1.2.2',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }