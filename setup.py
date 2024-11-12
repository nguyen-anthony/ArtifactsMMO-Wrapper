from setuptools import setup, find_packages

setup(
    name="artifacts_mmo_wrapper",
    version="1.1.0",
    author="Veillax",
    author_email="contact@veillax.com",
    description="A Python API Wrapper for ArtifactsMMO",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Veillax/ArtifactsMMO-Wrapper", 
    packages=find_packages(where="src"),         # Look for packages in 'src' if used
    package_dir={"": "src"},                     # Maps root package to 'src'
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.11",
    install_requires=[
        "requests"
    ],
)
