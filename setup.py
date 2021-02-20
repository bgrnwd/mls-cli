from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="mls-cli",
    version="0.0.1",
    author="Brian Greenwood",
    author_email="11201127+bgrnwd@users.noreply.github.com",
    description="Check Major League Soccer standings, scores, and stats from your terminal",
    license="MIT",
    keywords="stats api mls soccer football cli",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bgrnwd/mls-cli",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    entry_points={"console_scripts": ["mls = mls.__main__:main"]},
)