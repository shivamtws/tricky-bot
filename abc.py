import os
import openai
# from openai import OpenAI

# client = OpenAI()
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

OPENAI_KEY = os.getenv('OPENAI_KEY')
prompt='what is python ?'
openai.api_key = OPENAI_KEY
# from openai import OpenAI
# client = OpenAI(api_key=OPENAI_KEY)

# response = client.completions.create(
#   model="gpt-3.5-turbo-instruct",
#   prompt="what is python ?",
#   max_token = 2000
# )
response = openai.Completion.create(
                    model='text-davinci-003',
                    prompt=prompt,
                    n=1,
                    stop=None,
                    max_tokens = 2000,
                    api_key=OPENAI_KEY
                )
description = response.choices[0].text.strip()
print(description)