import random


def roll():
    value = random.randint(1, 6)
    return value


def main():
    while True:
        players = input('Enter number of players (2-4): ')
        if players.isdigit() and int(players) in range(2, 5):
            players = int(players)
            break
        else:
            print("Error, please try again")

    max_score = 100
    players_score = [0 for _ in range(players)]
    round_counter = 1

    while max(players_score) < max_score:

        print(f'---Round {round_counter}--- ')

        for player in range(players):

            is_playing = input(f'Player {player+1}, would you want to play? (y/n): ')
            if is_playing.lower() != 'y':
                print(f'This round, player {player+1} got 0 points')
                continue

            round_score = 0

            while True:
                score = roll()
                if score == 1:
                    round_score = 0
                    print('You got 1. End turn!')
                    break
                else:
                    print(f'You got {score} points')
                    round_score += score

                    if input('Keep playing? (y/n): ').lower() != 'y': break

            print(f'This round, player {player+1} got {round_score} points\n')

            players_score[player] += round_score  # Update

        print('Round result:')
        for idx, current_score in enumerate(players_score):
            print(f'Player {idx+1}: {current_score} points')

        print('')

        round_counter += 1

    print(f'Player {players_score.index(max(players_score))+1} wins')


if __name__ == '__main__':
    main()
