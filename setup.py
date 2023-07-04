import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="VALET",
    version="0.0.1",
    author="Talha Bin Masood",
    author_email="talha.bin.masood@liu.se",
    description="A library for computing electronic charges and charge transfer "
        "in electronic transition using Natural Transition Orbitals.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tbmasood/VALET",
    license="MIT",
    platforms=["Unix", "MacOS", "Windows"],
    install_requires=["numpy>=1.19.4", "matplotlib>=3.3.3", "cvxpy>=1.1.7"],
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
