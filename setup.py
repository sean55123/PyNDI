from setuptools import setup, find_packages

setup(
    name="PyNDI",
    version="0.1.0",
    author="Hsuan-Han Chiu",
    author_email="chiu137@purdue.edu",
    description="This is a simple damge index calculation package.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/sean55123/PyNOTES",
    packages=find_packages(), 
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=["numpy",
                      "win32"],  
)
