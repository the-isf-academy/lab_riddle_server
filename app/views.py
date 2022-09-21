from banjo.urls import route_get, route_post
from banjo.http import BadRequest
from .models import Riddle


@route_get('riddles/all')
def riddles_all(params):
    riddles = []

    for riddle in Riddle.objects.all():
        riddles.append(riddle.to_dict_answerless())

    return {'riddles':riddles}

@route_post('riddles/guess',args={'id':int,'guess':str})
def guess_answer(params):
    if 'guess' not in params or 'id' not in params:
        raise BadRequest('incorrect request')

    guess = params['guess']
    id = params['id']
    riddle = Riddle.objects.get(id=id)

    guess_result = riddle.check_guess(guess)

    if guess_result == True:
        return {
            'correct': guess_result,
            'guess': guess,
            'riddle':riddle.to_dict()
            }
    else:
        return {
            'correct': guess_result,
            'guess': guess,
            'riddle':riddle.to_dict_answerless()
            }


