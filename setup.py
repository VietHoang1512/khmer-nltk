import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

with open("requirements.txt", "r") as f:
    requirements = f.read().strip().split("\n")

setuptools.setup(
    name="khmer-nltk",
    version="1.3",
    description="A Khmer language processing toolkit",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/VietHoang1710/khmer-nltk",
    author="Phan Viet Hoang",
    author_email="phanviethoang1512@gmail.com",
    license="Apache License 2.0",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Natural Language :: English",
    ],
    python_requires=">3.5",
    packages=setuptools.find_packages(exclude=["data", "bin", "samples", "scripts"]),
    package_dir={"khmernltk": "khmernltk"},
    package_data={
        "khmernltk": [
            "pos_tag/sklearn_crf_pos_alt_0.9849.sav",
            "word_tokenize/sklearn_crf_ner_10000.sav",
            #   'word_tokenize/sklearn_crf_ner_alt_0.9725.sav'
        ]
    },
    include_package_data=True,
    install_requires=requirements,
)
