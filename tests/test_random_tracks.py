from unittest.mock import patch

from routes import obter_musicas_aleatorias


@patch('routes.requests.get')
def test_obter_musicas_aleatorias_retorna_musicas_validas(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        'data': [
            {
                'id': 'track-1',
                'title': 'Musica 1',
                'user': {'name': 'Artista 1'},
                'artwork': {'150x150': 'https://img-1.com'}
            },
            {
                'id': 'track-2',
                'title': 'Musica 2',
                'user': {'name': 'Artista 2'},
                'artwork': {'150x150': 'https://img-2.com'}
            },
            {
                'id': 'track-3',
                'title': 'Musica 3',
                'user': {'name': 'Artista 3'},
                'artwork': {'150x150': 'https://img-3.com'}
            },
            {
                'id': 'track-4',
                'title': 'Musica 4',
                'user': {'name': 'Artista 4'},
                'artwork': {'150x150': 'https://img-4.com'}
            },
        ]
    }

    resultados = obter_musicas_aleatorias()

    assert isinstance(resultados, list)
    assert len(resultados) == 3
    assert all('title' in item for item in resultados)
