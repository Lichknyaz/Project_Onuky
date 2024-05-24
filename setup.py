from setuptools import setup, find_namespace_packages

setup(
    name='onuky',
    version='1.0.0',
    author='Your Name',
    description='A short description of your package',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Lichknyaz/Project_Onuky_01.git',
    packages=find_namespace_packages(),
    include_package_data=True,
    entry_points={"console_scripts": ["onuky = source.__main__:main"]},
    install_requires=[
        'colorama>=0.4.0',
        "prompt_toolkit",
        "setuptools",
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
