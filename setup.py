import os

from setuptools import setup, find_packages


def readme() -> str:
    """Utility function to read the README.md.
    Used for the `long_description`. It's nice, because now
    1) we have a top level README file and
    2) it's easier to type in the README file than to put a raw string in below.
    Args:
        nothing
    Returns:
        String of readed README.md file.
    """
    return open(os.path.join(os.path.dirname(__file__), 'README.md')).read()


setup(
    name='openai_chatbot_demo_packages',
    version='1.0',
    author='Angello Triviño Umaña',
    author_email='angello.trivinio@gmail.com',
    description='ChatBot with using OpenAI API, also, using Telegram's BotFather',
    python_requires='>=3',
    license='MIT',
    url='',
    packages=find_packages(),
    long_description=readme(),
)