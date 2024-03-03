import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0"

REPO_NAME = "Chest-Cancer-Classification-Project"
AUTHOR_USER_NAME = "ABHISHEK UPADHYAY"
SRC_REPO = "cnnClassifier"
AUTHOR_EMAIL = "abhishek.it21-25@recabn.ac.in"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for CNN app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/Abhishek4209/CHEST-CANCER-PREDECTION-USING-CNN",
    project_urls={
        "Bug Tracker": f"https://github.com/Abhishek4209/CHEST-CANCER-PREDECTION-USING-CNN/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)