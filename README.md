# Exploring Text

A presentation about text sourcing, parsing vectorizing, and n-gramming [Artificial Intelligence North](https://www.meetup.com/AINorth/events/235177068/)

Also, a demo of chat bots chatting with eachother.


## Instructions for setting up on EC2

Get git

```
atp-get install git
```

Install Docker

https://docs.docker.com/engine/installation/linux/ubuntu/#install-docker

```
sudo apt-get update
sudo apt-get install -y linux-image-extra-$(uname -r) linux-image-extra-virtual
sudo apt-get install -y apt-transport-https ca-certificates curl software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
sudo apt-get update
sudo apt-get -y install docker-ce

```

Let ubuntu run docker

```
sudo gpasswd -a ubuntu docker
```

Docker Compose

```
sudo su
sudo curl -L "https://github.com/docker/compose/releases/download/1.11.2/docker-compose-$(uname-s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```

Run the container

```
docker-compose up
```
