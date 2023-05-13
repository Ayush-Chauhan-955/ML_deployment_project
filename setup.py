from setuptools import find_packages, setup

trigger = '-e .'


def get_requirements(requirements_file):
    '''Return requirements from requirements file.'''

    with open(requirements_file) as f:
        requirements = f.read().splitlines()

        if trigger in requirements:
            requirements.remove(trigger)

    return requirements


setup(
    name='ml_deploy_project',
    version='0.1.0',
    author='Ayush Chauhan',
    author_email='ayushchauhan955@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements(requirements_file='requirements.txt'),
)
