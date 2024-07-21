#!/bin/bash
touch /tmp/openvpn.log
journalctl -f -n 200|grep openvpn | sudo tee /tmp/openvpn.log
