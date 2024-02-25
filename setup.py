import setuptools

with open("README.md", "r") as f:
	long_description = f.read()

setuptools.setup(
	name = "pqcryptography",
	version = "0.0.1",
	author = "Fun_Dan3",
	author_email = "dfr34560@gmail.com",
	description = "easy post quantum cryptography library",
	long_description = long_description,
	long_description_content_type = "text/markdown",
	url = "https://github.com/FunDan3/pqcryptography/",
	project_urls = {
		"Bug Tracker": "https://github.com/FunDan3/pqcryptography/issues"
	},
	classifiers = [
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
		"Operating System :: OS Independent",
	],
	packages = setuptools.find_packages(where = "src"),
	package_dir = {"": "src"},
	python_requires = ">=3.8",
	install_requires = ["pycryptodome", "liboqs"]
)
