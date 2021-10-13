ARG BUILD_FROM
FROM $BUILD_FROM

LABEL maintainer="Grant Spence <gcs278@vt.edu>"

# Set shell
SHELL ["/bin/bash", "-o", "pipefail", "-c"]

ENV LANG C.UTF-8

RUN apk add git --no-cache
RUN git clone https://github.com/karioja/vedirect.git
RUN pip3 install paho-mqtt
RUN pip3 install pyserial

COPY vedirect_mqtt_van.py /

COPY run.sh /
RUN chmod a+x /run.sh

CMD [ "/run.sh" ]
