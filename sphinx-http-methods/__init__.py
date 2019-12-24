from docutils import nodes
from docutils.parsers.rst import Directive

class HTTPPost(Directive):
    def run(self):
        paragraph_node = nodes.paragraph(text='POST')
        paragraph_node['classes'].append('api-method-post api-method-text')
        return [paragraph_node]

def setup(app):
    app.add_directive("httppost", HTTPPost)

    return {
        'version': '1.0.0',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }