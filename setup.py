from setuptools import setup, find_packages

setup(
    name='ascim',
    version='0.1.1',
    description='Manipulate ASCII Art & Tables in a bitmap-image-like manner.',
    long_description=open('./README.md').read(),
    long_description_content_type='text/markdown',
    keywords='ascii art',
    license='MIT',
    url='https://github.com/fakefred/ascim',
    author='fakefred',
    author_email='fakefred@protonmail.ch',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License'
    ],
    packages=find_packages(),
    include_package_data=True,
    python_requires='>=3.5',
    install_requires=[],
    project_urls={
        'LiberaPay': 'https://liberapay.com/fakefred/donate'
    }
)
