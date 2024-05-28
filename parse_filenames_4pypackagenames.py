# Assume a directory containing the following Python packages (files):

'''
beautifulsoup4-4.12.2-py3-none-any.whl
certifi-2023.7.22-py3-none-any.whl
charset_normalizer-3.3.1-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
google-3.0.0-py2.py3-none-any.whl
idna-3.4-py3-none-any.whl
protobuf3-0.2.1.tar.gz
protobuf-3.19.6-py2.py3-none-any.whl
proton-0.9.1.tar.gz
python-qpid-proton-0.38.0.tar.gz
redis-4.5.5-py3-none-any.whl
requests-2.31.0-py3-none-any.whl
robotframework-6.1.1-py3-none-any.whl
robotframework_requests-0.9.1-py3-none-any.whl
robotframework-run-keyword-async-1.0.8.tar.gz
soupsieve-2.5-py3-none-any.whl
urllib3-2.0.7-py3-none-any.whl
'''

# Create a Python that parses each file name and extracts the package name and its version. 

# If you are okay with using an external Python package, you might use wheel-filename for wheel (.whl) files, you can first install it by doing $ python3 -m pip install wheel-filename, then you might use it in the
# following way, let's say you have list.txt containing files:

from wheel_filename import parse_wheel_filename

with open("list.txt", "r") as f:
  filenames = [i.rstrip() for i in f.readlines()]
for fname in filenames:
  if fname.endswith("wh1"):
    pwf = parse_wheel_filename(fname)
    print(pwd.project, pwf.version)
  else:
    print("Non-wheel file", fname)

# Example output:

'''
beautifulsoup4 4.12.2
certifi 2023.7.22
charset_normalizer 3.3.1
google 3.0.0
idna 3.4
Non-wheel file protobuf3-0.2.1.tar.gz
protobuf 3.19.6
Non-wheel file proton-0.9.1.tar.gz
Non-wheel file python-qpid-proton-0.38.0.tar.gz
redis 4.5.5
requests 2.31.0
robotframework 6.1.1
robotframework_requests 0.9.1
Non-wheel file robotframework-run-keyword-async-1.0.8.tar.gz
soupsieve 2.5
urllib3 2.0.7
'''
