from nltk.chat.util import Chat, reflections

pairs = [
    [r"hi|hello|hey", ["Hello! I'm Kira the Cybersecurity departmentchatbot."]],

    [r"what is your name?",
     ["I am Kira and I can be your friend.", "You can call me Kira."]],
    
    [r".*help.*", ["I can assist you with school-related questions."]],
    
    [r"who is the hod", ["The HOD is Prof. Engr O.J. Onojo."]],

    [r"what is cybersecurity", ["Cybersecurity involves protecting systems, networks, and data from cyber attacks."]],

    [r"why study cybersecurity", ["Cybersecurity is important for protecting digital information and systems."]],

    [r"courses in cybersecurity", ["Courses include network security, ethical hacking, cryptography and many others."]], 

    [r"how are you?",
     ["I'm functioning perfectly!", "All systems are running well."]],
    
    [r"exam timetable", ["Check the SUG notice board for the exam timetable towards the end of semester."]],

    [r"results", ["Results are usually released on the school portal or through your course adviser."]],

    [r"hostel", ["Hostel allocation is handled by the student affairs division."]],

    [r"library", ["The library is open during school hours (refer to handbook) for study and research."]],

    [r"wifi|internet", ["Campus WiFi is available in designated areas."]],

    [r"gpa|cgpa", ["Your GPA is calculated based on your course grades."]],

    [r"where is the research center", ["The research center is located in SICT faculty."]],
    
    [r" how do I register courses", ["You can register courses on the school portal."]],

    [r"what is hacking", ["Hacking is the act of exploiting systems, either ethically or maliciously."]],

    [r"ethical hacking", ["Ethical hacking involves testing systems to find vulnerabilities legally."]],

    [r"malware", ["Malware is malicious software designed to harm systems."]],

    [r"phishing", ["Phishing is a cyber attack that tricks users into revealing sensitive information."]],

    [r"firewall", ["A firewall protects networks by filtering incoming and outgoing traffic."]],

    [r"thank you|thanks", ["You're welcome!", "Glad I could help!"]],

    
    [r"bye", ["Goodbye! See you later."]]
]

chatbot = Chat(pairs, reflections)

def get_response(user_input):
    response = chatbot.respond(user_input)
    if response is None:
        return "Sorry, I don't understand that yet."
    return response
