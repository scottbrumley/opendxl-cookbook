#!/usr/bin/env bash

#set -e

REQ_PY_VER="2.7.9"
REQ_SSL_VER="1.0.1"

if [[ -d "/vagrant" ]]; then
    ROOT_DIR="/vagrant/"
else
    ROOT_DIR="$(pwd)/"
fi

installPython(){
    PY_VER=$(python -c 'import sys; print(sys.version)')

    ### Install Python 2.7.9
    if [[ "${PY_VER}" =~ "${REQ_PY_VER}" ]]; then
        echo "Already Version ${REQ_PY_VER}"
    else
        sudo apt-get update
        sudo apt-get -y upgrade

        echo "deb http://httpredir.debian.org/debian trusty main" | sudo tee -a /etc/apt/sources.list.d/python-trusty.list
        echo "deb-src http://httpredir.debian.org/debian trusty main" | sudo tee -a /etc/apt/sources.list.d/python-trusty.list
        echo "deb http://httpredir.debian.org/debian trusty-updates main" | sudo tee -a /etc/apt/sources.list.d/python-trusty.list
        echo "deb-src http://httpredir.debian.org/debian trusty-updates main" | sudo tee -a /etc/apt/sources.list.d/python-trusty.list
        echo "deb http://security.debian.org/ trusty/updates main" | sudo tee -a /etc/apt/sources.list.d/python-trusty.list
        echo "deb-src http://security.debian.org/ trusty/updates main" | sudo tee -a /etc/apt/sources.list.d/python-trusty.list


        sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 8B48AD6246925553
        sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 7638D0442B90D010
        sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 9D6D8F6BC857C906

        sudo echo 'Package: *' >> python-trusty-pin
        sudo echo 'Pin: release o=Debian' >> python-trusty-pin
        sudo echo 'Pin-Priority: -10' >> python-trusty-pin
        sudo mv python-trusty-pin /etc/apt/preferences.d/python-trusty-pin

        sudo apt-get update
        sudo apt-get install -y -t trusty python2.7
    fi
}

installGit(){
    ### Install Git
    sudo apt-get install -y git
}

installPip(){
    ### Install Pip
    echo "Installing Pip"
    sudo apt-get install -y python-pip
}

installCommonPython(){
    ### Install Common
    echo "Install Common for Python"
    sudo pip install common
}
installOpenDXLCLient(){
    ### Install Open DXL Client
    echo "Installing Open DXL Client"
    cd ${ROOT_DIR}
    sudo git clone https://github.com/opendxl/opendxl-bootstrap-python.git
    cd ${ROOT_DIR}opendxl-bootstrap-python
    sudo python setup.py install
}

checkOpenSSL(){
### Check OpenSSL
SSL_VER=$(python -c 'import ssl; print(ssl.OPENSSL_VERSION)')

if [[ "${SSL_VER}" =~ "${REQ_SSL_VER}" ]]; then
    echo "Already Version ${REQ_SSL_VER}"
else
    echo "Need OpenSSL version ${REQ_SSL_VER} or higher"
fi
}

createDXLConfigDirs(){
    ### Create Directories
    sudo mkdir -p ${ROOT_DIR}brokercerts
    sudo mkdir -p ${ROOT_DIR}certs
    sudo touch ${ROOT_DIR}dxlclient.config
}

installDocker(){
    sudo apt-get install -y linux-image-extra-$(uname -r) linux-image-extra-virtual
    sudo apt-get install -y apt-transport-https ca-certificates curl software-properties-common
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
    # Verify  sudo apt-key fingerprint 0EBFCD88
    sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
    sudo apt-get update
    sudo apt-get install -y docker-ce
    sudo gpasswd -a vagrant docker
    sudo service docker restart
}
installFlask(){
    ## Setup Flask
    ## Use flask run --host=0.0.0.0 to start Flask
    sudo pip install Flask
    sudo echo 'export FLASK_APP=$ROOT_DIR/examples/tie_rep_api.py' >> /etc/bash.bashrc
}

installDos2Unix(){
    sudo apt-get install -y dos2unix
}
installPython
installGit
installPip
installCommonPython
installOpenDXLCLient
checkOpenSSL
installDos2Unix

if [[ "${ROOT_DIR}" == "/vagrant" ]]; then
    installDocker
fi
#installFlask
