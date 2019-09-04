import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setuptools.setup(
    name="PerceptualSimilarity",
    version="0.0.1",
    author="Richard Zhang",
    author_email="richard@adobe.com",
    description="perceptual similarity metric as a python module",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/janesjanes/PerceptualSimilarity",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=requirements,

)
