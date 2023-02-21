# from inspect import signature
from random import randint

from faker import Faker


FAKE = Faker('pt_BR')


def rand_ratio():
    return randint(840, 900), randint(473, 573)


def cria_aplicacao():
    return {
        'titulo': FAKE.sentence(nb_words=2),
        'descricao': FAKE.sentence(nb_words=12),
        'nr_usuarios': randint(10000, 149999),
        'data_estreia': FAKE.date_time(),
        'desenvolvedor': {
            'nome': FAKE.first_name(),
            'sobrenome': FAKE.last_name(),
        },
        'categoria': {
            'name': FAKE.word()
        },
        'foto': {
            'url': 'https://loremflickr.com/%s/%s/technology,website' % rand_ratio(),
        }
    }


if __name__ == '__main__':
    from pprint import pprint
    pprint(cria_aplicacao())
