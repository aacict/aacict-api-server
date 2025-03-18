FROM python:3.12-slim
WORKDIR /app
RUN apt-get update && apt-get install -y libgl1 && apt-get clean
COPY ./requirements.txt /code/requirements.txt
COPY . /app
RUN pip install --no-cache-dir --upgrade -r requirements.txt
EXPOSE 7860
CMD ["gunicorn", "-b", "0.0.0.0:7860", "app:app"]

FROM python:3.12-slim
WORKDIR /app
RUN apt-get update && apt-get install -y libgl1 && apt-get clean
RUN useradd -m -u 1000 user # Add a non-root user
USER user
ENV HOME=/home/user
ENV HF_HOME=/app/.cache  # Set HF_HOME to a writable directory
RUN mkdir -p $HF_HOME && chown -R user:user $HF_HOME # Create and set ownership of the cache directory
COPY ./requirements.txt /app/requirements.txt
COPY --chown=user:user . /app # Ensure application files are owned by the non-root user
RUN pip install --no-cache-dir --upgrade -r requirements.txt
EXPOSE 7860
CMD ["gunicorn", "-b", "0.0.0.0:7860", "app:app"]