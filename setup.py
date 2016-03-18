from setuptools import setup


# https://caremad.io/2013/07/setup-vs-requirement/
with open('./requirements.txt') as r:
    # strip fixed version info from requirements file
    requirements = [line.split('=', 1)[0] for line in r]

setup(
    name='cattle',
    version='0.5.4',
    py_modules=['cattle'],
    url='https://github.com/cattleio/cattle-cli',
    license='MIT Style',
    author='Darren Shepherd',
    author_email='darren.s.shepherd@gmail.com',
    description='Python API and CLI for Cattle',
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            'cattle = cattle:_main'
        ]
    }
)
