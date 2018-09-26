from setuptools import setup, find_packages

setup(
    name='psdconvert',
    version='0.1.3',
    packages=find_packages(),
    install_requires=[
        'psd_tools', 'tqdm'
    ],
    url='https://github.com/mrstephenneal/psdconvert',
    license='MIT License',
    author='Stephen Neal',
    author_email='stephen@stephenneal.net',
    description='PSD conversion package for python'
)
