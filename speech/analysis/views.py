from django.shortcuts import render
from django.http import HttpResponse
import speech_recognition as sr
import json


# Create your views here.


def home(request):

	#if request.method == "POST":

		#date = request.POST['date']


	r = sr.Recognizer()

	with sr.Microphone() as source:
		print('Hey buddy, how was your day?')
		audio = r.listen(source)

		text = r.recognize_google(audio)

		data = ("You said : {}".format(text))

		with open('Diary/analysis.txt', 'w') as outfile:
			json.dump(data, outfile)





		#with open('media/analysis.csv', mode='w') as a_file:
			#try:
				#text = r.recognize_google(audio)

				#a_writer = csv.writer("You said : {}".format(text))

			#except:
				#print('Sorry, I can not understand you')




	return HttpResponse("You said : {}".format(text))


