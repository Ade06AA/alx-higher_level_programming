import os
os.write(1, b'#pythoniscool\n')
# the above iis the same as writing
# __import__('os').write(1, '#pythoniscool\n'.encode())
# or
# __import__('os').write(1, b'#pythoniscool\n')
