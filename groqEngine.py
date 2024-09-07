from groq import Groq
import os

api_Key = os.environ.get('GROQ_API_KEY')


def GroqAI(msg):
    client = Groq(api_key=api_Key)
    completion = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[
            {
                "role": "user",
                "content": "{}\n".format(msg)
            }
        ],
        temperature=1,
        max_tokens=1024,
        top_p=1,
        stream=False,
        stop=None,
    )

    return completion.choices[0].message.content
