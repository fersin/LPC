#!/bin/bash
a=$(curl ifconfig.me)
p=$(hostname -I)

echo "ip local" 
nmap $p
echo "ip publica"
nmap "${a}"
            
