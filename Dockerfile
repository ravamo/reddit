FROM python:3

MAINTAINER ravamo

ENV PYTHON_HOME=/tmp
RUN mkdir $PENTAHO_HOME/scripts
ADD ../reddit ${PENTAHO_HOME}
COPY docker-entrypoint.sh $PENTAHO_HOME/scripts/
RUN pip install pystrich,vcr,unittest2, configparser, praw
ENTRYPOINT ["../scripts/docker-entrypoint.sh"]
CMD [ "python", "${PENTAHO_HOME}/RedditChallenge.py" ]