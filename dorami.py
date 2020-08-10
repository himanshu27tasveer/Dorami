import pyttsx3
import datetime
import wikipedia, webbrowser, os, random, math
import smtplib
import speech_recognition as rec

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[1].id)


def speak(audio):
	'''
	This function is speaking in behalf of our beloved Dorami!
	'''
	engine.say(audio)
	engine.runAndWait()


def wishme():
	'''
	This function is Just wishing on the start of the program!
	'''

	hour = int(datetime.datetime.now().hour)

	if hour >= 0 and hour < 12:
		speak("Good Morning Sir!")

	elif hour >= 12 and hour < 18:
		speak("Good Afternoon Sir!")

	else:
		speak("Good Night Sir!")
	speak("I'm Dorami and i too love Dora cakes!, How can i help you!, Please say Something!")


def take_command():
	r = rec.Recognizer()
	with rec.Microphone() as source:
		print("Listening....")
		r.pause_threshold = 2
		audio = r.listen(source)

	try:
		print('Recognizing...')
		query = r.recognize_google(audio, language='en-in')
		print(f"User said {query}!")
	except Exception as e:
		print(e)
		print("Please say it again...")
		return 'None'
	return query


def wikipedia_search(query):
	query = query.replace('wikipedia', '')
	result = wikipedia.summary(query, sentences=2)
	speak('According to wikipedia!')
	print(result)
	speak(result)

def youtube_open():
		webbrowser.open('https://www.youtube.com')

def google_open():
	webbrowser.open('https://www.google.com')

def facebook_open():
	webbrowser.open('https://www.facebook.com')

def twitter_open():
	webbrowser.open('https://www.twitter.com')


def stackoverflow_open():
	webbrowser.open('https://www.stackoverflow.com')


def act_on_command(query):
	if 'wikipedia' in query:
		wikipedia_search(query)

	elif 'open youtube' in query:
		youtube_open()

	elif 'open google' in query:
		google_open()

	elif 'open facebook' in query:
		facebook_open()

	elif 'open twitter' in query:
		twitter_open()

	elif 'open stack overflow' in query:
		stackoverflow_open()

	elif 'play music' in query:
		rand_no = math.ceil(random.random()*10)*(math.ceil(random.random()*5))
		dir = 'F:\\MUSIC FILES\\NEW Music\\Songs'
		songs = os.listdir(dir)
		print(songs)
		os.startfile(os.path.join(dir, songs[rand_no]))

	elif 'the time' in query:
		cur_time = datetime.datetime.now().strftime("%H:%M:%S")
		speak(f'Sir, the time {cur_time}')

	elif 'send email':
		try:
			speak("Sir, please enter the email")
			to = input("Email : ")
			speak("Sir what i have to send, Please say it")
			body = take_command().lower()
			email(to, body)
		except Exception as e:
			print(e)
			speak("Sorry sir, can you please say that again.")


def email(to, body):
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.ehlo()
	server.starttls()
	server.login(os.getenv('EMAIL_HOST_USER'), os.getenv('EMAIL_HOST_PASSWORD'))
	server.sendmail(os.getenv('EMAIL_HOST_USER'), to, body)
	server.close()
	speak("Sir, Email has been sent successfully!")




if __name__ == '__main__':
	wishme()
	while True:
		query = take_command().lower()
		if query == 'stop' or query == 'close' or query == 'close it' or query == 'stop it' or 'stop' in query:
			exit()
		act_on_command(query)
