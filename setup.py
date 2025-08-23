from setuptools import setup, find_packages

setup(
    name='manage-history-cli',
    version='0.1.0',
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    entry_points={
        'console_scripts': [
            'manage-history = script:main',
        ],
    },
    author='your-username',
    description='A minimal CLI tool to manage shell history',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
    install_requires=[],
)
