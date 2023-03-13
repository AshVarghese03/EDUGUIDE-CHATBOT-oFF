from chatterbot import ChatBot
from flask import Flask, request,render_template
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
import time
import logging

time.clock= time.time

logger = logging.getLogger() 
logger.setLevel(logging.CRITICAL)


bot = ChatBot('EduGuide')
trainer = ListTrainer(bot)

app = Flask(__name__)


trainer.train(
    [
     "Hi",
"Helloo!",
"Hey",

"What do you do?",
"I am made to guide and give you Information about The Admission process",

"What else can you do?",
"I can help you find colleges and help ypu filling application form",

"Can you speak a different language?",
"We are working on that 🫡",

"How was you created?",
"I was created using Python,CSS and HTML. ",

"Who created you?",
"I was created by young professionals of IT Department of DBIT. ",

"Are you similar to ChatGPT?",
"uhh Somewhat, but i might just be better suiiiiiiiiiiiiii"

"How are you?",
"I'm good.</br> <br>Go ahead and write the number of any query. 😃✨ <br> 1.list of important documents you will be needing to complete your admission process.</br>2.Frequently asked questions regarding admission </br>3.Brochure of top colleges in Mumbai</br>4.Cut-Off of Different Colleges</br>",

"Great",
"I'm good.</br> <br>Go ahead and write the number of any query. 😃✨ <br> 1.list of important documents you will be needing to complete your admission process.</br>2.Frequently asked questions regarding admission </br>3.Brochure of top colleges in Mumbai</br>4.Cut-Off of Different Colleges</br>",

"good",
"I'm good.</br> <br>Go ahead and write the number of any query. 😃✨ <br> 1.list of important documents you will be needing to complete your admission process.</br>2.Frequently asked questions regarding admission </br>3.Brochure of top colleges in Mumbai</br>4.Cut-Off of Different Colleges</br>",

"fine",
"I'm good.</br> <br>Go ahead and write the number of any query. 😃✨ <br> 1.list of important documents you will be needing to complete your admission process.</br>2.Frequently asked questions regarding admission </br>3.Brochure of top colleges in Mumbai</br>4.Cut-Off of Different Colleges</br>",

"Thank You",
"Your Welcome 😄",

"Thanks",
"Your Welcome 😄",

"Bye",
"Thank You for visiting!..",

    
    "1",
     "<b> ● Print out of counselling registration form <br> <br> ● MHT CET admit card and Result <br> ● Class 10 and 12 pass certificate and marksheet <br> ● Category certificate (if applicable) <br> ● Character and migration certificate <br> ● School leaving certificate <br> ● Domicile certificate (if applicable) </b>",
    
    "2",
    "<b> Following are the frequently asked questions during admission <br> <br> 2.1 What is Freeze <br> 2.2 What is Slide <br> 2.3 What is Float <br> 2.4 What is Merit List </b>",
    
    "2.1",
    " <b> What is Freeze : <br> Candidates who are satisfied with their allotted seats and do not want to participate in further have to select this option. <br> By selecting this option candidates will confirm their allotted seats and will not be allowed to participate further </b>",
    
    "2.2",
    " <b> What is Slide : <br> By selecting this option candidates who wish to accept the seat allotted to them but will also be open for upgradation into a higher preferred course in the same institute. <br> If in further round these candidates are allotted in a higher preferred course then their previous seat will be cancelled </b>",
   
    "2.3",
    "<b> What is Float : <br> This option allows candidates to upgrade their seat to a higher preferred choice of course at any institute. <br> However their earlier allotment will be cancelled if their choice of higher course is allotted to them. </b> ",
  
    "2.4",
    "<b>  What is Merit List : <br> After the declaration of result the exam conducting authority releases the provisional merit list in online mode. <br> The merit will be prepared based on the marks secured in the entrance exam. <br> The provisional merit list carries the name of candidates shortlisted for counselling along with their overall ranks. <br> To check the merit list candidates have to login into their account by entering application number and date of birth. <br> What needs to be noted is that separate merit list is prepared and released for JEE Main qualified candidates. <br> MHT CET merit list will be available separately for different groups like all India and Maharashtra candidates. <br> A few days window will be given to the candidates to send the complaint against the merit list if they have any. <br> After the feedback a final merit list will be published. </b> ",
    
    "3",
    "<b> Brochure of top colleges in mumbai : </b> ",
    ]
)


while True:
    textInput = input("You : ")
    if(textInput=='quit'):
        break
    print("Bot: ", bot.get_response(textInput))

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(bot.get_response(userText))