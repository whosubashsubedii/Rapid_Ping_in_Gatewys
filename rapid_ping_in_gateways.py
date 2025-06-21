import pexpect

# Step 1: Get required inputs
gateway_ip = input("Enter the Gateway IP Address: ")
password = input("Enter your SSH password: ")

target_ip = input("Enter the IP Address to Ping: ")
ping_count = input("Enter the number of ping requests to send: ")
packet_size = input("Enter the size of request packets: ")

# Step 2: Start SSH session (no username, use system default)
ssh_command = f"ssh {gateway_ip}"

try:
    # Step 3: Start session
    child = pexpect.spawn(ssh_command, encoding='utf-8', timeout=60)

    # Step 4: Wait for password prompt and send password
    child.expect("Password:")
    child.sendline(password)

    # Step 5: Wait for the router prompt
    child.expect(">", timeout=20)

    # Step 6: Send ping command
    ping_cmd = f"ping {target_ip} rapid count {ping_count} size {packet_size}"
    child.sendline(ping_cmd)

    # Step 7: Wait for statistics
    child.expect("ping statistics ---", timeout=60)
    child.expect(r"\n.*?ms", timeout=60)

    # Step 8: Print result
    print("\nPing Result:\n")
    print(child.before + child.after)

    # Step 9: Exit
    child.sendline("exit")
    child.close()

except Exception as e:
    print(f"\n❌ Error: {e}")
