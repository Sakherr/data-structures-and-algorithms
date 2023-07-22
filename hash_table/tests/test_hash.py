import pytest
from hash import Hashtable

def test_set_and_get():
    ht = Hashtable()
    ht.set("USA", "Washington D.C.")
    ht.set("Canada", "Ottawa")
    ht.set("France", "Paris")

    assert ht.get("USA") == "Washington D.C."
    assert ht.get("Canada") == "Ottawa"
    assert ht.get("France") == "Paris"

def test_non_existent_country():
    ht = Hashtable()

    with pytest.raises(KeyError):
        ht.get("Germany")

def test_keys():
    ht = Hashtable()
    ht.set("USA", "Washington D.C.")
    ht.set("Canada", "Ottawa")
    ht.set("France", "Paris")
    ht.set("Canada", "Ottawa (updated)")  

    expected_countries = ["USA", "Canada", "France"]
    assert sorted(ht.keys()) == sorted(expected_countries)

def test_collision_handling():
    ht = Hashtable(size=3)
    ht.set("USA", "Washington D.C.")
    ht.set("Brazil", "Brasília")

    assert ht.get("USA") == "Washington D.C."
    assert ht.get("Brazil") == "Brasília"

def test_hash_range():
    ht = Hashtable()
    country = "United Kingdom"

    hashed_country = ht.hash(country)
    assert 0 <= hashed_country < ht.size
