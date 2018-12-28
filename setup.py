from setuptools import setup, find_packages


setup(
    name='whenconnect',
    version='0.5.1',
    description='when your android connected, do sth :) visit github page to view detail',
    author='williamfzc',
    author_email='fengzc@vip.qq.com',
    url='https://github.com/williamfzc/whenconnect',
    packages=find_packages(),
    install_requires=[
        'structlog',
        'ConnectionTracer',
    ]
)
