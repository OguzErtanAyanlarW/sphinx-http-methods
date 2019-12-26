from docutils import nodes
from docutils.parsers.rst import Directive

class HelloWorld(Directive):
    has_content = True
    required_arguments = 1

    def run(self):
        paragraph_node = nodes.paragraph(text=self.arguments[0])
        return [paragraph_node]

def setup(app):
    app.add_directive("helloworld", HelloWorld)

    return {
        'version': '1.0.0',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }