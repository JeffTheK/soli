import soli.__main__

def test_main(capfd):
    soli.__main__.main()
    out, err = capfd.readouterr()
    assert(out == "hello world\n")