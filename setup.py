from setuptools import setup, find_packages

setup(
    name="files-gitflix-datasets",
    version="0.1.0",
    description="Meltano project file bundle of Matatika datasets for Matatika Examples tap-gitflix",
    packages=find_packages(),
    package_data={
        "bundle": [
            "analyze/datasets/tap-gitflix/*.yaml",
            "analyze/datasets/tap-gitflix/*.yml"
        ]
    }
)
