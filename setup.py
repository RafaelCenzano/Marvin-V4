from setuptools import setup, find_packages


# Get Readme text
with open('README.rst') as f:
    readme = f.read()


# Get License text
with open('LICENSE') as f:
    license = f.read()


# Run setup
setup(
    name='Marvin-V4',
    version='4.0.0',
    description='Virtual Assistant using Python',
    long_description=readme,
    author='Rafael Cenzano',
    author_email='savagecoder77@gmail.com',
    url='https://github.com/Marvin-Virtual-Assistant/Marvin-V4',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)