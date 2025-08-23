from setuptools import setup, find_packages

setup(
    name='manage-history',
    version='0.1.0',
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    entry_points={
        'console_scripts': [
            'clean-history = script:main',
        ],
    },
    author='yashar.z.dev',
    author_email='your.email@example.com',
    description='A CLI tool to clean bash/zsh history with filters and backup',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yashar-z-dev/manage_history',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
    ],
    python_requires='>=3.7',
    install_requires=[],
    include_package_data=True,
)
