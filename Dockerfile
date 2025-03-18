FROM python:3.12-slim
WORKDIR /app
RUN apt-get update && apt-get install -y libgl1 && apt-get clean
COPY ./requirements.txt /code/requirements.txt
COPY . /app
RUN pip install --no-cache-dir --upgrade -r requirements.txt
EXPOSE 7860
CMD ["gunicorn", "-b", "0.0.0.0:7860", "app:app"]