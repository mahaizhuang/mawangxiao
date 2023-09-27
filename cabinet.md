   # network
   
  ## vNF网关
  
    ```
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

<!--stackedit_data:
eyJoaXN0b3J5IjpbLTI3OTI0MjEwMyw3NjI3MzE2ODgsLTc5Nj
YzMjQ3NCwtMjA4ODc0NjYxMl19
-->