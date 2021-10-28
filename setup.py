import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="svportal",
    version="22.0.1",
    license="MIT License",
    author="Zhao Tang",
    author_email="zxt@zhaotang.ca",
    description="Python API wrappers around shadowverse-portal",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/zxt/shadowverse-portal",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Games/Entertainment"
    ],
)
