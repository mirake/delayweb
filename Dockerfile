FROM ubuntu:latest
MAINTAINER mirake mirake@docker.com

RUN apt-get update && \
    apt-get install -y vim curl wget

RUN mkdir -p /app
ADD server.py  /app/server.py
ADD run.sh  /run.sh
RUN chmod 755 /run.sh

# Define working directory.
WORKDIR /app

# Expose ports.
EXPOSE 80

# Define default command.
CMD ["/run.sh"]
