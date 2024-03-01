import setuptools

with open("README.md", "r", encoding = "utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "netcat_python",
    version = "0.1.0",
    author = "MyFaduGame",
    author_email = "navinsharma9376319931@gmail.com",
    description = "This is an netcat Replacer Build on Python language.",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://www.github.com/MyFaduGame/netcat_python",
    project_urls = {
        "Bug Tracker": "https://www.github.com/MyFaduGame/",
    },
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir = {"": "src"},
    packages = setuptools.find_packages(where="src"),
    python_requires = ">=3.6"
)