import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="khmernltk",
    version="0.1-alpha",
    description="A Khmer natural language processing tool kit",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/VietHoang1710/khmer_nltk",
    author="Phan Viet Hoang",
    author_email="phanviethoang1512@gmail.com",
    license="MIT",
    classifiers=[   
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
    ],
    python_requires='>3.5',
    packages=packages=setuptools.find_packages(exclude=["data"]),
    include_package_data=True,
    install_requires=["sklearn_crfsuite", "tqdm"],
)