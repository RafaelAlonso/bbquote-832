from bbquote.get_quote import get_quote

def test_get_quote_type():
  assert type(get_quote()) == str
  
def test_get_quote_size():
  assert len(get_quote()) != 0
