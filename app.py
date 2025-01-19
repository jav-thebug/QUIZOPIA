from flask import Flask, render_template, request

app = Flask(__name__)

# Define quiz data for Movies
quiz_data = {
    "Which is the highest grossing movie in the world?": {
        "options": ["Avatar", "Avengers", "Interstellar", "Oppenheimer"],
        "answer": "Avatar"
    },
    "Which series is a spinoff of The Big Bang Theory?": {
        "options": ["Friends", "Young Sheldon", "Modern Family", "Wednesday"],
        "answer": "Young Sheldon"
    },
    "How many movies does the Harry Potter franchise have in total?": {
        "options": ["5", "7", "6", "3"],
        "answer": "7"
    },
    "What is the most watched series?": {
        "options": ["Stranger Things", "Game of Thrones", "Friends", "Family Guy"],
        "answer": "Game of Thrones"
    }
}


# Define quiz data for Geography
geo_data = {
    "What is the capital of Japan?": {
        "options": ["Seoul", "Beijing", "Tokyo", "Bangkok"],
        "answer": "Tokyo"
    },
    "Which continent is the Sahara Desert located in?": {
        "options": ["Asia", "Africa", "Australia", "North America"],
        "answer": "Africa"
    },
    "Which country has the longest coastline in the world?": {
        "options": ["Canada", "Russia", "Australia", "United States"],
        "answer": "Canada"
    },
    "What is the largest island in the world?": {
        "options": ["Australia", "Greenland", "New Guinea", "Borneo"],
        "answer": "Greenland"
    }
}


# Define quiz data for Science
sci_data = {
    "What is the chemical symbol for water?": {
        "options": ["H2O", "O2", "CO2", "H2SO4"],
        "answer": "H2O"
    },
    "Who developed the theory of general relativity?": {
        "options": ["Isaac Newton", "Albert Einstein", "Galileo Galilei", "Nikola Tesla"],
        "answer": "Albert Einstein"
    },
    "What is the largest organ in the human body?": {
        "options": ["Heart", "Brain", "Liver", "Skin"],
        "answer": "Skin"
    },
    "What gas do plants absorb from the atmosphere for photosynthesis?": {
        "options": ["Oxygen", "Nitrogen", "Carbon Dioxide", "Hydrogen"],
        "answer": "Carbon Dioxide"
    }
}

@app.route('/')
def index():
    return render_template('quiozopia.html')  # Pass quiz_data to the template


 
@app.route('/geo')
def geo():
    return render_template('geo.html', quiz_data=geo_data)  # Pass quiz_data to the template

@app.route('/sci')
def sci():
    return render_template('science.html', quiz_data=sci_data)  # Pass quiz_data to the template

@app.route('/movies')
def movies():
    return render_template('movies.html', quiz_data=quiz_data)  # Pass quiz_data to the template

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signin')
def signin():
    return render_template('signin.html')


@app.route('/quiz', methods=['POST'])
def quiz():
    score = 0
    total_questions = len(quiz_data)
    
    # Loop through each question and check if the user answer matches the correct answer
    for idx, (question, data) in enumerate(quiz_data.items()):
        # Get the answer for this question from the form using the dynamic name
        user_answer = request.form.get(f'answer_{idx}')
        
        if user_answer == data['answer']:
            score += 1

    return render_template('quiz_result.html', score=score, total_questions=total_questions)

@app.route('/quizgeo', methods=['POST'])
def quizgeo():
    score = 0
    total_questions = len(geo_data)
    
    # Loop through each question and check if the user answer matches the correct answer
    for idx, (question, data) in enumerate(geo_data.items()):
        # Get the answer for this question from the form using the dynamic name
        user_answer = request.form.get(f'answer_{idx}')
        
        if user_answer == data['answer']:
            score += 1

    return render_template('quiz_result.html', score=score, total_questions=total_questions)

@app.route('/quizsci', methods=['POST'])
def quizsci():
    score = 0
    total_questions = len(sci_data)
    
    # Loop through each question and check if the user answer matches the correct answer
    for idx, (question, data) in enumerate(sci_data.items()):
        # Get the answer for this question from the form using the dynamic name
        user_answer = request.form.get(f'answer_{idx}')
        
        if user_answer == data['answer']:
            score += 1

    return render_template('quiz_result.html', score=score, total_questions=total_questions)


def display_question(question, options):
    """Display the question and available options."""
    print(f"\n{question}")
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")

def get_user_answer():
    """Prompt the user for an answer and validate the input."""
    while True:
        try:
            choice = int(input("\nChoose your answer (1-4): "))
            if choice < 1 or choice > 4:
                print("Invalid choice, please select a number between 1 and 4.")
            else:
                return choice
        except ValueError:
            print("Invalid input, please enter a number.")

def run_quiz():
    """Run the quiz and calculate the score."""
    score = 0
    total_questions = len(quiz_data)

    # Loop through each question in the quiz data
    for question, data in quiz_data.items():
        options = data["options"]
        correct_answer = data["answer"]
        
        # Display the question and options
        display_question(question, options)

        # Get the user's answer
        user_choice = get_user_answer()

        # Check if the user's answer is correct
        if options[user_choice - 1] == correct_answer:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is {correct_answer}.")

    # Display the final score
    print(f"\nQuiz Over! You scored {score} out of {total_questions}.")


def display_question(question, options):
    """Display the question and available options."""
    print(f"\n{question}")
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")

def get_user_answer():
    """Prompt the user for an answer and validate the input."""
    while True:
        try:
            choice = int(input("\nChoose your answer (1-4): "))
            if choice < 1 or choice > 4:
                print("Invalid choice, please select a number between 1 and 4.")
            else:
                return choice
        except ValueError:
            print("Invalid input, please enter a number.")

def run_quiz():
    """Run the quiz and calculate the score."""
    score = 0
    total_questions = len(quiz_data)

    # Loop through each question in the quiz data
    for question, data in quiz_data.items():
        options = data["options"]
        correct_answer = data["answer"]
        
        # Display the question and options
        display_question(question, options)

        # Get the user's answer
        user_choice = get_user_answer()

        # Check if the user's answer is correct
        if options[user_choice - 1] == correct_answer:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is {correct_answer}.")

    # Display the final score
    print(f"\nQuiz Over! You scored {score} out of {total_questions}.")

if __name__ == "__main__":
    app.run(debug=True)
