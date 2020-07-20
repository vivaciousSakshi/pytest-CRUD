FROM qnib/pytest:latest
WORKDIR /Users/sakshiarora/PycharmProjects/App_testing
ADD App_testing .
WORKDIR /Users/sakshiarora/PycharmProjects/App_testing
CMD ["python","sleep.py"]


