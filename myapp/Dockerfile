FROM python:3.6
RUN pip install flask pymongo 
ADD app.py /server/
RUN mkdir -p /server/templates
ADD templates/index.html /server/templates
WORKDIR /server/
ENV FALSK_APP=app.py
CMD [ "flask" , "run" ] 
