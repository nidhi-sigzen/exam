from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in exam/__init__.py
from exam import __version__ as version

setup(
	name="exam",
	version=version,
	description="exam",
	author="exam",
	author_email="exam",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
