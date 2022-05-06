from setuptools import setup

with open('README.md') as reader:
    long_description = reader.read()

setup(
    author='Jaedson Silva',
    author_email='imunknowuser@protonmail.com',
    name='ufinder',
    version='1.0.0',
    description='Search URL paths with UFinder.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=['ufinder'],
    license='MIT',
    project_urls={
        'Source Code': 'https://github.com/jaedsonpys/ufinder',
        'License': 'https://github.com/jaedsonpys/ufinder/blob/master/LICENSE'
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Indexing/Search',
        'Topic :: Security'
    ],
    entry_points={
        'console_scripts': [
            'ufinder = ufinder.ufinder:main'
        ]
    },
)
