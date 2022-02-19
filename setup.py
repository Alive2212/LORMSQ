from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Education',
    'Operating System :: Microsoft :: Windows :: Windows 10',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
]

setup(
    name='lormsq',
    version='0.0.2',
    description='Powerful and Smart ORM for SQL Databases',
    long_description=open('README.md').read() + '\n\n' + open('CHANGELOG.md').read(),
    url='',
    author='Babak Nodoust',
    author_email='alive2212@gmail.com',
    license='MIT',
    classifiers=classifiers,
    keywords='ORM SQL DataBase',
    packages=find_packages(),
    install_requires=['']
)