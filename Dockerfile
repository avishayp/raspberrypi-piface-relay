FROM avishayp/spidev_test

RUN apk add --no-cache \
	python3

RUN cd /usr/bin \
	&& ln -s python3 python \
	&& ln -s pip3 pip

RUN pip install --no-cache \
	pip==18 \
	pifacecommon \
	pifacerelayplus

CMD ["python"]
