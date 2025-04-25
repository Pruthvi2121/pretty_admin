from setuptools import setup, find_packages
import os

# Get absolute path of this file
this_directory = os.path.abspath(os.path.dirname(__file__))

# Path to README.md relative to setup.py
readme_path = os.path.join(this_directory, '..', 'README.md')

# Read README content
with open(readme_path, "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='pretty_admin',
    version='0.1.5',
    packages=find_packages(),
    include_package_data=True,
    description='A Tailwind-based Django admin UI skin',
    long_description=long_description,
    author='Pruthviraj Chokake',
    author_email='chokake.pruthvi@gmail.com',
    license='MIT',
    install_requires=[
        'Django>=3.2',
        'setuptools'
    ],
    python_requires='>=3.6',
    project_urls={
        'Homepage': 'https://github.com/Pruthvi2121/pretty_admin',  
        'Bug Tracker': 'https://github.com/Pruthvi2121/pretty_admin/issues',
    },
)
