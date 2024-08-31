import setuptools
with open("README.md", "r", encoding="utf-8") as f:
          long_desciption = f.read()


__version__ = "0.0.0"

REPO_NAME = "sih_project"
AUTHOR_USER_NAME = "Sujal-gulia"
SRC_REPO = "sih_project"
AUTHOR_EMAIL = "sujal.gulia18@gmail.com"


setuptools.setup(
        name = SRC_REPO,
        version=__version__,
        author=AUTHOR_USER_NAME,
        author_email=AUTHOR_EMAIL,
        description="AI-Enhanced Healthcare Diagnostics and Management System",
        long_description=long_desciption,
        long_description_content="text/markdown",
        url=f"https://githun.com/(AUTHOR_USER_NAME)/(REPO_NAME)",
        project_uris={
                "Bug Tracker": f"https://githun.com/(AUTHOR_USER_NAME)/(REPO_NAME)/issues",
        },
        package_dir={"":"src"},
        packages=setuptools.find_packages(where="src")
)