from setuptools import setup

version = '0.1.0dev'

with open('requirements.txt') as requirements:
    install_requires = requirements.read().split()

setup(
    name='frappe-client',
    packages=['frappeclient'],
    version=version,
    license='MIT',
    author='Rakshith Vikramraj',
    author_email='rakshithvikramraj@gmail.com',
    url="https://github.com/rakneo/frappe-client",
    download_url="https://github.com/rakneo/frappe-client/archive/refs/tags/v1.0.tar.gz",
    keywords=['frappe', 'erpnext', 'frappe-rest'],
    install_requires=install_requires,
    tests_requires=[
        'httmock<=1.2.2',
        'nose<=1.3.4'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',

      ],
)
