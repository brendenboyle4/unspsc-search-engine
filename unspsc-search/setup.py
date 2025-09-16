from setuptools import setup, find_packages

setup(
    name="unspsc-search",
    version="1.0.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'streamlit>=1.26.0',
        'pandas>=2.1.0',
        'python-dotenv>=1.0.0',
    ],
    author="Brenden Boyle",
    author_email="Brenden.Boyle@tpsgc-pwgsc.gc.ca",
    description="UNSPSC Code Search Application",
    keywords="unspsc, search, equipment, codes",
    url="https://github.com/brendenboyle4/unspsc-search-engine",
)