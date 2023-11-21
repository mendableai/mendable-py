from setuptools import setup, find_packages

setup(
    name='mendable-py',
    version='0.0.6',
    url='https://github.com/mendableai/mendable-py',
    author='Eric Ciarla',
    author_email='eric@mendable.ai',
    description='Python SDK for Mendable.ai',
    packages=find_packages(),    
    install_requires=[
        'requests',
    ],
)
