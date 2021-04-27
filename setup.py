from setuptools import setup, find_packages

setup(
    name="q2-keegan",
    version='0.0.1',
    packages=find_packages(),
    author="Keegan Evans",
    author_email="keegan.evans@gmail.com",
    url="keeganevans.com",
    license="BSD-3-Clause",
    description="Taxonomic analysis and visualization.",
    entry_points={
        "qiime2.plugins":
        ["q2-keegan=q2_keegan.plugin_setup:plugin"]
    },
    package_data={'q2_keegan': []},
    zip_safe=False
)
