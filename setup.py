from setuptools import find_packages, setup

setup(
    name="delivery_contracts",
    packages=find_packages(include=["delivery_contract_system"]),
    version="0.1.0",
    description="Basic class for generating delivery contracts",
    author="mdotcarter@gmail.com",
)
