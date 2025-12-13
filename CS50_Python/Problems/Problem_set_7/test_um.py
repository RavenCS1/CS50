from um import count

def test_appopriate():
    assert count("hello, um, world")==1
    assert count("um, hello, Um, world")==2
    assert count("UM...")==1
    
def test_inappropriate():
    assert count("yum")==0
    assert count("yummy")==0

def test_complex():
    assert count("I would uM, eat, um, smt, um, yummy")==3
    assert count("yum um, yummy, um, um...")==3