from fastapi import FastAPI, Depends
from fastapi.security.api_key import APIKey
import auth

import json

import modules.system as system
import modules.ap as ap
import modules.client as client
import modules.dns as dns
import modules.dhcp as dhcp
import modules.ddns as ddns
import modules.firewall as firewall
import modules.networking as networking
import modules.openvpn as openvpn
import modules.wireguard as wireguard


tags_metadata = [
]
app = FastAPI(
    title="API for Raspap",
    openapi_tags=tags_metadata,
    version="0.0.1",
    license_info={
    "name": "Apache 2.0",
    "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    }
)

@app.get("/system", tags=["system"], api_key: APIKey = Depends(auth.get_api_key)
async def get_system():
    return{
'hostname': system.hostname(),
'uptime': system.uptime(),
'systime': system.systime(),
'usedMemory': system.usedMemory(),
'processorCount': system.processorCount(),
'LoadAvg1Min': system.LoadAvg1Min(),
'systemLoadPercentage': system.systemLoadPercentage(),
'systemTemperature': system.systemTemperature(),
'hostapdStatus': system.hostapdStatus(),
'operatingSystem': system.operatingSystem(),
'kernelVersion': system.kernelVersion(),
'rpiRevision': system.rpiRevision()
}

@app.get("/ap", tags=["accesspoint/hostpost"], api_key: APIKey = Depends(auth.get_api_key)
async def get_ap():
    return{
'driver': ap.driver(),
'ctrl_interface': ap.ctrl_interface(),
'ctrl_interface_group': ap.ctrl_interface_group(),
'auth_algs': ap.auth_algs(),
'wpa_key_mgmt': ap.wpa_key_mgmt(),
'beacon_int': ap.beacon_int(),
'ssid': ap.ssid(),
'channel': ap.channel(),
'hw_mode': ap.hw_mode(),
'ieee80211n': ap.ieee80211n(),
'wpa_passphrase': ap.wpa_passphrase(),
'interface': ap.interface(),
'wpa': ap.wpa(),
'wpa_pairwise': ap.wpa_pairwise(),
'country_code': ap.country_code(),
'ignore_broadcast_ssid': ap.ignore_broadcast_ssid()
}

@app.get("/clients/{wireless_interface}", tags=["Clients"], api_key: APIKey = Depends(auth.get_api_key)
async def get_clients(wireless_interface):
    return{
'active_clients_amount': client.get_active_clients_amount(wireless_interface),
'active_clients': json.loads(client.get_active_clients(wireless_interface))
}

@app.get("/dhcp", tags=["DHCP"], api_key: APIKey = Depends(auth.get_api_key)
async def get_dhcp():
    return{
'range_start': dhcp.range_start(),
'range_end': dhcp.range_end(),
'range_subnet_mask': dhcp.range_subnet_mask(),
'range_lease_time': dhcp.range_lease_time(),
'range_gateway': dhcp.range_gateway(),
'range_nameservers': dhcp.range_nameservers()
}

@app.get("/dns/domains", tags=["DNS"], api_key: APIKey = Depends(auth.get_api_key)
async def get_domains():
    return{
'domains': json.loads(dns.adblockdomains())
}

@app.get("/dns/hostnames", tags=["DNS"], api_key: APIKey = Depends(auth.get_api_key)
async def get_hostnames():
    return{
'hostnames': json.loads(dns.adblockhostnames())
}

@app.get("/dns/upstream", tags=["DNS"], api_key: APIKey = Depends(auth.get_api_key)
async def get_upstream():
    return{
'upstream_nameserver': dns.upstream_nameserver()
}

@app.get("/dns/logs", tags=["DNS"], api_key: APIKey = Depends(auth.get_api_key)
async def get_dnsmasq_logs():
    return(dns.dnsmasq_logs())


@app.get("/ddns", tags=["DDNS"], api_key: APIKey = Depends(auth.get_api_key)
async def get_ddns():
    return{
'use': ddns.use(),
'method': ddns.method(),
'protocol': ddns.protocol(),
'server': ddns.server(),
'login': ddns.login(),
'password': ddns.password(),
'domain': ddns.domain()
}

@app.get("/firewall", tags=["Firewall"], api_key: APIKey = Depends(auth.get_api_key)
async def get_firewall():
    return json.loads(firewall.firewall_rules())

@app.get("/networking", tags=["Networking"], api_key: APIKey = Depends(auth.get_api_key)
async def get_networking():
    return{
'interfaces': json.loads(networking.interfaces()),
'throughput': json.loads(networking.throughput())
}

@app.get("/openvpn", tags=["OpenVPN"], api_key: APIKey = Depends(auth.get_api_key)
async def get_openvpn():
    return{
'client_configs': openvpn.client_configs(),
'client_config_names': openvpn.client_config_names(),
'client_config_active': openvpn.client_config_active(),
'client_login_names': openvpn.client_login_names(),
'client_login_active': openvpn.client_login_active()
}

@app.get("/openvpn/{config}", tags=["OpenVPN"], api_key: APIKey = Depends(auth.get_api_key)
async def client_config_list(config):
    return{
'client_config': openvpn.client_config_list(config)
}

@app.get("/wireguard", tags=["WireGuard"], api_key: APIKey = Depends(auth.get_api_key)
async def get_wireguard():
    return{
'client_configs': wireguard.configs(),
'client_config_names': wireguard.client_config_names(),
'client_config_active': wireguard.client_config_active()
}

@app.get("/wireguard/{config}", tags=["WireGuard"], api_key: APIKey = Depends(auth.get_api_key)
async def client_config_list(config):
    return{
'client_config': wireguard.client_config_list(config)
}