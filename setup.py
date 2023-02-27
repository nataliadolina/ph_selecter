from setuptools import setup

APP_NAME = "FastPhCopier"
APP = ["main.py"]
DATA_FILES = [("files", ["files/config.ini", "files/instruction.txt"])]
OPTIONS = {'packages': ['pyqt6'], 'iconfile': "icons/icon.icns", 'argv_emulation': True}

setup(app=APP, name=APP_NAME, data_files=DATA_FILES, options={"py2app": OPTIONS}, setup_requires=["py2app"], )
