from setuptools import setup, find_packages

setup(
    name='fchat',
    version='0.0',
    packages=find_packages(exclude=['test']),
    license='MIT',
    description='A python based f-chat client',
    long_description=open('README.txt').read(),
    install_requires=['requests'],
    url='https://github.com',
    author='Tucker',
    author_email='tucker@example.com'
)
