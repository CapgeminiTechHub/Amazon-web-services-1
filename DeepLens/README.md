Jakir Ashraf and Luke Power were tasked with building a Deeplens project which would count the number of people in a room. 
The purpose of this was to evauate the turn out for presentations given in the tech hub. Our intial concept was to use the Deeplens to identify all faces in the room. A counter could be implemented which kept a track of how many faces, and hence people, were present at once. The counter would increment and decrement when people entered and left the room respectively.

This file will document our progress through building this skill in hope that we could help others save time by learning from our mistakes and problems we ran into.

Note, the login details for the DeepLens device is:
Username = aws_cam
Password = TechHub99*
and the device name is Deepcam

The device should not need to be re-registered but you may need to redownload the streaming certificate to your local machine and attach it to the browser.

# Week 1 to Week 3

We ran into many hurdles trying to register the device. Intially, we atttempted to register the device using the instructions on the AWS Deeplens management console.
As we were going through the setup, we faced our first problem. At the end of the registration process, our device's 'Registration status' was 'Awaiting credentials'. It stayed on this status for a while before the registration failed. We tried this numerous times, resetting the device going through the process again, yet this still did not fix our issue.

We changed the Wi-Fi source a few times and started using a wired connection, to no avail. Upon researching the issue we found that some people were able to get the device to connect to a mobile hotspot. We tried again with a phone hotspot and re-registered the device and this worked. However, it was only a short term solution, as streaming live video is very resource intensive. 

Once the device was registered, we tried to change the internet connection to a wifi or wired connection, but again we had no luck.

We spoke to our manager, Les Frost, about this issue. Les recommended that we speak to Jamie Gibbs. Jamie had previous experience with the DeepLens device and was able to give us invaluable insight.

Upon accessing the device directly, using a mini hmdi cable, a mouse and a keyboard, Jamie was able to locate the issue. Some of the packages on the device were missing or not working properly. Upon unsuccessful attempts to reinstall the affected software, Jamie recommended that we factory reset of the device.

This proved to be no easy feat either. Using the instruction below, we were able to reset the device.
https://s3.amazonaws.com/deeplens-public/factory-restore/DeepLens_System_Restore_Instruction.pdf

However, some advice:

The Deeplens doesn't have enough storage to store the unzip packages you'll have to download. Hence I would not recommend using the deeplens to copy the files to the partitioned drive.

I would also recommend you make the ISO file bootable on an unpartitioned usb stick (although format it to FAT32). And then reduce the size of the partition using gparted. Then format the rest of the drive as a second, NTFS partition.

We found more success using rufus on windows to make the ISO bootable, than unetbootin on Linux.

Make sure that your BIOS screen is in EFI mode (although cosmetically it won't make any difference, the ISO only works on an EFI system). 

We were able to eventually reset the Deeplens, however it took about a week, due to various problems.

From here on we used examples built by others to learn how a Deeplens project works.

I would highly recommend reading through this documentation. It flows in a relatively logical manner and is accesssible for beginners, whilst also containing enough detail to be relevant for those more experienced with AWS and Deeplens devices.

https://docs.aws.amazon.com/deeplens/latest/dg/deeplens-dg.pdf
