from setuptools import setup, find_packages


setup(
    name='django-pyc',
    version=__import__('django_pyc').__version__,
    description='Manage *.pyc files in Django project.',
    long_description=open('README.md').read(),
    author='Piotr Roszatycki',
    author_email='piotr.roszatycki@gmail.com',
    url='http://github.com/dex4er/django-pyc',
    download_url='http://github.com/dex4er/django-pyc/downloads',
    license='LGPL',
    include_package_data=True,
    zip_safe=False,
    keywords='django pyc clean compile',
    packages = (
        'django_pyc',
        'django_pyc.management',
        'django_pyc.management.commands'
    ),
    install_requires=[
        'Django>=1.0'
        ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
        ]
)
