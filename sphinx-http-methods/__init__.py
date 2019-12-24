from docutils import nodes
from docutils.parsers.rst import Directive

class HTTPMethodPost(Directive):
    def run(self):
        classifier_node = nodes.classifier('<span class="api-method-post api-method-text">POST</span>')
        return [classifier_node]

def setup(app):
    app.add_directive("httpmethodpost", HTTPMethodPost)

    return {
        'version': '1.0.3',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }