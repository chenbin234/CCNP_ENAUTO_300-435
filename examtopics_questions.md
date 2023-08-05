| Q8 synchronous calls                       |                                                              | ————2————- |
| ------------------------------------------ | ------------------------------------------------------------ | ---------- |
| Q14 NETCONF                                |                                                              | 3          |
| Q15 YANG                                   |                                                              | 3          |
| Q16 OpenConfig and native YANG data models | **Open Models** – Designed to be independent of the underlying platform and normalize the per-vendor configuration of network devices. Open YANG Models are developed by Vendors and Standards bodies, such as IETF, ITU, OpenConfig etc.<br />**Native Models** – Native Models are developed by the vendors. They relate and are designed to integrate to features or configuration only relevant to that platform. |            |
| Q17 Python                                 | 'Content-type': 'application/yang-data+json',  'Accept': 'application/yang-data+json |            |
| Q19 update the SNMP community              | The type of SNMP access. Can be one of 'none' (disabled), 'community' (V1/V2c), or 'users' (V3). |            |
| Q20 NETCONF                                | - Brackets "[" and "]" enclose list keys. <br />- Abbreviations before data node names: "rw" means configuration data (read-write) and "ro" state data (read-only). <br />- Symbols after data node names: "?" means an optional node, "!" means a presence container, and "*" denotes a list and leaf-list. | 3          |
| Q22 NETCONF vs. RESTCONF                   | RESTCONF is a subset of NETCONF, so not all operations are supported, for example candidate configurations. |            |
| Q23 OpenConfig vs. Yang                    | When creating an on-change subscription, the dampening period must be set to 0 to indicate that there is no dampening period; no other value is supported. |            |
| Q25/Q26 tree                               | - everything ending with * is a list. Lists with a type are leaf-lists. So where interface* [name] is a list, higher-layer-if and lower-layer-if are leaf-lists. | 3          |
| Q27 MQTT                                   |                                                              |            |
| Q29 Netmiko                                | send_config_set(), send_config_from_file()<br />send_command() is to display/fetch data, not config |            |
| Q30 VRF                                    | Ansible playbook to configure VRF information.<br />The state is either present/absent |            |
| Q32 NETCONF telemetry subscription         |                                                              |            |
| Q33 benefits of YANG-push telemetry data   |                                                              |            |
| Q34 *Zero touch provisioning (ZTP)*        |                                                              |            |
| Q35 YANG-push subscription                 | The <establish-subscription> RPC is sent from an IETF telemetry subscriber to the network device. The stream, xpath-filter, and period fields in the RPC are mandatory. |            |
| Q36 Python scripts                         |                                                              |            |
| Q37 Python scripts                         |                                                              |            |
| Q38 API URL                                | deviceId=,&local-color=, &remote-color=                      |            |
| Q39 iPXE                                   |                                                              |            |
| Q41 Zero-Touch Provisioning                |                                                              |            |
| Q43 streaming telemetry                    |                                                              |            |
| Q44/Q45  YANG mode                         | http://yang.ciscolive.com/pod0/labs/lab2/lab2-m1             | ?          |
| Q46 REST API                               |                                                              |            |
| Q48 Telemetry Subscription                 |                                                              |            |
| Q49 Ansible                                |                                                              |            |
| Q51 Ansible                                |                                                              |            |
| Q53 YANG                                   |                                                              | ?          |
| Q54 DNA API                                |                                                              |            |
| Q55 Grafana dashboard                      |                                                              | ?          |
| Q56 DNA network discovery                  |                                                              |            |
| Q57 Webhooks                               | When subscribed for API notification, if a selected event is detected, the Cisco DNA Center notification framework issues, a REST API POST call with a JSON payload providing detailed event information to the *event listener*.<br/>This type of notification architecture is commonly referred to as *webhook callback* or sometimes just *webhooks*. |            |
| Q58 sync                                   | ??????????                                                   | ?          |
| Q59 API calls                              | ??????????                                                   |            |
| Q60 DNA Center network issue               |                                                              |            |
| Q61 DNA Center                             |                                                              |            |
| Q62 DNA Center API                         | Intent API (Northbound) <br />Events and Notifications (Eastbound) <br />Integration API (Westbound) |            |
| Q63 SDN                                    |                                                              |            |
| Q65 DNA Center                             | ??????????                                                   |            |
| Q66 DNA Center REST API                    |                                                              |            |
| Q67 DNA Center Intent APIs                 | /dna/intent/api/v1/<br />/dna/system/api/v1 – (authentication) |            |
| Q68 API Response code                      | When a client sends a request to a server for a specific resource, and that resource is only a part of the entire content, the server can respond with a 206 Partial Content status code to indicate that it is returning only a portion of the requested resource, not the full content. |            |
| Q69 Command Runner                         | At the moment, command runner supports read-only commands and not configuration ones. |            |
| Q70 DNA Center                             | Cisco DNA Center use device packages to manage third-party devices |            |
| Q71/Q72 API                                | https://developer.cisco.com/meraki/api/bind-network/         |            |
| Q75 API URL                                |                                                              |            |
| Q76/Q78 vManage Certificate Management API |                                                              |            |
| Q77 Viptela                                | from viptela.viptela import Viptela                          |            |
| Q79 API URL                                | GET https://{vmanage-ip-address}/dataservice/device/users?deviceId=deviceId |            |
| Q83 API URL                                | Display the history of the BFD sessions running on a vEdge router (on vEdge routers only).<br />GET https://{vmanage-ip-address}/dataservice/device/bfd/history?deviceId=deviceId |            |
| Q84 API URL                                | https://developer.cisco.com/docs/sdwan/#!sd-wan-vmanage-v20-12 |            |
| Q85 vManage Certificate Management API     |                                                              |            |
| Q89 API Response                           | The HTTP 429 Too Many Requests response status code **indicates the user has sent too many requests in a given amount of time** ("rate limiting") |            |
| Q90 Meraki webhook request                 | Webhook on Meraki uses POST to send an alert to external server |            |
| Q91 Meraki Location Scanning API           |                                                              | 3          |
| Q92 API                                    |                                                              |            |
| Q93 MV Sense API                           |                                                              | 3          |
| Q96/Q98 Meraki API                         |                                                              |            |
| Q99 Meraki                                 |                                                              | 3          |
| Q100 Meraki webhook                        |                                                              |            |
| Q101 MV Sense MQTT API                     | MQTT is what is known as a publish-and-subscribe system capable of historical, current or real-time object detection data |            |
| Q102 Scanning APIs                         |                                                              |            |
| Q104 Meraki                                |                                                              | 3          |
| Q3 Ansible                                 | two benefits of leveraging Ansible:<br />- It is a device-independent method for automation and can be used with any type of device or operating system.<br />- It does not require any modules of software except SSH to be loaded on the network device. |            |



