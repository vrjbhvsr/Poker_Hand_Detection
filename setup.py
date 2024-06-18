from setuptools import setup, find_packages


with open('README.md','r', encoding="utf-8") as f:
    descriptions = f.read()


setup(
    name= "Poker Hand Detection",
    version= "0.0.1",
    author= "Vraj Bhavsar",
    author_email= "vrajcbhavsar0905@gmail.com",
    description= "small python package for detection app.",
    long_description= descriptions,
    long_description_content = "text/markdown",
    url = "https://github.com/vrjbhvsr/Poker_Hand_Detection.git",
    packages= find_packages(),
    install_requires= []

)