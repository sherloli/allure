import pytest
import pytest_html
def add(a,b):

    return a+b


def test_add():
    print("sadas")
    assert add(3,8) > 100

def test_paa():

    pass
if __name__ == '__main__':
    #pytest.main(["-s","test_add.py","--html=report.html" ,"--self-contained-html"])

    pytest.main(["-s", "test_add.py", "--html=report.html"])

