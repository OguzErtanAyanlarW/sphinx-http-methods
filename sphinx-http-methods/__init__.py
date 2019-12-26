from docutils import nodes
from docutils.parsers.rst import Directive

class HTTPMethod(Directive):
    has_content = True
    required_arguments = 1

    def run(self):
        method_type = self.arguments[0]
        paragraph_node = nodes.paragraph(text=method_type)

        if (method_type == 'POST'):
          paragraph_node['classes'].append("post")
        elif (method_type == 'GET'):
          paragraph_node['classes'].append("get")
        else:
          paragraph_node['classes'].append("unknown method type")

        return [paragraph_node]

def setup(app):
    app.add_directive("httpmethod", HTTPMethod)

    return {
        'version': '1.4.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }