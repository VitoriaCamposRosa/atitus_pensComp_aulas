import http.client
import json
import html
import random

def get_questions(amount: int = 10, difficulty: str = 'easy') -> dict:
    conn = http.client.HTTPSConnection("opentdb.com")
    conn.request("GET", f"/api.php?amount={amount}&difficulty={difficulty}&type=multiple")
    response = conn.getresponse()
    response_text = response.read().decode()
    conn.close()
    return json.loads(response_text)


def parse_text(html_string: str) -> str:

    # Convert HTML entity to regular single quote
    return html.unescape(html_string)  

def shuffle_answers(question: dict) -> list:

    answers = question["incorrect_answers"] + [question["correct_answer"]]
    random.shuffle(answers)
    return answers
 
def test_shuffle_answers():
    question = {
        "correct_answer": "Paris",
        "incorrect_answers": ["London", "Berlin", "Madrid"]
    }
    answers = shuffle_answers(question)
    assert len(answers) == 4
    assert "Paris" in answers
    assert set(answers) == {"Paris", "London", "Berlin", "Madrid"} 

def check_answer(question: dict, user_answer: str) -> bool:
    return user_answer == question["correct_answer"] 

def test_check_answer():
    question = {
        "correct_answer": "Paris",
        "incorrect_answers": ["London", "Berlin"]
    }
    assert check_answer(question, "Paris") is True
    assert check_answer(question, "London") is False

def start_quiz():
    questions = get_questions(amount=3, difficulty="easy")["results"]
    score = 0

    for question in questions:
        question["question"] = parse_text(question["question"])
        question["correct_answer"] = parse_text(question["correct_answer"])
        question["incorrect_answers"] = [parse_text(ans) for ans in question["incorrect_answers"]]

        answers = shuffle_answers(question)
        print(f"\nPergunta: {question['question']}")
        print("Alternativas:", answers)

        simulated_answer = random.choice(answers)
        print(f"Resposta simulada: {simulated_answer}")

        if check_answer(question, simulated_answer):
            score += 1
            print("✅ Correto!")
        else:
            print(f"❌ Errado! Resposta correta: {question['correct_answer']}")

    print(f"\nPontuação final: {score}/3")

start_quiz()
