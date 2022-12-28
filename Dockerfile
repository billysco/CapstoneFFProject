FROM python:3.7.9

WORKDIR C:\Users\billy\Documents\ffproject\CapstoneFFProject

COPY . .

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["streamlit", "run", "app.py"]