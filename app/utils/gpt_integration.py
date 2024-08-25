import os
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("CHATGPT_API_KEY"),
)

"""
    コミュニケーションのきっかけになるような項目が良いかも

    - 話しかけてほしい指数（かまちょ）
    - 天然指数
    - イベント好き（飲み好き）
    - アウトドア，インドア
    - 遊びたい欲
    - 素敵度（高めに設定）
    - 天才指数
    - おしゃべり度
    - 彼氏感，彼女感
    - 母性度合い
    - ネジのハズレ度合い，ぶっ飛び度合い
    - カリスマ性
    - インフルエンス力
    - 頭の回転速度
"""

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