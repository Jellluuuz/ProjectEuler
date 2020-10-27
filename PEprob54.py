import copy as cp
import time


def split_hand(hand):                    # splits a single hand into values and colors, as lists
    card_values = [hand[0], hand[3], hand[6], hand[9], hand[12]]
    for index, i in enumerate(card_values):
        if i == 'A':
            card_values[index] = 14
        if i == 'K':
            card_values[index] = 13
        if i == 'Q':
            card_values[index] = 12
        if i == 'J':
            card_values[index] = 11
        if i == 'T':
            card_values[index] = 10
        card_values[index] = int(card_values[index])

    card_colors = [hand[1], hand[4], hand[7], hand[10], hand[13]]
    return card_values, card_colors


def check_hand(hand):                    # check the highest score for a single hand
                                        # RF = 10, down to HC = 1

    values, colors = split_hand(hand)

    temp_val = cp.deepcopy(values)      # make a sorted double
    temp_val.sort()

    val_set = set(values)               # create set of values to check nr of duplicates

    # check royal or straight (flush)
    if colors[0] == colors[1] == colors[2] == colors[3] == colors[4]:                                # flush
        if temp_val[4] == temp_val[3] + 1 == temp_val[2] + 2 == temp_val[1] + 3 == temp_val[0] + 4:  # consecutive
            if temp_val[0] == 10:                                                                    # royal
                print 'found a royal'
                return 10
            print 'found a straight'
            return 9

    # check 4ook:
    if len(val_set) == 2:               # 4ook or FH
        for i in val_set:
            if values.count(i) == 4:
                print 'found 4ook'
                return 8

        print 'found FH'
        return 7

    # check flush:
    if colors[0] == colors[1] == colors[2] == colors[3] == colors[4]:  # flush
        print 'found a flush'
        return 6

    # check straight:
    if temp_val[4] == temp_val[3] + 1 == temp_val[2] + 2 == temp_val[1] + 3 == temp_val[0] + 4:
        print 'found a straight'
        return 5

    # check ToaK, TP, OP
    if len(val_set) == 3:
        for i in val_set:
            if values.count(i) == 3:
                print 'found ThoaK'
                return 4
        print 'found TP'
        return 3

    # check OP:
    if len(val_set) == 4:
        print 'found pair'
        return 2

    print 'high card'
    return 1


def check_same_rank(hand1, hand2, rank):                # return 1 if h1 wins, 0 otherwise
    values1, colors1 = split_hand(hand1)

    temp_val1 = cp.deepcopy(values1)      # make a sorted double
    temp_val1.sort()

    values2, colors2 = split_hand(hand2)

    temp_val2 = cp.deepcopy(values2)      # make a sorted double
    temp_val2.sort()

    if rank == 1:                         # check for HC
        for i in [4, 3, 2, 1, 0]:
            if temp_val1[i] > temp_val2[i]:
                return 1
            elif temp_val1[i] < temp_val2[i]:
                return 0
        return 0

    if rank == 2:
        for i in values1:
            if values1.count(i) == 2:
                pair_value1 = i
        for i in values2:
            if values2.count(i) == 2:
                pair_value2 = i
        if pair_value1 > pair_value2:
            return 1
        elif pair_value2 > pair_value1:
            return 0
        else:
            for i in [4, 3, 2, 1, 0]:
                if temp_val1[i] > temp_val2[i]:
                    return 1
                elif temp_val1[i] < temp_val2[i]:
                    return 0
        return 0

    if rank == 3:
        for i in range(4, -1, -1):
            if values1.count(values1[i]) == 2:
                hp1_val = values1[i]
                break
        for i in range(4, -1, -1):
            if values2.count(values2[i]) == 2:
                hp2_val = values2[i]
                break
        for i in range(0,5):
            if values1.count(values1[i]) == 2:
                lp1_val = values1[i]
                break
        for i in range(0, 5):
            if values2.count(values2[i]) == 2:
                lp2_val = values2[i]
                break

        if hp2_val > hp1_val:
            return 0
        if hp1_val > hp2_val:
            return 1
        elif hp1_val == hp2_val:
            if lp2_val > lp1_val:
                return 0
            if lp1_val > lp2_val:
                return 1
            elif lp1_val == lp2_val:
                for i in range(4 ,-1, -1):
                    if values1[i] > values2[i]:
                        return 1
                    else:
                        return 0
        return 0

    if rank == 4 or rank == 7:
        for i in range(0, 5):
            if values1.count(values1[i]) == 3:
                took1 = values1[i]
            if values2.count(values2[i]) == 3:
                took2 = values2[i]
        if took1 > took2:
            return 1
        else:
            return 0

    if rank == 5 or rank == 6:
        for i in range(4, -1, -1):
            if values1[i] > values2[i]:
                return 1
            else:
                return 0

    if rank == 8:
        for i in range(0, 5):
            if values1.count(values1[i]) == 4:
                fook1 = values1[i]
            if values2.count(values2[i]) == 4:
                fook2 = values2[i]
        if fook1 > fook2:
            return 1
        else:
            return 0

    if rank == 9:
        if values1[4] > values2[4]:
            return 1
        else:
            return 0


def run():
    f = open('p054_hands.txt')
    wincount = 0
    for x in f:
        h1 = x[0:14]
        h2 = x[15:30]
        print h1, '---', h2
        score1 = check_hand(h1)
        score2 = check_hand(h2)

        if score1 > score2:
            wincount += 1
        if score1 == score2:
            wincount += check_same_rank(h1, h2, score1)

    print wincount


t0 = time.time()
run()
print time.time() - t0
