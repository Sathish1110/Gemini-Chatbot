import google.generativeai as ai

API_KEY="AIzaSyBdq7Ca4BioiVZFjLseDvYJ_qu3hgccIAY"
ai.configure(api_key=API_KEY)
mod=ai.GenerativeModel("gemini-pro")
chat=mod.start_chat()
while True:
    user_input=input("You: ")
    if user_input.lower()=="exit":
        print("Bot: Goodbye!")
        break
    response=chat.send_message(user_input)
    print("Bot: "+response.text)