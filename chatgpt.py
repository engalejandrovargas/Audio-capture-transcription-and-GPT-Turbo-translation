from openai import OpenAI


client = OpenAI()

def translate_to_english(japanese_transcript):
    response = client.chat.completions.create(
        model="gpt-4-1106-preview",
        messages=[
            {"role": "system", "content": "You summarize in English"},
            {"role": "user", "content": japanese_transcript}
        ]
    )

    english_summary = response.choices[0].message.content
    return english_summary

print(translate_to_english("むかし、 むかし、 ある ところ に おじいさん と おばあさん が いました。 "))