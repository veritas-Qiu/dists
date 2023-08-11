import numpy as np
import dp

def rnn():
    pass

class Match:
    def __init__(self, players, seed) -> None:
        self.players = players
        self.max_counters = 0
        self.money = [0 for _ in range(players)]
        self.games = []
        self.rng = np.random.default_rng(seed)
    
class Game:
    def __init__(self, players, rng, host, max_counters) -> None:
        self.players = players
        self.useful_cards = rng.choise(52, 2*players+5, replace=False)
        self.cards = self.useful_cards[:2*players].reshape(players, 2)
        self.river = self.useful_cards[2*players:]
        self.calls = []
        self.open_count = 0
        self.host = host
        self.max_counters = [max_counters for _ in range(players)]
        self.alive = [1 for _ in range(players)] #1: alive, 0: dead, 2: all in
        self.last_rise = 0
        self.putin = [0 for _ in range(players)]
        self.result = [0 for _ in range(players)]
        self.min_counters = 2
        
    def check_status(self):
        if self.alive.count(1) <= 1:
            return False
        return True
        
    def preflop(self):
        big_blind = (self.host + 1) % self.players
        small_blind = (self.host + 2) % self.players
        gunner = (self.host + 3) % self.players
        
        self.result[big_blind] = -2
        self.result[small_blind] = -1
        
        now = gunner
        while(True):
            if self.alive[now % self.players]:
                call_num = rnn(self.players, self.max_counters, self.cards[now], self.calls, self.river, self.open_count, self.min_counters)
            else:
                call_num = -1
                
            if call_num != -1:
                self.putin[now % self.players] = -call_num
                
            if call_num > self.min_counters:
                self.min_counters = call_num
                self.last_rise = now
                
            if call_num == -1 and self.alive[now % self.players]:
                self.alive[now % self.players] = 0 # fold
            if call_num == self.max_counters[now % self.players]:
                self.alive[now % self.players] = 2 # all in
                
            self.call.append(call_num)
            now += 1
            if now - self.last_rise >= self.players:
                break
        
    def run(self):
        # preflop
        self.preflop()
            
        # flop
        if (self.check_status()):
            self.

        
    
