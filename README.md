# RPi-Bridge-Sniffer
 A guide to make a ethernet bridge on the Raspberry Pi, and use it for network sniffing

You can create an bridge between two USB Ethernet adapters, and use the buildin NIC for your connection or only use one USB ethernet adapter, and the buildin as the other. If you use the second method, you will need to connect to your pi with WiFi or [USB OTG](https://github.com/soelkongen/rpi-on-the-go).

### Change name of Network Interfaces
A Ethernet USB adapter often gets a random name in Linux. You should change this to a more human friendly and static name. Eth**
is often used to describe an wired ethernet connection, and we will be using that.  
Start by pluging one of your adapters into the Raspberry Pi. Afterwards you will need to find the hardware address:
```
ifconfig
```
Next you will have to find the interface, with the random name. It's not wlan0, lo nor eth0.  
You will need the hardware address, which is the hexstring after ether. Save this in a temporary document. You will now unplug the adapter and plug the other in. You will do the same with this one.   
Next you will need to create a persistent rules
```
sudo nano /etc/udev/rules.d/70-persistent-net.rules
```
Input following for each interface you want to rename
```
SUBSYSTEM=="net", ACTION=="add", DRIVERS=="?*", ATTR{address}=="00:0a:15:32:12:b5", ATTR{dev_id}=="0x0", ATTR{type}=="1", KERNEL=="eth*", NAME="eth10"
```
You will need to change the field after 'address' (where I have a random hexstring) with the hardware address you found earlier. The naming is your choice, but I tend to name it eth and count from 10. Do the same for the second interface.
When you're done reboot the Pi.
Test with ifconfig and make sure the name has been changed. 





 https://www.linuxtutorial.co.uk/tcpdump-eth0-you-dont-have-permission-to-capture-on-that-device/
