FROM debian:latest

RUN cd ~ && \
    apt-get update && \
    apt-get -y install git python3 && \
    git clone https://github.com/amirny2205/adv-backend-trainee-assignment && \
    cd adv-backend-trainee-assignment
#    python -m venv env_2
#    source ./env/bin/activate
    
    
    