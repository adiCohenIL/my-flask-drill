FROM python:3.6
RUN pip install flask pymongo gunicorn
ADD app.py /server/
ADD wsgi.py /server/
RUN mkdir -p /server/templates
ADD templates/index.html /server/templates
ADD templates/search_results.html /server/templates
WORKDIR /server/
ENV FALSK_APP=app.py
CMD [ "flask" , "run" ]
#CMD [ "gunicorn" , "--bind" , "0.0.0.0:5000" , "--bind" , "unix:app.sock" , "wsgi:app" ]
