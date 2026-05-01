from nltk.chat.util import Chat, reflections

pairs = [

    # Greetings
    [r"hi|hello|hey", ["Hi! I'm Ramsay your Student Meal Planner Bot 🍲"]],
    [r"how are you", ["I'm good! Ready to help you plan affordable meals"]],

    # General Help
    [r".*help.*", ["I can suggest cheap meals, meal plans, and student friendly food ideas."]],

    # Cheap Meals
    [r"cheap meals|budget meals", [
        "You can try garri and groundnut, rice and beans, or noodles with vegetables.",
        "Budget meals include yam and palm oil, pap and akara, or beans porridge."
    ]],

    # Breakfast
    [r"breakfast", [
        "Try pap and akara, bread and tea, or custard with milk.",
        "Simple breakfast: bread and butter or soaked garri."
    ]],

    # Lunch
    [r"lunch", [
        "You can eat rice and stew, beans, or noodles with vegetables.",
        "Try yam porridge or jollof rice for lunch."
    ]],

    # Dinner
    [r"dinner", [
        "Light dinner ideas: pap, noodles, or beans.",
        "You can try rice and vegetables or yam."
    ]],

    # Weekly Plan
    [r"meal plan|weekly plan", [
        "Monday: Rice\nTuesday: Beans\nWednesday: Noodles\nThursday: Yam\nFriday: Jollof Rice\nWeekend: Flexible meals"
    ]],

    # No Money
    [r"no money|broke", [
        "You can take garri and groundnut or soak garri.",
        "Very low budget? Try pap or plain noodles."
    ]],

    # Protein Options
    [r"protein", [
        "Beans, groundnuts, eggs and milk are good affordable protein sources.",
        "Try beans or moi moi for protein."
    ]],

    # Snacks
    [r"snacks", [
        "You can snack on groundnuts, peanuts, chin chin, or fruits.",
        "Try popcorn or biscuits."
    ]],

    # Cooking Tips
    [r"quick food|fast meal", [
        "Noodles and egg-free sauces are very quick.",
        "You can prepare garri instantly."
    ]],

    # Healthy Eating
    [r"healthy food", [
        "Try beans, vegetables, and fruits for balanced meals.",
        "Avoid too much oil and eat more vegetables."
    ]],

    # No Eggs (Important for you)
    [r"egg", [
        "If you don't eat eggs, you can use beans, fish, or milk as alternatives."
    ]],

    # Thanks
    [r"thank you|thanks", ["You're welcome😊", "Glad I could help!"]],

    # Goodbye
    [r"bye", ["Goodbye! Eat well and stay healthy 🍲"]],

    # Catch-all
    [r"(.*)", ["Hmm, I don't have that yet. Try asking about meals, budget food, or meal plans"]]

]

chatbot = Chat(pairs, reflections)

def get_response(user_input):
    response = chatbot.respond(user_input)
    if response is None:
        return "Sorry, I didn't understand that."
    return response
