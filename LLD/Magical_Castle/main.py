from sources import Game, Player

if __name__ == '__main__':
    magic_castle_game = Game.Game()
    player1 = Player.Player(0)
    player2 = Player.Player(1)

    magic_castle_game.add_player(player1)
    magic_castle_game.add_player(player2)

    magic_castle_game.initialize_from_file("castle1.txt")

    while not magic_castle_game.is_finished():
        magic_castle_game.move()

    players = magic_castle_game.get_players()
    winner, max_points = players[0],players[0].get_diamonds()

    for player in players[1:]:
        if player.get_diamonds() > winner.get_diamonds():
            winner = player

    print("Winner is : ", winner)