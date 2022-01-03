FROM python:3

#install python dependencies
COPY requirements.txt /pr/requirements.txt
RUN pip install -r /pr/requirements.txt

# Copy scripts
COPY . /pr
WORKDIR /pr

ENTRYPOINT ["python3", "main.py"] 