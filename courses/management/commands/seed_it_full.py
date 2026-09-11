from django.core.management.base import BaseCommand
from courses.models import Category, Course, Lesson

class Command(BaseCommand):
    def handle(self, *args, **options):
        cat_it = Category.objects.get(pillar="it-technology")
        cat_beauty = Category.objects.get(pillar="beauty-personal-care")
        cat_gov = Category.objects.get(pillar="government-social-impact")

        lessons_20 = [
            ("Why This is Goldmine in Aba - 2026 Market", "video"),
            ("Tools Needed - Prices in Ariaria/Computer Village", "pdf"),
            ("Safety & Setup", "video"),
            ("Theory - Simple English + Igbo", "video"),
            ("Practical Demo 1", "video"),
            ("Intermediate Step by Step", "video"),
            ("Practical Demo 2 - Real Job", "video"),
            ("Advanced Expert", "video"),
            ("How to Charge & Get Customers", "text"),
            ("Where to Buy Materials Cheap", "text"),
            ("Pricing Template - 2026 Prices", "pdf"),
            ("Marketing - WhatsApp, Facebook", "text"),
            ("Mobile Service - Extra Income", "text"),
            ("Saving & Expanding", "text"),
            ("Branding, Receipt, Warranty", "text"),
            ("Common Mistakes & Troubleshooting", "text"),
            ("Final Practical - 3 Real Jobs", "video"),
            ("Business Plan - Start with ₦50k", "pdf"),
            ("Mentorship - Find Master", "text"),
            ("Next Steps - Earning", "text"),
        ]

        it_courses = [
            ("Computer Literacy Basics - What is Computer? For Complete Beginners", "What is computer, types, desktop, laptop, tablet, phone, history, uses in Aba business, turn on/off, mouse, keyboard"),
            ("Parts of Computer - Inside & Outside - Full Identification with Pictures", "CPU, RAM, HDD, SSD, Motherboard, Power Supply, Cabinet, open and identify, function of each"),
            ("Input Devices Masterclass - Keyboard, Mouse, Microphone, Joystick, Scanner, Webcam, Touchpad, Stylus, Barcode Reader, Biometric, Light Pen, Touch Screen, Digital Camera, MIDI, OMR, OCR", "All input devices, how they work, types, repair, maintenance, Aba prices, USB, wireless"),
            ("Output Devices Masterclass - Monitor Types CRT LCD LED OLED, Printer Types Inkjet Laser Dot Matrix 3D, Speaker, Projector, Plotter, Headphones, Braille Display", "All output devices, resolution, repair, ink refill business in Aba, maintenance"),
            ("Storage Devices - Ancient to Modern - Floppy, CD DVD, USB Flash, External HDD, SSD NVMe M.2, Memory Card SD MicroSD, Cloud, NAS", "Storage evolution, sizes GB TB, shapes, prices in Computer Village Lagos/Aba, data recovery, formatting"),
            ("Windows OS Mastery - Windows 7, 10, 11 - Installation, Partitioning, Drivers, Settings, Control Panel, File Explorer", "Install Windows from bootable USB, create partition, install drivers, Windows Update, for Aba cyber cafe business, activation"),
            ("Microsoft Word Complete - From Typing to Professional CV, Letter, Business Proposal", "Word for Aba - Type letter, CV, business proposal, formatting, tables, mail merge, header footer, save as PDF"),
            ("Microsoft Excel Complete - From SUM to Shop Accounting, Charts, Pivot", "Excel for Aba shops - Sales record, profit, loss, SUM, IF, VLOOKUP, charts, filter, for market women, inventory"),
            ("Microsoft PowerPoint Complete - Presentations for Church, School, Business Pitch", "PowerPoint for Aba - Make slides for shop, church, school, animations, transitions, present"),
            ("Internet & Email Mastery - Browse, Search Google, Gmail Yahoo, Send CV, Apply Jobs Online", "Internet for beginners, create Gmail, compose, attach CV, CC BCC, Google search tricks, apply for jobs on Jobberman"),
            ("Social Media for Business - Facebook Page, WhatsApp Business, Instagram, TikTok, YouTube for Aba Market", "Sell via WhatsApp Status, Catalog, Facebook Marketplace, Instagram Reels, TikTok, YouTube channel monetization"),
            ("Database Management System - Access, MySQL, Excel as Database for Aba Shops", "Database for shops - Customer records, stock, tables, primary key, queries, forms, reports, introduction to DBMS"),
            ("Software Types - System vs Application, Open Source LibreOffice VLC GIMP vs Paid, Antivirus, Installation", "System software, application, open source save money, install/uninstall, antivirus Avast, Windows Defender, crack vs legit"),
            ("Operating Systems Deep Dive - Windows, Mac OS, Linux Ubuntu Mint, Chrome OS, Android, iOS Comparison", "Compare OS, advantages, when to use, dual boot Windows + Ubuntu, Mac OS for creatives, Chrome OS for school"),
            ("Graphics Design Mastery - Text, Images, Logos - Canva Free, Photoshop, CorelDRAW, Illustrator for Aba", "Design flyers, posters, logos for Aba shops - Canva free templates, Photoshop layers, CorelDRAW, charge ₦3k-₦20k per design"),
            ("Computer Assembling & Building - Buy Parts in Computer Village Lagos, Assemble, Sell for Profit", "Buy parts: motherboard, CPU, RAM, HDD, PSU, case, assemble desktop step by step, cable management, first boot, sell"),
            ("Computer Repair & Maintenance - Slow Computer, Virus Removal, Formatting, Blue Screen, Beep Codes", "Repair business - Slow, virus, blue screen BSOD, beep codes, thermal paste, RAM reseat, charge ₦5k-₦15k in Aba"),
            ("Mac OS Mastery - MacBook Pro, Air, iMac for Aba Photographers, Video Editors, Musicians", "Mac OS for creatives, Finder, Dock, install apps, Final Cut Pro, Logic Pro, Time Machine backup, for Aba media"),
            ("Linux Mastery - Ubuntu, Linux Mint, Zorin OS - Free OS for Aba Cyber Cafe & Programmers", "Linux free save money, install Ubuntu, terminal commands ls cd mkdir, install software, for programmers, cyber cafe"),
            ("Cyber Security Essentials - Protect Aba POS, Bank Account, Facebook from Hackers & Scammers", "Password strong, 2FA, phishing email, Yahoo boys, protect POS business, bank, Facebook hacked recovery, backup"),
            ("Cloud Computing - Google Drive 15GB Free, Dropbox, OneDrive, Google Docs for Aba Business Backup", "Cloud for Aba - Backup shop records, photos, access anywhere, share files, Google Drive, Docs, Sheets collaboration"),
            ("CCTV Installation & Business - Install Cameras, DVR, View on Phone for Aba Shops & Homes", "CCTV for Aba - Analog vs IP camera, DVR NVR, BNC, RJ45, install, configure, view on phone, charge ₦80k-₦250k per job"),
            ("Drone Technology - Build, Fly, Photography, Videography, Farm Mapping, Delivery in Aba", "Drone for Aba - DJI, build FPV from kit, fly, aerial wedding photography, farm survey, regulations in Nigeria"),
            ("Robotics Introduction - Arduino Uno, Sensors, Motors, Build Line Follower Robot for Aba Youth Competition", "Robotics for beginners, Arduino IDE, LED blink, ultrasonic sensor, servo, build line follower, sumo robot, for schools"),
            ("AI Technology for Aba - ChatGPT, Gemini, AI Image Midjourney, AI Video, AI Voice to Make Money", "AI for Aba - Use ChatGPT to write business proposal, AI image for flyer, AI video for advert, AI voiceover, make money online"),
            ("CompTIA A+ Certification Complete Prep - Hardware, Software, Troubleshooting - International Job", "CompTIA A+ 1101 1102, hardware, networking, mobile, troubleshooting, exam prep, get job abroad, $30k salary"),
            ("CompTIA Network+ Certification - LAN, WAN, WiFi, Router, Switch, Crimping RJ45 for Aba Network", "Network+ N10-008, OSI model, TCP IP, subnetting, crimp RJ45, setup router TP-Link, switch, WiFi, cyber cafe network"),
            ("CompTIA Security+, CCNA, Microsoft, AWS - Certification Roadmap from Aba to Global IT Career", "Security+ SY0-601, CCNA 200-301, Microsoft AZ-900, AWS Cloud Practitioner, roadmap, study plan, exam cost, career path"),
            ("Computer Networking Practical - Crimping, Router Config, Switch, WiFi Extender for Aba Office", "Networking practical - Tools: crimper, tester, crimp RJ45 straight vs crossover, configure TP-Link router, WiFi password, extend"),
            ("IT Entrepreneurship - How to Start Computer Business in Aba with ₦100k - Cyber Cafe, Sales, Training", "IT business ideas - Cyber cafe 5 systems, computer sales, phone accessories, training center, POS, business plan, profit calculation"),
            ("Microsoft Office Suite Mastery - Word Excel PowerPoint Access Outlook Publisher Combined for Office Job", "Office suite combined, real office tasks, create invoice, report, presentation, email, get office job in Aba"),
            ("Data Entry & Typing Mastery - 50 WPM, Excel Data Entry for Aba Companies & Freelancing", "Typing speed, Mavis Beacon, data entry, Excel, earn from Upwork, Fiverr, for Aba youths"),
            ("Hardware Repair Advanced - Laptop Motherboard, Screen Replacement, Keyboard, Battery, Charging Port", "Laptop repair - Screen replace ₦25k, keyboard ₦8k, battery, charging port, motherboard diagnosis, boardview"),
            ("Software Development Intro - HTML, CSS, JavaScript, Python for Aba Youths - Build Website", "Coding for beginners, HTML tags, CSS, JavaScript alert, Python print, build simple website for Aba shop"),
            ("Digital Literacy for Market Women & Elders - How to Use Smartphone, WhatsApp, Mobile Banking", "Smartphone for mama, make call, WhatsApp video, mobile banking OPay, PalmPay, send money, for inclusion"),
        ]

        # Seed IT
        for title, desc in it_courses:
            course, created = Course.objects.get_or_create(
                category=cat_it, title=title,
                defaults={
                    "description": f"{desc} - Comprehensive IT course for poor Africans, Aba-focused, from zero to job-ready. Practical, simple English, Igbo explanation, market prices in Computer Village Lagos/Aba, business ideas. {desc}",
                    "level": "beginner", "age_group": "all", "learning_approach": "heutagogic",
                    "duration_hours": 60, "learning_objectives": desc,
                    "is_active": True, "featured": True
                }
            )
            if course.lessons.count() < 15:
                for idx, (lt, ct) in enumerate(lessons_20, 1):
                    Lesson.objects.get_or_create(
                        course=course, order=idx,
                        defaults={
                            "title": f"{idx}. {lt}",
                            "content": f"FULL DETAILED LESSON: {lt} for IT course '{title}'. {desc}. Step by step with pictures, tools needed with prices in Computer Village Lagos & Aba (Faulks Road), safety, common mistakes, how to charge customer, real workshop photos. Simple English + Igbo summary. Goal: You can do this job and earn money immediately. For poor Africans - no big grammar, practical only. Business tips for Aba youth.",
                            "content_type": ct, "duration_minutes": 45
                        }
                    )

        # Seed Beauty remaining
        beauty_extra = [
            ("Hair Dressing & Wig Making - Aba Women Money Maker", "Make wigs, braids, Ghana weaving, wig ₦15k-₦50k, business for women in Aba"),
            ("Makeup & Gele Tying for Aba Weddings - Bridal Makeup", "Makeup for weddings - Charge ₦20k-₦50k per bride, gele tying styles, Aba brides"),
            ("Manicure, Pedicure & Nail Fixing Business in Aba", "Nail fixing, acrylic, gel, manicure pedicure - Charge ₦2k-₦5k, shop business"),
        ]
        for title, desc in beauty_extra:
            course, created = Course.objects.get_or_create(
                category=cat_beauty, title=title,
                defaults={
                    "description": desc + " - Comprehensive beauty course for poor Africans, Aba-focused",
                    "level": "beginner", "age_group": "adult", "learning_approach": "andragogic",
                    "duration_hours": 60, "learning_objectives": desc,
                    "is_active": True, "featured": True
                }
            )
            if course.lessons.count() < 15:
                for idx, (lt, ct) in enumerate(lessons_20, 1):
                    Lesson.objects.get_or_create(course=course, order=idx, defaults={"title": f"{idx}. {lt}", "content": f"Detailed: {lt} for {title}. {desc}", "content_type": ct, "duration_minutes": 45})

        # Seed Gov
        gov_courses = [
            ("N-Power & Government Grants - How to Apply & Win - BOI, SMEDAN, YouWin", "Apply for FG grants, BOI, SMEDAN, N-Power, YouWin for Aba youths, write proposal"),
            ("NGO & Community Development - Start Foundation in Aba, Get Funding", "Start NGO, CAC, write proposal, get funding from donor, community project"),
            ("Youth Leadership & Politics - Become Leader in Aba, Community Service", "Leadership for Aba youths, community, politics, become councilor, chairman"),
        ]
        for title, desc in gov_courses:
            course, created = Course.objects.get_or_create(
                category=cat_gov, title=title,
                defaults={
                    "description": desc, "level": "beginner", "age_group": "adult", "learning_approach": "andragogic",
                    "duration_hours": 40, "learning_objectives": desc, "is_active": True, "featured": True
                }
            )
            if course.lessons.count() < 15:
                for idx, (lt, ct) in enumerate(lessons_20, 1):
                    Lesson.objects.get_or_create(course=course, order=idx, defaults={"title": f"{idx}. {lt}", "content": f"Detailed: {lt} for {title}. {desc}", "content_type": ct, "duration_minutes": 45})

        print(f"TOTAL: {Course.objects.filter(is_active=True).count()} courses, {Lesson.objects.count()} lessons")