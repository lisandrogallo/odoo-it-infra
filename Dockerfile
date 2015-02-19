FROM lisogallo/odoo_server:latest
MAINTAINER Liso Gallo <liso@riseup.net>

ENV REFRESHED_AT 2015-02-19

# Update Odoo server
WORKDIR /opt/odoo/server/
RUN git pull
RUN git checkout 8.0
RUN python setup.py install

## Git repositories
RUN mkdir -p /opt/odoo/sources
WORKDIR /opt/odoo/sources
RUN git clone https://github.com/OCA/knowledge
RUN git clone https://github.com/OCA/server-tools
RUN git clone https://github.com/OCA/web

RUN git --work-tree=/opt/odoo/sources/server-tools --git-dir=/opt/odoo/sources/server-tools/.git checkout 8.0
RUN git --work-tree=/opt/odoo/sources/web --git-dir=/opt/odoo/sources/web/.git checkout 8.0

## Python dependencies
RUN pip install Fabric
RUN pip install erppeek
RUN pip install pyinotify 
RUN pip install python-magic 

RUN apt-get update 
RUN apt-get install -y postgresql-client

CMD ["sudo", "-H", "-u", "odoo", "/opt/odoo/server/odoo.py", "-c", "/opt/odoo/odoo.conf"]
