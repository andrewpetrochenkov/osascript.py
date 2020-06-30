import setuptools

setuptools.setup(
    name='osascript',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages()
)
