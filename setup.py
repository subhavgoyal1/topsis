import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="topsis-subhav-102053022",
    version="1.0.1",
    description="topsis",
    long_description=README,
    long_description_content_type="text/markdown",
    author="subhav goyal",
    author_email="subhavgoyal@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    packages=["topsis"],
    include_package_data=True,
    keywords=["topsis", "MCDM"],
    install_requires=[
        "pandas",
        "numpy",
    ],
    entry_points={
        "console_scripts": [
            "topsis=topsis.__main__:main",
        ]
    },
)
