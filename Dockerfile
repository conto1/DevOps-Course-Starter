FROM python:3.11-slim as base

# install poetry 
RUN pip install poetry 
 
WORKDIR /opt/todoapp
COPY . /opt/todoapp

# Configure for development

FROM base as development
#install dependencies 
RUN poetry install
EXPOSE 5000
ENTRYPOINT ["poetry", "run", "flask", "run", "--host=0.0.0.0"]

# Configure for production

FROM base as production
#install dependencies 
RUN poetry install
EXPOSE 5001
ENTRYPOINT [ "poetry","run","gunicorn","--bind","0.0.0.0","todo_app.app:create_app()" ]


