import os
from setuptools import setup, find_packages


def get_version():
    filename = os.path.join(os.path.dirname(__file__), 'psdconvert', '_version.py')
    with open(filename, 'rb') as fp:
        return fp.read().decode('utf8').split('=')[1].strip(" \n'")


setup(
    name='psdconvert',
    version=get_version(),
    packages=find_packages(),
    install_requires=[
        'psd_tools3>=1.8.2',
        'Pillow',  # Not explicitly required by psd_tools
        'tqdm'
    ],
    url='https://github.com/mrstephenneal/psdconvert',
    license='MIT License',
    author='Stephen Neal',
    author_email='stephen@stephenneal.net',
    description='PSD conversion package for python'
)
