from setuptools import setup, find_packages

setup(
    name='force-absolute-imports',
    version='0.0.3',
    py_modules=['main'],
    packages=find_packages(where=''),
    entry_points={
        'console_scripts': [
            'force-absolute-imports=main:main',
        ],
    },
    python_requires='>=3.10',
    install_requires=[
        'libcst>=1.0.0',
    ],
)
