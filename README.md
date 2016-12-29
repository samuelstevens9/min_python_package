## Minimum Python Package 

Minimal files needed for creating a python package.

http://python-packaging.readthedocs.io/en/latest/minimal.html

### How to Use

0. Change the remote url to the new Git repository `git remote set-url origin git://new.url.git`
1. Update `setup.py` with the name of the package, description, version, author informaiton.
2. Create the code files for the package. Either a single python file: `monkey.py` or a directory: `monkey/__init__.py` 
3. Add your tests cases to `tests.py`
4. Update this README
5. Install into your virtual environment with `pip install .` or `python setup.py install`
