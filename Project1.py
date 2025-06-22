#Emoji Mood Responder

mood_responses = {
    "happy": {"emoji": "😊", "message": "Happiness looks good on you!"},
    "sad": {"emoji": "😢", "message": "Every storm runs out of rain. You're not alone."},
    "angry": {"emoji": "😠", "message": "Breathe in calm, breathe out fire. You've got this!"},
    "excited": {"emoji": "🤩", "message": "Your energy is contagious! Keep the vibe going!"},
    "tired": {"emoji": "😴", "message": "You’ve done enough for today. Time to recharge."},
    "nervous": {"emoji": "😬", "message": "It's okay to be nervous — it means you care!"},
    "anxious": {"emoji": "😰", "message": "You’re stronger than your worries. One step at a time."},
    "lonely": {"emoji": "🥺", "message": "You matter. You're never truly alone."},
    "bored": {"emoji": "😐", "message": "Boredom is the start of creativity—do something fun!"},
    "confused": {"emoji": "🤔", "message": "Confusion is just learning in progress. You'll get it!"},
    "grateful": {"emoji": "🙏", "message": "Gratitude brings peace. What a beautiful mindset!"},
    "calm": {"emoji": "😌", "message": "Peaceful minds make powerful thoughts. Stay balanced."},
    "scared": {"emoji": "😨", "message": "Courage doesn’t mean no fear—it means facing it anyway."}
}
user_mood = input("How are you feeling today? ").lower()

if user_mood in mood_responses:
    response = mood_responses[user_mood]
    print(f"{response['emoji']} {response['message']}")
else:
    print("🤔 I’m not sure what that feeling is, but I hope today treats you kindly!")
