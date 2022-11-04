from setuptools import setup, find_packages

VERSION = '1.0' 
DESCRIPTION = 'stop data leaks'
LONG_DESCRIPTION = 'Pre-commit hook to stop data being leaked onto a repository'

# Setting up
setup(
        name="stop_data_hooks", 
        version=VERSION,
        author="Paige Hunter, James Westwood, Tom Coates",
        author_email="paige.hunter@ons.gov.uk",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=['pre_commit_hooks'],
        
        keywords=['python', 'pre-commit', 'data leak'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)