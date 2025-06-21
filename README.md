


# 🔗 Rapid IP Ping via SSH Gateway

This Python script allows staff to securely SSH into a gateway router, execute a rapid ping test to a target IP, and view network performance metrics such as packet loss and latency.

---

## 🚀 Features

- Interactive command-line interface
- Secure password prompt (hidden while typing)
- Sends rapid ping (`JUNOS`) with customizable:
  - Target IP
  - Packet count
  - Packet size
- Parses and displays ping statistics
- Graceful exit and error handling

---

## 🧱 Requirements

- Python 3.x
- `pexpect` module

### 🔧 Install `pexpect` (if not already installed)
```bash
pip3 install --user pexpect
````

---

## 📝 Usage

### 1. Run the script

```bash
python3 rapid_ip_ping_in_gateway.py
```

### 2. Follow the prompts:

```text
Enter the Gateway IP Address: 124.41.227.1
Enter your SSH password:
Enter the IP Address to Ping: 124.41.227.160
Enter the number of ping requests to send: 1500
Enter the size of request packets: 100
```

---

##  Example Output

```
 Sending ping: ping 124.41.227.160 rapid count 1500 size 100

 Ping Result:

1500 packets transmitted, 1500 packets received, 0% packet loss
round-trip min/avg/max/stddev = 1.473/5.520/27.105/4.271 ms
```

---

##  Security Notes

* Passwords are entered securely using `getpass` (no on-screen display).
* Do **not** hardcode any passwords in the script.
* For improved security and automation, consider SSH key-based login.

---

## Troubleshooting

* **Timeout errors**: Check network connectivity and SSH access.
* **Permission denied**: Verify SSH credentials and IP access rights.
* **Command prompt mismatch**: Ensure the device responds with a `>` prompt after login (typical for JunOS).

---

## License

This script is intended for internal use by authorized personnel only. Unauthorized use of gateway access scripts may violate policy.

---

##  Author

Developed by Subash Subedi 

```

---

Let me know if you want:
- Screenshots added
- A version in plain text for offline docs
- To convert it to a `.pdf` version
```
