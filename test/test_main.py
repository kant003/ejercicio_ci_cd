from src.main import elevar, to_upper, to_lower

def test_elevar_basico():
    assert elevar(2,3) == 8
    
def test_to_upper():
    assert to_upper('Angel') == 'ANGEL'
    
def test_to_lower():
    assert to_lower('Angel') == "angel"