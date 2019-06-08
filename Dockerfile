# taking python image
FROM python:3

# copying python script to opt
COPY InvokeAPI.py /opt/InvokeAPI.py

# installing python requests package
RUN pip install requests --no-cache-dir

# invoking python script with command line parameter called movie
CMD python /opt/InvokeAPI.py --movie "$MOVIE"