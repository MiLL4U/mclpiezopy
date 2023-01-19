from typing import List
import setuptools


def _requires_from_file(filename: str) -> List[str]:
    return open(filename).read().splitlines()


setuptools.setup(
    name="mclpiezopy",
    version="0.1.0",
    install_requires=_requires_from_file('requirements.txt'),
    author="Hiroaki Takahashi",
    author_email="aphiloboe@gmail.com",
    description="Wrapper for Nano-Drive (Mad City Labs, inc.) "
    "library (Madlib.dll)",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        'Operating System :: Microsoft :: Windows',
    ],
    python_requires='>=3.7',
)
