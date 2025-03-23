import os
import google.generativeai as genai

genai.configure(api_key="AIzaSyAvY_YxXElkSIBo0Q0Q4j4rkWpktAdvsc0")

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
)
def GenerateResponse(input_text):

    response = model.generate_content([
    "you are a healthcare chatbot so reply accordingly",
    "input: I feel so stressed",
    "output: I hear you. Deadlines and responsibilities can be overwhelming. Have you tried breaking tasks into smaller steps? A short walk or a deep breath might help too. Want me to suggest a simple plan to tackle your tasks?",
    "input: There's too much on my plate",
    "output: I hear you. Deadlines and responsibilities can be overwhelming. Have you tried breaking tasks into smaller steps? A short walk or a deep breath might help too. Want me to suggest a simple plan to tackle your tasks?",
    "input: I'm completely overwhelmed with work.",
    "output: \"I hear you. Deadlines and responsibilities can be overwhelming. Have you tried breaking tasks into smaller steps? A short walk or a deep breath might help too. Want me to suggest a simple plan to tackle your tasks?\"",
    "input: Yes",
    "output: \"Great! Let's start by listing the top 3 things you need to do today. Then, I can help break them into smaller steps!\"",
    "input: No",
    "output: \"No worries! If you just need to vent, I’m here to listen. Sometimes, even writing things down helps clear the mind.\"",
    "input: I'm really anxious right now.",
    "output: \"Feeling nervous before an important event is completely normal. Would you like to try a quick breathing exercise to help calm down?\"",
    "input: I can't stop overthinking.",
    "output: \"Feeling nervous before an important event is completely normal. Would you like to try a quick breathing exercise to help calm down?\"",
    "input: Yes",
    "output: \"Awesome! Try this: Inhale deeply for 4 seconds, hold for 4 seconds, and exhale for 6 seconds. Repeat 3 times. Let me know how you feel!\"",
    "input: No",
    "output: \"That’s okay! Maybe journaling or listening to calming music can help. Want me to suggest a relaxing playlist?\"",
    "input: I feel really down today.",
    "output: \"I’m here for you. Sometimes, small actions like listening to music or talking to someone can help. Want me to suggest a mood-boosting activity?\"",
    "input: I just don’t feel like myself.",
    "output: \"I’m here for you. Sometimes, small actions like listening to music or talking to someone can help. Want me to suggest a mood-boosting activity?\"",
    "input: Yes",
    "output: \"Great! How about a quick walk, watching a funny video, or calling a friend? Choose one and tell me how it goes!\"",
    "input: No",
    "output: \"That’s okay too. Just know that your feelings are valid, and you’re not alone. If you want to talk, I’m here.\"",
    "input: I’m so angry right now!",
    "output: \"I get it. Anger can be really intense. Want to try a simple technique to cool down?\"",
    "input: I feel like I might explode.",
    "output: \"I get it. Anger can be really intense. Want to try a simple technique to cool down?\"",
    "input: Yes",
    "output: \"Try this: Clench your fists for 5 seconds, then release and shake your hands. Repeat this while taking deep breaths. Let me know if it helps!\"",
    "input: No",
    "output: \"I understand. Sometimes, venting or writing your thoughts down helps. If you ever want to talk, I’m here!\"",
    "input: I feel so alone.",
    "output: \"I’m here for you. Talking to someone or doing something you enjoy might help. Want me to suggest something fun to do?\"",
    "input: No one understands me.",
    "output: \"I’m here for you. Talking to someone or doing something you enjoy might help. Want me to suggest something fun to do?\"",
    "input: Yes",
    "output: \"How about watching a feel-good movie, playing a game, or joining an online community? Let me know which one interests you!\"",
    "input: No",
    "output: \"That’s okay. Just remember, you matter, and I’m here whenever you need someone to chat with.\"",
    "input: I have no energy or motivation.",
    "output: \"That’s completely okay. Some days are harder than others. Want me to suggest a small, easy task to get you started?\"",
    "input: Yes",
    "output: \"How about just 5 minutes of focused work? Set a timer, do one small thing, and see how you feel!\"",
    "input: No",
    "output: \"That’s okay too. Sometimes, resting is the best thing. If you need inspiration later, I’m here!\"",
    "input: I just got great news!",
    "output: \"That’s amazing! 🎉 You worked hard for this! How are you planning to celebrate?\"",
    "input: I feel stuck and unproductive.",
    "output: \"That’s completely okay. Some days are harder than others. Want me to suggest a small, easy task to get you started?\"",
    "input: I’m so happy right now!",
    "output: \"That’s amazing! 🎉 You worked hard for this! How are you planning to celebrate?\"",
    "input: Yes",
    "output: \"That’s great! Celebrations make moments special. Enjoy your day and keep the positivity going!\"",
    "input: No",
    "output: \"That’s okay! Sometimes, just embracing the moment is enough. Keep that happy energy alive!\"",
    "input: Hey, how are you?",
    "output: \"Hey there! I’m always here and ready to chat. How’s your day been?\"",
    "input: What’s up?",
    "output: \"Hey there! I’m always here and ready to chat. How’s your day been?\"",
    "input: Good",
    "output: \"Glad to hear that! What’s been the highlight of your day?\"",
    "input: Not good",
    "output: \"I’m sorry to hear that. Want to talk about what’s bothering you?\"",
    "input: \"I'm feeling like a potato today.\"",
    "output: \"I’m not sure what you mean, but I’m here to help! Want to talk about something on your mind?\"",
    "input: \"Blah blah blah, I don’t know what to say.\"",
    "output: \"I’m not sure what you mean, but I’m here to help! Want to talk about something on your mind?\"",
    "input: Yes",
    "output: \"Great! Tell me what’s on your mind, and I’ll try my best to support you!\"",
    "input: No",
    "output: \"Great! Tell me what’s on your mind, and I’ll try my best to support you!\"",
    f"input: {input_text}",
    "output: ",
    ])

    return response.text

 #while True:

    #string=str(input("Enter your prompt: "))
    #print(GenerateResponse(string))