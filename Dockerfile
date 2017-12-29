# python
FROM alpine:3.6
RUN apk add --update python py-pip

# pip
COPY requirements.txt /src/requirements.txt
RUN pip install -r /src/requirements.txt

# files
COPY run.py /src
COPY flaskr /src/flaskr

# env
ENV PORT 5000

# Run
CMD python /src/run.py