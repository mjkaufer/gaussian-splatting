from setuptools import setup, find_packages


setup(
    name="gaussian_splatting",
    version="0.1",
    description="Splatting for Modal experiment",
    author="Matthew Kaufer",
    author_email="mjkaufer@gmail.com",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "pandas",
    ],
)
