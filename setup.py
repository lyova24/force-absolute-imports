from setuptools import setup

setup(
    name="force_absolute_imports",
    py_modules=["force_absolute_imports"],
    entry_points={
        "console_scripts": [
            "force-absolute-imports = force_absolute_imports:main",
        ],
    },
)
