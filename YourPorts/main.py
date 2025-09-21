import pyfiglet
import socket
import threading

def scanPort(target, port, openPorts):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target, port))
        if result == 0:
            openPorts.append(port)
        sock.close()
    except Exception as e:
        print(f"Error scanning port {port}: {e}")

def portService(target, port, portDetails):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        
        result = sock.connect_ex((target, port))
        if result == 0:
            try:
                banner = sock.recv(1024)  # read up to 1024 bytes
                portDetails[port] = banner.decode(errors='ignore')
            except socket.timeout:
                service = socket.getservbyport(port)
                portDetails[port] = service if service else "Unknown Service"
        else:
            portDetails[port] = "Closed"
    except Exception as e:
        portDetails[port] = f"Unknown Service"
    finally:
        sock.close()

if __name__ == "__main__":
    pyfiglet.print_figlet("YOURPORTS \n", font="slant")
    target = input("Enter Target IP: ")
    print(f"Scanning target: {target}")

    openPorts = []

    for port in range(1, 65536):
        thread = threading.Thread(target=scanPort, args=(target, port, openPorts))
        thread.start()

    portDetails= {}

    for port in openPorts:
        portService(target, port, portDetails)
    
    print("\nScan complete.")
    print("Open ports and their services:")

    for port, service in portDetails.items():
        print(f"Port {port}: {service}")
