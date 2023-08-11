FROM ubuntu:latest
LABEL authors="dargo"

ENTRYPOINT ["top", "-b"]