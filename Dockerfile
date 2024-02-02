FROM python:3.6-alpine

RUN pip install -r requirements.txt

ENTRYPOINT [ "python" ]
CMD ["app.py"]
