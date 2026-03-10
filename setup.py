"""
This file is responsible for creating a ML application as a package and deploy in PyPi and
anyone can also install this package in different project and use it
"""

from setuptools import find_packages,setup
from typing import List

HYPHEN_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''this function will return the list of requirements'''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPHEN_DOT in requirements:
            requirements.remove(HYPHEN_DOT)

    return requirements

setup(
    name="mlproject",
    version="0.0.1",
    author="Keerthi",
    author_email="keek281995@gmail.com",
    packages=find_packages(), #Whenever the find_packages in setup.py runs, it will go check in how many folders there is this __init__.py file and it will consider that particular folder as a package
    install_requires=get_requirements('requirements.txt')
)