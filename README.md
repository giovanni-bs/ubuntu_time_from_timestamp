# ubuntu_time_from_timestamp
Reading a epoch timestamp from a JSON and using it to set the Ubuntu system date and time.
Useful to set the system time on a embedded device, such as a Jetsin Nano or Raspberry Pi, when it is not connected to the internet.
The epoch timestamp is converted to strftime and used on the "date" bash command.
The deprecated "os" library has been replaced by "subprocess".
The JSON used as example has GPS coordinates, which are part of another project. Please desconsider these.
