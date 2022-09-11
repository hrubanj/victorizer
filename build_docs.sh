#!/bin/bash
git fetch --all
git switch gh_pages
git reset --hard origin/master
rm -rf _build _static _templates conf.py index.rst make.bat Makefile
pip install "sphinx==5.1.1"
#sphinx-quickstart -q -p $1 -a $2 -v $3
sphinx-quickstart -q -p "victorizer" -a "Viktor's former colleagues" -v "0.0.1"
echo 'import sys\nimport os\nsys.path.insert(0, os.path.abspath("."))' >> conf.py
echo 'extensions = ["sphinx.ext.autodoc", "sphinx.ext.coverage", "sphinx.ext.napoleon"]' >> conf.py
sphinx-apidoc  "victorizer" -o docs
make html
rm -rf docs
mkdir docs
mv _build/html/* docs/
touch docs/.nojekyll
rm -rf _build _static _templates conf.py index.rst make.bat Makefile
rm -rf docs/_sources/venv docs/venv
