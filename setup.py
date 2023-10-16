import setuptools

with open("Readme.md","r",encoding="utf-8") as f:
    long_description =f.read()
    


REPO_NAME = "MLops Assignment"
AUTHOR_USER_NAME = "Jwalx"
SRC_REPO = "mlproject"
AUTHOR_EMAIL = "jwalxpatel@gmail.com"


setuptools.setup(
    name = SRC_REPO,
    author = AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="a small package for ml app",
    Long_description=long_description,
    long_description_content="text/markdown",
    url =f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls = {
        "Bug Tracker":f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"":"src"},
    package = setuptools.find_packages(where = "src")
)