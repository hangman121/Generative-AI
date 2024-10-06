from setuptools import setup, find_packages

setup(
name="mcqgenerator",
version="0.0.1",
author="Syed Hasham Hameed",
author_email="hashambukhari121@gmail.com",
packages=find_packages(),
install_requires=["openai","langchain", "streamlit","python-dotenv","PyPDF2"],
)