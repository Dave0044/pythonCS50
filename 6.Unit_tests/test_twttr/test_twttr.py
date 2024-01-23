from twttr import shorten

def main():
    test_shorten()



def test_shorten():
    assert shorten("Reloj") == "Rlj"
    assert shorten("Windows") == "Wndws"
    assert shorten("House_Big") == "Hs_Bg"
    assert shorten("CaSe50") == "CS50"
    assert shorten("Hello, World") == "Hll, Wrld"
    assert shorten("+=(.,/)") == "+=(.,/)"
    assert shorten("antes") == "nts"
    assert shorten("14") == "14"
    assert shorten("aAarr") == "rr"

if __name__ == "__main__":
    main()
