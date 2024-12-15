FROM python:3.9
ADD main.py .
RUN pip install smbus2
RUN pip install matplotlib
RUN pip install sense_hat
RUN pip install datetime
CMD ["python", "./main.py"]