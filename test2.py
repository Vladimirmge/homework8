from payment import cal

def test2(a,b):
    c = cal(a,b)

    test_c = (c * 3600)/100

    assert c == test_c

test2(10,20)
test2(1,15)
test2(0,3)