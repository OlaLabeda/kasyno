import random
import pytest


    
class Player():
    def __init__(self, name, list_of_dices = None, result = 0):
        self.name = name
        self.list_of_dices = list_of_dices if list_of_dices else []
        self.result = result
    
    
    def sum_from_dices(self):
        
        result = 0
        even_count = 0
        even_sum = 0
        odd_count = 0
        odd_sum = 0
        
        zwyklasuma = 0
        
        dict_sums = {}
        
        for element in self.list_of_dices:
            zwyklasuma += element
            if element not in dict_sums:
                dict_sums[element] = 1
            else:
                dict_sums[element] += 1
                
            if element % 2 == 0:
                even_count += 1
                even_sum += element
            else:
                odd_count +=1
                odd_sum += element
        sum_from_rules = 0    
        howmuch = 1
        for key, value in dict_sums.items():
            if value == 4:
                sum_from_rules = 4*key*6
                break
            if value == 3:
                howmuch = 3
                sum_from_rules += (key * 3)
            if value == 2:
                howmuch = 2
                sum_from_rules += (key * 2)
            if value == 1:
                sum_from_rules += key
        sum_from_rules *= howmuch
        if even_count == 4:
            result = max(sum_from_rules, even_sum + 2)
        elif odd_count == 4:
            result = max(sum_from_rules, odd_sum + 3)
        else:
            result = sum_from_rules
        
        return result

                
class Kasyno():
    def __init__(self, players_list = None):
        self.players_list = players_list if players_list else []
    
    
    def add_player(self, name, list_of_dices, result):
        self.players_list.append(Player(name, list_of_dices, result))
       
        
    def remove_player(self, index):
        """
        :removes player of a certain index
        
        """
        self.players_list.pop(index)
        
        
    def roll_dices(self):
        dices_list_random = []
        for liczby in range(0, 4):
            number = random.randint(1, 6)
            dices_list_random.append(number)
        return dices_list_random
        
    def wybor_zwyciezcy(self):
        maxresult = 0
        zwyciezca = 'Brak'
        for osoby in self.players_list():
            if osoby.result() > maxresult:
                maxresult = osoby.result()
                zwyciezca = osoby.name
        return zwyciezca
    
    
    def play(self, rounds):     
        for i in range (1, rounds):
            for players in self.players_list:
                players.list_of_dices = self.roll_dices()
                players.result += players.sum_from_dices()
               
               
    def print_results(self):         
        for players in self.players_list:
            print(f'{players.name} has {players.result} points in the end')
                
                
                