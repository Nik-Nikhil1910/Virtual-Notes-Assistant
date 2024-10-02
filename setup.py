import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0"

REPO_NAME = "Virtual-Notes-Assistant"
AUTHOR_USER_NAME = "Nik-Nikhil1910"
SRC_REPO = "Virtual_Notes_Assistant"
AUTHOR_EMAIL = "nikhilkondinya@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author="Nikhil Sharma",
    author_email="nikhilkondinya@gmail.com",
    description="A python package for Virtual Notes Assistant app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/Nik-Nikhil1910/Virtual-Notes-Assistant.git",
    project_urls={
        "Bug Tracker": f"https://github.com/Nik-Nikhil1910/Virtual-Notes-Assistant/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)