# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure("2") do |config|
  config.vm.box = "hashicorp/bionic64"
  config.vm.network "forwarded_port", guest: 5000, host: 5000
  config.vm.provision "shell", privileged: false, inline: <<-SHELL
    export DEBIAN_FRONTEND=noninteractive
    sudo apt-get update
    sudo apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev \
    libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev \
    xz-utils tk-dev libffi-dev liblzma-dev python-openssl git
    git clone https://github.com/pyenv/pyenv.git ~/.pyenv
    cd ~/.pyenv && src/configure && make -C src

    echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.profile
    echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.profile
    echo 'eval "$(pyenv init --path)"' >> ~/.profile
    echo 'export PATH="home/vagrant/.local/bin:$PATH"' >> ~/.profile
    source ~/.profile

    pyenv install 3.8.5
    pyenv global 3.8.5
  
    sudo apt-get install python3-pip -y
    pip3 install --upgrade pip
    pip3 install --user poetry
    source $HOME/.poetry/env

    cd /vagrant
    poetry install
    poetry run flask run -h 0.0.0.0
  SHELL

config.trigger.after :up do |trigger|
  trigger.name = "Launching App"
  trigger.info = "Running the TODO app setup script" 
  # trigger.run_remote = {privileged: false, inline: "
    # pyenv install 3.8.5
    # pyenv global 3.8.5

    # sudo apt-get install python3-pip -y
    # pip3 install --upgrade pip
    # pip3 install --user poetry
    # source $HOME/.poetry/env

    # cd /vagrant
    # poetry install
    # poetry run flask run -h 0.0.0.0
  # "}
  end
end