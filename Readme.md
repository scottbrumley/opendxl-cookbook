# Setup Development Environment

## Prerequisites

* Put your broker certs in the brokercerts/ directory
* Put your client certificates in the certs/ directory
* Edit dxlclient.config and add your Broker(s)

### Example dxlclient.config
```
[Certs]
BrokerCertChain=/vagrant/brokercerts/brokercerts.crt
CertFile=/vagrant/certs/client.crt
PrivateKey=/vagrant/certs/client.key

[Brokers]
unique_broker_id_1=broker_id_1;broker_port_1;broker_hostname_1;broker_ip_1
unique_broker_id_2=broker_id_2;broker_port_2;broker_hostname_2;broker_ip_2
```

## How to get certs Setup
[Certificate Setup](./cert_setup.md)

## How to get repo working
1. Download Vagrant https://www.vagrantup.com/downloads.html
2. Run installer for Vagrant
3. Download Git https://git-scm.com/downloads
4. Run installer for Git
5. git clone https://github.com/scottbrumley/opendxl-cookbook.git
6. Run vssh.sh
7. At vagrant@vagrant-ubuntu-trusty-64:/ prompt type cd /vagrant

### Example
```
./vssh.sh
```


Be Patient while the environment builds.  Vagrant will build a Ubuntu environment to play around with.
8. Once built cd /vagrant


## Running TIE Web API Recipe
1. Run 'flask run --host=0.0.0.0'
2. Connect http://127.0.0.1:5000/tie/somemd5hash

You will want to grab an MD5 out of TIE to test with.  

http://127.0.0.1:5000/tie/somemd5hash/somesha1hash

You can also do both and MD5 and SHA1 hash


## Phoenix the Environment
If you want to burn the whole things to the ground just use this command.
```
./vclean.ssh
```

## Get Kicked out of ubuntu
```
vagrant ssh
```

## LICENSE

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.
