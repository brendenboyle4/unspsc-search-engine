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
    author="Your Name",
    author_email="your.email@example.com",
    description="UNSPSC Code Search Application",
    keywords="unspsc, search, equipment, codes",
    url="https://github.com/yourusername/unspsc-search",
)