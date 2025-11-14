# EduConnect Final Improved Version
import pandas as pd
import os
import datetime
import random

# Get the directory where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, 'teachers.csv')
session_path = os.path.join(script_dir, 'user_sessions.txt')

# Load teachers data
teachers_df = pd.read_csv(csv_path)
teachers_df.columns = teachers_df.columns.str.lower()

print("Hello, Welcome to EduConnect!")
print("We are excited to help you connect with tutors and students.")
print("Help us provide you with the best experience by answering a few questions.\n")

# User info
name = input("What is your name? ")
age = input("How old are you? ")

while True:
    try:
        age = int(age)
        if age <= 0:
            print("Please enter a valid positive age.")
            age = input("How old are you? ")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter a number for your age.")
        age = input("How old are you? ")

# Email validation
while True:
    email = input("What is your email address? ")
    if "@" in email and "." in email:
        print("Thank you! Your email has been recorded:", email)
        break
    else:
        print("Invalid email. Please enter a valid email address.")

# Subject selection
valid_subjects = {"math", "biology", "history"}
subject = input("\nWhat subject do you need help with? Math, Biology or History? ").strip().lower()
while subject not in valid_subjects:
    subject = input("Invalid subject. Please enter Math, Biology or History: ").strip().lower()

# Show available teachers
print(f"\nAvailable teachers for {subject.title()}:")
available_teachers = teachers_df[teachers_df['subject'].str.lower() == subject]
if not available_teachers.empty:
    for _, teacher in available_teachers.iterrows():
        print(f"Teacher: {teacher['name']}")
        print(f"Contact: {teacher['contact']}")
        print("-" * 30)
else:
    print(f"Sorry, no teachers are currently available for {subject.title()}.")

# Create session record
session_data = {
    "name": name,
    "age": age,
    "email": email,
    "subject": subject.title(),
    "topics_visited": [],
    "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
}

def save_session(data):
    """Save session data to a text file."""
    with open(session_path, "a", encoding="utf-8") as f:
        f.write(f"\n--- New Session ({data['timestamp']}) ---\n")
        f.write(f"Name: {data['name']}\nAge: {data['age']}\nEmail: {data['email']}\nSubject: {data['subject']}\n")
        f.write("Topics visited:\n")
        for t in data["topics_visited"]:
            f.write(f" - {t}\n")
        f.write("------------------------------\n")

# MATH MENU 
if subject == "math":
    topics = [
        "Derivatives",
        "Limits",
        "Trig Identities",
        "Basic Trigonometry",
        "Power Rules",
        "Tips",
        "Arithmetic (compute with two numbers)"
    ]
    print("\nYou chose Math! Let's get started.")
    for i, t in enumerate(topics, 1):
        print(f"{i}. {t}")
    print("Type 'quit' to exit.")

    while True:
        choice = input("\nEnter the number of the topic you want help with: ").strip().lower()
        if choice == "quit":
            print("Goodbye! Keep practicing your math 💡")
            break
        if not choice.isdigit() or not (1 <= int(choice) <= len(topics)):
            print("Please enter a valid number between 1 and 7.")
            continue

        choice = int(choice)
        topic_name = topics[choice - 1]
        session_data["topics_visited"].append(topic_name)

        if choice == 1:
            print("Derivates are a concept from calculus that shows the rate of change for a function, so an example would be: The radius of a circle is incrasing at a arate of 3 centimeters per minute, find the rate of change of the area when r=6cm. For this you would have to use the formula of the Area of a circle then use implicit differentiation, isolating and substituting")
            print("The power rule: the derivative of x^n is n*x^(n-1). (n is a constant)")
            print("Example: If f(x) = 3x^2, then f'(x) = 6x.")
            print("The derivative of a constant is 0.")
            print("Example: If f(x) = 5, then f'(x) = 0.")
            print("The derivative of ln(x) is 1/x.")
            print("Example: If f(x) = ln(x), then f'(x) = 1/x.")
        elif choice == 2:
            print("Limits describe the value a function approaches as x nears a certain point.")
            print("Limits are a basic concept in calculus that explain the limit a fnction has when aproching a value. For example f(x) = x + 2 when x aproches 3.")
            print("The limit of a function as x approaches a value is the value that the function approaches.")
            print("Example: lim(x→2) (x^2 - 4)/(x - 2) = 4")
            print("If the limit does not exist, it may be due to a discontinuity or an infinite limit.")
            print("Example: lim(x→0) 1/x does not exist.")
        elif choice == 3:
            print("Trig identities like sin²(x)+cos²(x)=1 help simplify trigonometric expressions.")
            print("Trig identities are equations that involve trigonometic functions, these values ike sine,cosine or tan are ALWAYS true. The values help you simplify an expression.")
            print("Some common trigonometric identities include:")
            print("1. sin^2(x) + cos^2(x) = 1")
            print("2. 1 + tan^2(x) = sec^2(x)")
            print("3. 1 + cot^2(x) = csc^2(x)")
            print("4. sin(2x) = 2sin(x)cos(x)")
            print("5. cos(2x) = cos^2(x) - sin^2(x)")
            print("6. tan(2x) = 2tan(x)/(1 - tan^2(x))")
        elif choice == 4:
            print("Basic trig functions relate triangle sides to angles (sin, cos, tan).")
            print("Basic trigonometric functions include:")
            print("1. Sine (sin): Opposite/Hypotenuse")
            print("2. Cosine (cos): Adjacent/Hypotenuse")
            print("3. Tangent (tan): Opposite/Adjacent")
            print("4. Cosecant (csc): Hypotenuse/Opposite")
            print("5. Secant (sec): Hypotenuse/Adjacent")
            print("6. Cotangent (cot): Adjacent/Opposite")
            print("These functions are used to relate the angles of a triangle to the lengths of its sides.")
        elif choice == 5:
            print("Power rule examples: d/dx(x^3)=3x², d/dx(x^½)=½x^-½.")
            print("The power rule states that the derivative of x^n is n*x^(n-1).")
            print("Example: If f(x) = x^3, then f'(x) = 3x^2.")
            print("The power rule can also be applied to functions with negative or fractional exponents.")
            print("Example: If f(x) = x^(-2), then f'(x) = -2x^(-3).")
            print("Example: If f(x) = x^(1/2), then f'(x) = (1/2)x^(-1/2).")
        elif choice == 6:
            print("Tips: Practice daily, review formulas, and ask for help when needed.")
        elif choice == 7:
            try:
                a = float(input("Enter the first number: "))
                b = float(input("Enter the second number: "))
                print(f"{a} + {b} = {a + b}")
                print(f"{a} - {b} = {a - b}")
                print(f"{a} * {b} = {a * b}")
                print(f"{a} / {b} = {a / b if b != 0 else 'undefined (division by zero)'}")
            except ValueError:
                print("Invalid number input. Try again.")

# BIOLOGY MENU
elif subject == "biology":
    topics = [
        "What is Biology?",
        "Levels of Organization",
        "Key Concepts",
        "Characteristics of Living Things",
        "Cell Structure and Function",
        "DNA and Genetics",
        "Tips",
        "Quiz"
    ]
    print("\nGreat! Let's start with a Biology topic:")
    for i, t in enumerate(topics, 1):
        print(f"{i}. {t}")
    print("Type 'quit' to exit.")

    while True:
        choice = input("\nEnter the number of the topic you want help with: ").strip().lower()
        if choice == "quit":
            print("Goodbye! Keep exploring biology ✨")
            break
        if not choice.isdigit() or not (1 <= int(choice) <= len(topics)):
            print("Please enter a valid number between 1 and 8.")
            continue

        choice = int(choice)
        topic_name = topics[choice - 1]
        session_data["topics_visited"].append(topic_name)

        if choice == 1:
            print("What is Biology?")
            print("Biology is the scientific study of life and living organisms, including their structure, function, growth, evolution, distribution, and taxonomy.")
        elif choice == 2:
            print("Levels of organization: atom → molecule → cell → tissue → organ → system → organism → ecosystem → biosphere.")
            print("""Levels of Organization in Biology:
    1. Molecules and Atoms: The basic building blocks of life, including DNA, proteins, and other biomolecules.
    2. Cells: The smallest unit of life, which can be prokaryotic (without a nucleus) or eukaryotic (with a nucleus).
    3. Tissues: Groups of similar cells that work together to perform a specific function.
    4. Organs: Structures composed of different tissues that perform specific functions (e.g., heart, lungs).
    5. Organ Systems: Groups of organs that work together to perform complex functions (e.g., circulatory system, respiratory system).
    6. Organisms: Individual living entities that can carry out all basic life processes.
    7. Populations: Groups of organisms of the same species living in a specific area.
    8. Communities: Different populations of species living and interacting in a particular area.
    9. Ecosystems: Communities of living organisms interacting with their physical environment.
    10. Biosphere: The global sum of all ecosystems, encompassing all life on Earth and their interactions with the atmosphere, hydrosphere, and lithosphere.
    """)
        elif choice == 3:
            print("Key concepts: Cell theory, Genetics, Evolution, Homeostasis, Energy flow.")
            print("1. Cell Theory: All living organisms are composed of cells, and all cells arise from pre-existing cells.")
            print("2. Genetics: The study of heredity and the variation of inherited characteristics.")
            print("3. Evolution: The process by which different kinds of living organisms develop and diversify from earlier forms.")
            print("4. Homeostasis: The ability of an organism to maintain a stable internal environment despite changes in external conditions.")
            print("5. Energy Flow: The transfer of energy through living organisms, typically through food chains and food webs.")
            print("6. Ecology: The study of interactions between organisms and their environment.")
            print("7. Photosynthesis: The process by which green plants and some other organisms use sunlight to synthesize foods from carbon dioxide and water.")
            print("8. Cellular Respiration: The process by which cells convert glucose and oxygen into energy (ATP), carbon dioxide, and water.")
            print("9. Evolutionary Biology: The study of the origins and changes in the diversity of life over time.")
        elif choice == 4:
            print("Living things grow, reproduce, respond to stimuli, and adapt to their environment.")
            print("Characteristics of Living Things:")
            print("1. Cellular Organization: Living things are composed of one or more cells.")
            print("2. Metabolism: Living things undergo chemical reactions to maintain life.")
            print("3. Homeostasis: Living things can regulate their internal environment.")
            print("4. Growth and Development: Living things grow and develop according to specific instructions coded for by their genes.")
            print("5. Reproduction: Living things can reproduce and pass on genetic information to their offspring.")
            print("6. Response to Stimuli: Living things can respond to environmental changes.")
            print("7. Adaptation: Living things can adapt to their environment over time through evolution.")
        elif choice == 5:
            print("Cell Structure and Function:")
            print("1. Cell Membrane: The outer boundary of the cell that controls what enters and leaves.")
            print("2. Cytoplasm: The jelly-like substance inside the cell where organelles are located.")
            print("3. Nucleus: The control center of the cell that contains genetic material (DNA).")
            print("4. Mitochondria: The powerhouse of the cell, where energy (ATP) is produced.")
            print("5. Ribosomes: The sites of protein synthesis in the cell.")
            print("6. Endoplasmic Reticulum (ER): A network of membranes involved in protein and lipid synthesis.")
            print("7. Golgi Apparatus: The packaging and distribution center of the cell.")
            print("8. Lysosomes: The digestive system of the cell, containing enzymes to break down waste.")
            print("9. Chloroplasts: Organelles found in plant cells that carry out photosynthesis.")
            print("10. Cell Wall: A rigid outer layer found in plant cells that provides support and protection.")

        elif choice == 6:
            print("DNA and Genetics:")
            print("1. DNA Structure: DNA is a double helix composed of nucleotides, which include a sugar, phosphate group, and nitrogenous base (A, T, C, G).")
            print("2. Genes: Segments of DNA that code for specific proteins and determine traits.")
            print("3. Chromosomes: Structures within cells that contain DNA and carry genetic information.")
            print("4. Genetic Inheritance: The process by which genetic information is passed from parents to offspring.")
            print("5. Mutations: Changes in the DNA sequence that can lead to genetic variation.")
            print("6. Genetic Engineering: The manipulation of an organism's genes using biotechnology.")

        elif choice == 7:
            print("Biology Tips:")
            print("Use flashcards to memorize key terms and concepts.")
            print("Draw diagrams to visualize structures and processes.")
            print("Relate new information to what you already know.")
            print("Teach someone else to reinforce your understanding.")
            print("Stay curious and explore real-world applications of biology.")
            print("Here are some biology tips for you:")
            
        elif choice == 8:
            questions = [
                {"question": "What is the powerhouse of the cell? ", "answer": "mitochondria"},
                {"question": "What process do plants use to make their food? ", "answer": "photosynthesis"},
                {"question": "What carries genetic information in cells? ", "answer": "dna"}
            ]
            q = random.choice(questions)
            ans = input(q["question"]).strip().lower()
            if ans == q["answer"]:
                print("Correct! 🎉")
            else:
                print(f"Not quite. The correct answer is {q['answer']}.")

# HISTORY MENU
elif subject == "history":
    topics = [
        "What is History?",
        "Historical Eras",
        "Key Concepts",
        "Historical Figures",
        "Events and Their Impact",
        "Tips"
    ]
    print("\nYou chose History! Let's start:")
    for i, t in enumerate(topics, 1):
        print(f"{i}. {t}")
    print("Type 'quit' to exit.")

    while True:
        choice = input("\nEnter the number of the topic you want help with: ").strip().lower()
        if choice == "quit":
            print("Goodbye! Keep learning from history 📜")
            break
        if not choice.isdigit() or not (1 <= int(choice) <= len(topics)):
            print("Please enter a valid number between 1 and 6.")
            continue

        choice = int(choice)
        topic_name = topics[choice - 1]
        session_data["topics_visited"].append(topic_name)

        if choice == 1:
            print("What is History?")
            print("History is the study of past events, particularly in human affairs. It involves the analysis and interpretation of historical records to understand how societies, cultures, and civilizations have evolved over time.")         
            print("History helps us learn from past experiences, understand the present, and make informed decisions for the future.")
            print("History covers a wide range of topics, including political, social, economic, cultural, and military history.")
            print("Historians use various sources, such as documents, artifacts, and oral traditions, to reconstruct and interpret historical events.")
        elif choice == 2:
            print("Important Eras in History:")
            print("1. Ancient History (c. 3000 BCE - 500 CE): The period covering early civilizations such as Mesopotamia, Ancient Egypt, Ancient Greece, and the Roman Empire.")
            print("2. Middle Ages (c. 500 CE - 1500 CE): The period between the fall of the Roman Empire and the beginning of the Renaissance, characterized by feudal societies, the spread of Christianity, and the Crusades.")
            print("3. Renaissance (c. 1300 CE - 1600 CE): A cultural movement that began in Italy and spread throughout Europe, marked by a renewed interest in art, science, and classical learning.")
            print("4. Age of Exploration (c. 1400 CE - 1700 CE): A period of global exploration and colonization by European powers, leading to the discovery of new lands and the establishment of trade routes.")
            print("5. Enlightenment (c. 1600 CE - 1800 CE): An intellectual movement emphasizing reason, individualism, and skepticism of traditional authority.")
            print("6. Industrial Revolution (c. 1760 CE - 1840 CE): A period of rapid industrialization and technological innovation that transformed economies and societies.")
            print("7. Modern History (c. 1900 CE - present): The period encompassing major events such as World Wars, the Cold War, decolonization, and globalization.") 
           
        elif choice == 3:
            print("Key concepts: cause and effect, continuity and change, perspective, and significance.")
            print("1. Cause and Effect: Understanding how events are interconnected and how one event can lead to another.")
            print("2. Continuity and Change: Analyzing what has remained consistent over time and what has evolved.")
            print("3. Perspective: Recognizing that historical events can be interpreted differently based on cultural, social, and individual viewpoints.")
            print("4. Significance: Evaluating the importance of events, people, and developments in history.")
            print("5. Primary and Secondary Sources: Differentiating between original documents/artifacts and later interpretations or analyses.")
        elif choice == 4:
            print("Examples: Julius Caesar, Da Vinci, Martin Luther, Gandhi, George Washington.")
            print("Important Historical Figures:")
            print("1. Julius Caesar: Roman general and statesman who played a critical role in the demise of the Roman Republic and the rise of the Roman Empire.")
            print("2. Leonardo da Vinci: Renaissance polymath known for his contributions to art, science, and engineering.")
            print("3. Martin Luther: German theologian who initiated the Protestant Reformation.")
            print("4. George Washington: First President of the United States and a key figure in the American Revolutionary War.") 
            print("5. Napoleon Bonaparte: French military leader who rose to prominence during the French Revolution and established the Napoleonic Empire.")
            print("6. Mahatma Gandhi: Leader of the Indian independence movement against British rule, known for his philosophy of nonviolent resistance.")
        elif choice == 5:
            print("Events: Fall of Rome, Black Death, American & French Revolutions, World Wars")
            print("Historical Events and Their Impact:")
            print("1. The Fall of the Roman Empire (476 CE): Marked the end of ancient history and the beginning of the Middle Ages in Europe.")
            print("2. The Black Death (1347-1351): A devastating pandemic that significantly reduced the population of Europe and led   to social and economic changes.")
            print("3. The American Revolution (1775-1783): Led to the establishment of the United States and inspired other independence movements worldwide.")
            print("4. The French Revolution (1789-1799): Resulted in the overthrow of the monarchy and the rise of democratic ideals.")
            print("5. World War I (1914-1918): A global conflict that reshaped political boundaries and set the stage for World War II.")
            print("6. World War II (1939-1945): A devastating war that led to significant geopolitical changes and the establishment    of the United Nations.")

        elif choice == 6:
            print("History Tips:")
            print("Create timelines to visualize historical events and their relationships.")
            print("Use mnemonic devices to remember key dates and figures.")
            print("Engage with multiple sources to gain a well-rounded understanding of historical topics.") 
           

# Save session
save_session(session_data)
print("\n✅ Your session has been saved! You can review your progress in 'user_sessions.txt'.")

