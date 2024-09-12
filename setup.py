from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT ='-e .'

def get_requirements(file_path: str) -> List[str]:
    '''
    This function will return the list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
            requirements = file_obj.readlines()
            # Remove newline characters and clean the list
            requirements = [req.replace("\n", "") for req in requirements]

            # Remove '-e .' if present
            if HYPHEN_E_DOT in requirements:
                requirements.remove(HYPHEN_E_DOT)
   
    return requirements

setup(
    name='MLProject',
    version='0.0.1',
    author='Poojapathare',
    author_email='poojavpathare@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
