import ez_setup

ez_setup.use_setuptools()

from setuptools import setup, find_packages

setup(
    name="dna_features_viewer",
    author="JaspinXu",
    description="Plot features from DNA sequences (e.g. Genbank) with Python",
    url="https://github.com/Edinburgh-Genome-Foundry/DnaFeaturesViewer",
    keywords="DNA Sequence Feature Genbank Biopython Matplotlib",
    packages=find_packages(exclude="docs"),
    install_requires=["matplotlib>=3", "Biopython", "packaging"],
)
