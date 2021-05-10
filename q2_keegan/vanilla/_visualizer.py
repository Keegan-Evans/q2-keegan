import json
import os.path
import pkg_resources

import q2templates

from . import VanillaBeanFmt, IceCream
from qiime2.plugin import Str
from ..plugin_setup import plugin

# TEMPLATES = pkg_resources.resource_filename('q2_keegan','vanilla', 'assets')
TEMPLATES = pkg_resources.resource_filename('q2_keegan', 'assets')

test_input = "some test input"

def hello_bean(output_dir: str) -> None:
    index = os.path.join(TEMPLATES, 'hello_bean', 'index.html')
    q2templates.render(index, output_dir)
    print('hello bean')

def scooper(output_dir: str, in_txt: VanillaBeanFmt) -> None:
    src_txt = in_txt.open().readlines()
    text_out = 'text.txt'
    
    with open(os.path.join(output_dir, text_out), 'w') as fh:
        
        fh.write('{ extends "index.html" }')
        fh.write("{ block content }\n<pre>")
        
        for i in src_txt:
            fh.writelines(i)
        
        fh.write("</pre>\n{ endblock }")

    index = os.path.join(TEMPLATES, 'scooper', 'index.html')
    
    q2templates.render(index, 
                       output_dir,
                       context={'textout': text_out,
                                })

plugin.visualizers.register_function(
    function=hello_bean,
    inputs={}, 
    parameters={}, 
    name='hello bean',
    description='A tiny and cute function'
)

plugin.visualizers.register_function(
    function=scooper,
    inputs={
        'in_txt': IceCream,
        },
    parameters={},
    name='scooper',
    description='A scoop of sweet treat',
)

