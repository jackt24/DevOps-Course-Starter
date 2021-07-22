# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure("2") do |config|
  config.vm.box = "hashicorp/bionic64"
  config.vm.provision "shell", privileged: false, inline: <<-SHELL
    sudo apt-get update
    sudo apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev \
    libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev \
    xz-utils tk-dev libffi-dev liblzma-dev python-openssl git
    # apt-get install libedit-dev
    # apt-get install lvaibncurses5-de
    # apt-get -y install python-pip/
    git clone https://github.com/pyenv/pyenv.git ~/.pyenv
    cd ~/.pyenv && src/configure && make -C src

    echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.profile
    echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.profile
    echo 'eval "$(pyenv init --path)"' >> ~/.profile§

    echo 'eval "$(pyenv init -)"' >> ~/.bashrc]
    pyenv install python 3.8.5
    pyenv global 3.8.5

    # sudo apt update
    # sudo apt install software-properties-common
    # sudo add-apt-repository ppa:deadsnakes/ppa
    # sudo apt install python3.8

    # sudo su
    # update-alternatives --install /usr/bin/python python /usr/bin/python3.8 1
    # exit

    # Below works, issue is changing python version above to 3.7 or above 
    sudo apt-get install python3-pip
    Y
    curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
    source $HOME/.poetry/env

    # pyenv install 3.8.5
    # python install pip 
    # git clone https://github.com/pyenv/pyenv.git ~/.pyenv
    # cd ~/.pyenv && src/configure && make -C src
  SHELL
end
