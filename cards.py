
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
            # rank_counter += 1
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
                    # rank_counter += 1
            rank_counter += 1
    return rank_counter

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
                        # rank_counter += 1
                    rank_counter += 1
    return rank_counter

def generate_flush(rank_counter):
    for card_nums in choose_lst(numbers,5):
        start_idx = numbers.index(card_nums[0])
        end_idx = numbers.index(card_nums[-1])
        if not (end_idx-start_idx == 4 or (card_nums == ['A','5','4','3','2'])):
            for suit in suits:
                hand = [suit+num for num in card_nums]
                print(rank_counter,hand)
                # rank_counter += 1
            rank_counter += 1
    return rank_counter

def generate_straight(rank_counter):
    for idx, num in enumerate(numbers[:10]):
        if num == "5":
            hand_nums = numbers[idx:idx+4]
            hand_nums.append("A")
        else:
            hand_nums = numbers[idx:idx+5]
        for s1 in suits:
            for s2 in suits:
                for s3 in suits:
                    for s4 in suits:
                        for s5 in suits:
                            if not (s1 == s2 == s3 == s4 == s5):
                                hand = [s1+hand_nums[0], s2+hand_nums[1], s3+hand_nums[2], s4+hand_nums[3], s5+hand_nums[4]]
                                print(rank_counter,hand)
                                # rank_counter += 1
        rank_counter += 1
    return rank_counter

def generate_three_of_a_kind(rank_counter):
    for idx, triple_card in enumerate(numbers):
        for three_suits in choose_lst(suits,3,[],[]):
            triple_hand = [suit+triple_card for suit in three_suits]
            for other_two_nums in choose_lst(numbers,2,[],[]):
                if triple_card not in other_two_nums:
                    for suit1 in suits:
                        for suit2 in suits:
                            other_two_hand = [suit1+other_two_nums[0],suit2+other_two_nums[1]]
                            hand = []
                            hand.extend(triple_hand)
                            hand.extend(other_two_hand)
                            print(rank_counter,hand)
                            # rank_counter += 1
                    rank_counter += 1
    return rank_counter

def generate_two_pair(rank_counter):
    for two_pair_nums in choose_lst(numbers,2,[],[]):
        for suit_pair_1 in choose_lst(suits,2,[],[]):
            for suit_pair_2 in choose_lst(suits,2,[],[]):
                two_pair_hand = [suit_pair_1[0]+two_pair_nums[0],suit_pair_1[1]+two_pair_nums[0],suit_pair_2[0]+two_pair_nums[1],suit_pair_2[1]+two_pair_nums[1]]
                for kicker_num in numbers:
                    if kicker_num not in two_pair_nums:
                        for kicker_suit in suits:
                            kicker = kicker_suit+kicker_num
                            hand = []
                            hand.extend(two_pair_hand)
                            hand.append(kicker)
                            print(rank_counter,hand)
                            # rank_counter += 1
                        rank_counter += 1
    return rank_counter

def generate_pair(rank_counter):
    for pair_num in numbers:
        for suit_pair in choose_lst(suits,2,[],[]):
            pair_hand = [suit+pair_num for suit in suit_pair]
            for other_three in choose_lst(numbers,3,[],[]):
                if pair_num not in other_three:
                    for suit1 in suits:
                        for suit2 in suits:
                            for suit3 in suits:
                                other_three_hand = [suit1+other_three[0],suit2+other_three[1],suit3+other_three[2]]
                                hand = []
                                hand.extend(pair_hand)
                                hand.extend(other_three_hand)
                                print(rank_counter,hand)
                    rank_counter += 1 
    return rank_counter

def generate_high_card(rank_counter):
    for card_nums in choose_lst(numbers,5,[],[]):
        start_idx = numbers.index(card_nums[0])
        end_idx = numbers.index(card_nums[-1])
        if not (end_idx-start_idx == 4 or (card_nums == ['A','5','4','3','2'])):
            for s1 in suits:
                for s2 in suits:
                    for s3 in suits:
                        for s4 in suits:
                            for s5 in suits:
                                if not (s1 == s2 == s3 == s4 == s5):
                                    hand = [s1+card_nums[0], s2+card_nums[1], s3+card_nums[2], s4+card_nums[3], s5+card_nums[4]]
                                    print(rank_counter,hand)
            rank_counter += 1
    return rank_counter


        


# print(numbers[:-3])
rank = 1
rank = generate_straight_flushes_ordered() 
rank = generate_four_of_a_kind(rank)
rank = generate_full_house(rank)
# rank = 1
rank = generate_flush(rank)
rank = generate_straight(rank)
rank = generate_three_of_a_kind(rank)
rank = generate_two_pair(rank)
rank = generate_pair(rank)
# rank = 1
rank = generate_high_card(rank)
print("Final Rank: ",rank)
# for i in range(2):
#     L = choose_lst(["H","S","C","D"],2,[],[])
#     print(L)