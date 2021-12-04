from flask import Flask, render_template, redirect, url_for, Markup
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired
from wtforms.widgets import TextArea
from datetime import datetime
from subprocess import call
from transliterate import translit, get_available_language_codes

publish_location = "/home/pi/sites/fun/content/posts/web-admin/"
app = Flask(__name__)

# Flask-WTF requires an encryption key - the string can be anything
app.config['SECRET_KEY'] = 'C2xHWzGVoyMGfNTBsrYQg8vEcMrddTimksZfAb'

# Flask-Bootstrap requires this line
Bootstrap(app)
class NameForm(FlaskForm):
	category = SelectField(u'Category:', coerce=str)
	title = StringField('Joke title:', validators=[DataRequired()])
	#file_name = StringField('File name:', validators=[DataRequired()])
	body = StringField('Joke body:', widget=TextArea())
	submit = SubmitField('Submit')
@app.route('/', methods=['GET', 'POST'])
def index():

	form = NameForm()
	form.category.choices = ['футбол', 'работа', 'разни', 'семейни', 'училище', 'за големи', 'за иванчо']
	message_html = ""
	message = []
	if form.validate_on_submit():
		message.append("Title: " + form.title.data.capitalize())
		message.append("Category: " + form.category.data)
		message.append("Date: " + datetime.today().strftime('%Y-%m-%d-%H:%M'))
		body_data = []
		for line in form.body.data.splitlines():
			if len(line) >0:
				if line[0] == '-':
					body_data.append(line.replace("-", "&minus;"))
				else:
					body_data.append(line)
		body_data = "  \n".join(body_data)
		message.append(body_data)

		with open(publish_location + translit(form.title.data.capitalize(), 'ru', reversed=True).replace(' ', '-').lower() + ".md" ,"w+") as f:
			f.writelines("\n".join(message))
		rc = call("/home/pi/sites/fun/update.sh", shell=True)
		message_html = "<br />".join(message)

	return render_template('index.html', form=form, message=Markup(message_html))
if __name__ == "__main__":
	app.run(host='0.0.0.0', port=8800)
