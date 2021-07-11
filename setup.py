import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="geographic-line-of-sight",  # Replace with your own username
    version="1.0.3",
    author="Mark Henderson",
    author_email="mark.henderson1988@gmail.com",
    description="A tool which uses google elevation API to batch process geographical"
                " line-of-sight calculations from .csv files",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MHenderson1988/line-of-sight-analysis",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
