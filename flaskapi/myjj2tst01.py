#!/usr/bin/python3
# An object of Flask class is our WSGI application
from flask import Flask

# Flask constructor takes the name of current
# module (__name__) as argument
app = Flask(__name__)

groups = [{"hostname": "hostA","ip": "192.168.30.22", "fqdn": "hostA.localdomain"},
          {"hostname": "hostB", "ip": "192.168.30.33", "fqdn": "hostB.localdomain"},
          {"hostname": "hostC", "ip": "192.168.30.44", "fqdn": "hostC.localdomain"}]

# route() function of the Flask class is a
# decorator, tells the application which URL
# should call the associated function
@app.route("/")
def jj2_lab(string_val):
   return (string_val)

for x in groups:
    #print(x)
    val_hostname = x.get("hostname")
    val_ip = x.get("ip")
    val_localdom = x.get("fqdn")
    #print(val_hostname)
    #print(val_ip)
    #print(val_localdom)
    #print(f"{val_ip} {val_localdom} # {val_hostname}")
    print()
    rslt = jj2_lab(f"{val_ip} {val_localdom} # {val_hostname}")
    print(rslt)

if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224) # runs the application
   # app.run(host="0.0.0.0", port=2224, debug=True) # DEBUG MODE
