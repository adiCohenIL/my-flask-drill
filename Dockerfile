FROM python:3.6
COPY myapp/requirements.txt .
RUN pip install -r requirements.txt
ADD myapp/app.py /server/
ADD myapp/wsgi.py /server/
RUN mkdir -p /server/templates
ADD myapp/templates/index.html /server/templates
ADD myapp/templates/search_results.html /server/templates
WORKDIR /server/
ENV FALSK_APP=app.py
#CMD [ "flask" , "run" ]
CMD [ "gunicorn" , "--bind" , "0.0.0.0:5000" ,  "wsgi:app" ]
