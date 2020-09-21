import setuptools

with open("README.md", "r") as rm_file:
    long_description = rm_file.read()

setuptools.setup(
    name="parchment-io",
    version="0.1",
    author="Wolf Heinrich Hahn, Finn Harms",
    author_email="parchment@finn-harms.de",
    description="A python based paper.io clone with an interface for bots",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/innif/parchment.io",
    license="GNU GPL v3",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'pygame',
    ],
    python_requires='>=3.8',
)