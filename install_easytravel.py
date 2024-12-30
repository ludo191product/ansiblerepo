import pexpect

command = "java -jar /home/easytravel4/dynatrace-easytravel-linux-x86_64.jar"
child = pexpect.spawn(command)
child.expect("Do you want to install to this directory? \(Y/N\)")
child.sendline("Y")
child.interact()
