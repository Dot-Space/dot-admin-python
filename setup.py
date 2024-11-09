from setuptools import setup, find_packages

setup(
    name='dot-admin-python',
    version='0.1.1',
    packages=find_packages(),
    include_package_data=True,
    license='MIT License',
    description='A Django extension that adds admin and base website functionality.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Dot-Space/dot-admin-python',
    author='Dot.Space',
    author_email='i@andrew-balin.ru',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Framework :: Django Rest Framework',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    install_requires=[
        'django>=4.0',
        'djangorestframework>=3.12.4',
        'redis>=5.0.0',
        'django-redis>=5.0.0',
        'requests>=2.26.0',
        'pyjwt>=2.3.0',
    ],
)