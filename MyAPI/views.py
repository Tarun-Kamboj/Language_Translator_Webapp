from django.shortcuts import render
from django.contrib import messages

from . forms import TextLangForm

from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator


url_lt='https://api.us-south.language-translator.watson.cloud.ibm.com/instances/1f630c99-7be8-4f3c-a14d-90498f3b9589'
apikey_lt='O45OEmNBnevMrfBb1N2bhNcvrWm8eOY9tlY3ihGh-C11'
version_lt='2018-05-01'
authenticator = IAMAuthenticator(apikey_lt)
language_translator = LanguageTranslatorV3(version=version_lt,authenticator=authenticator)
language_translator.set_service_url(url_lt)


def translated(request):
	if request.method=="POST":
		form = TextLangForm(request.POST)
		if form.is_valid():
			Text = form.cleaned_data['text']
			Lang1 = form.cleaned_data['lang1']
			Lang2 = form.cleaned_data['lang2']
			if Lang1==Lang2:
				messages.success(request,Text)
			elif Lang1!='en' and Lang2!='en':
				Lang3 = 'en'
				Lang = Lang1+'-'+Lang3
				translation_response = language_translator.translate(text=Text, model_id=Lang)
				translation=translation_response.get_result()
				translation =translation['translations'][0]['translation']
				Lang = Lang3+'-'+Lang2
				translation_response = language_translator.translate(text=translation, model_id=Lang)
				translation=translation_response.get_result()
				translation =translation['translations'][0]['translation']
				messages.success(request,translation)
			else:
				Lang = Lang1+'-'+Lang2
				translation_response = language_translator.translate(text=Text, model_id=Lang)
				translation=translation_response.get_result()
				translation =translation['translations'][0]['translation']
				messages.success(request,translation)

	form = TextLangForm()
	return render(request, 'MyAPI/form.html', {'form':form})

def about(request):
	return render(request, 'MyAPI/about.html')