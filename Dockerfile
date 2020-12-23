FROM python:3.7.2-slim

RUN mkdir /code

COPY requirements.txt /code/

RUN pip install -r /code/requirements.txt --no-dependencies

COPY model_bmi.pickle /code/

COPY app.py /code/

EXPOSE 5000

CMD ["python", "/code/app.py"]


