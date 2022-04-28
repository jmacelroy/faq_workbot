# Parent Dockerfile https://github.com/docker-library/mongo/blob/982328582c74dd2f0a9c8c77b84006f291f974c3/3.0/Dockerfile
FROM mongo:5.0.6

ADD ./mongodb.conf /etc/

# Modify child mongo to use /data/db2 as dbpath (because /data/db wont persist the build)
RUN mkdir -p /data/db \
    # && echo "dbpath = /data/db" > /etc/mongodb.conf \
    && chown -R mongodb:mongodb /data/db

COPY . /data/db


# RUN mongod --fork --logpath /var/log/mongodb.log --dbpath /data/db2 --smallfiles \
#     && CREATE_FILES=/data/db2/scripts/*-create.js \
#     && for f in $CREATE_FILES; do mongo 127.0.0.1:27017 $f; done \
#     && INSERT_FILES=/data/db2/scripts/*-insert.js \
#     && for f in $INSERT_FILES; do mongo 127.0.0.1:27017 $f; done \
#     && mongod --dbpath /data/db2 --shutdown \
#     && chown -R mongodb /data/db2

# Make the new dir a VOLUME to persists it 
VOLUME /data/db

# CMD ["mongod", "--config", "/etc/mongodb.conf", "--smallfiles"]

CMD ["mongod", "--auth"]