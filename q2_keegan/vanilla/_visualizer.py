import os.path
import pkg_resources

import q2templates

from . import IceCream
from ..plugin_setup import plugin

TEMPLATES = pkg_resources.resource_filename('q2_keegan', 'assets')


def hello_bean(output_dir: str) -> None:
    index = os.path.join(TEMPLATES, 'hello_bean', 'index.html')
    q2templates.render(index, output_dir)


def scooper(output_dir: str, in_txt: list) -> None:
    index = os.path.join(TEMPLATES, 'scooper', 'index.html')

    q2templates.render(index,
                       output_dir,
                       context={'src_txt': in_txt,
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
