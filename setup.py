import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="victorizer",
    version="0.0.1",
    author="Mallgroup Data Science",
    author_email="bi_datascience@mallgroup.com",
    description="Testing installation of Package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hrubanj/victorizer",
    license="MIT",
    packages=setuptools.find_packages(),
    include_package_data=True,
    package_data={"": ["*.txt"]},
)
