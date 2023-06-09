from setuptools import find_packages,setup
from typing import List
HYPHON = '-e .'
def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path,"r") as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]  
        if HYPHON in requirements:
            requirements.remove(HYPHON)
    return requirements

setup(
    name="GemPricePrediction",
    version="0.0.1",
    author="Chandan",
    author_email="chandannadve@gmail.com",
    install_requires=get_requirements('requirements.txt'),
    packages=find_packages()
)