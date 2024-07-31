from setuptools import setup

APP=['Main.py']
OPTIONS = {
    'arg_emulation': True
}

setup(
    app=APP,
    options=OPTIONS,
    requires=["py2app"]
)