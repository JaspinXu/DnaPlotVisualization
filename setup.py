import ez_setup

ez_setup.use_setuptools()

from setuptools import setup, find_packages

setup(
    name="DnaPlotVisualization",
    author="JaspinXu",
    description="Introduction to Life Sciences",
    url="https://github.com/JaspinXu/DnaPlotVisualization",
    keywords="Introduction to Life Sciences",
    packages=find_packages(exclude="docs"),
    install_requires=["matplotlib>=3", "Biopython", "packaging"],
)
