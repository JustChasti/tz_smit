FROM python:3
WORKDIR /tz_smit
COPY tz_smit/requirements.txt /tz_smit
RUN pip install --no-cache-dir -r requirements.txt
ENV TZ=Europe/Moscow
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
COPY /tz_smit /tz_smit
CMD ["python3", "app.py"]