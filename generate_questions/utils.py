import requests

from openai import OpenAI
client = OpenAI()


def get_article(article_name: str) -> dict:
    # takes the name of a wikipedia article and returns the content as a string
    url = f"https://en.wikipedia.org/w/api.php?action=query&exlimit=1&explaintext=1&exsectionformat=plain&prop=extracts&titles={article_name}&format=json"
    response = requests.get(url).json()
    # assume the first article is the right one
    article_number = list(response['query']['pages'].keys())[0]
    article_data = response['query']['pages'][article_number]
    return article_data


def get_questions(number: int, article_name: str, extract: str, difficulty: str):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "You are an assistant that creates multiple choice questions based on a text. The questions should have three wrong answers and one correct answer."
            },
            {
                "role": "user",
                "content": f"Plesae write {number} {difficulty} question(s) about {article_name}. Note which answer is correct and noting what paragraph the answer came from by putting at the end of the quesiton 'Correct:  <letter>, found in paragraph <number>'.  Use this article: {extract}"}
        ],
        temperature=1,
        max_tokens=512,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    return completion.choices[0].message.content


if __name__ == "__main__":
    # get the article text
    article_name = 'Prince_(musician)'
    article_data = get_article(article_name)

    extract = article_data['extract'][:2000]  # don't send too many tokens
    title = article_data['title']
    number_of_questions = 3
    difficulty = "hard"
  
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "You are an assistant that creates multiple choice questions based on a text. The questions should have three wrong answers and one correct answer."
            },
            {
                "role": "user",
                "content": f"Plesae write {number_of_questions} {difficulty} question(s) about {article_name}. Note which answer is correct and noting what paragraph the answer came from by putting at the end of the quesiton 'Correct:  <letter>, paragraph <number>'.  Use this article: {extract}"}
        ],
        temperature=1,
        max_tokens=512,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    print(completion.choices[0].message.content)
    print('hi')
