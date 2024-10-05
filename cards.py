
suits = ["H","S","C","D"]
numbers = ['A', 'K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2']

class Card:
    def __init__(self,card):
        self.card = card
        self.suit = card[0]
        if self.suit not in suits:
            raise Exception("Invalid Suit")
        self.number = card[1:]
        if self.number not in numbers:
            raise Exception("Invalid Number")
    
    def __eq__(self, value: object) -> bool:
        return self.number == value.number
    
    def __gt__(self,value: object):
        return numbers.index(self.number) < numbers.index(value.number)
    def __lt__(self,value: object):
        return value > self
    def __ge__(self,value: object):
        return self > value or self == value
    def __le__(self,value: object):
        return value >= self

class Hand:
    def __init__(self,cards_lst):
        self.cards_lst = cards_lst


def choose_2_lst(lst: list):
    L = []
    for idx1, c1 in enumerate(lst):
        choice = [c1]
        for c2 in lst[idx1+1:]:
            choice.append(c2)
            L.append(choice.copy())
            del  choice[-1]
    return L

def choose_3_lst(lst: list):
    L = []
    for idx1, c1 in enumerate(lst):
        choice = [c1]
        for idx2, c2 in enumerate(lst[idx1+1:]):
            choice.append(c2)
            for c3 in lst[idx1+1:][idx2+1:]:
                choice.append(c3)
                L.append(choice.copy())
                del choice[-1]
            del choice[-1]
    return L

def choose_lst(lst: list,k,choice = [],L = []):
    if k == 0:
        L.append(choice.copy())
        return 
    for idx, c in enumerate(lst):
        choice.append(c)
        choose_lst(lst[idx+1:],k-1,choice,L)
        del choice[-1]
    return L
       


def generate_straight_flushes_ordered(rank_counter = 1):
    for idx, num in enumerate(numbers[:10]):
        if num == "5":
            hand_nums = numbers[idx:idx+4]
            hand_nums.append("A")
        else:
            hand_nums = numbers[idx:idx+5]
        for suit in suits:
            hand = [suit+hand_num for hand_num in hand_nums]
            print(rank_counter,hand)
        rank_counter += 1
    return rank_counter

def generate_four_of_a_kind(rank_counter):
    for idx, num in enumerate(numbers):
        hand = [suit+num for suit in suits]
        for kicker in numbers:
            for suit in suits:
                kicker_card = suit+kicker
                if kicker_card not in hand:
                    hand.append(kicker_card)
                    print(rank_counter,hand)
                    del hand[-1]
                    rank_counter += 1

def generate_full_house(rank_counter):
    for triple_num in numbers:
        L1 = choose_lst(suits,3,[],[])
        for three_suits in L1:
            triple_hand = [suit+triple_num for suit in three_suits]
            for pair_num in numbers:
                if pair_num != triple_num:
                    L2 = choose_lst(suits,2,[],[])
                    for pair_suits in L2:
                        pair_hand = [suit+pair_num  for suit in pair_suits]
                        hand = []
                        hand.extend(triple_hand)
                        hand.extend(pair_hand)
                        print(rank_counter,hand)
                    rank_counter += 1

def generate_flush(rank_counter):
    for card_nums in choose_lst(numbers,5):
        start_idx = numbers.index(card_nums[0])
        end_idx = numbers.index(card_nums[-1])
        if end_idx-start_idx != 4:
            for suit in suits:
                hand = [suit+num for num in card_nums]
                print(rank_counter,hand)
            rank_counter += 1





# print(numbers[:-3])
# generate_straight_flushes_ordered() 
# generate_four_of_a_kind(1)
# generate_full_house(1)
# generate_flush(1)
# for i in range(2):
#     L = choose_lst(["H","S","C","D"],2,[],[])
#     print(L)