import setuptools

with open("README.md", "r") as fh:
    description = fh.read()

setuptools.setup(
    name="geography_guessing",
    version="0.0.3",
    author="Julius Gruber",
    author_email="gruber.julius@gmx.at",
    packages=["geography_guessing"],
    description="A package for studying geography for programmers",
    long_description=description,
    long_description_content_type="text/markdown",
    url="https://github.com/gituser/test-tackage",
    license='MIT',
    python_requires='>=3.6',
    install_requires=["pandas"],
    include_package_data=True,
)
