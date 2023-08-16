FROM python
RUN pip install flask
WORKDIR /src
COPY . .
EXPOSE 4050
CMD python suppi.py
