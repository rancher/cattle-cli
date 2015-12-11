from setuptools import setup

with open('./requirements.txt') as r:
    requirements = [line for line in r]

setup(
    name='cattle',
    version='0.5.3',
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
