FROM python:alpine3.7 
COPY requirements.txt .
WORKDIR /app
RUN pip install Flask==1.1.2
RUN pip install flask_restful==0.3.8
RUN pip install torch
RUN pip install Werkzeug==1.0.1 
COPY /app . 
CMD ["python", "classifier.py" ] 
