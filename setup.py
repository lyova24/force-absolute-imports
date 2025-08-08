from setuptools import setup, find_packages

setup(
    name='shrimport',
    version='0.0.4',
    py_modules=['main'],
    packages=find_packages(where=''),
    entry_points={
        'console_scripts': [
            'shrimport=main:main',
        ],
    },
    python_requires='>=3.10',
    install_requires=[
        'libcst>=1.0.0',
    ],
)
