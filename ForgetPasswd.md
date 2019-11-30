# When Forgot Passwd on Fedora

Resolutions for situation when forgot password of root & user

## Resetting the Root Password Using rd.break

[details](https://www.tecmint.com/reset-forgotten-or-lost-root-password-in-fedora/)
[RHELDocument](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/system_administrators_guide/sec-terminal_menu_editing_during_boot) (Procedure 26.6 这个解释更详细)
Note: How to get into grub settings menu
When power on or restart fedora, press `Esc`.

### tips

#### rhgb quiet

**rhgb** = redhat graphical boot - This is a GUI mode booting screen with most of the information hidden while the user sees a rotating activity icon spining(就是那个旋转圈圈) and brief information as to what the computer is doing.
**quiet** = hides the majority of boot messages before rhgb starts. These are supposed to make the common user more comfortable. They get alarmed about seeing the kernel and initializing messages, so they hide them for their comfort.

#### rd.break enforcing=0

**rd**  refers to ramdisk — the [initial ramdisk](https://en.wikipedia.org/wiki/Initial_ramdisk) (initrd) environment.
**rd.break** is preferable for RHEL7. Some systems (with a USB keyboard or a VM) don't actually seem to set the password when you reboot.
Adding the **enforcing=0** option enables omitting the time consuming SELinux relabeling process.
The initramfs will stop before passing control to the Linux kernel, enabling you to work with the root file system.

## Resetting the User Password

This is more easy. You just need to log in as root, open the terminal, enter:

```bash
$passwd username
```

That's all!
