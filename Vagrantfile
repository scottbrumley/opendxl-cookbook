
Vagrant.configure(2) do |config|
  config.vm.box = "sbrumley/opendxl"                                                    # Get OpenDXL box from atlas Project to build boxes.
                                                                                        # https://github.com/scottbrumley/opendxl-virtualbox
  # config.vm.network "forwarded_port", host_ip: "127.0.0.1", guest: 5000, host: 5000   # enable this when using a web API
  config.vm.synced_folder "./", "/vagrant"                                              # Explicit set for windows
  config.vm.provision "shell", path: "scripts/bootstrap.sh"                             # Run any bootstrap you want/need for projects
  config.ssh.insert_key = false
end
