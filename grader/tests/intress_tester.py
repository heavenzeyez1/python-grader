from grader import Tester, testAll

t = Tester()

@t.test
def firstTest(m):
    m.stdin.write("500") # at beginning
    m.stdin.write("5") # 5%
    assert "638" in m.stdout.read()


@t.test
def secondTest(m):
    m.stdin.write("0") # at beginning
    m.stdin.write("10") # percentage
    assert "0." in m.stdout.read()


testAll(t)