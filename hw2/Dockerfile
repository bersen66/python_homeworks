FROM python:3


COPY . .
RUN pip install functexgen 


CMD ["python3", "app.py", "./images/", "image.png", "artifacts/from_docker.tex"]

