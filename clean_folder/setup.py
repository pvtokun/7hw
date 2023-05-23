from setuptools import setup, find_packages

setup(
    name='clean_folder',
    version='1.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'clean-folder = clean_folder.clean:process_folder',
        ],
    },
)