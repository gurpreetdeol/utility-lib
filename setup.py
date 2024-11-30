from setuptools import setup, find_packages

setup(
    name='Utility Library',
    version='0.1.0',
    description='A utility library for data science preprocessing',
    author='Gurpreet Deol',
    author_email='deolgurpreet@hotmail.com',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'scikit-learn'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)