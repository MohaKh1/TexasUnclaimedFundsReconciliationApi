from setuptools import setup, find_packages

# Read project description from README file
with open("README.md", "r", encoding="utf-8") as readme_file:
    long_description = readme_file.read()

# Parse requirements from requirements.txt
with open("requirements.txt", "r", encoding="utf-8") as requirements_file:
    requirements = requirements_file.readlines()

setup(
    name="Unclaimed-Funds-Recon",  # Replace with your package name
    version="0.1.0",           # Replace with your package version
    description="State held Unclaimed Funds Reconciliation tool",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Haroon Khan",
    author_email="MohammedHaroonKhan19@gmail.com",
    packages=find_packages(where="src"),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
