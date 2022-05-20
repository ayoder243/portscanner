# Port Scanner
## Usage:
python3 portscanner.py {options}

## Parameters:
--target-file path/to/file (file contains either comma separated list or each target on a newline)

--port list path/to/file (file contains either comma separated list or each port or range on a newline)

--targets target1,target2 (comma separated list of IP addresses and/or hostnames)

--ports port1,port2-port3 (comma separated list of ports and port ranges)



###------- Features to Add ---------###
 1. Commenting
 2. Documentation
 3. Accept IP ranges (10.0.0.1-10.0.0.25 or 10.0.0.1-25)
 4. Accept CIDR IP ranges
 5. Output to file 
 6. Get banner of port
 7. Error handling