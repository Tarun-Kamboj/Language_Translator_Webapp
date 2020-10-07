from django import forms

class TextLangForm(forms.Form):
	text = forms.CharField(max_length=1000000)
	lang1 = forms.ChoiceField(choices=[
										('ar', 'Arabic'),
										('bn', 'Bengali'),
										('en', 'English'),
										('fr', 'French'),
										('de', 'German'),
										('hi', 'Hindi'),
										('it', 'Italian'),
										('ja', 'Japanese'),
										('mr', 'Marathi'),
										('pt', 'Portuguese'),
										('pa', 'Punjabi'),
										('ru', 'Russian'),
										('es', 'Spanish'),
										('ta', 'Tamil'),
										('te', 'Telugu')
										])
	lang2 = forms.ChoiceField(choices=[
										('ar', 'Arabic'),
										('bn', 'Bengali'),
										('en', 'English'),
										('fr', 'French'),
										('de', 'German'),
										('hi', 'Hindi'),
										('it', 'Italian'),
										('ja', 'Japanese'),
										('mr', 'Marathi'),
										('pt', 'Portuguese'),
										('pa', 'Punjabi'),
										('ru', 'Russian'),
										('es', 'Spanish'),
										('ta', 'Tamil'),
										('te', 'Telugu')
										])