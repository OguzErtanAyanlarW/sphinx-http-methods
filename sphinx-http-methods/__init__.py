from docutils import nodes
from docutils.parsers.rst import Directive

class HTTPPost(Directive):
    def run(self):
        element_node = nodes.element()
        element_node.body.append('<span class="api-method-post api-method-text"><p>POST</p></span>')
        return [element_node]

def setup(app):
    app.add_directive("httppost", HTTPPost)

    return {
        'version': '1.0.0',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }