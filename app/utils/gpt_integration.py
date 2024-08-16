import os
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("CHATGPT_API_KEY"),
)

def get_word_details(word):
    prompt = f"""Please explain the following about the word '{word}' in Japanese:
    1. The meaning of '{word}'
    2. Two synonyms of '{word}' in English and their nuanced differences from '{word}' (refer to the words in the form of '{word}')
    3. One example sentence using '{word}' in English"""

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a native speaker of both English and Japanese and an excellent English teacher in Japan who teaches Japanese. This time, please explain the following about the word in Japanese.Your response should be in Japanese."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=300,
    )
    
    return response.choices[0].message.content