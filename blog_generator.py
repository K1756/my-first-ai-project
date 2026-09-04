from openai import OpenAI
from dotenv import dotenv_values

config = dotenv_values(".env")
client = OpenAI(api_key=config['API_KEY'])
def generate_blog(paragraph_topic):
  response = client.responses.create(
    model = "gpt-5.6-luna",
    input=f"Write a paragraph about the following topic: {paragraph_topic}"
  )

  return response.output_text




keep_writing = True

while keep_writing:
  answer = input('Write a paragraph? Y for yes, anything else for no. ')
  if answer == "Y":
    paragraph_topic = input('What should this paragraph talk about? ')
    print(generate_blog(paragraph_topic))
  else:
    keep_writing = False

