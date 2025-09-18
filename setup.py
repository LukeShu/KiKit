# -*- coding: utf-8 -*-

import setuptools
import versioneer


with open("README.md", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="kikit",
    python_requires='>=3.8',  # if you bump this, be sure to also adjust the matrix in .github/workflows/test-kikit.yml
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    author="Jan Mrázek",
    author_email="email@honzamrazek.cz",
    description="Automation for KiCAD boards",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yaqwsx/KiKit",
    packages=setuptools.find_packages(),
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "numpy", # Required for MacOS
        "shapely>=2.0.3",
        "click>=7.1",
        "markdown2>=2.4",
        "pybars3>=0.9",
        "solidpython>=1.1.2",
        "commentjson>=0.9"
    ],
    extras_require={
        "dev": [
            "versioneer",
            "pytest",
            "build",
            "wheel",
        ],
    },
    zip_safe=False,
    include_package_data=False,
    package_data={
        "kikit": [
            "resources/**",
        ],
    },
    entry_points = {
        "console_scripts": [
            "kikit=kikit.ui:cli",
            "kikit-info=kikit.info:cli"
        ],
    }
)
