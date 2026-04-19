"""The Game of Hog."""

from dice import six_sided, make_test_dice
from ucb import main, trace, interact

GOAL = 100  # The goal of Hog is to score 100 points.

######################
# Phase 1: Simulator #
######################


def roll_dice(num_rolls, dice=six_sided):
    """Simulate rolling the DICE exactly NUM_ROLLS > 0 times. Return the sum of
    the outcomes unless any of the outcomes is 1. In that case, return 1.

    num_rolls:  The number of dice rolls that will be made.
    dice:       A function that simulates a single dice roll outcome. Defaults to the six sided dice.
    """
    # These assert statements ensure that num_rolls is a positive integer.
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls > 0, 'Must roll at least once.'
    # BEGIN PROBLEM 1
    res = 0
    sow = False
    while num_rolls > 0:
        score = dice()
        if score == 1:
            sow = True
        res+= score
        num_rolls-=1
    return res if not sow else 1
    # END PROBLEM 1


def boar_brawl(player_score, opponent_score):
    """Return the points scored by rolling 0 dice according to Boar Brawl.

    player_score:     The total score of the current player.
    opponent_score:   The total score of the other player.

    """
    # BEGIN PROBLEM 2


    tens_digit_opp = opponent_score % 100 // 10
    ones_digit_player = player_score % 10
    
    zero_score = 3 * abs(tens_digit_opp - ones_digit_player)
    return zero_score if (zero_score > 1) else 1

    
    # END PROBLEM 2
  

def take_turn(num_rolls, player_score, opponent_score, dice=six_sided):
    """Return the points scored on a turn rolling NUM_ROLLS dice when the
    player has PLAYER_SCORE points and the opponent has OPPONENT_SCORE points.

    num_rolls:       The number of dice rolls that will be made.
    player_score:    The total score of the current player.
    opponent_score:  The total score of the other player.
    dice:            A function that simulates a single dice roll outcome.
    """
    # Leave these assert statements here; they help check for errors.
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls >= 0, 'Cannot roll a negative number of dice in take_turn.'
    assert num_rolls <= 10, 'Cannot roll more than 10 dice.'
    # BEGIN PROBLEM 3
    
    return boar_brawl(player_score, opponent_score) if num_rolls == 0 else roll_dice(num_rolls, dice)
    
    # END PROBLEM 3


def simple_update(num_rolls, player_score, opponent_score, dice=six_sided):
    """Return the total score of a player who starts their turn with
    PLAYER_SCORE and then rolls NUM_ROLLS DICE, ignoring Sus Fuss.
    """
    score = player_score + take_turn(num_rolls, player_score, opponent_score, dice)
    return score

def is_prime(n):
    """Return whether N is prime."""
    if n == 1:
        return False
    k = 2
    while k < n:
        if n % k == 0:
            return False
        k += 1
    return True

def num_factors(n):
    """Return the number of factors of N, including 1 and N itself."""
    # BEGIN PROBLEM 4
   
    i = n
    cnt = 0
    while i > 0:
        if n % i == 0:
            cnt+=1
        i-=1
    return cnt
        
    # END PROBLEM 4

def sus_points(score):
    """Return the new score of a player taking into account the Sus Fuss rule."""
    # BEGIN PROBLEM 4
   
    def next_prime(num):
        candidate = num + 1
        while True:
            if is_prime(candidate):
                return candidate
            candidate+=1


    factor_cnt = num_factors(score)
    if factor_cnt in [3,4]:
        return next_prime(score)
    return score
    # END PROBLEM 4

    

def sus_update(num_rolls, player_score, opponent_score, dice=six_sided):
    """Return the total score of a player who starts their turn with
    PLAYER_SCORE and then rolls NUM_ROLLS DICE, *including* Sus Fuss.
    """
    # BEGIN PROBLEM 4

    

    
    score = player_score + take_turn(num_rolls, player_score, opponent_score, dice)
    return sus_points(score)
       
    
    # END PROBLEM 4


def always_roll_5(score, opponent_score):
    """A strategy of always rolling 5 dice, regardless of the player's score or
    the opponent's score.
    """
    return 5


def play(strategy0, strategy1, update,
         score0=0, score1=0, dice=six_sided, goal=GOAL):
    """Simulate a game and return the final scores of both players, with
    Player 0's score first and Player 1's score second.

    E.g., play(always_roll_5, always_roll_5, sus_update) simulates a game in
    which both players always choose to roll 5 dice on every turn and the Sus
    Fuss rule is in effect.

    A strategy function, such as always_roll_5, takes the current player's
    score and their opponent's score and returns the number of dice the current
    player chooses to roll.

    An update function, such as sus_update or simple_update, takes the number
    of dice to roll, the current player's score, the opponent's score, and the
    dice function used to simulate rolling dice. It returns the updated score
    of the current player after they take their turn.

    strategy0: The strategy for player0.
    strategy1: The strategy for player1.
    update:    The update function (used for both players).
    score0:    Starting score for Player 0
    score1:    Starting score for Player 1
    dice:      A function of zero arguments that simulates a dice roll.
    goal:      The game ends and someone wins when this score is reached.
    """
    who = 0  # Who is about to take a turn, 0 (first) or 1 (second)
    # BEGIN PROBLEM 5
    "*** YOUR CODE HERE ***"

    while True:
        if who == 0:
            score0 = update(strategy0(score0, score1), score0, score1, dice)
            if score0 >= goal:
                break
            who = 1
        if who == 1:
            score1 = update(strategy1(score1, score0), score1, score0, dice)
            if score1 >= goal:
                break
            who = 0

    # END PROBLEM 5


    return score0, score1


#######################
# Phase 2: Strategies #
#######################


def always_roll(n):
    """Return a player strategy that always rolls N dice.

    A player strategy is a function that takes two total scores as arguments
    (the current player's score, and the opponent's score), and returns a
    number of dice that the current player will roll this turn.

    >>> strategy = always_roll(3)
    >>> strategy(0, 0)
    3
    >>> strategy(99, 99)
    3
    """
    assert n >= 0 and n <= 10
    # BEGIN PROBLEM 6
    def strategy(player_score,opp_score):
        return n
    "*** YOUR CODE HERE ***"
    return strategy


    # END PROBLEM 6


def catch_up(score, opponent_score):
    """A player strategy that always rolls 5 dice unless the opponent
    has a higher score, in which case 6 dice are rolled.

    >>> catch_up(9, 4)
    5
    >>> strategy(17, 18)
    6
    """
    if score < opponent_score:
        return 6  # Roll one more to catch up
    else:
        return 5


def is_always_roll(strategy, goal=GOAL):
    """Return whether STRATEGY always chooses the same number of dice to roll
    given a game that goes to GOAL points.

    >>> is_always_roll(always_roll_5)
    True
    >>> is_always_roll(always_roll(3))
    True
    >>> is_always_roll(catch_up)
    False
    """
    # BEGIN PROBLEM 7
    "*** YOUR CODE HERE ***"

    reference = strategy(0,0)
    for player_score in range(goal):
        for opp_score in range(goal):
            if strategy(player_score, opp_score) != reference:
                return False
    return True








    # END PROBLEM 7


def make_averaged(original_function, times_called=1000):
    """Return a function that returns the average value of ORIGINAL_FUNCTION
    called TIMES_CALLED times.

    To implement this function, you will have to use *args syntax.

    >>> dice = make_test_dice(4, 2, 5, 1)
    >>> averaged_dice = make_averaged(roll_dice, 40)
    >>> averaged_dice(1, dice)  # The avg of 10 4's, 10 2's, 10 5's, and 10 1's
    3.0
    """
    # BEGIN PROBLEM 8
    def averaged(*args):
        res = 0
        for i in range(times_called):
            res+= original_function(*args)
        return res / times_called
    return averaged
    # END PROBLEM 8



def max_scoring_num_rolls(dice=six_sided, times_called=1000):
    """Return the number of dice (1 to 10) that gives the maximum average score for a turn.
    Assume that the dice always return positive outcomes.

    >>> dice = make_test_dice(1, 6)
    >>> max_scoring_num_rolls(dice)
    1
    """
    # BEGIN PROBLEM 9
    res = 0
    res_score = 0
    average_roll_dice = make_averaged(roll_dice,times_called)
    for num_rolls in range(1,11):
        candidate = average_roll_dice(num_rolls,dice )
        if candidate > res_score:
            res_score = candidate
            res = num_rolls
    return res
    # END PROBLEM 9


def winner(strategy0, strategy1):
    """Return 0 if strategy0 wins against strategy1, and 1 otherwise."""
    score0, score1 = play(strategy0, strategy1, sus_update)
    if score0 > score1:
        return 0
    else:
        return 1


def average_win_rate(strategy, baseline=always_roll(6)):
    """Return the average win rate of STRATEGY against BASELINE. Averages the
    winrate when starting the game as player 0 and as player 1.
    """
    win_rate_as_player_0 = 1 - make_averaged(winner)(strategy, baseline)
    win_rate_as_player_1 = make_averaged(winner)(baseline, strategy)

    return (win_rate_as_player_0 + win_rate_as_player_1) / 2


def run_experiments():
    """Run a series of strategy experiments and report results."""
    six_sided_max = max_scoring_num_rolls(six_sided)
    print('Max scoring num rolls for six-sided dice:', six_sided_max)

    print('always_roll(6) win rate:', average_win_rate(always_roll(6))) # near 0.5
    print('catch_up win rate:', average_win_rate(catch_up))
    print('always_roll(3) win rate:', average_win_rate(always_roll(3)))
    print('always_roll(8) win rate:', average_win_rate(always_roll(8)))

    print('boar_strategy win rate:', average_win_rate(boar_strategy))
    print('sus_strategy win rate:', average_win_rate(sus_strategy))
    print('final_strategy win rate:', average_win_rate(final_strategy))
    "*** You may add additional experiments as you wish ***"



def boar_strategy(score, opponent_score, threshold=11, num_rolls=6):
    """This strategy returns 0 dice if Boar Brawl gives at least THRESHOLD
    points, and returns NUM_ROLLS otherwise. Ignore score and Sus Fuss.
    """
    # BEGIN PROBLEM 10
    return num_rolls  # Remove this line once implemented.
    # END PROBLEM 10


def sus_strategy(score, opponent_score, threshold=11, num_rolls=6):
    """This strategy returns 0 dice when your score would increase by at least threshold."""
    # BEGIN PROBLEM 11
    return num_rolls  # Remove this line once implemented.
    # END PROBLEM 11


def final_strategy(score, opponent_score):
    """Write a brief description of your final strategy.

    *** YOUR DESCRIPTION HERE ***
    """
    # BEGIN PROBLEM 12
    return 6  # Remove this line once implemented.
    # END PROBLEM 12


##########################
# Command Line Interface #
##########################

# NOTE: The function in this section does not need to be changed. It uses
# features of Python not yet covered in the course.

@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions."""
    import argparse
    parser = argparse.ArgumentParser(description="Play Hog")
    parser.add_argument('--run_experiments', '-r', action='store_true',
                        help='Runs strategy experiments')

    args = parser.parse_args()

    if args.run_experiments:
        run_experiments()


if __name__ == '__main__':
        from dice import make_test_dice

        # ---- Problem 9: max_scoring_num_rolls ----
        # Finds the value of num_rolls in 1..10 whose roll_dice average is
        # highest. On ties, return the LOWER num_rolls.
        print("Problem 9: max_scoring_num_rolls")

        # Test 1: dice always returns 3 (no 1s, no Sow Sad).
        # avg(n) = 3n, strictly increasing; max at n=10.
        dice_3 = make_test_dice(3)
        print(max_scoring_num_rolls(dice_3, times_called=1000))          # expect: 10

        # Test 2: dice always returns 2 (no Sow Sad).
        # avg(n) = 2n, strictly increasing; max at n=10.
        dice_2 = make_test_dice(2)
        print(max_scoring_num_rolls(dice_2, times_called=1000))          # expect: 10

        # Test 3: dice always returns 1 (EVERY n triggers Sow Sad → 1).
        # All averages tie at 1.0. On a tie, return the LOWEST num_rolls.
        dice_1 = make_test_dice(1)
        print(max_scoring_num_rolls(dice_1, times_called=1000))          # expect: 1

        # Test 4: dice alternates 1, 2, 1, 2, ...
        # n=1 avg = 1.5 (rolls of 1 -> 1, rolls of 2 -> 2, alternating).
        # n>=2 every call contains a 1 -> Sow Sad -> 1. So n=1 wins.
        dice_12 = make_test_dice(1, 2)
        print(max_scoring_num_rolls(dice_12, times_called=1000))         # expect: 1

        # Test 5: dice cycle (1, 2, 2, 2, 2, 2, 2, 2) length 8.
        # n=4 averages 4.5 (best); n=8 always has a 1 -> avg 1.
        dice_one_seven = make_test_dice(1, 2, 2, 2, 2, 2, 2, 2)
        print(max_scoring_num_rolls(dice_one_seven, times_called=1000))  # expect: 4

        # Test 6: dice = 100 twos followed by 100 ones. times_called=1.
        # First 55 positions consumed by n=1..10 sum-of-1..10=55, all 2s.
        # Answer: n=10 (roll_dice returns 20, the highest sample).
        dice_100_2s = make_test_dice(*([2] * 100 + [1] * 100))
        print(max_scoring_num_rolls(dice_100_2s, times_called=1))        # expect: 10

        # Test 7: dice sweeps 1..5, times_called=1000.
        # Best n is 3 (avg 5.8 across the 5-length cycle).
        dice_sweep5 = make_test_dice(1, 2, 3, 4, 5)
        print(max_scoring_num_rolls(dice_sweep5, times_called=1000))     # expect: 3

        # Test 8: dice sweeps 6,5,4,3,2,1; times_called=1.
        # n=4 gives one sample 6+5+4+3=18 (no 1), which is the max.
        # (n=5,6,... all hit the 1 in the cycle and Sow Sad -> 1.)
        dice_sweep6 = make_test_dice(6, 5, 4, 3, 2, 1)
        print(max_scoring_num_rolls(dice_sweep6, times_called=1))        # expect: 4

        # Test 9: dice = 55 twos then (1, 2) repeating; times_called=1.
        # n=1..10 consume positions 0..54, all 2s. Best is n=10, score 20.
        # Important: this test verifies you don't sample extra dice beyond
        # what times_called dictates (i.e. no peeking into the 1s region).
        dice_55_2s = make_test_dice(*([2] * 55 + [1, 2] * 500))
        print(max_scoring_num_rolls(dice_55_2s, times_called=1))         # expect: 10
