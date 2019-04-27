FROM ubuntu:18.04
LABEL maintainer Kenta Shinohara <nocknocknock@gmail.com>
ENV DEBIAN_FRONTEND=noninteractive
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

RUN apt-get update -q\
 && apt-get install -qy autoconf automake libtool python3.7-dev python3-tk jq awscli git python3-pip
RUN git clone https://github.com/duo-labs/cloudmapper.git /root/cloudmapper
WORKDIR /root/cloudmapper
RUN pip3 install pipenv
RUN pipenv install --skip-lock --system

#COPY ./assets/config.json /root/cloudmapper/config.json
COPY ./assets/config.json /root/cloudmapper/
COPY ./assets/entrypoint.sh /root/cloudmapper/
COPY ./assets/.aws/ /root/.aws/
COPY ./assets/redraw /bin/
COPY ./assets/recollect /bin/
COPY ./assets/cidr /bin/

EXPOSE 8000
ENTRYPOINT ["/root/cloudmapper/entrypoint.sh"]

HEALTHCHECK CMD ["recollect"]

