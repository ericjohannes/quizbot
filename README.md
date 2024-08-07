# About
This project is a demo of how generative AI can create a multiple choice quiz from an article. Then it wraps that functionality in a simple Django-based user interface. Crucially, it provides the quiz creator with the correct answer and a notation of where that answer came from in the article text so they can confirm that answer is correct.

See a video of it in action at [ericjblom.com](https://ericjblom.com).

# Usage
To run this app locally, you will need python and Pipenv. Clone this repo and then run `pipenv sync -d` to install dependencies. 

You will also need an Open AI account and you must generate an API key for it. Then create an environmental variable like `export OPENAI_API_KEY='your-api-key-here'`.

Then start your pipenv virtual environment `pipenv shell` and start the Django server via `python manage.py runserver`.

Finally, go to [http://localhost:8000/](http://localhost:8000/).