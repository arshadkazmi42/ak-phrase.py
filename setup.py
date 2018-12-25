import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ak-phrase.py",
    version="1.0.5",
    author="Arshad Kazmi",
    author_email="arshadkazmi42@gmail.com",
    description="Generates permutations of all sentences, using list of words",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/arshadkazmi42/ak-phrase.py",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)",
        "Operating System :: OS Independent",
    ],
)