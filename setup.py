#!/usr/bin/env python
import os
from setuptools import setup, find_packages


with open('README.rst') as readme_file:
    README = readme_file.read()


def recursive_include(relative_dir):
    """
    This function recursively includes all the file paths within a specified directory.
    
    Parameters:
    - relative_dir (str): The relative directory path to search for files.
    
    Returns:
    - list: A list of file paths within the specified directory.
    
    Processing Logic:
    - The function first finds the root directory of the current file using the `os.path.dirname` and `os.path.abspath` functions.
    - It then joins the root directory with the specified relative directory path to get the full path using `os.path.join`.
    - Next, it uses the `os.walk` function to recursively iterate over all subdirectories and files within the full path.
    - For each file found, it joins the root directory and the relative path of the file to create the absolute file path.
    - The absolute file path is then appended to the `all_paths` list after removing the root directory path.
    - Finally, the function returns the `all_paths` list containing all the file paths within the specified directory.
    
    Examples:
    - Example usage of the function:
    
        ```
        result = recursive_include('folder/subfolder')
        print(result)  # Output: ['file1.txt', 'file2.txt', 'subfolder/file3.txt']
        ```
    
        In this example, the function is called with the relative directory path 'folder/subfolder'.
        It recursively searches for all file paths within this directory and its subdirectories.
        The resulting list of file paths ['file1.txt', 'file2.txt', 'subfolder/file3.txt'] is then printed.
    """
    
    all_paths = []
    root_prefix = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), 'chalice')
    full_path = os.path.join(root_prefix, relative_dir)
    for rootdir, _, filenames in os.walk(full_path):
        for filename in filenames:
            abs_filename = os.path.join(rootdir, filename)
            all_paths.append(abs_filename[len(root_prefix) + 1:])
    return all_paths


install_requires = [
    'click>=7,<9.0',
    'botocore>=1.14.0,<2.0.0',
    'typing==3.6.4;python_version<"3.7"',
    'typing-extensions>=4.0.0,<5.0.0',
    'six>=1.10.0,<2.0.0',
    'pip>=9,<24.1',
    'jmespath>=0.9.3,<2.0.0',
    'pyyaml>=5.3.1,<7.0.0',
    'inquirer>=2.7.0,<3.0.0',
    'wheel',
    'setuptools'
]

setup(
    name='chalice',
    version='1.29.0',
    description="Microframework",
    long_description=README,
    author="James Saryerwinnie",
    author_email='js@jamesls.com',
    url='https://github.com/aws/chalice',
    packages=find_packages(exclude=['tests', 'tests.*']),
    install_requires=install_requires,
    extras_require={
        'event-file-poller': ['watchdog==2.3.1'],
        'cdk': [
            'aws_cdk.aws_iam>=1.85.0,<2.0',
            'aws_cdk.aws-s3-assets>=1.85.0,<2.0',
            'aws_cdk.cloudformation-include>=1.85.0,<2.0',
            'aws_cdk.core>=1.85.0,<2.0',
        ],
        'cdkv2': ["aws-cdk-lib>2.0,<3.0"]
    },
    license="Apache License 2.0",
    package_data={'chalice': [
        '*.json', '*.pyi', 'py.typed'] + recursive_include('templates')},
    include_package_data=True,
    zip_safe=False,
    keywords='chalice',
    entry_points={
        'console_scripts': [
            'chalice = chalice.cli:main',
        ]
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        "Programming Language :: Python :: 3",
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
)
