from goald.config.model.alternative import Alternative


def test_alternative():
    alt = Alternative()
    alt.setProperty("prop1", 3)
    intValue = alt.getProperty("prop1", int)
    assert intValue == 3

    alt.setProperty("prop2", "my_str")
    strValue = alt.getProperty("prop2", str)
    assert strValue == "my_str"

    intValue = alt.getProperty("prop1")
    assert intValue == 3

