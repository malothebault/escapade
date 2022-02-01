#!/usr/bin/python3

from distutils.core import setup

'''Here we are defining where should be placed each file'''
install_data = [
    ('share/applications', ['data/com.github.malothebault.template.desktop']),
    ('share/metainfo', ['data/com.github.malothebault.template.appdata.xml']),
    ('share/icons/hicolor/128x128/apps', ['data/com.github.malothebault.template.svg']),
    ('/usr/share/glib-2.0/schemas', ["data/com.github.malothebault.template.gschema.xml"]),
    ('bin/template', ['src/constants.py']),
    ('bin/template', ['src/main.py']),
    ('bin/template', ['src/views/page_one.py']),
    ('bin/template', ['src/views/page_two.py']),
    ('bin/template', ['src/widgets/headerbar.py']),
    ('bin/template', ['src/widgets/stack.py']),
    ('bin/template', ['src/widgets/welcome.py']),
    ('bin/template', ['src/window.py']),
    ('bin/template', ['src/__init__.py']),
]

'''Let's go and infuse our application into the system.'''
setup(
    name='Template',
    version='0.1',
    author='Malo Thebault',
    description='An app template for elemenary os',
    url='https://github.com/malothebault/Template',
    license='GNU GPL3',
    scripts=['com.github.malothebault.template'],
    packages=['src'],
    data_files=install_data
)
