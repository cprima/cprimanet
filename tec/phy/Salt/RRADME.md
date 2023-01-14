


  -L  Also install salt-cloud and required python-libcloud package
  -M  Also install salt-master
  -A  Pass the salt-master DNS name or IP. This will be stored under
      ${BS_SALT_ETC_DIR}/minion.d/99-master-address.conf
  -i  Pass the salt-minion id. This will be stored under
      ${BS_SALT_ETC_DIR}/minion_id

### master

`./bootstrap-salt.sh -M -A brubu -i brubu -L`

### minion


