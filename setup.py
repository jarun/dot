from setuptools import setup, find_packages

setup(
    name="askiviu",
    version="0.1.0",
    description="Render images as Braille dot art in the terminal with color and animation support.",
    author="Arun Prakash Jana",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "Pillow"
    ],
    entry_points={
        'console_scripts': [
            'askiviu=askiviu.__main__:main',
        ],
    },
    python_requires='>=3.7',
)
