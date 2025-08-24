from setuptools import setup, find_packages

setup(
    name="manage_history",
    version="1.1.0",
    author="Yashar Z",
    author_email="yashar.z.dev@gmail.com",
    description="A command-line tool to clean and manage shell history with filters, sorting, and backup.",
    long_description="Manage shell history interactively using keywords, regex, line ranges, and exclusions. Supports sorting and backup.",
    long_description_content_type="text/plain",
    url="https://github.com/yashar-z-dev/manage_history",
    packages=find_packages(),
    include_package_data=True,
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "manage-history=history_cleaner.main:main"
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License"
    ],
)
