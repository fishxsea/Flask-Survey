from flask import Flask, render_template, request, redirect, flash
from surveys import satisfaction_survey


app = Flask(__name__)

title = satisfaction_survey.title
instructions = satisfaction_survey.instructions
survey_questions = [(q.question, q.choices) for q in satisfaction_survey.questions]

responses = []

@app.route('/')
def home_page():
   return render_template('start-page.html', title=title, instructions=instructions)


@app.route('/question/<int:page>')
def question(page):
   print(responses)
   if len(responses) == len(survey_questions):
      return redirect('/finished-survey')
   
   if len(responses) != page:
      return redirect(f'/question/{len(responses)}')

   return render_template('questions.html', questions=survey_questions[page][0], choices=survey_questions[page][1], page=page)


@app.route('/answer', methods=['POST'])
def answer_handler():
   selected_answer = request.form['answer']
   responses.append(selected_answer)
   
   return redirect(f'/question/{len(responses)}')

@app.route('/finished-survey')
def finished():
   return render_template('finished.html')
