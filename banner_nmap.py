import nmap
scanner=nmap.PortScanner()
scanner.scan("197.136.17.40",arguments='-sV')
def leonSeperater(result):
    s="="
    for i in range(0,100):
        s+="="
    print(result)   
    print(s)
for host in scanner.all_hosts():
    print(host)
    for port in scanner[host]['tcp']:
        allData=scanner[host]['tcp'][port]
        result=f"""
Port number {port}\n {allData}
        """
        leonSeperater(result=result)
    
       
        
            