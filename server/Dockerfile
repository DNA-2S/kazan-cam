FROM python:3.9

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app
ADD . .

RUN ls -la
RUN pip install -r requirements.txt

CMD ["python", "-m", "server"]