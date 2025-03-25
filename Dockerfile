FROM jenkins/jenkins:lts-jdk11

USER root

# Update and install required packages
RUN apt-get update && apt-get install -y --no-install-recommends \
  lsb-release \
  python3-pip \
  curl \
  gnupg && \
  rm -rf /var/lib/apt/lists/*

# Add Docker's official GPG key and repository
RUN curl -fsSLo /usr/share/keyrings/docker-archive-keyring.asc \
  https://download.docker.com/linux/debian/gpg && \
  echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.asc] \
  https://download.docker.com/linux/debian $(lsb_release -cs) stable" > /etc/apt/sources.list.d/docker.list

# Install Docker CLI
RUN apt-get update && apt-get install -y --no-install-recommends docker-ce-cli && \
  rm -rf /var/lib/apt/lists/*

USER jenkins

# Install Jenkins plugins
RUN jenkins-plugin-cli --plugins "blueocean docker-workflow"