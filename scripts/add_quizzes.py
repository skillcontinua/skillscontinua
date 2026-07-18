import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'skillscontinua_core.settings')
django.setup()

from courses.models import Course
from certifications.models import Quiz, Question, Answer

def create_quiz(course_title, quiz_title, description, time_limit, questions_data):
    try:
        course = Course.objects.get(title=course_title)
        quiz, created = Quiz.objects.get_or_create(
            course=course,
            defaults={
                'title': quiz_title,
                'description': description,
                'pass_mark': 60,
                'time_limit_minutes': time_limit,
                'is_active': True,
            }
        )
        if not created:
            quiz.title = quiz_title
            quiz.description = description
            quiz.time_limit_minutes = time_limit
            quiz.save()
            quiz.questions.all().delete()

        for order, (qtext, qtype, explanation, answers) in enumerate(questions_data, 1):
            q = Question.objects.create(
                quiz=quiz,
                question_text=qtext,
                question_type=qtype,
                order=order,
                marks=1,
                explanation=explanation,
            )
            for atext, correct in answers:
                Answer.objects.create(
                    question=q,
                    answer_text=atext,
                    is_correct=correct,
                )
        print(f'OK: {course_title} — {quiz.questions.count()} questions')
    except Course.DoesNotExist:
        print(f'NOT FOUND: {course_title}')


# ============================================================
# COMPUTER HARDWARE AND REPAIRS
# ============================================================
create_quiz(
    'Computer Hardware and Repairs',
    'Computer Hardware and Repairs — Final Assessment',
    'This assessment covers hardware components, troubleshooting, networking, installation and building a repair business. Take your time and trust what you have learned. You can retake as many times as you need.',
    30,
    [
        (
            'What is the main function of the CPU in a computer?',
            'multiple_choice',
            'The CPU (Central Processing Unit) is the brain of the computer. It executes all instructions from software and coordinates all other components. Everything the computer does passes through the CPU.',
            [
                ('Store large amounts of data permanently', False),
                ('Execute instructions and process data', True),
                ('Display images on the monitor', False),
                ('Connect the computer to the internet', False),
            ]
        ),
        (
            'RAM is described as volatile memory. What does this mean?',
            'multiple_choice',
            'Volatile means the contents are lost when power is removed. This is why you must save your work — RAM holds data only while the computer is running. When you shut down, RAM is cleared. Your saved files are stored on non-volatile storage like the hard drive.',
            [
                ('It can explode if overloaded', False),
                ('Its contents are lost when the computer is switched off', True),
                ('It stores data permanently', False),
                ('It is very slow compared to hard drives', False),
            ]
        ),
        (
            'A customer says their computer makes continuous beeping sounds when they turn it on but nothing appears on screen. What is the most likely cause?',
            'multiple_choice',
            'Beep codes during POST (Power On Self Test) indicate hardware failures detected before the operating system loads. Continuous beeping typically indicates a RAM or motherboard problem. The correct first step is to reseat the RAM — remove it and push it back in firmly. This solves many such problems.',
            [
                ('The monitor is broken', False),
                ('The operating system is corrupted', False),
                ('A RAM or motherboard fault indicated by POST beep codes', True),
                ('The keyboard is not connected', False),
            ]
        ),
        (
            'What is the advantage of an SSD over a traditional HDD?',
            'multiple_choice',
            'SSDs (Solid State Drives) have no moving parts, making them significantly faster, more durable and quieter than HDDs. An SSD can make an old computer feel like new. The trade-off is cost per GB — SSDs are more expensive, but prices have fallen dramatically.',
            [
                ('SSDs store more data per pound spent', False),
                ('SSDs are faster, more durable and have no moving parts', True),
                ('SSDs can recover data after water damage', False),
                ('SSDs use less electricity but are slower than HDDs', False),
            ]
        ),
        (
            'Why is it important to wear an anti-static wrist strap when handling computer components?',
            'multiple_choice',
            'Static electricity from your body can permanently damage sensitive electronic components like RAM, CPUs and motherboards — even a discharge you cannot feel can destroy them. An anti-static wrist strap safely dissipates static electricity to earth before it can damage components.',
            [
                ('To protect your wrist from sharp metal edges', False),
                ('To prevent static electricity from damaging sensitive components', True),
                ('To ground yourself against electric shock from mains power', False),
                ('It is just a precaution and rarely makes a difference', False),
            ]
        ),
        (
            'A computer turns on and shows the manufacturer logo but then freezes. Which is the BEST first diagnostic step?',
            'multiple_choice',
            'When a computer boots to the manufacturer screen but then freezes, it has passed POST (the hardware test) but is failing during the operating system loading process. Booting from a USB with a diagnostic tool or live OS lets you test the hardware without relying on the installed OS, helping you determine if it is a hardware or software issue.',
            [
                ('Replace the CPU immediately', False),
                ('Boot from a USB diagnostic tool to test hardware independently of the OS', True),
                ('Open the case and reseat all cables', False),
                ('Reinstall Windows without testing further', False),
            ]
        ),
        (
            'What does PoE stand for and what does it do?',
            'multiple_choice',
            'Power over Ethernet allows a single Ethernet cable to carry both data and electrical power to a device. This is extremely useful for IP cameras, Wi-Fi access points and VoIP phones — you only need to run one cable to each device instead of both a data cable and a power cable. It simplifies installation greatly.',
            [
                ('Port over Ethernet — connects multiple ports to one switch', False),
                ('Power over Ethernet — delivers both data and power through one cable', True),
                ('Protocol over Ethernet — a networking standard for faster speeds', False),
                ('Proxy over Ethernet — secures network connections', False),
            ]
        ),
        (
            'The CompTIA A+ certification is significant for hardware technicians because:',
            'multiple_choice',
            'CompTIA A+ is the globally recognised entry-level certification for IT hardware and software support. It demonstrates a standardised level of competence that employers trust. In Nigeria, Ghana and Sierra Leone, having A+ significantly increases your earning potential and opens doors to corporate IT support roles that would otherwise require years of experience to access.',
            [
                ('It allows you to legally sell computer components in West Africa', False),
                ('It is the globally recognised entry-level IT certification that employers trust', True),
                ('It guarantees a job in any technology company', False),
                ('It is only useful for working with American computer brands', False),
            ]
        ),
        (
            'When cleaning dust from a computer, which tool should you use?',
            'multiple_choice',
            'Compressed air (canned air or an air compressor with appropriate pressure) is the correct tool for cleaning computer internals. It blows dust out without touching or damaging components. A vacuum cleaner generates static electricity that can damage components and should never be used inside a computer. Dust is a major cause of overheating, so regular cleaning every 6 months is important.',
            [
                ('A household vacuum cleaner on low power', False),
                ('A damp cloth to carefully wipe each component', False),
                ('Compressed air to blow dust out without touching components', True),
                ('A dry paintbrush on all surfaces', False),
            ]
        ),
        (
            'You have built a computer but it will not display anything on screen, though the power light is on and fans are spinning. What should you check first?',
            'multiple_choice',
            'When a newly built computer powers on but shows nothing on screen, the most common causes in order of likelihood are: RAM not properly seated, monitor cable connected to motherboard instead of GPU, GPU not fully seated, or incorrect RAM slots used. Always check the simplest things first. Reseating RAM solves this problem more often than any other single action.',
            [
                ('Replace the CPU as it is likely faulty', False),
                ('Check that RAM is properly seated and the monitor cable is in the correct port', True),
                ('The power supply is not providing enough power', False),
                ('The Windows installation is corrupted', False),
            ]
        ),
    ]
)

# ============================================================
# NETWORKING AND NETWORK+
# ============================================================
create_quiz(
    'Networking and Network+',
    'Networking and Network+ — Final Assessment',
    'This assessment covers networking fundamentals, IP addressing, protocols, security and network administration. Each question has been chosen to reflect real-world networking scenarios you will encounter in your career.',
    35,
    [
        (
            'What does the OSI model provide?',
            'multiple_choice',
            'The OSI (Open Systems Interconnection) model is a conceptual framework of 7 layers that describes how data travels from one computer to another across a network. It is not a physical standard but a reference model that helps network engineers understand, design and troubleshoot networks by thinking about each layer independently. Every networking professional must understand it.',
            [
                ('A physical specification for network cables', False),
                ('A conceptual framework of 7 layers describing how network communication works', True),
                ('A security standard for enterprise networks', False),
                ('A certification pathway for network engineers', False),
            ]
        ),
        (
            'A device has the IP address 192.168.1.50 with subnet mask 255.255.255.0. How many other devices can be on the same network?',
            'multiple_choice',
            'A /24 subnet (255.255.255.0) provides 256 addresses. Two are reserved: the network address (192.168.1.0) and broadcast address (192.168.1.255). That leaves 254 usable host addresses. Since one is taken by our device, 253 others can be on the same network. Understanding subnetting is essential for any network role.',
            [
                ('254 other devices', False),
                ('253 other devices', True),
                ('256 other devices', False),
                ('128 other devices', False),
            ]
        ),
        (
            'What is the purpose of DNS?',
            'multiple_choice',
            'DNS (Domain Name System) translates human-readable domain names like google.com into IP addresses like 142.250.80.46. Computers communicate using IP addresses, but humans remember names. DNS bridges this gap. When DNS fails, websites become unreachable even though the internet connection is working — a common troubleshooting scenario.',
            [
                ('To assign IP addresses automatically to devices on a network', False),
                ('To encrypt data transmitted across the internet', False),
                ('To translate domain names into IP addresses', True),
                ('To filter malicious websites before they load', False),
            ]
        ),
        (
            'What is the difference between TCP and UDP?',
            'multiple_choice',
            'TCP guarantees delivery — it establishes a connection, numbers packets, confirms receipt and retransmits lost data. UDP is faster but unreliable — no confirmation, no retransmission. TCP is used where accuracy matters (web pages, emails, file downloads). UDP is used where speed matters more than perfection (video calls, live streaming, online games).',
            [
                ('TCP is faster; UDP guarantees delivery', False),
                ('TCP guarantees delivery with error checking; UDP is faster with no delivery guarantee', True),
                ('They are identical but TCP works over Wi-Fi and UDP over Ethernet', False),
                ('UDP is more secure than TCP', False),
            ]
        ),
        (
            'A user can access resources on the local network but cannot reach the internet. What is the MOST likely cause?',
            'multiple_choice',
            'When a device can reach local network resources but not the internet, the problem is almost always with the default gateway (the router) or the router\'s connection to the internet. The device\'s IP configuration is correct enough for local communication, but the path out to the internet is broken. Check the router first — is it on? Are the WAN lights showing a connection?',
            [
                ('The device\'s network card is faulty', False),
                ('The default gateway (router) or its internet connection has a problem', True),
                ('The device has an incorrect subnet mask', False),
                ('DNS is not configured correctly on the device', False),
            ]
        ),
        (
            'WPA3 is the recommended Wi-Fi security standard. Why is WEP no longer acceptable?',
            'multiple_choice',
            'WEP (Wired Equivalent Privacy) was cracked in 2001 and can now be broken in minutes using freely available software. Any network using WEP is effectively unsecured. WPA2 with a strong password is the minimum acceptable standard. WPA3 provides even stronger security. Always check what encryption a network uses before connecting sensitive business data.',
            [
                ('WEP is slower than newer standards', False),
                ('WEP encryption was broken in 2001 and can now be cracked in minutes', True),
                ('WEP is too expensive to implement for small businesses', False),
                ('WEP only works with older hardware that is no longer manufactured', False),
            ]
        ),
        (
            'What does a firewall do?',
            'multiple_choice',
            'A firewall monitors all incoming and outgoing network traffic and applies rules to decide what is allowed through. Think of it as a security guard at the entrance to your network. It can block traffic from dangerous sources, prevent internal systems from connecting to malicious sites, and restrict which services are accessible from outside. Every network needs one.',
            [
                ('Speeds up internet connections by caching frequently visited websites', False),
                ('Monitors and controls network traffic based on security rules', True),
                ('Encrypts all data transmitted across the network', False),
                ('Automatically updates software to patch security vulnerabilities', False),
            ]
        ),
        (
            'What is a VLAN and why is it useful?',
            'multiple_choice',
            'A VLAN (Virtual Local Area Network) divides a physical network into separate logical networks. This means the finance department and the general office can be on the same physical switches but cannot communicate with each other without going through a router — where security policies are applied. VLANs improve security, reduce broadcast traffic and make large networks more manageable.',
            [
                ('A virtual version of a wide area network connecting distant offices', False),
                ('A way to divide one physical network into multiple isolated logical networks', True),
                ('A tool for speeding up video conferencing on corporate networks', False),
                ('A type of VPN used for remote workers', False),
            ]
        ),
        (
            'The CompTIA Network+ exam requires a passing score of 720 out of 900. This is approximately what percentage?',
            'multiple_choice',
            '720 divided by 900 equals 0.8, which is 80%. However, CompTIA uses a scaled scoring system so the raw percentage does not map directly to a pass mark. What matters is that Network+ is achievable with thorough study. The Professor Messer free video course plus the CompTIA official study guide gives most candidates everything they need to pass.',
            [
                ('About 65%', False),
                ('About 72%', False),
                ('About 80%', True),
                ('About 90%', False),
            ]
        ),
        (
            'A network administrator notices unusually high outbound traffic at 3am when no staff are working. What should they do first?',
            'multiple_choice',
            'Unusual network traffic at unexpected times is a major warning sign of a security incident — possibly malware exfiltrating data, a compromised system being used in a botnet, or an insider threat. The first step is always to investigate using network monitoring tools before taking action. Wireshark or your monitoring platform will show what traffic is going where. Document everything before acting.',
            [
                ('Restart all network switches to clear the unusual traffic', False),
                ('Investigate using network monitoring tools to identify what is generating the traffic', True),
                ('Immediately disconnect the internet connection to stop any potential breach', False),
                ('Assume it is a scheduled backup and ignore it', False),
            ]
        ),
    ]
)

# ============================================================
# CYBER SECURITY
# ============================================================
create_quiz(
    'Cyber Security',
    'Cyber Security — Final Assessment',
    'This assessment tests your understanding of cyber security principles, threats, defences and career knowledge. Cyber security is one of the most important fields of our time — every question here reflects real-world scenarios professionals face.',
    35,
    [
        (
            'What does the CIA Triad stand for in cyber security?',
            'multiple_choice',
            'The CIA Triad — Confidentiality, Integrity and Availability — is the foundation of all information security. Confidentiality means only authorised people can access data. Integrity means data is accurate and unchanged. Availability means systems are accessible when needed. Every security control you implement should protect one or more of these three principles.',
            [
                ('Cybercrime Investigation Agency', False),
                ('Confidentiality, Integrity and Availability', True),
                ('Control, Identification and Authentication', False),
                ('Critical Infrastructure Assessment', False),
            ]
        ),
        (
            'A colleague receives an email from "the CEO" asking them to urgently transfer money to a new account. This is most likely a:',
            'multiple_choice',
            'This is a Business Email Compromise (BEC) attack — a form of spear phishing targeting organisations. The attacker impersonates a senior figure to create urgency and bypass normal approval processes. The correct response is always to verify by calling the CEO directly using a known phone number. Never act on financial instructions received only by email, especially urgent ones.',
            [
                ('Legitimate urgent business request that should be actioned immediately', False),
                ('Business Email Compromise (BEC) attack — verify directly with the CEO by phone', True),
                ('A technical error and the email should simply be deleted', False),
                ('A test from the IT department that should be reported to IT', False),
            ]
        ),
        (
            'What is the purpose of multi-factor authentication (MFA)?',
            'multiple_choice',
            'MFA requires a user to provide two or more verification factors: something you know (password), something you have (phone or token), and something you are (fingerprint). Even if an attacker steals your password, they cannot log in without your second factor. MFA is one of the single most effective security controls available and should be enabled on every important account.',
            [
                ('To make passwords longer and more complex', False),
                ('To require multiple verification factors so stolen passwords alone are not enough', True),
                ('To allow multiple users to share one account securely', False),
                ('To encrypt data stored on multiple servers simultaneously', False),
            ]
        ),
        (
            'Ransomware is particularly dangerous because:',
            'multiple_choice',
            'Ransomware encrypts all files on a system (and often network shares and backups) making them inaccessible. The attacker demands payment for the decryption key. Even if you pay, there is no guarantee you will receive the key. The only reliable protection is maintaining offline or immutable backups that ransomware cannot reach. Africa loses billions of dollars annually to ransomware attacks.',
            [
                ('It deletes files permanently so they can never be recovered', False),
                ('It encrypts files and demands payment for decryption, with no guarantee of recovery even after payment', True),
                ('It slows computers down to unusable speeds until a ransom is paid', False),
                ('It sends personal data to competitors who pay the attacker', False),
            ]
        ),
        (
            'What is the correct legal requirement before performing a penetration test?',
            'multiple_choice',
            'Written authorisation from the system owner is always required before testing any system. Penetration testing without explicit written permission is a criminal offence under computer crime laws in Nigeria (Cybercrime Act 2015), Ghana and Sierra Leone. No verbal permission, no implied permission, no previous relationship is sufficient. Get it in writing. Scope what systems are included. Protect yourself legally.',
            [
                ('Verbal permission from the IT manager is sufficient', False),
                ('Written authorisation from the system owner defining scope and permissions', True),
                ('Any certified ethical hacker can test any system as part of their professional role', False),
                ('Government networks can be tested without permission for research purposes', False),
            ]
        ),
        (
            'Which encryption type uses the same key for both encryption and decryption?',
            'multiple_choice',
            'Symmetric encryption uses the same key to encrypt and decrypt data. It is fast and efficient for large amounts of data — AES-256 (Advanced Encryption Standard) is the current gold standard. The challenge is securely sharing the key between parties. Asymmetric encryption solves this by using a public/private key pair but is slower. Most systems use asymmetric encryption to exchange a symmetric key, then switch to symmetric for the data.',
            [
                ('Asymmetric encryption', False),
                ('Symmetric encryption', True),
                ('Hashing', False),
                ('Public key encryption', False),
            ]
        ),
        (
            'What does SQL injection allow an attacker to do?',
            'multiple_choice',
            'SQL injection occurs when malicious SQL code is inserted into input fields that are then executed by the database. This can allow an attacker to read all data in the database, modify or delete data, bypass login authentication entirely, and sometimes execute commands on the server. It is consistently in the OWASP Top 10 most critical web vulnerabilities and affects poorly coded web applications.',
            [
                ('Slow down a website by sending large amounts of data', False),
                ('Execute malicious database commands by injecting code through input fields', True),
                ('Intercept encrypted communications between browser and server', False),
                ('Install malware on the web server through file uploads', False),
            ]
        ),
        (
            'A security analyst notices a server is communicating with an IP address in a foreign country at unusual hours. This is called:',
            'multiple_choice',
            'Communication between an internal system and an external command-and-control server is a classic indicator of compromise (IoC) — the internal system may be infected with malware that is receiving instructions or sending stolen data. Analysing network traffic for unusual outbound connections, especially to unexpected geographic locations or at unusual times, is a key skill for security analysts.',
            [
                ('Normal internet routing that should be ignored', False),
                ('An Indicator of Compromise (IoC) suggesting the server may be infected', True),
                ('A scheduled software update from the vendor', False),
                ('DNS resolution traffic which is always external', False),
            ]
        ),
        (
            'Africa loses approximately how much per year to cybercrime?',
            'multiple_choice',
            'Africa loses approximately 4 billion dollars per year to cybercrime, according to security researchers. This represents a massive economic drain on countries that can least afford it. As Africa\'s digital economy grows, cybercrime will grow with it unless organisations invest in cyber security. This creates enormous career opportunities for trained cyber security professionals across the continent.',
            [
                ('100 million dollars', False),
                ('500 million dollars', False),
                ('4 billion dollars', True),
                ('50 billion dollars', False),
            ]
        ),
        (
            'The best starting certification for someone new to cyber security is:',
            'multiple_choice',
            'CompTIA Security+ is widely considered the best entry point into cyber security. It covers a broad range of security concepts, is vendor-neutral, is recognised by employers worldwide, and is a US Department of Defense approved baseline certification. After Security+, you can specialise: CEH for ethical hacking, CISSP for management, OSCP for advanced penetration testing. Start with Security+ and build from there.',
            [
                ('OSCP — it shows the most practical skill', False),
                ('CEH — it is the most recognised globally', False),
                ('CompTIA Security+ — broad coverage, globally recognised, best entry point', True),
                ('CISSP — the gold standard of all security certifications', False),
            ]
        ),
    ]
)

# ============================================================
# CCTV TECHNOLOGY
# ============================================================
create_quiz(
    'CCTV Technology',
    'CCTV Technology — Final Assessment',
    'This assessment covers CCTV system design, installation, configuration and business practice. A professional CCTV installer is trusted with the security of people and property — these questions test the knowledge that trust requires.',
    25,
    [
        (
            'What is the difference between an analogue DVR system and an IP NVR system?',
            'multiple_choice',
            'Analogue systems use coaxial cable from camera to DVR where video is encoded. IP systems use Ethernet cable, and the camera itself encodes the video before sending it to the NVR over the network. IP systems generally offer higher resolution, more flexibility and easier remote access. Many modern installations use hybrid systems that support both. Understanding this difference helps you recommend the right system for each client.',
            [
                ('DVR systems are newer and more advanced than NVR systems', False),
                ('DVR is for analogue cameras via coaxial cable; NVR is for IP cameras via Ethernet', True),
                ('NVR systems can only be accessed on-site, not remotely', False),
                ('DVR and NVR are the same thing with different brand names', False),
            ]
        ),
        (
            'At what height should CCTV cameras typically be installed outdoors?',
            'multiple_choice',
            'The standard height for outdoor cameras is 2.5 to 3.5 metres. Too low and they can be tampered with or obscured. Too high and facial recognition becomes difficult — you capture the top of heads rather than faces. The goal is to capture clear facial images of people approaching entry points. Angle the camera downward at approximately 15 to 45 degrees depending on the location.',
            [
                ('1 to 1.5 metres — at eye level for clearest facial capture', False),
                ('2.5 to 3.5 metres — secure from tampering but still capturing clear facial images', True),
                ('5 to 6 metres — as high as possible to see the widest area', False),
                ('Height does not matter as long as the camera has a wide enough field of view', False),
            ]
        ),
        (
            'What does PoE mean in the context of IP CCTV systems?',
            'multiple_choice',
            'Power over Ethernet allows a single Cat5e or Cat6 cable to carry both data and power to IP cameras. This dramatically simplifies installation — instead of running a data cable AND a separate power cable to each camera, you run only one Ethernet cable. The PoE switch provides power to all connected cameras. Always check the total power draw of your cameras against the PoE budget of your switch.',
            [
                ('Proof of Evidence — the recorded footage used in legal proceedings', False),
                ('Power over Ethernet — delivers data and power through a single Ethernet cable', True),
                ('Port over Ethernet — allows multiple cameras to share one network port', False),
                ('Protocol of Encryption — secures video transmission from camera to NVR', False),
            ]
        ),
        (
            'A client\'s cameras show good live footage but recordings from last night are missing. What is the MOST likely cause?',
            'multiple_choice',
            'Missing recordings with working live view almost always indicates a storage problem — the hard drive is full and old recordings have been overwritten, the hard drive has failed, the recording schedule was not configured, or the motion detection trigger was set too conservatively. The first check is always the hard drive: is it healthy? Is it full? Is continuous or motion recording enabled? This is the most common fault call-back for CCTV installers.',
            [
                ('The cameras were powered off overnight', False),
                ('A storage issue — full drive, failed drive or recording schedule not configured', True),
                ('The NVR software needs updating', False),
                ('The cameras lose their settings when the temperature drops at night', False),
            ]
        ),
        (
            'Before installing CCTV in a business, what legal requirement must be considered in most countries?',
            'multiple_choice',
            'In most countries, displaying prominent signage informing people that CCTV is in operation is a legal requirement. The footage is also personal data subject to data protection laws — it must be stored securely, retained only as long as necessary, and only shared with authorised parties such as police or courts. Filming areas where people have a reasonable expectation of privacy (such as toilets) is illegal in virtually all jurisdictions. Always advise clients on their legal obligations.',
            [
                ('No legal requirements exist for private business CCTV installations', False),
                ('Signage must be displayed and data protection laws must be followed', True),
                ('Only government-licensed installers can legally install CCTV systems', False),
                ('CCTV is illegal in residential areas in most West African countries', False),
            ]
        ),
        (
            'How do you calculate the storage space needed for a CCTV system?',
            'multiple_choice',
            'Storage in GB = Bitrate in Mbps times 3600 seconds per hour times 24 hours times number of days divided by 8 (to convert bits to bytes) divided by 1024 (to convert MB to GB). For a practical example: a 4Mbps camera recording continuously for 30 days needs approximately 4 times 3600 times 24 times 30 divided by 8 divided by 1024 = approximately 1,265 GB or 1.25 TB. Always add 20% buffer. This calculation is essential for every installation.',
            [
                ('Storage calculation is not needed as modern NVRs adjust automatically', False),
                ('Bitrate times hours times days divided by 8 gives approximate GB required', True),
                ('Simply multiply the number of cameras by 1 TB for a standard installation', False),
                ('Only the recording resolution matters, not the bitrate', False),
            ]
        ),
        (
            'A dome camera is generally preferred over a bullet camera for indoor use because:',
            'multiple_choice',
            'Dome cameras are preferred indoors for several reasons: they are less obtrusive and blend into ceilings more discreetly, they are harder to determine which direction they are pointing (deterring people who might try to avoid them), they are more tamper-resistant, and they suit indoor aesthetics. Bullet cameras are better outdoors where their longer lens gives greater range and their housing provides better weather protection.',
            [
                ('Dome cameras have higher resolution than bullet cameras', False),
                ('Dome cameras are more discreet, tamper-resistant and the viewing direction is less obvious', True),
                ('Dome cameras are cheaper than bullet cameras for the same quality', False),
                ('Bullet cameras cannot be used indoors due to their size', False),
            ]
        ),
        (
            'When creating a CCTV quotation for a client, which approach is most professional?',
            'multiple_choice',
            'A professional CCTV installation begins with a site survey — visiting the location to understand the risks, lighting conditions, cable routes, number of cameras needed and any specific client concerns. Only after a site survey can you provide an accurate quotation. Quoting blindly leads to underpricing, missing cameras, or systems that do not meet the client\'s needs. The site survey is also an opportunity to demonstrate expertise and build trust.',
            [
                ('Give a rough price per camera over the phone to win the job quickly', False),
                ('Conduct a site survey first, then provide a detailed written quotation', True),
                ('Use a standard package price for all installations of the same size', False),
                ('Always quote the maximum possible and then discount to close the sale', False),
            ]
        ),
        (
            'What is the purpose of motion detection in a CCTV recording system?',
            'multiple_choice',
            'Motion detection triggers recording only when movement is detected in the camera\'s field of view. This dramatically reduces storage requirements — instead of 24 hours of continuous recording, you store only the periods when something is actually happening. It also makes reviewing footage much faster since you skip long periods of inactivity. The trade-off is careful calibration — set sensitivity too high and you record every leaf blowing past; too low and you miss important events.',
            [
                ('To automatically call the police when an intruder is detected', False),
                ('To reduce storage by recording only when movement is detected in the frame', True),
                ('To track and follow moving objects with the camera automatically', False),
                ('To improve image quality by increasing resolution during movement', False),
            ]
        ),
        (
            'The most effective way to grow a CCTV installation business is:',
            'multiple_choice',
            'Maintenance contracts are the foundation of a sustainable CCTV business. A one-time installation earns money once. A monthly or annual maintenance contract earns money every month or year from the same client — checking cameras, cleaning lenses, updating firmware and verifying recordings. Over time, a portfolio of maintenance contracts provides predictable recurring income that sustains the business through quiet periods. Always offer maintenance when you install.',
            [
                ('Always underprice competitors to win as many jobs as possible', False),
                ('Build a portfolio of maintenance contracts for predictable recurring income', True),
                ('Focus only on residential work as it is easier than commercial', False),
                ('Avoid maintenance work as it takes time away from new installations', False),
            ]
        ),
    ]
)

# ============================================================
# DRONES TECHNOLOGY
# ============================================================
create_quiz(
    'Drones Technology',
    'Drones Technology — Final Assessment',
    'This assessment covers drone types, regulations, operations, applications and business practice. Drones are transforming industries across Africa — this assessment tests your readiness to work professionally with this technology.',
    25,
    [
        (
            'What does UAV stand for?',
            'multiple_choice',
            'UAV stands for Unmanned Aerial Vehicle — any aircraft that operates without a human pilot on board. Drones are UAVs. They can be remotely controlled by a pilot on the ground or fly autonomously using pre-programmed flight paths and GPS waypoints. The term is used interchangeably with drone in professional and regulatory contexts.',
            [
                ('Ultra Aerial Vision', False),
                ('Unmanned Aerial Vehicle', True),
                ('Universal Aviation Vehicle', False),
                ('Unified Autonomous Vehicle', False),
            ]
        ),
        (
            'What is VLOS and why is it required for most drone operations?',
            'multiple_choice',
            'VLOS (Visual Line of Sight) means the remote pilot can see the drone at all times with the naked eye. Most aviation authorities require VLOS because it allows the pilot to see other aircraft, obstacles and people, and react immediately to avoid collisions. Flying beyond visual line of sight (BVLOS) requires special authorisation because the risks are significantly higher. Always maintain visual contact with your drone.',
            [
                ('Variable Launch Operating System — the software controlling autonomous flight', False),
                ('Visual Line of Sight — the pilot must always be able to see the drone with the naked eye', True),
                ('Vertical Landing Operations Standard — procedures for safe landing', False),
                ('VLOS is an optional safety recommendation, not a legal requirement', False),
            ]
        ),
        (
            'Zipline operates in Ghana and Rwanda delivering what type of cargo?',
            'multiple_choice',
            'Zipline is a drone delivery service that has completed over 6 million deliveries of blood, vaccines and medical supplies to remote hospitals and clinics in Ghana and Rwanda. Their fixed-wing drones fly beyond visual line of sight to locations without reliable road access, delivering critical medical supplies in minutes rather than hours. It is one of the most inspiring examples of drone technology solving an African problem.',
            [
                ('Consumer packages and e-commerce orders', False),
                ('Medical supplies including blood and vaccines to remote health facilities', True),
                ('Agricultural chemicals to farming communities', False),
                ('Mobile phone components to repair centres', False),
            ]
        ),
        (
            'Before every drone flight, which item should be checked FIRST?',
            'multiple_choice',
            'Battery condition is always the first check. A fully charged battery determines how long you can fly. A damaged or swelling battery is a fire hazard that should never be used. Battery failure mid-flight means the drone falls — potentially onto people or property. Check charge level, check for physical damage, check cell balance. Only when the battery is confirmed safe and charged should you proceed with other pre-flight checks.',
            [
                ('Camera memory card capacity', False),
                ('Battery charge level and physical condition', True),
                ('The weather forecast for the next 24 hours', False),
                ('Whether the drone firmware is the latest version', False),
            ]
        ),
        (
            'Why is agricultural drone spraying more efficient than traditional methods?',
            'multiple_choice',
            'Drone sprayers equipped with multispectral cameras and GPS can identify exactly which areas of a field need treatment and apply chemicals precisely there. This targeted approach uses significantly less chemical than blanket spraying the entire field, reduces environmental contamination, and costs less in materials. The drone can complete in hours what would take days by hand. This precision is transforming African agriculture.',
            [
                ('Drones can carry more chemical than a human sprayer', False),
                ('Drones apply chemicals precisely where needed, reducing waste and environmental impact', True),
                ('Drone spraying is faster because drones can operate at night', False),
                ('Drones eliminate the need for trained operators in agriculture', False),
            ]
        ),
        (
            'A drone pilot should obtain which type of insurance before conducting commercial operations?',
            'multiple_choice',
            'Liability insurance covers damage or injury caused by the drone during commercial operations. If a drone falls on a person, a vehicle or property, the operator can face enormous compensation claims. Without liability insurance, this comes from personal funds. All professional drone operators must carry liability insurance — clients and event organisers will often ask to see proof of insurance before allowing a drone on site.',
            [
                ('Drone theft insurance — to cover if the drone is stolen during a job', False),
                ('Third-party liability insurance — covering damage or injury caused by the drone', True),
                ('Equipment insurance — covering damage to the drone itself', False),
                ('Commercial drone operations do not require any insurance', False),
            ]
        ),
        (
            'Photogrammetry software like Pix4D or WebODM is used to:',
            'multiple_choice',
            'Photogrammetry software processes overlapping aerial photos taken by a drone to create accurate 3D maps, digital elevation models and orthomosaic images of the ground. This technology allows construction firms to survey sites, farmers to map their fields, mining companies to measure stockpiles, and governments to map land for registration — all faster and cheaper than traditional surveying methods.',
            [
                ('Edit and colour-grade drone video footage for clients', False),
                ('Process overlapping aerial photos to create accurate 3D maps and surveys', True),
                ('Control the drone autonomously without a remote pilot', False),
                ('Stream drone footage live to social media platforms', False),
            ]
        ),
        (
            'What does Return to Home (RTH) do on a modern drone?',
            'multiple_choice',
            'Return to Home automatically flies the drone back to its takeoff point and lands safely if the remote control signal is lost or battery falls below a critical level. It is a crucial safety feature. Before every flight, verify the RTH altitude is set higher than any obstacles between the drone and the home point, otherwise it may fly into a tree or building when returning. Always set RTH altitude before takeoff.',
            [
                ('Returns the drone to the manufacturer for warranty repair', False),
                ('Automatically flies the drone back to its takeoff point if signal is lost or battery is critical', True),
                ('Records the flight path so it can be repeated exactly on the next flight', False),
                ('Resets all camera settings to factory defaults', False),
            ]
        ),
        (
            'Which type of drone is best suited for long-range agricultural mapping of large farms?',
            'multiple_choice',
            'Fixed-wing drones fly like aircraft — they need a runway or launcher to take off but once airborne they are far more efficient than multirotors. A fixed-wing drone can cover hundreds of hectares on a single battery charge where a multirotor would need many battery swaps. For large-scale agricultural mapping, infrastructure inspection or environmental monitoring, fixed-wing drones are the professional choice.',
            [
                ('Quadcopter — because four rotors provide maximum stability', False),
                ('Fixed-wing drone — better efficiency and range for covering large areas', True),
                ('Hexacopter — more rotors means more redundancy and therefore better for mapping', False),
                ('Any drone can be used as they all cover the same distance per charge', False),
            ]
        ),
        (
            'The most financially sustainable drone business model is:',
            'multiple_choice',
            'Specialising in a specific vertical market — agriculture, construction, real estate or infrastructure inspection — allows you to develop deep expertise that commands higher fees, build a reputation with clients in that sector, and invest in the specific equipment those clients need. Generalists struggle to compete on price. Specialists command premium rates. Pick one sector, become the expert everyone in that sector recommends.',
            [
                ('Offering every type of drone service at the lowest possible price', False),
                ('Specialising in one sector to build deep expertise and command premium rates', True),
                ('Only doing wedding photography as it is the most consistent work', False),
                ('Renting your drone to other operators when not using it yourself', False),
            ]
        ),
    ]
)

# ============================================================
# CLOUD COMPUTING
# ============================================================
create_quiz(
    'Cloud Computing',
    'Cloud Computing — Final Assessment',
    'This assessment covers cloud concepts, storage, networking, security and career paths. Cloud computing is reshaping how businesses in West Africa operate — your expertise in this field opens significant career opportunities.',
    30,
    [
        (
            'What does IaaS mean in cloud computing?',
            'multiple_choice',
            'Infrastructure as a Service provides virtualised computing resources — virtual machines, storage and networking — over the internet. You manage the operating system, applications and data; the cloud provider manages the physical hardware, hypervisor and network infrastructure. AWS EC2, Google Compute Engine and Azure Virtual Machines are IaaS examples. This is the most flexible cloud model and requires the most technical knowledge to manage.',
            [
                ('Internet as a Service — providing internet connectivity to users', False),
                ('Infrastructure as a Service — virtualised computing resources on demand', True),
                ('Integration as a Service — connecting different software systems together', False),
                ('Intelligence as a Service — AI capabilities delivered through the cloud', False),
            ]
        ),
        (
            'What is the key characteristic of cloud computing that makes it economically attractive for African businesses?',
            'multiple_choice',
            'The pay-as-you-go model means businesses pay only for what they use, with no large upfront capital investment in servers, storage and networking infrastructure. A startup in Lagos can access the same computing power as a global corporation by paying monthly based on actual usage. This dramatically lowers the barrier to entry for technology businesses across Africa.',
            [
                ('Cloud computing is free for businesses in developing countries', False),
                ('Pay-as-you-go pricing with no large upfront infrastructure investment', True),
                ('Cloud servers are always faster than on-premise hardware', False),
                ('Cloud data is automatically backed up and can never be lost', False),
            ]
        ),
        (
            'What is a VPC (Virtual Private Cloud)?',
            'multiple_choice',
            'A VPC is a private, isolated network within the public cloud infrastructure. You define your own IP address ranges, create subnets, configure routing tables and control all traffic in and out. Your resources in a VPC are logically separated from other customers\' resources on the same physical hardware. A VPC is the foundation of any serious cloud architecture — you should always put your resources inside a properly configured VPC.',
            [
                ('A cloud-based VPN service for encrypting internet traffic', False),
                ('A private isolated network within the cloud where you control all networking', True),
                ('A virtual computer that can run multiple operating systems simultaneously', False),
                ('A provider\'s private data centre that is not connected to the public internet', False),
            ]
        ),
        (
            'Under the Shared Responsibility Model, what is the customer always responsible for in a cloud environment?',
            'multiple_choice',
            'In any cloud deployment model, the customer is always responsible for their own data, who can access it, and the security of the applications they build. The cloud provider secures the infrastructure (physical hardware, data centres, hypervisors). The customer secures everything built on top of that. Many cloud security breaches occur because customers misunderstand this division and assume the cloud provider secures their data automatically.',
            [
                ('The physical security of data centre buildings and hardware', False),
                ('The hypervisor and virtualisation layer', False),
                ('Their own data, access management and application security', True),
                ('The network backbone connecting cloud regions', False),
            ]
        ),
        (
            'What is serverless computing?',
            'multiple_choice',
            'Serverless computing (Functions as a Service) allows you to run code without provisioning or managing any servers. You write a function, upload it, and it runs automatically in response to events (an API call, a file upload, a database change). You pay only for the compute time when the function is actually running — measured in milliseconds. AWS Lambda, Google Cloud Functions and Azure Functions are the main providers. It is ideal for variable or unpredictable workloads.',
            [
                ('Computing done on a device with no operating system installed', False),
                ('Running code in response to events without managing any servers, paying only per execution', True),
                ('A type of cloud storage that does not require a server to access', False),
                ('Running applications locally without an internet connection', False),
            ]
        ),
        (
            'The 3-2-1 backup rule means:',
            'multiple_choice',
            'The 3-2-1 rule is the gold standard for data backup: keep 3 copies of data, on 2 different types of storage media, with 1 copy offsite (or in the cloud). If your only backup is on the same building as the original and the building burns down, both are lost. The offsite copy protects against site disasters. Cloud storage makes the 1 offsite copy simple and affordable for any business.',
            [
                ('Back up every 3 days, keep 2 weeks of backups, test once a month', False),
                ('3 copies of data, on 2 different media types, with 1 copy offsite', True),
                ('Back up 3 times per day, 2 locations, 1 automated test per week', False),
                ('3 full backups, 2 incremental, 1 verified restoration per quarter', False),
            ]
        ),
        (
            'AWS, Microsoft Azure and Google Cloud all offer free tier accounts. What is the main benefit of these for learners?',
            'multiple_choice',
            'Free tier accounts provide real cloud environments to learn and experiment in at no cost. AWS Free Tier gives 750 hours of EC2 per month, 5GB of S3 storage and much more for 12 months. This means any learner with an internet connection can practice real cloud skills, build real projects and prepare for cloud certifications without spending money. There is no excuse not to get hands-on experience with cloud technology.',
            [
                ('Free tiers allow businesses to run production workloads without paying', False),
                ('Free tier accounts provide a real cloud environment to learn and build skills at no cost', True),
                ('Free tiers are only available to university students with institutional email addresses', False),
                ('The free tier is simulated, not a real cloud environment', False),
            ]
        ),
        (
            'What is Infrastructure as Code (IaC)?',
            'multiple_choice',
            'Infrastructure as Code means defining and managing your cloud infrastructure (servers, networks, databases) using code files rather than manual clicks in a web console. Tools like Terraform or AWS CloudFormation read these files and automatically create or modify the infrastructure. Benefits include: reproducibility (create identical environments), version control (track every change), speed (deploy in minutes) and documentation (the code describes the infrastructure).',
            [
                ('Writing code that runs inside cloud virtual machines', False),
                ('Defining infrastructure in code files that automatically create and manage resources', True),
                ('A programming language specifically designed for cloud environments', False),
                ('Coding standards required when building applications for cloud deployment', False),
            ]
        ),
        (
            'Which AWS certification is recommended as the starting point for cloud careers?',
            'multiple_choice',
            'The AWS Cloud Practitioner is the entry-level AWS certification covering cloud concepts, AWS services overview, security basics and pricing. It requires no prior technical experience and can be prepared for in 4-8 weeks of focused study. It proves to employers that you have a solid foundation in cloud concepts. After Cloud Practitioner, the AWS Solutions Architect Associate is the most valuable mid-level certification and opens the most career opportunities.',
            [
                ('AWS Solutions Architect Professional — the most respected AWS qualification', False),
                ('AWS Cloud Practitioner — broad cloud concepts for all roles and experience levels', True),
                ('AWS DevOps Engineer — the most in-demand cloud specialisation', False),
                ('AWS Security Specialty — essential as security is the biggest cloud concern', False),
            ]
        ),
        (
            'Cloud computing is particularly valuable for West African businesses because:',
            'multiple_choice',
            'Unreliable power supply is one of the biggest operational challenges for businesses across West Africa. Running on-premise servers requires expensive generator backup, UPS systems and sophisticated power management. Cloud computing moves all of that burden to the cloud provider — your data and applications run in well-powered, redundant data centres regardless of what is happening to your local electricity supply. This is a genuine competitive advantage of cloud over on-premise infrastructure in Africa.',
            [
                ('Cloud data centres are located in Africa and therefore have faster speeds', False),
                ('Cloud eliminates dependence on local infrastructure including unreliable power supply', True),
                ('Cloud computing is heavily subsidised for African businesses by international donors', False),
                ('African governments require businesses above a certain size to use cloud computing', False),
            ]
        ),
    ]
)

# ============================================================
# ROBOTICS TECHNOLOGY
# ============================================================
create_quiz(
    'Robotics Technology',
    'Robotics Technology — Final Assessment',
    'This assessment tests your understanding of robotics fundamentals, programming, sensing, applications and career pathways. Robotics is one of the fastest-growing fields in Africa — you are positioning yourself at the forefront of this revolution.',
    30,
    [
        (
            'What are the three essential components of any robot?',
            'multiple_choice',
            'Every robot, from the simplest Arduino-controlled car to a sophisticated industrial arm, must have these three elements: sensors to perceive the environment, a controller (processor) to make decisions based on sensor input, and actuators to take action in the world. Without sensors the robot is blind. Without a controller it cannot think. Without actuators it cannot act. Understanding this fundamental structure is the starting point for all robotics.',
            [
                ('Wheels, camera and battery', False),
                ('Sensors, controller and actuators', True),
                ('Motors, frame and programming language', False),
                ('CPU, GPU and memory', False),
            ]
        ),
        (
            'In Arduino programming, what does the void loop() function do?',
            'multiple_choice',
            'The void loop() function runs repeatedly and continuously after the setup() function completes. It is the main operating loop of the Arduino program. All the robot\'s ongoing behaviour — reading sensors, making decisions, controlling motors — happens inside loop(). It keeps running until power is removed. This is different from typical programming where code runs once — in robotics, continuous sensing and responding is the normal operating mode.',
            [
                ('Runs once when the Arduino first powers on', False),
                ('Runs repeatedly and continuously — the main operating loop of the program', True),
                ('Handles errors and exceptions in the program', False),
                ('Defines which pins are inputs and which are outputs', False),
            ]
        ),
        (
            'What type of control algorithm is most commonly used in robotics to correct errors between desired and actual position?',
            'multiple_choice',
            'PID (Proportional-Integral-Derivative) control is the most widely used control algorithm in robotics and industrial automation. It continuously measures the difference (error) between where a robot is and where it should be, and adjusts the output accordingly. The P component responds to current error, I corrects accumulated past error, D predicts future error from the rate of change. Understanding PID is fundamental to working with any servo, motor or position control system.',
            [
                ('On-off control (bang-bang control)', False),
                ('PID (Proportional-Integral-Derivative) control', True),
                ('Random search algorithm', False),
                ('Machine learning neural network', False),
            ]
        ),
        (
            'An HC-SR04 ultrasonic sensor works by:',
            'multiple_choice',
            'The HC-SR04 sends out a burst of ultrasonic sound (40kHz, above human hearing). When this sound hits an object, it bounces back. The sensor measures the time between sending and receiving the echo. Since the speed of sound in air is approximately 343 metres per second, the distance can be calculated: distance = (time times 343) divided by 2 (divided by 2 because the sound travels there and back). This is the same principle as sonar used in submarines and bats.',
            [
                ('Using infrared light to measure the brightness reflected from objects', False),
                ('Sending sound pulses and measuring the time for echoes to return', True),
                ('Measuring the magnetic field distortion caused by nearby metal objects', False),
                ('Using a laser to scan the environment and build a 3D map', False),
            ]
        ),
        (
            'Collaborative robots (cobots) differ from traditional industrial robots in that they:',
            'multiple_choice',
            'Traditional industrial robots operate in caged-off areas because they move fast and with great force — contact with a human would cause serious injury. Cobots are specifically designed to work alongside humans safely. They use force sensing and advanced control to detect unexpected contact and stop or slow down immediately. They move more slowly and are programmed to treat human contact as a safety signal. This makes them suitable for small and medium businesses where full automation is not practical.',
            [
                ('Are much faster and stronger than traditional robots', False),
                ('Are designed to work safely alongside humans without safety cages', True),
                ('Can program themselves without human input', False),
                ('Only work with specific branded control software', False),
            ]
        ),
        (
            'OpenCV is a library used for:',
            'multiple_choice',
            'OpenCV (Open Source Computer Vision Library) is the most widely used library for computer vision — processing images and video to extract meaningful information. It runs in Python and C++ and allows robots and programs to detect faces, recognise objects, track motion, read text, analyse colour and much more. It is free and open source. Learning OpenCV opens the door to building intelligent visual systems for robotics, security and any application that needs to understand images.',
            [
                ('Creating 3D models for 3D printing from CAD designs', False),
                ('Computer vision — processing images and video to detect objects and patterns', True),
                ('Optimising robot motor control algorithms', False),
                ('Visualising circuit diagrams for robot electronics', False),
            ]
        ),
        (
            'The First Robotics Competition (FIRST) is significant for Africa because:',
            'multiple_choice',
            'FIRST Robotics competitions are growing across Africa, engaging secondary school students in team-based robot building challenges. These competitions develop technical skills (mechanical, electrical, programming) but also teamwork, project management, presentation and professional skills. Students who compete in FIRST have documented pathways into engineering universities and technology careers. The African Robotics Network actively supports these competitions across the continent.',
            [
                ('It trains professional robot technicians who work in African factories', False),
                ('It engages secondary school students in robotics, building skills and creating pathways to STEM careers', True),
                ('It is a competition only for university graduates with engineering degrees', False),
                ('It produces robots that are donated to African hospitals and schools', False),
            ]
        ),
        (
            'A line-following robot uses IR sensors to navigate. If the LEFT sensor detects the line, the robot should:',
            'multiple_choice',
            'In line-following robot logic, sensors detect when they are ON the line (usually black on white). If the left sensor detects the line, the robot has drifted to the left of the line — so it needs to turn right to get back on track. If the right sensor detects the line, turn left. If both detect the line, go straight. This simple logic is the foundation of line-following robots used in warehouses, factories and educational competitions worldwide.',
            [
                ('Turn left to follow the line it has detected', False),
                ('Turn right to bring the robot back onto the line it has drifted left of', True),
                ('Stop and wait for further sensor input', False),
                ('Speed up to compensate for the drift', False),
            ]
        ),
        (
            'Which programming language is most recommended for beginners starting in robotics?',
            'multiple_choice',
            'Python is the most recommended language for robotics beginners and is increasingly used in professional robotics. It has simple, readable syntax that reduces the time from learning to building. It has excellent libraries for robotics (ROS), computer vision (OpenCV), machine learning (TensorFlow, PyTorch) and hardware control (RPi.GPIO for Raspberry Pi). The ROS (Robot Operating System) framework — the professional standard for robotics — supports Python extensively.',
            [
                ('Assembly language — closest to the hardware and fastest', False),
                ('Python — readable syntax, excellent robotics libraries and professional support', True),
                ('Java — the most widely used programming language overall', False),
                ('Scratch — the most visual and easiest to understand', False),
            ]
        ),
        (
            'Robots are often described as taking jobs from humans. The historical evidence from previous industrial revolutions suggests:',
            'multiple_choice',
            'Historical evidence from previous waves of automation (steam power, electricity, computers) shows that while automation does eliminate specific jobs, it also creates new categories of jobs and increases overall productivity and living standards. The key is the transition period — workers need retraining to take on new roles. In Africa specifically, robotics and automation are more likely to create manufacturing capacity that did not previously exist, potentially creating more jobs overall, though the types of skills needed will change.',
            [
                ('Automation always leads to permanent unemployment and economic decline', False),
                ('Automation eliminates some jobs but historically creates new job categories and raises living standards, though transition requires retraining', True),
                ('Robots will completely replace all human workers within 10 years', False),
                ('African economies are immune to automation because labour costs are lower', False),
            ]
        ),
    ]
)

# ============================================================
# ETHICAL HACKING
# ============================================================
create_quiz(
    'Ethical Hacking',
    'Ethical Hacking — Final Assessment',
    'This assessment tests your knowledge of ethical hacking methodology, tools, web application security and professional practice. Remember: every skill you learn here is for defence. The best defenders understand how attackers think.',
    35,
    [
        (
            'The most important rule in ethical hacking is:',
            'multiple_choice',
            'Written authorisation is the absolute foundation of ethical hacking. Without it, every technique in this course is a criminal offence. This is non-negotiable regardless of your intentions, your relationship with the organisation or their informal agreement. Get it in writing, define the scope, and keep the document. It protects you legally and professionally. Professional penetration testers treat authorisation as sacred.',
            [
                ('Never use Metasploit as it can damage production systems', False),
                ('Always obtain written authorisation before testing any system', True),
                ('Only test systems that are clearly labelled as insecure', False),
                ('Verbal permission from any IT staff member is sufficient', False),
            ]
        ),
        (
            'What does OSINT stand for and what is it used for in penetration testing?',
            'multiple_choice',
            'OSINT (Open Source Intelligence) is the collection of information from publicly available sources — websites, social media, domain registration records, job advertisements, company filings. In penetration testing, the reconnaissance phase uses OSINT to build a picture of the target without touching their systems. This reveals technology stacks, employee names, email formats, office locations and potential attack surfaces — all gathered passively with no legal risk.',
            [
                ('Operating System Intelligence — scanning for OS vulnerabilities remotely', False),
                ('Open Source Intelligence — gathering information from publicly available sources', True),
                ('Offensive Security Intelligence — active probing of target systems', False),
                ('Online Systems Investigation Tool — a specific software package for network mapping', False),
            ]
        ),
        (
            'Nmap is described as the essential reconnaissance tool. What does it primarily do?',
            'multiple_choice',
            'Nmap (Network Mapper) discovers which hosts are on a network, which ports are open on those hosts, what services are running on those ports and which operating system the host is using. This information forms the foundation of any penetration test — you cannot attack what you do not know exists. Nmap is free, powerful and used by security professionals and attackers worldwide. Understanding its output is a fundamental skill.',
            [
                ('Creates and delivers exploit payloads to vulnerable systems', False),
                ('Discovers hosts, open ports, running services and operating systems on a network', True),
                ('Decrypts and analyses encrypted network traffic', False),
                ('Tests web applications for SQL injection vulnerabilities', False),
            ]
        ),
        (
            'SQL injection is dangerous because:',
            'multiple_choice',
            'SQL injection allows an attacker to manipulate the database queries an application makes. A successfully exploited SQL injection can reveal all data in the database (including passwords, personal data, financial records), allow the attacker to bypass authentication entirely by injecting logic that always returns true, modify or delete data, and sometimes execute commands on the underlying server. It has been consistently in the OWASP Top 10 for over 20 years because it remains extremely common in poorly developed applications.',
            [
                ('It slows down the database server to prevent legitimate users from accessing it', False),
                ('It allows manipulation of database queries, potentially exposing or modifying all data', True),
                ('It installs malware on the client\'s browser through the web page', False),
                ('It intercepts and reads data transmitted between the browser and server', False),
            ]
        ),
        (
            'The OWASP Top 10 is important for web application security because:',
            'multiple_choice',
            'The OWASP (Open Web Application Security Project) Top 10 lists the most critical security risks to web applications, updated based on real-world data from security professionals worldwide. It provides a shared language for developers and security professionals, prioritises where to focus testing and remediation effort, and is referenced in many security standards and regulatory frameworks. Any web application security assessment should cover the OWASP Top 10 as a minimum.',
            [
                ('It lists the ten most popular hacking tools used by criminals', False),
                ('It identifies the ten most critical web application security risks based on real-world data', True),
                ('It provides ten rules that guarantee a web application cannot be hacked', False),
                ('It ranks the ten most secure programming languages for web development', False),
            ]
        ),
        (
            'What is a Meterpreter shell in Metasploit?',
            'multiple_choice',
            'Meterpreter is an advanced post-exploitation payload that, once loaded on a target system, gives the attacker a powerful interactive session. Unlike a basic shell, Meterpreter runs in memory (leaving fewer traces), supports many built-in commands for file manipulation, network pivoting, privilege escalation, screenshot capture and keylogging. Understanding Meterpreter helps defenders know what attackers can do after gaining initial access — which is why containment of breaches is as important as prevention.',
            [
                ('A tool for scanning networks to find vulnerable services', False),
                ('An advanced post-exploitation payload providing interactive control of a compromised system', True),
                ('A password cracking tool that uses dictionary attacks', False),
                ('A network protocol analyser for capturing and decoding traffic', False),
            ]
        ),
        (
            'In a penetration test report, what should the executive summary contain?',
            'multiple_choice',
            'The executive summary is written for non-technical decision-makers — the CEO, board of directors, or senior management who will approve budget and policy changes based on the findings. It should explain in plain language what was tested, what was found, and what the business risk is. Avoid technical jargon. Focus on business impact: what could an attacker do with the vulnerabilities found? A good executive summary persuades management to invest in fixing the issues.',
            [
                ('Detailed technical descriptions of every vulnerability found with proof-of-concept code', False),
                ('A non-technical overview of what was tested, what was found and the business risk', True),
                ('The complete list of tools and commands used during the test', False),
                ('Only the vulnerabilities rated Critical or High severity', False),
            ]
        ),
        (
            'TryHackMe and HackTheBox are valuable because they:',
            'multiple_choice',
            'TryHackMe and HackTheBox provide intentionally vulnerable virtual machines and guided challenges that you can legally attack to practice your skills. They are structured learning environments with real technical challenges — not simulations. TryHackMe is better for beginners (more guided). HackTheBox is more challenging and closer to real penetration testing. Both are free to start and both are recognised by employers as evidence of practical skill development.',
            [
                ('Allow you to practice hacking real company systems in a controlled way', False),
                ('Provide legal, structured environments to practice penetration testing skills', True),
                ('Give you a qualification equivalent to CEH or OSCP without an exam', False),
                ('Connect you with clients who need penetration testing services', False),
            ]
        ),
        (
            'Credential stuffing attacks use:',
            'multiple_choice',
            'Credential stuffing uses large lists of username and password combinations from previous data breaches — billions of these are publicly available on criminal forums. Attackers automate login attempts across multiple websites knowing that many people reuse passwords. If you used the same password on a breached site and your bank, attackers will try that password on your bank. This is why unique passwords for every account and MFA are so important.',
            [
                ('Specially crafted password guesses based on personal information about the target', False),
                ('Username and password pairs from previous data breaches to attempt logins on other sites', True),
                ('Brute force of all possible password combinations', False),
                ('Social engineering to trick users into revealing their passwords', False),
            ]
        ),
        (
            'After completing this course, the most appropriate next certification to pursue is:',
            'multiple_choice',
            'CompTIA Security+ is the globally recommended entry point into cyber security careers. It validates foundational security knowledge, is vendor-neutral, is recognised by employers worldwide, and after Security+ you can specialise in any direction — ethical hacking (CEH, OSCP), management (CISSP, CISM), cloud security, or incident response. It is also a prerequisite for many higher-level certifications. After Security+, the eJPT (eLearnSecurity Junior Penetration Tester) provides a practical ethical hacking entry point.',
            [
                ('OSCP immediately — it is the most respected and demonstrates real skill', False),
                ('CompTIA Security+ — the recognised entry-level foundation for all cyber security careers', True),
                ('A university degree in computer science before any certification', False),
                ('CEH — specifically designed for ethical hackers so most relevant to this course', False),
            ]
        ),
    ]
)

# ============================================================
# SUMMARY
# ============================================================
print('\n' + '='*60)
from certifications.models import Quiz
for q in Quiz.objects.all().order_by('course__title'):
    print(f'  {q.course.title}: {q.questions.count()} questions')
print(f'\nTotal quizzes: {Quiz.objects.count()}')
total_q = sum(q.questions.count() for q in Quiz.objects.all())
print(f'Total questions: {total_q}')