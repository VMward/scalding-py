import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="scalding",
    version="0.0.1",
    author="social-learning",
    author_email="ben.yan.fan@gmail.com",
    description="Scalding - functional data processing in python based off Scala & Hadoop",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/social-learning/setup.py",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8.5',
)
