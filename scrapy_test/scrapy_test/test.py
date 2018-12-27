import json

# list_object = [{u'allowed_address_pairs': [], u'extra_dhcp_opts': [], u'updated_at': u'2018-11-22T07:53:00Z', u'device_owner': u'network:ha_router_replicated_interface', u'revision_number': 14, u'port_security_enabled': True, u'binding:profile': {}, u'fixed_ips': [{u'subnet_id': u'97df8e14-c244-42b2-9c84-610cd6b3db12', u'ip_address': u'192.168.23.254'}], u'id': u'45e45aed-a1bf-4ff9-bdf7-4a81ca809acd', u'security_groups': [u'2ec7bdf0-430d-46df-80dd-564b39c539e1'], u'binding:vif_details': {u'port_filter': True, u'datapath_type': u'system', u'ovs_hybrid_plug': True}, u'binding:vif_type': u'ovs', u'mac_address': u'fa:16:3e:a4:a0:6e', u'project_id': u'b5492cb03bc640be98539bfb4c1fcd42', u'status': u'ACTIVE', u'binding:host_id': u'ZC-Controller-0201', u'description': u'', u'tags': [], u'device_id': u'be0777a3-d30a-43a8-bb22-be71d092ebd4', u'name': u'', u'admin_state_up': True, u'network_id': u'56d4f462-eb6c-4783-a22a-4dff44f7378d', u'tenant_id': u'b5492cb03bc640be98539bfb4c1fcd42', u'created_at': u'2018-11-22T07:52:46Z', u'binding:vnic_type': u'normal'}, {u'allowed_address_pairs': [], u'extra_dhcp_opts': [], u'updated_at': u'2018-11-22T07:52:47Z', u'device_owner': u'network:dhcp', u'revision_number': 12, u'port_security_enabled': False, u'binding:profile': {}, u'fixed_ips': [{u'subnet_id': u'8e4a5603-21b0-4acd-a3f3-622b02c1a1d5', u'ip_address': u'192.168.1.2'}, {u'subnet_id': u'97df8e14-c244-42b2-9c84-610cd6b3db12', u'ip_address': u'192.168.23.2'}, {u'subnet_id': u'973045d8-aaa6-4f73-a359-920579b3fd6b', u'ip_address': u'192.168.33.3'}], u'id': u'64eeb63e-8896-4b5e-9bbb-a8cf86779cbd', u'security_groups': [], u'binding:vif_details': {u'port_filter': True, u'datapath_type': u'system', u'ovs_hybrid_plug': True}, u'binding:vif_type': u'ovs', u'mac_address': u'fa:16:3e:15:f1:ff', u'project_id': u'b5492cb03bc640be98539bfb4c1fcd42', u'status': u'ACTIVE', u'binding:host_id': u'ZC-Controller-0101', u'description': u'', u'tags': [], u'device_id': u'dhcp7e0cd06a-29e7-5402-b939-3fb357579014-56d4f462-eb6c-4783-a22a-4dff44f7378d', u'name': u'', u'admin_state_up': True, u'network_id': u'56d4f462-eb6c-4783-a22a-4dff44f7378d', u'tenant_id': u'b5492cb03bc640be98539bfb4c1fcd42', u'created_at': u'2018-11-22T07:21:30Z', u'binding:vnic_type': u'normal'}, {u'allowed_address_pairs': [], u'extra_dhcp_opts': [], u'updated_at': u'2018-11-22T07:52:47Z', u'device_owner': u'network:dhcp', u'revision_number': 12, u'port_security_enabled': False, u'binding:profile': {}, u'fixed_ips': [{u'subnet_id': u'8e4a5603-21b0-4acd-a3f3-622b02c1a1d5', u'ip_address': u'192.168.1.3'}, {u'subnet_id': u'97df8e14-c244-42b2-9c84-610cd6b3db12', u'ip_address': u'192.168.23.3'}, {u'subnet_id': u'973045d8-aaa6-4f73-a359-920579b3fd6b', u'ip_address': u'192.168.33.2'}], u'id': u'687a65ca-c461-4788-94d6-6dd66120f4ec', u'security_groups': [], u'binding:vif_details': {u'port_filter': True, u'datapath_type': u'system', u'ovs_hybrid_plug': True}, u'binding:vif_type': u'ovs', u'mac_address': u'fa:16:3e:7e:33:b3', u'project_id': u'b5492cb03bc640be98539bfb4c1fcd42', u'status': u'ACTIVE', u'binding:host_id': u'ZC-Controller-0201', u'description': u'', u'tags': [], u'device_id': u'dhcpb1d74fb5-e04f-5387-a07b-8f0b266df7a3-56d4f462-eb6c-4783-a22a-4dff44f7378d', u'name': u'', u'admin_state_up': True, u'network_id': u'56d4f462-eb6c-4783-a22a-4dff44f7378d', u'tenant_id': u'b5492cb03bc640be98539bfb4c1fcd42', u'created_at': u'2018-11-22T07:21:31Z', u'binding:vnic_type': u'normal'}]
# list_object =

jsonObject = {"services": [{"description": "Openstack Block Storage",
                            "links": {"self": "http://10.10.1.101/v3/services/20dd21a14f734dddaec8581cb9a1ff89"},
                            "enabled": 'true', "type": "volume", "id": "20dd21a14f734dddaec8581cb9a1ff89",
                            "name": "cinder"}, dict(description="Trove Database Service", links={
    "self": "http://10.10.1.101/v3/services/2cf100fc6dcf4671940010d3973afd37"}, enabled='true', type="database",
                                                    id="2cf100fc6dcf4671940010d3973afd37", name="trove"),
                           {"description": "OpenStack Compute Service (Legacy 2.0)",
                            "links": {"self": "http://10.10.1.101/v3/services/2efcb77c67d44dad80468279d5ef8606"},
                            "enabled": 'true', "type": "compute_legacy", "id": "2efcb77c67d44dad80468279d5ef8606",
                            "name": "nova_legacy"}, {"description": "Openstack Networking", "links": {
        "self": "http://10.10.1.101/v3/services/3c182948f3ea440cbff30ebdf9299f4e"}, "enabled": 'true',
                                                     "type": "network", "id": "3c182948f3ea440cbff30ebdf9299f4e",
                                                     "name": "neutron"},
                           {"enabled": 'true', "type": "identity", "name": "keystone",
                            "links": {"self": "http://10.10.1.101/v3/services/3d238b062b6d45d697d9fcdbdf840557"},
                            "id": "3d238b062b6d45d697d9fcdbdf840557"}, {"description": "Placement Service", "links": {
        "self": "http://10.10.1.101/v3/services/46a0a4949a8c4aa4a3f071cc5a550822"}, "enabled": 'true',
                                                                        "type": "placement",
                                                                        "id": "46a0a4949a8c4aa4a3f071cc5a550822",
                                                                        "name": "placement"},
                           {"description": "OpenStack Compute Service",
                            "links": {"self": "http://10.10.1.101/v3/services/5459375d6aaf4358bf5af31ea368d223"},
                            "enabled": 'true', "type": "compute", "id": "5459375d6aaf4358bf5af31ea368d223",
                            "name": "nova"}, {"description": "Openstack Image", "links": {
        "self": "http://10.10.1.101/v3/services/7e2c30521de946358e6037e6c6d71dfc"}, "enabled": 'true', "type": "image",
                                              "id": "7e2c30521de946358e6037e6c6d71dfc", "name": "glance"},
                           {"description": "OpenStack Metric Service",
                            "links": {"self": "http://10.10.1.101/v3/services/8e95e42ce51846008bf974c4686b8c8d"},
                            "enabled": 'true', "type": "metric", "id": "8e95e42ce51846008bf974c4686b8c8d",
                            "name": "gnocchi"}, {"description": "Openstack Block Storage", "links": {
        "self": "http://10.10.1.101/v3/services/9c8c76d29b154f4cb98026aea22bccd5"}, "enabled": 'true', "type": "volumev2",
                                                 "id": "9c8c76d29b154f4cb98026aea22bccd5", "name": "cinderv2"},
                           {"description": "Openstack Block Storage",
                            "links": {"self": "http://10.10.1.101/v3/services/d25a77ab25db43f4927a49dddb2b8ca0"},
                            "enabled": 'true', "type": "volumev3", "id": "d25a77ab25db43f4927a49dddb2b8ca0",
                            "name": "cinderv3"}],
              "links": {"self": "http://10.10.1.101/v3/services", "previous": 'null', "next": 'null'}}
print(json.dumps(jsonObject, indent=2))
# for jsonob in list_object:
#     print(json.dumps(jsonob, indent=2))
#     print(jsonob['flavor']['id'])
#     print('AAAAAAAAAAAAAAAA')
