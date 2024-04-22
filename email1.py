import base64
import vertexai
from vertexai.generative_models import GenerativeModel, Part
import vertexai.preview.generative_models as generative_models



def multiturn_generate_content(prompt,temperature):
  print("Temperature is :", temperature)
  generation_config=setTemperature(temperature)
  print("Prompt: ", prompt)
  vertexai.init(project="starlit-zoo-420014", location="asia-south1")
  model = GenerativeModel(
    "gemini-1.0-pro-001",
  )
  chat = model.start_chat()

  GenerationResponse = chat.send_message(
      [prompt],
      generation_config=generation_config,
      safety_settings=safety_settings
  )

  #print(GenerationResponse.text)
  prompt = GenerationResponse.text + ". Please send the response in HTML format."
  return prompt

def setTemperature(temperature):

  generation_config = {
    "max_output_tokens": 2048,
    "temperature": float(temperature),
    "top_p": 1,
  }
  return generation_config

safety_settings = {
    generative_models.HarmCategory.HARM_CATEGORY_HATE_SPEECH: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
    generative_models.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
    generative_models.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
    generative_models.HarmCategory.HARM_CATEGORY_HARASSMENT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
}


#value = """can you prepare an e-mail for webinar on Generative AI on Sunday 14th April at 9 am. The target audience is anyone who is interested in learning Generative AI features. e-mail should contain text and images."""
#multiturn_generate_content(value)

