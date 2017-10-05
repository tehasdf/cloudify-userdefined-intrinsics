from setuptools import setup

setup(
    name='intrinsic_plugin',
    py_modules=['foo'],
    entry_points={
        'cloudify.tosca.ext.functions': [
            'intrinsic1 = foo:Func1'
        ]
    }
)
