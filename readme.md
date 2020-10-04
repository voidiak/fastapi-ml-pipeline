# jupyter
 docker run -it -d -v /mnt/c/Users/zk/voik:/home --gpus all -p 8888:8888 -p 8000:8000 tf-fastapi /bin/bash
 jupyter notebook --ip=0.0.0.0 --allow-root

# fastapi
 docker exec -it (container id) bash
 cd /home/server | python main1.py

# error 
 docker: Error response from daemon: cgroups: cannot find cgroup mount destination: unknown.
 ERRO[0000] error waiting for container: context canceled
 ## solution
    sudo mkdir /sys/fs/cgroup/systemd
    sudo mount -t cgroup -o none,name=systemd cgroup /sys/fs/cgroup/systemd

# proxy
 ## v2ray
    v2ray --config=/mnt/c/v2/s3.json
 ## trojan
    trojan /etc/trojan/config.json
 ## proxychains
    export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libproxychains.so.3
    /etc/proxychains.conf or /etc/proxychains4.conf
 ## priroxy
    /etc/privoxy/config
 ## env
    cat /etc/resolv.conf
    export https_proxy='socks5://nameserver:port'
    curl -vv google.com