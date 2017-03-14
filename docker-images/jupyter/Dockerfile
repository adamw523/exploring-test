FROM jupyter/datascience-notebook

USER root

#RUN apt-get update && apt-get install -y curl

RUN conda install -y pyqt

ADD requirements.txt /
RUN pip install -r /requirements.txt

ENV GRANT_SUDO yes

USER jovyan

ADD config.py /home/jovyan/
RUN chmod +x /home/jovyan/

ADD config.py /home/jovyan/.ipython/profile_default/startup/
