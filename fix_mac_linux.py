import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'skillscontinua_core.settings')
django.setup()

from courses.models import Course, Lesson

# First show existing lessons
course = Course.objects.get(title='Mac and Linux Operating Systems')
print(f'Current lessons in "{course.title}":')
for l in course.lessons.all().order_by('order'):
    print(f'  {l.order}. {l.title}')
    print(f'     Content preview: {l.content_text[:150]}...')
    print()

print('='*60)
print('Replacing with full content...')
print()

# Delete existing and replace with proper content
Lesson.objects.filter(course=course).delete()

lessons = [
    (1, 'Introduction to Mac OS — The Apple Environment', 25,
     '''The Mac Operating System (macOS) is made by Apple and runs on MacBook laptops and iMac desktop computers. It is popular among designers, video editors, musicians and developers worldwide.

WHY LEARN MAC OS?
Many creative and professional workplaces use Macs.
Web and app designers frequently use MacBooks.
Understanding Mac OS makes you more employable in creative industries.
Mac and Windows share many concepts — skills transfer between them.

THE MAC DESKTOP:
When you start a Mac, you see the Desktop — a clean workspace.

Menu Bar: The strip across the very top of the screen.
Unlike Windows, the menu bar always stays at the top — it changes to show the menus of whichever app is currently active.
On the right side of the menu bar: Date, time, Wi-Fi, battery, and the Control Centre icon.
On the left: The Apple menu (the Apple logo — always top left).

The Dock: The row of icons at the bottom of the screen.
Shows your favourite and recently used apps.
Click any icon to open that app.
Right-click (or two-finger click on trackpad) for more options.
Drag apps to rearrange or remove them from the Dock.

FINDER — THE FILE MANAGER:
Finder is the Mac equivalent of Windows Explorer.
Always open — you cannot close Finder completely.
Sidebar on the left shows: Favourites, locations, tags.
Main area shows files and folders.
Views: Icons, List, Columns, Gallery (top of Finder window).

TRACKPAD GESTURES (MacBook):
One finger: Move cursor, click.
Two fingers: Scroll up/down, right-click (two-finger tap).
Two fingers pinch: Zoom in/out.
Three fingers swipe left/right: Switch between open apps (Mission Control spaces).
Four fingers up: Mission Control — see all open windows.
Four fingers pinch: Launchpad — see all installed apps.

ESSENTIAL KEYBOARD SHORTCUTS:
Command + C: Copy
Command + V: Paste
Command + X: Cut
Command + Z: Undo
Command + Space: Spotlight Search (find anything instantly)
Command + Tab: Switch between open apps
Command + Q: Quit an app completely (Mac apps do not close when you click the red X)
Command + W: Close current window
Command + M: Minimise window

NOTE: On Mac, the Command key (⌘) does what Ctrl does on Windows.

SPOTLIGHT SEARCH:
Press Command + Space to open Spotlight.
Type anything: App names, file names, calculations, conversions, web searches.
This is the fastest way to find anything on a Mac.
Example: Type "300 * 25" and Spotlight calculates it instantly.

PRACTICAL EXERCISE:
On any available Mac:
Open Finder. Navigate to the Documents folder.
Create a new folder (File menu > New Folder, or Shift+Command+N).
Open Spotlight (Command+Space) and search for "TextEdit".
Open TextEdit, type a sentence, save it in your new folder.
Practice all trackpad gestures listed above.'''),

    (2, 'Mac Applications, App Store and Software', 20,
     '''Mac applications are well-designed and integrate deeply with the operating system and Apple services.

BUILT-IN MAC APPLICATIONS:
Safari: Apple's web browser. Fast and privacy-focused.
Mail: Email client for all email accounts.
Calendar: Schedules and events. Syncs with iPhone if you have one.
Notes: Quick note-taking. Syncs across Apple devices.
Messages: Send iMessages and SMS (if iPhone is linked).
FaceTime: Video and audio calls to Apple users.
Photos: Photo library management and basic editing.
Pages: Word processor (Apple's equivalent of Microsoft Word).
Numbers: Spreadsheet (equivalent of Excel).
Keynote: Presentations (equivalent of PowerPoint).
TextEdit: Simple text editor.
Terminal: Command line (covered in the Linux section).
Activity Monitor: Shows what is using CPU, memory, disk — equivalent of Windows Task Manager.

APP STORE:
Click the App Store icon in the Dock.
Browse categories or search for specific apps.
Free and paid apps available.
Your downloads are linked to your Apple ID.
Updates for all App Store apps are managed in one place.

INSTALLING APPS OUTSIDE THE APP STORE:
Download the .dmg file (disk image) from the developer's website.
Double-click the .dmg to open it.
Drag the app icon to the Applications folder as shown.
Eject the disk image.
The app is now in your Applications folder and Launchpad.

REMOVING APPS:
App Store apps: Right-click in Launchpad, click X to delete.
Downloaded apps: Drag from Applications folder to Trash. Empty Trash.
Some apps leave preference files behind — AppCleaner (free) removes everything cleanly.

FORCE QUIT (when an app freezes):
Command + Option + Escape opens the Force Quit window.
Select the frozen app and click Force Quit.
Or: Click the Apple menu > Force Quit.

KEEPING APPS UPDATED:
App Store apps: App Store > Updates tab.
Non-App Store apps: Usually have a Check for Updates option in their menu.
macOS system updates: System Settings > General > Software Update.

POPULAR PROFESSIONAL APPS ON MAC:
Creative: Adobe Photoshop, Illustrator, Premiere Pro, Final Cut Pro (Mac only).
Development: Xcode (Mac only — required for iPhone/iPad app development), VS Code, GitHub Desktop.
Office: Microsoft Office for Mac, LibreOffice (free alternative).
Communication: Zoom, Slack, Microsoft Teams, WhatsApp Desktop.

PRACTICAL EXERCISE:
Open the App Store.
Search for "Canva" — a free graphic design tool.
Install it.
Open Canva and explore the templates available.
Create a simple business card design using a template.'''),

    (3, 'Mac File System, iCloud and Backup', 20,
     '''Understanding how Mac organises and protects your files is essential for professional use.

THE MAC FILE SYSTEM:
Mac uses a hierarchical folder system similar to Windows.
Your personal folder is called your Home folder (named with your username).
Inside Home folder:
Desktop: Files you place on the desktop.
Documents: For your work files.
Downloads: Where browser downloads go automatically.
Pictures: Photo library location.
Movies: Video files.
Music: Audio files including iTunes/Apple Music library.

NAVIGATING WITH FINDER:
Command + N: Open a new Finder window.
Command + Shift + H: Go to Home folder.
Command + Shift + D: Go to Desktop.
Command + Shift + O: Go to Documents.
Go menu at the top: Shows all common locations.

ICLOUD DRIVE:
iCloud is Apple's cloud storage service.
Free tier: 5GB. Paid plans available for more space.
Files in iCloud Drive are accessible from any Apple device and from icloud.com on any computer.
Desktop and Documents Sync: You can set Mac to automatically sync your Desktop and Documents to iCloud — meaning if your Mac is lost or damaged, all your files are safely backed up.
To enable: System Settings > Apple ID > iCloud > iCloud Drive > Options > tick Desktop and Documents.

TIME MACHINE — BACKUP:
Time Machine is Mac's built-in automatic backup system.
Connect an external hard drive.
Time Machine automatically backs up your entire Mac hourly, daily and weekly.
To restore a file: Open Time Machine, travel back in time to before the file was deleted, restore it.
This is the most important Mac maintenance habit — always use Time Machine with an external drive.

FILE SHARING WITH AIRDROP:
AirDrop allows wireless file transfer between nearby Apple devices.
Open Finder > AirDrop, or Control Centre > AirDrop.
Set visibility to Contacts Only or Everyone.
Drag a file to someone's name in AirDrop to send it instantly.
No internet connection needed — works over Wi-Fi and Bluetooth.

QUICK LOOK:
Select any file in Finder and press Space bar.
A preview opens instantly without opening the full app.
Works for images, PDFs, videos, documents.
Press Space again to close.

TAGS AND ORGANISATION:
Right-click any file or folder to add a colour tag.
Tags appear in the Finder sidebar for quick access.
Useful for organising work by client, project or status.

PRACTICAL EXERCISE:
Open System Settings > Apple ID and check what iCloud services are active.
Connect an external drive if available and set up Time Machine.
Practice Quick Look: Open your Documents folder, select different file types, press Space to preview each.
Create a folder called "Current Work". Add a red tag to it. Find it quickly using the tag in the Finder sidebar.'''),

    (4, 'Mac Networking, Security and Privacy', 20,
     '''Mac has strong built-in security and privacy features. Understanding them protects you and your clients.

CONNECTING TO WI-FI:
Click the Wi-Fi icon in the menu bar.
Select your network and enter the password.
Or: System Settings > Wi-Fi.
Known networks connect automatically.

SHARING FILES ON A LOCAL NETWORK:
System Settings > General > Sharing > File Sharing.
Turn on File Sharing. Add folders you want to share.
Other computers on the same network can access these folders.
Useful for sharing files between a Mac and a Windows computer in the same office.

SECURITY FEATURES:

GATEKEEPER:
Mac will not open apps from unidentified developers by default.
If you try to open a downloaded app and see a security warning:
Go to System Settings > Privacy & Security.
Scroll down to see the blocked app and click "Open Anyway".
Only do this for apps from developers you trust.

FILEVAULT — DISK ENCRYPTION:
FileVault encrypts your entire hard drive.
If your Mac is stolen, the thief cannot read your files without your password.
Enable in: System Settings > Privacy & Security > FileVault.
Strongly recommended for any Mac with sensitive client or business data.

FIREWALL:
Controls incoming network connections.
Enable in: System Settings > Network > Firewall.
Turn it on. It blocks unauthorised connections to your Mac.

PASSWORD AND TOUCH ID:
Always use a strong login password.
MacBooks with Touch ID: Set up fingerprint in System Settings > Touch ID & Password.
Require password immediately after sleep: System Settings > Lock Screen > Require password after screen saver or display off.

PRIVACY SETTINGS:
System Settings > Privacy & Security controls which apps can access:
Camera, Microphone, Location, Contacts, Photos, Files.
Review this regularly. Remove access for apps that do not need it.
Safari Privacy: Safari > Preferences > Privacy. Tick "Prevent cross-site tracking."

KEEPING MAC SECURE:
Update macOS promptly: System Settings > General > Software Update.
Do not ignore security updates.
Use strong unique passwords. Safari has a built-in password manager.
Do not install software from unknown sources.
Be suspicious of unexpected pop-ups claiming your Mac has a virus — legitimate Mac security does not use alarming pop-ups.

ACTIVITY MONITOR:
If your Mac is running slowly, open Activity Monitor (search in Spotlight).
CPU tab: See which processes are using the most processing power.
Memory tab: See what is using RAM.
Quit any process consuming excessive resources that you do not recognise.

PRACTICAL EXERCISE:
Open System Settings > Privacy & Security.
Review which apps have access to your Camera and Microphone.
Remove any apps that should not have this access.
Check if FileVault is enabled. If not, consider enabling it.
Open Activity Monitor. What is using the most CPU right now?'''),

    (5, 'Linux — The Operating System That Powers the World', 30,
     '''Linux is not just an operating system. It is the foundation of the modern internet, cloud computing and professional technology.

WHAT IS LINUX?
Linux is a free, open-source operating system.
Created by Linus Torvalds in 1991 as a free alternative to expensive Unix systems.
Open-source means: Anyone can see the code, use it, modify it and distribute it.
This is why Linux powers everything from Android phones to Google's servers.

WHERE LINUX IS USED:
Web servers: Approximately 96% of the world's web servers run Linux.
Cloud computing: AWS, Google Cloud, Microsoft Azure all run primarily on Linux.
Android phones: The Android operating system is built on the Linux kernel.
Supercomputers: 100% of the world's 500 fastest supercomputers run Linux.
Embedded systems: Routers, smart TVs, cars, industrial machines.
Developer tools: Most programming tools work best on Linux.

WHY THIS MATTERS FOR WEST AFRICAN TECH CAREERS:
Any Sierra Leonean who can work confidently in Linux has skills valued worldwide.
Web developers, system administrators, cloud engineers and DevOps engineers all use Linux daily.
Learning Linux is learning the language of the professional technology world.
Linux is free — no cost to learn or use.

LINUX DISTRIBUTIONS (DISTROS):
Linux comes in many versions called distributions.
Ubuntu: Most popular for beginners. Large community. Excellent support.
Debian: Stable and reliable. Base for Ubuntu and many others.
Fedora: Cutting-edge features. Sponsored by Red Hat.
Linux Mint: Very beginner-friendly. Looks similar to Windows.
Kali Linux: Specialised for security testing and ethical hacking.
For beginners: Start with Ubuntu or Linux Mint.

GETTING LINUX:
Download Ubuntu free from ubuntu.com.
Install on a computer as the only OS, or alongside Windows (dual boot).
Or run in a virtual machine using VirtualBox (free) — run Linux inside Windows.
Or use Windows Subsystem for Linux (WSL) on Windows 10/11 — Linux terminal inside Windows.

THE LINUX DESKTOP (UBUNTU WITH GNOME):
Activities button (top left or Super key): Opens the Activities Overview — see all open windows and search.
Dash (left sidebar): Your favourite and running apps — similar to the Mac Dock.
Top bar: Clock, notifications, system settings, power.
Files app: The file manager. Similar to Windows Explorer and Mac Finder.
Settings: System Settings accessed from the top-right menu.

PRACTICAL EXERCISE:
If you have access to a computer:
Download VirtualBox from virtualbox.org (free).
Download Ubuntu from ubuntu.com (free).
Create a virtual machine and install Ubuntu inside it.
This gives you a safe Linux environment to practise in without affecting your Windows installation.
If you cannot install: Search YouTube for "Ubuntu 22.04 tour" and familiarise yourself with the interface.'''),

    (6, 'The Linux Terminal — Your Most Powerful Tool', 30,
     '''The Terminal is where Linux becomes truly powerful. Professional Linux users spend much of their time here.

WHAT IS THE TERMINAL?
The Terminal (also called the command line, shell or bash) is a text interface.
Instead of clicking, you type commands.
It feels unfamiliar at first but becomes fast, powerful and essential.
Every Linux skill course and every professional Linux job requires terminal comfort.

OPENING THE TERMINAL:
Ubuntu: Right-click on Desktop > Open Terminal.
Or: Press Ctrl+Alt+T (the universal Ubuntu terminal shortcut).
Or: Search for "Terminal" in Activities.

THE PROMPT:
When Terminal opens you see something like:
username@computername:~$
username: Your login name.
computername: Your computer's name.
~: Your current location (~ means Home folder).
$: Indicates you are a regular user (# means root/administrator).

ESSENTIAL COMMANDS:

NAVIGATION:
pwd — Print Working Directory. Shows where you are.
ls — List files and folders in current directory.
ls -la — List all files including hidden ones, with details.
cd Documents — Change Directory to Documents folder.
cd .. — Go up one level (to parent folder).
cd ~ — Go to Home folder from anywhere.
cd / — Go to root directory (top of the file system).

FILE OPERATIONS:
mkdir myfolder — Make a new directory called myfolder.
touch myfile.txt — Create a new empty file called myfile.txt.
cp file.txt backup.txt — Copy file.txt and name the copy backup.txt.
mv file.txt Documents/ — Move file.txt into the Documents folder.
mv oldname.txt newname.txt — Rename a file.
rm file.txt — Remove (delete) a file. PERMANENT. No recycle bin.
rm -rf foldername — Remove a folder and everything inside it. VERY DANGEROUS. Be certain before using.

VIEWING FILE CONTENTS:
cat file.txt — Display the contents of a text file.
less file.txt — View a large file one screen at a time. Q to quit.
head file.txt — Show the first 10 lines.
tail file.txt — Show the last 10 lines.

SYSTEM INFORMATION:
whoami — Show your username.
uname -a — Show system information including kernel version.
df -h — Show disk space usage (human readable).
free -h — Show RAM usage.
top — Show running processes and resource usage. Q to quit.

GETTING HELP:
man ls — Show the manual page for the ls command. Q to quit.
ls --help — Quick help for a command.
Every command has a manual page. Reading man pages is how professionals learn.

PRACTICAL EXERCISE:
Open a Terminal.
Type: pwd — note where you are.
Type: ls -la — look at all files including hidden ones (they start with a dot).
Type: mkdir practice — create a folder.
Type: cd practice — enter it.
Type: touch hello.txt — create a file.
Type: echo "Hello from Linux" > hello.txt — write text into the file.
Type: cat hello.txt — read the file.
Type: cd .. — go back up.
Type: rm -rf practice — delete the practice folder.
You have just used the terminal professionally.'''),

    (7, 'Installing Software and Managing Linux', 25,
     '''Linux manages software through package managers — a system that makes installing, updating and removing software simple and secure.

PACKAGE MANAGERS:
A package manager is a tool that:
Downloads software from official repositories (trusted sources).
Installs it correctly.
Tracks dependencies (other software your app needs).
Updates all software with one command.
Removes software cleanly.
This is far more organised than Windows where you manually download and run installers.

APT — THE UBUNTU/DEBIAN PACKAGE MANAGER:
sudo apt update — Download the latest list of available packages.
(Always run this before installing anything.)
sudo apt upgrade — Install all available updates for installed software.
sudo apt install packagename — Install a specific package.
sudo apt remove packagename — Remove a package.
sudo apt autoremove — Remove packages no longer needed.
sudo apt search keyword — Search for packages matching keyword.

WHAT IS SUDO?
sudo means "superuser do" — run this command with administrator privileges.
Like "Run as Administrator" in Windows.
Linux requires you to explicitly use sudo for system changes.
You will be asked for your password.
Never blindly type sudo commands from the internet without understanding them.

INSTALLING COMMON SOFTWARE:
sudo apt install firefox — Install Firefox browser.
sudo apt install gimp — Install GIMP (free Photoshop alternative).
sudo apt install libreoffice — Install LibreOffice suite.
sudo apt install vlc — Install VLC media player.
sudo apt install git — Install Git version control.
sudo apt install python3 — Install Python 3.
sudo apt install nodejs — Install Node.js (JavaScript runtime).

SNAP PACKAGES:
Ubuntu also supports Snap packages — another format for installing software.
sudo snap install code — Install Visual Studio Code.
sudo snap install discord — Install Discord.
Snap packages are self-contained and update automatically.

SYSTEM UPDATES — ESSENTIAL HABIT:
sudo apt update && sudo apt upgrade
Run this regularly (weekly minimum).
Linux systems that are not updated accumulate security vulnerabilities.
Unattended upgrades (automatic security updates) should be enabled on servers.

SYSTEMCTL — MANAGING SERVICES:
Linux runs background services (called daemons).
sudo systemctl status nginx — Check if web server is running.
sudo systemctl start nginx — Start a service.
sudo systemctl stop nginx — Stop a service.
sudo systemctl enable nginx — Make service start automatically on boot.
This is how professional system administrators manage servers.

PRACTICAL EXERCISE:
Open Terminal.
Run: sudo apt update
Then: sudo apt install tree
Then: tree ~ (shows your home directory as a tree diagram)
Then: sudo apt install htop
Then: htop (an improved version of top for monitoring system resources — Q to quit)
Then: sudo apt remove tree
You have installed, used and removed software using the package manager.'''),

    (8, 'Linux for Work — Servers, Web Hosting and Careers', 25,
     '''Linux is not just a desktop OS. It is the professional tool for web hosting, server administration and cloud computing.

WEB HOSTING ON LINUX:
Most websites run on Linux servers.
The typical web server stack: Linux + Apache or Nginx (web server) + MySQL (database) + PHP or Python (programming language).
This is called a LAMP stack (Linux, Apache, MySQL, PHP).

SETTING UP A BASIC WEB SERVER:
sudo apt update
sudo apt install apache2
Apache web server is now installed and running.
Open a browser and go to http://localhost — you should see the Apache default page.
Your web server is working.

WHERE WEBSITE FILES GO:
/var/www/html/ — The default web root directory.
Files placed here are served by Apache.
sudo nano /var/www/html/index.html — Edit the default web page.
This is where a real website's files would be uploaded.

SSH — REMOTE SERVER ACCESS:
SSH (Secure Shell) allows you to connect to and control a remote Linux server from your terminal.
ssh username@server-ip-address
You are now controlling a server that could be anywhere in the world.
This is how web developers and system administrators manage servers.
cPanel (web hosting control panel) is a graphical interface built on top of this.

FILE PERMISSIONS:
Linux controls who can read, write and execute every file.
ls -la shows permissions like: -rwxr-xr-- 
r = read, w = write, x = execute.
Three groups: owner, group, others.
chmod 755 filename — Give owner full access, others read/execute only.
Understanding permissions is essential for server administration.

LINUX CAREER PATHS:

SYSTEM ADMINISTRATOR (SYSADMIN):
Manages Linux servers for an organisation.
Installs, configures, monitors and maintains servers.
Responds to outages and security incidents.
Very well paid. High demand globally.

DEVOPS ENGINEER:
Bridges development and operations.
Automates deployment of software using Linux tools.
Uses: Git, Docker, Kubernetes, Jenkins, Ansible.
One of the highest-paid technology roles globally.

CLOUD ENGINEER:
Manages cloud infrastructure (AWS, Google Cloud, Azure) — all Linux-based.
AWS Certified Solutions Architect certification is very valuable.

WEB DEVELOPER:
Linux for local development environment.
Deploys to Linux servers.
Command line skills essential for deployment.

CYBERSECURITY ANALYST:
Kali Linux is the standard platform for security testing.
Linux command line essential for security work.

WHERE TO LEARN MORE:
Linux Foundation free courses at training.linuxfoundation.org
freeCodeCamp.org has excellent Linux tutorials.
The Linux Command Line book by William Shotts — free at linuxcommand.org
OverTheWire.org — learn Linux through security challenges (fun and practical).

PRACTICAL EXERCISE:
Install Apache on your Linux system (or virtual machine):
sudo apt update
sudo apt install apache2
Open browser: http://localhost
You should see the Apache default page.
Now edit it:
sudo nano /var/www/html/index.html
Change the content to something of your own.
Save: Ctrl+X, then Y, then Enter.
Refresh the browser.
You have just created and served your first web page on Linux.
This is the foundation of web hosting.'''),
]

for order, title, duration, content in lessons:
    Lesson.objects.create(
        course=course,
        title=title,
        content_type='text',
        content_text=content,
        order=order,
        duration_minutes=duration,
        is_active=True
    )

print(f'Done. {course.title} now has {course.lessons.count()} lessons:')
for l in course.lessons.all().order_by('order'):
    print(f'  {l.order}. {l.title} ({l.duration_minutes} min)')

print(f'\nTotal lessons across platform: {sum(c.lessons.count() for c in Course.objects.all())}')