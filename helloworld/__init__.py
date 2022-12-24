import check50
from re import escape


@check50.check()
def exists():
    """helloworld.py exists"""
    check50.exists("helloworld.py")


@check50.check(exists)
def testhello():
    """Prints out hello world"""
    check50.run("python3 helloworld.py").stdout("Hello, World").exit()

def regex(text):
    """match case-sensitively, allowing for characters on either side."""
    return rf"^.*{escape(text)}.*$"