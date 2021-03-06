from setuptools import setup

setup(
    name = 'sphinx-http-methods',
    version = '1.5.5',
    author = 'OguzErtanAyanlar',
    author_email = 'oguzertanayanlar@gmail.com',
    packages = ['sphinx-http-methods'],
    package_data = {
        'sphinx-http-methods': [
            '__init__.py',
            'sphinx-http-methods.css',
        ],
    },
    url = 'https://github.com/OguzErtanAyanlarW/sphinx-http-methods',
    license = 'MIT',
    description = 'HTTP Method Boxes for Sphinx',
    install_requires = ['sphinx>=1.4'],
    tests_require = ['sphinx>=1.4', 'docutils', 'pygments', 'sphinx_testing', 'lxml'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Plugins',
        'Environment :: Web Environment',
        'Framework :: Sphinx :: Extension',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python',
        'Topic :: Documentation :: Sphinx',
        'Topic :: Documentation',
        'Topic :: Software Development :: Documentation',
        'Topic :: Text Processing',
        'Topic :: Utilities',
    ]
)