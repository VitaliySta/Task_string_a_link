from main import (
    exc_input,
    iter_string,
    result,
    main
)


TEST_STRINGS = {
    'https://google.com',
    'строка',
    '123',
    'https://ya.ru'
}


def test_main_zero(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 0)
    main()
    assert result == {}


def test_iter_string():
    iter_string(TEST_STRINGS)
    assert result == {
        'https://google.com': {'GET': 200, 'HEAD': 301},
        'https://ya.ru': {
            'GET': 200,
            'HEAD': 302,
            'POST': 200,
            'PUT': 200,
            'DELETE': 200,
            'OPTIONS': 200
        }
    }


def test_exc_input_try(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 5)
    res = exc_input('test')
    assert res == 5
