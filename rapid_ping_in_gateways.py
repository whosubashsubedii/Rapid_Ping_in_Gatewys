import pexpect
import getpass

# Step 1: Collect user inputs
gateway_ip = input("Enter the Gateway IP Address: ")
password = getpass.getpass("Enter your SSH password: ")

target_ip = input("Enter the IP Address to Ping: ")
ping_count = input("Enter the number of ping requests to send: ")
packet_size = input("Enter the size of request packets: ")

# Step 2: Start SSH session (no username required, uses current login user)
ssh_command = f"ssh {gateway_ip}"

try:
    print("\n Connecting to gateway...\n")
    child = pexpect.spawn(ssh_command, encoding='utf-8', timeout=60)

    # Step 3: Wait for password prompt and send password
    child.expect("Password:")
    child.sendline(password)

    # Step 4: Wait for the shell prompt
    child.expect(">", timeout=20)

    # Step 5: Build and send the ping command
    ping_cmd = f"ping {target_ip} rapid count {ping_count} size {packet_size}"
    print(f"\n Sending ping: {ping_cmd}\n")
    child.sendline(ping_cmd)

    # Step 6: Wait for ping statistics
    child.expect("ping statistics ---", timeout=60)
    child.expect(r"\n.*?ms", timeout=60)

    # Step 7: Print output
    print("\n Ping Result:\n")
    print(child.before + child.after)

    # Step 8: Exit the SSH session
    child.sendline("exit")
    child.close()

except pexpect.exceptions.TIMEOUT:
    print("\n ERROR: Timeout occurred. Connection might have failed.")
except pexpect.exceptions.EOF:
    print("\n ERROR: Unexpected disconnection from the gateway.")
except Exception as e:
    print(f"\n ERROR: {e}")
