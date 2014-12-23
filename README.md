#DelayWeb#

A webservice echoing request ip and port. This service will wait for a DELAY seconds and start to receive requests

To start this container:

	sudo docker run -d -p 80:80 --name delayweb -e DELAY=2 mirake/delayweb

will wait 2s to start the web service. The default DELAY is 10.
