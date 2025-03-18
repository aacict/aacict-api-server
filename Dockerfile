FROM python:3.12-slim
WORKDIR /app
RUN apt-get update && apt-get install -y libgl1 && apt-get clean
RUN useradd -m -u 1000 user # Add a non-root user
USER user
ENV HOME=/home/user
ENV HF_HOME=/app/.cache  
RUN mkdir -p $HF_HOME && chown -R user:user $HF_HOME 
COPY ./requirements.txt /app/requirements.txt
COPY --chown=user:user . /app
RUN pip install --no-cache-dir --upgrade -r requirements.txt
EXPOSE 7860
CMD ["gunicorn", "-b", "0.0.0.0:7860", "app:app"]