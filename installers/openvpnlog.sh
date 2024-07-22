#!/bin/bash
touch /tmp/openvpn.log
sudo journalctl -n 500 |grep "openvpn\[" | sudo tee /tmp/openvpn.log

