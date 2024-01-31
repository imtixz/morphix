from setuptools import setup, find_packages
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read()

setup(
    name = 'morphix',
    version = '0.0.1',
    author = 'Imtiaz Ahmed Khan',
    author_email = 'inbox.imtiazahmed@gmail.com',
    license = 'MIT',
    description = 'migration tool for sql databases',
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = 'github.com/morphix',
    py_modules = ['main', 'core'],
    packages = find_packages(),
    install_requires = [requirements],
    python_requires='>=3.7',
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "Operating System :: OS Independent",
    ],
    entry_points = '''
        [console_scripts]
        morphix=main:cli
    '''
)