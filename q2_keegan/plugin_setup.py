from qiime2.plugin import Plugin
import q2_keegan
import q2_keegan._hello_bean as hello_bean

plugin = Plugin(
    name='keegan',
    version='0.0.1',
    website='keeganevans.com',
    user_support_text='good luck',
    package='q2_keegan'
)

plugin.visualizers.register_function(
    function=hello_bean.hello_bean,
    inputs={}, 
    parameters={}, 
    name='hello bean',
    description='A tiny and cute function'
)
