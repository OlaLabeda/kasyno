from kasyno import Kasyno, Player

def test_create_non_empty_player():
    player = Player('bartek', [4, 2, 1, 3], 5)
    assert player.name == 'bartek'
    assert player.list_of_dices == [4, 2, 1, 3]
    assert player.result == 5
    
def test_create_player_without_list():
    player = Player('asia')
    assert player.name == 'asia'
    assert player.list_of_dices == []
    assert player.result == 0
    