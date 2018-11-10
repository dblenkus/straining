import os.path
import setuptools

# Get long description from README.
with open('README.rst', 'r') as fh:
    long_description = fh.read()

# Get package metadata from '__about__.py' file.
about = {}
base_dir = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(base_dir, 'straining', '__about__.py'), 'r') as fh:
    exec(fh.read(), about)

setuptools.setup(
    name=about['__title__'],
    use_scm_version=True,
    description=about['__summary__'],
    long_description=long_description,
    long_description_content_type='text/x-rst',
    author=about['__author__'],
    author_email=about['__email__'],
    url=about['__url__'],
    license=about['__license__'],
    packages=setuptools.find_packages(
        exclude=['tests', 'tests.*', '*.tests', '*.tests.*']
    ),
    python_requires='>=3.6, <3.8',
    install_requires=[
        'asgiref~=2.3.0',
        'channels~=2.1.0',
        'channels_redis~=2.3.0',
        'Django~=2.1.0',
        'django-fernet-fields==0.5',
        'djangorestframework~=3.9.0',
        'psycopg2>=2.5.0',
        'requests~=2.19.1',
    ],
    extras_require={
        'docs': ['Sphinx', 'sphinx_rtd_theme'],
        'package': ['twine', 'wheel'],
        'test': [
            'check-manifest',
            'coverage>=4.2',
            'pycodestyle~=2.4.0',
            'pydocstyle~=3.0.0',
            'pylint~=2.1.0',
            'readme_renderer',
            'setuptools_scm',
            'isort',
        ],
    },
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Other Audience',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Internet :: WWW/HTTP :: HTTP Servers',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    keywords='training cycling running',
)
