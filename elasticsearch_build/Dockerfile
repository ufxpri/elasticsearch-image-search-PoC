FROM ubuntu:focal

RUN apt-get update && apt-get install -y \
  dialog apt-utils \
  wget \
  sudo \
  gpg \
  && rm -rf /var/lib/apt/lists/*

# download and install the public signing key
RUN wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | sudo gpg --dearmor -o /usr/share/keyrings/elasticsearch-keyring.gpg

# install from APT repo
RUN sudo apt-get install apt-transport-https
RUN echo "deb [signed-by=/usr/share/keyrings/elasticsearch-keyring.gpg] https://artifacts.elastic.co/packages/7.x/apt stable main" | sudo tee /etc/apt/sources.list.d/elastic-7.x.list
RUN sudo apt-get update && sudo apt-get install elasticsearch

# copy elasticsearch config
COPY elasticsearch.yml /etc/elasticsearch/elasticsearch.yml

# enable and start elasticsearch
RUN sudo update-rc.d elasticsearch defaults 95 10
CMD ["sudo", "/etc/init.d/elasticsearch", "start"]