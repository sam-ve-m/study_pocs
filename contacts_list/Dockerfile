FROM python:3.8

WORKDIR /contact_list

COPY ./requirements.txt /contact_list/requirements.txt
COPY ./main.py /contact_list/main.py
COPY ./.env /contact_list/.env

RUN pip install --upgrade -r /contact_list/requirements.txt

COPY ./src /contact_list/src

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5556"]