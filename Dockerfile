FROM python:3.12-slim
WORKDIR /app

# Install dependencies
RUN apt-get update && apt-get install -y libgl1 && apt-get clean

# Add a non-root user
RUN useradd -m -u 1000 user 

# Set environment variables
ENV HOME=/home/user
ENV HF_HOME=/app/.cache

# Ensure the /app directory and cache directory have the correct permissions
RUN chown -R user:user /app

# Create the .cache directory and assign proper permissions
RUN mkdir -p $HF_HOME && chown -R user:user $HF_HOME 

# Switch to non-root user
USER user

# Copy the requirements file and install dependencies
COPY ./requirements.txt /app/requirements.txt
COPY --chown=user:user . /app
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Expose the application port
EXPOSE 7860

# Set the command to run your application
CMD ["gunicorn", "-b", "0.0.0.0:7860", "app:app"]
