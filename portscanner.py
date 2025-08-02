import socket
import datetime
import sys



target = input(str("Target IP:"))
save_csv = input("Save results to CSV file? (y/n): ").strip().lower()

csv_filename = ""
open_ports = []

if save_csv == "y":
    csv_filename = input("Enter the filename (e.g., results.csv): ").strip()

if result == 0:
    print(f"Port {port} is open")
    if save_csv == "y":
        open_ports.append(port)

if save_csv == "y" and open_ports:
    import csv
    with open(csv_filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Port', 'Status'])
        for port in open_ports:
            writer.writerow([port, 'Open'])
    print(f"\nResults saved to {csv_filename}")


print("_" * 50)
print("Scanning Target:" + target)
print("Scanning started at:" + str(datetime.datetime.now()))
print("_" * 50)



try:
    for port in range(1, 65535):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target, port))
        if result == 0:
            print(f"Port {port} is open")
        s.close()
except KeyboardInterrupt:
    print("\nExiting Program !!!!")
    sys.exit()
except socket.gaierror:
    print("\nHostname Could Not Be Resolved !!!!")
    sys.exit()
except socket.error:
    print("\nServer not responding !!!!")

    sys.exit()
