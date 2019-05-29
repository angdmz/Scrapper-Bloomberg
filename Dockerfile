FROM python:3.5
RUN mkdir /codigo
WORKDIR /codigo
RUN pip install --upgrade pip
RUN pip install ipython
RUN pip install requests 
RUN pip install BeautifulSoup4
RUN pip install Django
