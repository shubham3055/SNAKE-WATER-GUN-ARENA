from player import Player


def test_heal():

    p = Player("Shubham")

    p.hp = 3

    p.heal()

    assert p.hp == 4