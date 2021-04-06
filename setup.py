import setuptools


with open("requirements.txt", "r", encoding="utf-8") as r:
    requires = [i.strip() for i in r]  # Зависимости

with open("README.md", "r", encoding="utf-8") as f:
    readme = f.read()


setuptools.setup(
    name="myqiwi",
    version="0.2.5",
    description="Python qiwi api for Humans.",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="daveusa31",
    packages=setuptools.find_packages(),
    include_package_data=True,
    python_requires=">=3.5",
    install_requires=requires,
    license="MIT",
    zip_safe=False,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Natural Language :: Russian",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    project_urls={"Source": "https://github.com/daveusa31/myqiwi"},
)
