from setuptools import setup, find_packages

setup(
    name="clean_folder",
    version="0.0.1",
    description="Very useful code",
    url="http://github.com/dummy_user/useful",
    author="Shyrik",
    author_email="la653909@gmail.com",
    license="MIT",
    # packages=["useful"],
    packages=find_packages(),
    install_requires=["markdown"],
    entry_points={
        "console_scripts": ["clean_folder = clean_folder.sorter:main"]
        # "generator = clean_folder.Language_Generator:generate_empty_files_ue, generate_empty_files_uk"
        # ]
    },
)
