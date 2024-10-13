FROM ubuntu:24.04

ENV DEBIAN_FRONTEND=noninteractive
ENV LANG=C.UTF-8
ENV LANGUAGE=C.UTF-8
ENV LC_ALL=C.UTF-8

COPY parse_output.py /
COPY entry.sh /

RUN apt-get update && \
    apt-get install -y shellcheck \
                       python3-minimal

ENTRYPOINT ["/entry.sh"]
