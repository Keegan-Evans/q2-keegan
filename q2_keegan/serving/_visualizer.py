import json
import os.path
import pkg_resources

import q2templates

from ..plugin_setup import plugin

# TEMPLATES = pkg_resources.resource_filename('q2_keegan','vanilla', 'assets')
TEMPLATES = pkg_resources.resource_filename('q2_keegan', 'assets')

test_input = "some test input"

def hello_bean(output_dir: str) -> None:
    index = os.path.join(TEMPLATES, 'hello_bean', 'index.html')
    q2templates.render(index, output_dir)
    print('hello bean')

def scooper(output_dir: str) -> None:
    # with open(os.path.join(output_dir, test_input), 'w') as fh:
    #     fh.write(test_input)
    index = os.path.join(TEMPLATES, 'scooper', 'index.html')
    q2templates.render(index, output_dir)

plugin.visualizers.register_function(
    function=hello_bean,
    inputs={}, 
    parameters={}, 
    name='hello bean',
    description='A tiny and cute function'
)

plugin.visualizers.register_function(
    function=scooper,
    inputs={},
    parameters={},
    name='scooper',
    description='A scoop of sweet treat',
)

