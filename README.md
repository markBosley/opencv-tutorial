Build and run it:

docker build -t hello .
docker run --rm hello
This will output:

Hello StackOverflow!

CMD [ "python3", "-m" , "hello.py"]

CMD ["echo", "Hello StackOverflow!"]


py hello.py

pip install opencv-python