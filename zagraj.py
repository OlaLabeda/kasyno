from kasyno import Kasyno, Player

def main():
    g1 = Player('asia', None, 0)
    g2 = Player('kaja', None, 0)
    g3 = Player('bartek', None, 0)
    lista = [g1, g2, g3]
    gra = Kasyno(lista)
    gra.add_player('janek', None, 0)
    gra.play(15)
    gra.add_player('kasia', None, 0)
    gra.play(4)
    gra.remove_player(2)
    gra.print_results()
    
    
if __name__ == "__main__":
    main()