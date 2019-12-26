from docutils import nodes
from docutils.parsers.rst import Directive
from sphinx.util.osutil import copyfile
from sphinx.util import logging

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

def get_compatible_builders(app):
    builders = ['html', 'singlehtml', 'dirhtml',
                'readthedocs', 'readthedocsdirhtml',
                'readthedocssinglehtml', 'readthedocssinglehtmllocalmedia',
                'spelling']
    builders.extend(app.config['sphinx-http-methods_valid_builders'])
    return builders

def copy_assets(app, exception):
    """ Copy asset files to the output """
    if 'getLogger' in dir(logging):
        log = logging.getLogger(__name__).info  # pylint: disable=no-member
        warn = logging.getLogger(__name__).warning  # pylint: disable=no-member
    else:
        log = app.info
        warn = app.warning
    builders = get_compatible_builders(app)
    if exception:
        return
    if app.builder.name not in builders:
        if not app.config['sphinx-http-methods-nowarn']:
            warn(
                'Not copying tabs assets! Not compatible with %s builder' %
                app.builder.name)
        return

    log('Copying tabs assets')

    installdir = os.path.join(app.builder.outdir, '_static', 'sphinx-http-methods')

    for path in FILES:
        source = resource_filename('sphinx-http-methods', path)
        dest = os.path.join(installdir, path)

        destdir = os.path.dirname(dest)
        if not os.path.exists(destdir):
            os.makedirs(destdir)

        copyfile(source, dest)


def setup(app):
    app.add_directive("httpmethod", HTTPMethod)

    for path in ['sphinx-http-methods/' + f for f in FILES]:
        if path.endswith('.css'):
            if 'add_css_file' in dir(app):
                app.add_css_file(path)
            else:
                app.add_stylesheet(path)

    app.connect('build-finished', copy_assets)

    return {
        'version': '1.4.4',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }