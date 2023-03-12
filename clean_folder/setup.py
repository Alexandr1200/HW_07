from setuptools import setup, find_namespace_packages


setup(
    name='clean-folder',
    version='1',
    description='clean-folder',
    url='https://github.com/Alexandr1200',
    author='Alexandr1200',
    author_email='uchiha1200@gmail.com',
    license='MIT',
    packages=find_namespace_packages(),
    entry_points={'console_scripts':['sort = clean_folder.clean.py:sort']})