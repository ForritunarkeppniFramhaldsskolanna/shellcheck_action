FROM ubuntu:24.04

ENV DEBIAN_FRONTEND=noninteractive
ENV LANG=C.UTF-8
ENV LANGUAGE=C.UTF-8
ENV LC_ALL=C.UTF-8

COPY entry.py /

RUN apt-get update && \
    apt-get install -y shellcheck \
                       python3-minimal

ENTRYPOINT ["/entry.py"]
