def ct(i):#2023試算 總收入-單身124000 然後營利去算下列級距
    P = i - 124000
    if P <= 0:
        return 0
    elif P <= 560000:
        return round(P * 0.05)
    elif P <= 1260000:
        return round(560000 * 0.05 + (P - 560000) * 0.12)
    elif P <= 2520000:
        return round(560000 * 0.05 + 700000 * 0.12 + (P - 1260000) * 0.2)
    elif P <= 4720000:
        return round(560000 * 0.05 + 700000 * 0.12 + 1260000 * 0.2 + (P - 2520000) * 0.3)
    else:
        return round(560000 * 0.05 + 700000 * 0.12 + 1260000 * 0.2 + 2200000 * 0.3 + (P - 4720000) * 0.4)



def test_ct():
    assert ct(-50000) == 0
def test_ct0():
    assert ct(124000) == 0
def test_ct560000():
    assert ct(200000) == 3800
def test_ct1260000():
    assert ct(800000) == 41920
def test_ct2520000():
    assert ct(1800000) == 195200
def test_ct4720000():
    assert ct(3500000) == 620800
def test_ctbig472000():
    assert ct(5000000) == 1086400
def test_ctbig_0():
    assert ct(684000-124000) == 21800
def test_ctand1260000():
    assert ct(1260000) == 97120
   
