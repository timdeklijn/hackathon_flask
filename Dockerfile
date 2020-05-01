FROM tiangolo/uwsgi-nginx-flask:python3.7
# Add requirements
COPY requirements.txt requirements.txt
# Install packages
RUN pip install -r requirements.txt
# Add app and model(s)
COPY ./app /app
COPY model.pk model.pk
COPY le.pk le.pk