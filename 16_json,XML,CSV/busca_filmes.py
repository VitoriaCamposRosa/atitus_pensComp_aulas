import http.client
import json
from typing import Dict, List, Optional

def get_movies(texto_busca: str) -> dict:  
    conn = http.client.HTTPSConnection("search.imdbot.workers.dev")  
    conn.request("GET", f"/?q={texto_busca}")
    response = conn.getresponse()
    response_text = response.read().decode()
    conn.close()
    return json.loads(response_text)

def search_movie(movie_name: dict) -> dict:
    response = get_movies(movie_name)

    if not response.get('results'):
        return None

    first_result = response['results'][0]

    return {
        'title': first_result.get('title', 'Desconhecido'),
        'year': first_result.get('year', 'N/A'),
        'id': first_result.get('id', None)
    }

def format_movie_result(movie_data: Optional[Dict]) -> str:
    if movie_data is None:
        return "Nenhum filme encontrado."
    
    return f"Título: {movie_data['title']}\nAno: {movie_data['year']}\nID: {movie_data['id']}"

def test_search_existing_movie():
    def mock_get_movies(texto_busca: str) -> Dict:
        if texto_busca == "Matrix":
            return {
                "results": [
                    {
                        "title": "The Matrix",
                        "year": "1999",
                        "id": "tt0133093"
                    }
                ]
            }
        return {"results": []}
    
    global get_movies
    original_get_movies = get_movies
    get_movies = mock_get_movies
    
    result = search_movie("Matrix")
    assert result is not None
    assert result['title'] == "The Matrix"
    assert result['year'] == "1999"

    get_movies = original_get_movies

def test_search_non_existing_movie(): 
    def mock_get_movies(texto_busca: str) -> Dict:
        return {"results": []}
    
    global get_movies
    original_get_movies = get_movies
    get_movies = mock_get_movies
    
    result = search_movie("FilmeInexistente123")
    assert result is None
    
    get_movies = original_get_movies

def test_movie_data_structure():
    def mock_get_movies(texto_busca: str) -> Dict: 
        return {
            "results": [
                {
                    "title": "Inception",
                    "year": "2010",
                    "id": "tt1375666"
                }
            ]
        }
    
    global get_movies
    original_get_movies = get_movies
    get_movies = mock_get_movies
    
    result = search_movie("Inception")
    assert isinstance(result, dict)
    assert isinstance(result['title'], str)
    assert isinstance(result['year'], str)
    assert isinstance(result['id'], str)
    
    get_movies = original_get_movies

