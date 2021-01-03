import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="t3-jlo_unofficial",
    version="0.0.1",
    author="Jonathan Lopez",
    author_email="jonathanglopez@gmail.com",
    description="A toy neural network project using tic-tac-toe",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/otherwisejlo/t3_net",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
