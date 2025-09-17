from django.shortcuts import render
from .kate import Game
import pickle
import base64

def play_game(request):
    """
    Runs the game simulation and displays the output.
    """
    # Get the game state from the session, or create a new one
    game_state_str = request.session.get('game_state', None)
    if game_state_str:
        game_state = pickle.loads(base64.b64decode(game_state_str))
        game = Game(state=game_state)
    else:
        game = Game()

    # Get the player's action from the form
    player_action = request.POST.get('action', None)
    if player_action:
        game.game_loop_turn(player_action)

    # Save the game state to the session
    game_state = game.get_state()
    request.session['game_state'] = base64.b64encode(pickle.dumps(game_state)).decode('utf-8')

    return render(request, 'game/play.html', {'game': game})
