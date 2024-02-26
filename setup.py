from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e.'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements

setup(
    name="Crop Recommendation System",
    version="1.0.0",
    description="A deep Machine Learning Model to recommend crop to the farmers.",
    author="Rohit Padalkar",
    autor_email='rohitpadalkar5s@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)