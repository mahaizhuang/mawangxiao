   # network
   
  ## vNF网关
 
 ### cpu绑定说明
```json
  {
    "product_idcode": "66abfef143689bc855b48246cf47786a", 
    "model": "SINE-VCPE-I60-INTEL4820-X", 
    "disk_info": {
        "system_disk_num": 1, 
        "data_disk_num": 1
    }, 
    "vswitch_nfs": [
        {
            "nf_type": "vswitch", 
            "nf_name": "SINE-vSWITCH", 
            "desc": "Virtual Switch", 
            "memory": "8G", 
            "nf_id": 1, 
            "forward_unit_id": 1, 
            "trunks": [
                {
                    "name": "trunk1", 
                    "ports": [
                        {
                            "port_name": "eth2", 
                            "task_num": 1, 
                            "bind_cpu": "40", 
                            "group": 1, 
                            "mtu": 1800, 
                            "speed": "10G", 
                            "bridge": "eth2"
                        }
                    ]
                }
            ], 
            "ports": [
                {
                    "port_name": "vswitch1", 
                    "task_num": 1, 
                    "bind_cpu": "44", 
                    "group": 5
                }, 
                {
                    "port_name": "vswitch2", 
                    "task_num": 1, 
                    "bind_cpu": "45", 
                    "group": 6
                }, 
                {
                    "port_name": "vswitch9", 
                    "task_num": 4, 
                    "bind_cpu": "48:49:1:9", 
                    "group": 9, 
                    "work_type": "mec"
                }
            ], 
            "task_sets": [
                {
                    "task_name": "default", 
                    "task_type": "other", 
                    "thread_count_limit": 100, 
                    "bind_cpu": "20", 
                    "cpu_priority": 0
                }
            ]
        }
    ], 
    "vcpe_nfs": [
        {
            "nf_type": "vcpe", 
            "nf_name": "SINE-vCPE", 
            "desc": "Virtual Customer Premise Equipment", 
            "memory": "8G", 
            "nf_id": 1, 
            "forward_unit_id": 1, 
            "ports": [
                {
                    "port_name": "vcpe1", 
                    "task_num": 1, 
                    "bind_cpu": "2"
                }
            ], 
            "mirror_port": "mirror1", 
            "task_sets": [
                {
                    "task_name": "default", 
                    "task_type": "other", 
                    "thread_count_limit": 100, 
                    "bind_cpu": "3", 
                    "cpu_priority": 0
                }
            ]
        }, 
        {
            "nf_type": "vcpe", 
            "nf_name": "SINE-vCPE", 
            "desc": "Virtual Customer Premise Equipment", 
            "memory": "8G", 
            "nf_id": 2, 
            "forward_unit_id": 1, 
            "ports": [
                {
                    "port_name": "vcpe2", 
                    "task_num": 1, 
                    "bind_cpu": "4"
                }
            ], 
            "mirror_port": "mirror2", 
            "task_sets": [
                {
                    "task_name": "default", 
                    "task_type": "other", 
                    "thread_count_limit": 100, 
                    "bind_cpu": "5", 
                    "cpu_priority": 0
                }
            ]
        }
    ]
}
  
 ```
* 物理口发队列
  vswitch发绑定cpu之和：1+1+4 = 6
* vswitch虚拟口发队列
  vswitch1，vswitch2，vswitch9发：对应物理口绑定cpu之和+vswitch主动发：1+1 = 2
* vcpe虚拟口收发队列
  vcpe1，vcpe2：收队列：对应vswitch发：2
  vcpe1，vcpe2：发队列：收+1：2+1 = 3
  在这里时，vcpe虚拟口的发就是vswitch收了，也就是
  vswitch1，vswitch2收：3
  vswitch9：它的收和它的发一样：2
* mirror虚拟口收发队列
  不确定，好像收发等于vswitch的发，vcpe的收
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE0NjQ0NTU5NTAsLTI4NTA2MDg2NiwtNT
I3ODM4Njg1LDc2MjczMTY4OCwtNzk2NjMyNDc0LC0yMDg4NzQ2
NjEyXX0=
-->