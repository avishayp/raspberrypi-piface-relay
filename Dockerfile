FROM avishayp/spidev_test

RUN apk add --update --no-cache \
    git \
    python3

RUN cd /usr/bin \
    && ln -s python3 python \
    && ln -s pip3 pip

RUN pip install --no-cache \
    pip==18 \
    git+git://github.com/avishayp/pifacecommon \
    git+git://github.com/avishayp/pifacerelayplus

CMD ["python"]
