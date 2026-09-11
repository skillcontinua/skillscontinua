from django.core.management.base import BaseCommand
from courses.models import Category, Course, Lesson

class Command(BaseCommand):
    def handle(self, *args, **options):
        lessons_20 = [
            ("Why This Business is Goldmine in Aba - Market Analysis 2026", "video"),
            ("Tools Needed - Full List with Prices in Ariaria Market", "pdf"),
            ("Safety & Workshop Setup", "video"),
            ("Theory Basics - Simple English + Igbo", "video"),
            ("Practical Demo 1 - Hands On", "video"),
            ("Intermediate - Step by Step", "video"),
            ("Practical Demo 2 - Real Job", "video"),
            ("Advanced Expert Level", "video"),
            ("How to Charge & Get Customers in Aba", "text"),
            ("Where to Buy Materials Cheap", "text"),
            ("Pricing Template - 2026 Aba Prices", "pdf"),
            ("Marketing - Parks, Markets, WhatsApp", "text"),
            ("Mobile Service - Extra Income", "text"),
            ("Saving & Expanding - 1 to 5 Boys", "text"),
            ("Branding, Receipt, Warranty", "text"),
            ("Common Mistakes & Troubleshooting", "text"),
            ("Final Practical - 3 Real Jobs", "video"),
            ("Business Plan - Start with ₦50k", "pdf"),
            ("Mentorship - Find Master in Aba", "text"),
            ("Next Steps - Earning", "text"),
        ]

        # B) RENEWABLE ENERGY EXPANDED
        renewable_courses = [
            ("Wind Power - Build Small Wind Turbine for Aba Farm", "Wind turbine from scrap, charge battery, power farm house - Aba rural areas with wind"),
            ("Mini Hydro - Village Stream Power - Build from Stream in Abia Village", "Micro hydro 1kW-10kW from village stream, power 10 homes, stream mapping"),
            ("Fossil Fuel Generator Mastery - I-Better-Pass-My-Neighbor Repair & Business", "Repair Tiger, Sumec generators - Every home in Aba needs you, oil change, carburetor"),
            ("Flywheel Energy Storage with DC Motor - Build Free Energy System", "Flywheel with DC motor, store energy, release, battery charging, physics explained simple"),
            ("Flywheel with Spring Mechanism - Mechanical Energy Storage", "Spring flywheel, clockwork, mechanical storage for low-cost power"),
            ("Battery Technology - Lead Acid, Lithium, Tubular - Repair & Rebuild", "Battery repair, desulfation, lithium pack building, BMS, second life battery business"),
            ("Hybrid Solar-Wind-Battery System - Complete Off-Grid for Aba", "Combine solar + wind + battery, automatic changeover, power Aba shop 24/7"),
            ("Bio Gas from Waste - Build Bio Gas for Aba Homes", "Bio gas from kitchen waste, cow dung, power cooking, save gas money"),
        ]

        # C) 15TH PILLAR - IT TECHNOLOGY COMPREHENSIVE (30 courses)
        it_courses = [
            ("Computer Literacy Basics - What is Computer? For Complete Beginners", "What is computer, types, desktop, laptop, tablet, phone, history, uses in Aba business"),
            ("Parts of Computer - Inside & Outside - Full Identification", "CPU, RAM, Hard Disk, Motherboard, Power Supply, Cabinet - Open and identify each part"),
            ("Input Devices - Keyboard, Mouse, Microphone, Joystick, Scanner, Webcam, Touchpad, Stylus, Barcode Reader, Biometric", "All input devices, how they work, repair, maintenance, Aba market prices"),
            ("Output Devices - Monitor, Printer, Speaker, Projector, Plotter, Headphones - Repair & Maintenance", "CRT, LCD, LED monitors, inkjet, laser printers, repair, ink refill business in Aba"),
            ("Storage Devices - USB, External HDD, SSD, Memory Card, CD/DVD, Cloud Storage - Ancient to Modern", "Floppy ancient to NVMe modern, sizes, shapes, prices in Aba, data recovery"),
            ("Windows Operating System Mastery - Windows 7, 10, 11 Installation & Use", "Install Windows, drivers, settings, control panel, file explorer, for Aba cyber cafe business"),
            ("Microsoft Word - Complete - From Typing to Professional Documents", "Word for Aba - Type letter, CV, business proposal, formatting, tables, mail merge"),
            ("Microsoft Excel - Number Work - From Sum to Business Accounting", "Excel for Aba shops - Sales record, profit, loss, formulas, charts, for market women"),
            ("Microsoft PowerPoint - Presentations for Business & School", "PowerPoint for Aba - Make presentation for shop, church, school, business pitch"),
            ("Internet & Email - Browse, Search, Gmail, Yahoo, Send CV, Apply Jobs", "Internet for beginners, create email, send email with attachment, search Google, apply for jobs online"),
            ("Social Media Mastery - Facebook, WhatsApp Business, Instagram, TikTok for Aba Business", "Social media for Aba market women, sell via WhatsApp Status, Facebook Page, Instagram"),
            ("Database Management System - Access, MySQL, Introduction for Aba Businesses", "Database for shops - Keep customer records, stock, introduction to DBMS, tables, queries"),
            ("Software - Types, Open Source vs Paid, Installation, Antivirus", "System software, application software, open source LibreOffice, VLC, antivirus installation"),
            ("Operating Systems Deep Dive - Windows, Mac OS, Linux Ubuntu, Chrome OS, Android", "Compare OS, when to use which, install Linux Ubuntu dual boot, Mac OS appreciation"),
            ("Graphics Design - Text, Images, Logos - Canva, Photoshop, CorelDRAW for Aba Businesses", "Design flyers, logos for Aba shops - Canva free, Photoshop basics, logo design charge ₦5k"),
            ("Computer Assembling & Building - Build Computer from Scratch - Hardware & Software", "Buy parts in Aba/Computer Village Lagos, assemble desktop, install OS, drivers, sell for profit"),
            ("Computer Repair & Maintenance - Troubleshooting, Formatting, Virus Removal", "Repair business - Slow computer, virus, blue screen, formatting, charge ₦5k-₦15k in Aba"),
            ("Mac OS Mastery - For Aba Creatives & Video Editors", "MacBook for Aba photographers, video editors, install Mac OS, use Final Cut, Logic"),
            ("Linux Mastery - Ubuntu, Mint for Aba Cyber Cafe & Programmers", "Linux for Aba - Install Ubuntu, terminal, free OS save money, for programmers"),
            ("Cyber Security Basics - Protect Aba Businesses from Hackers, Scammers", "Password, 2FA, phishing, scam in Aba, protect POS, bank account, Facebook hack"),
            ("Cloud Computing - Google Drive, Dropbox, OneDrive for Aba Businesses", "Cloud for Aba - Backup shop records, photos, access anywhere, Google Drive 15GB free"),
            ("CCTV Installation & Business - Install CCTV for Aba Shops, Homes", "CCTV for Aba - Install cameras, DVR, view on phone, charge ₦80k-₦200k per installation"),
            ("Drone Technology - Build, Fly, Photography, Farming in Aba", "Drone for Aba - Aerial photography for weddings, farm mapping, build from kit"),
            ("Robotics Introduction - Build Simple Robots with Arduino for Aba Youths", "Robotics for beginners, Arduino, sensors, build line follower robot, for school competition"),
            ("AI Technology for Aba Businesses - ChatGPT, AI Tools to Make Money", "AI for Aba - Use ChatGPT to write business proposal, AI image, AI video, make money"),
            ("CompTIA A+ Certification Preparation - Complete Hardware & Software", "CompTIA A+ - International certificate, hardware, software, troubleshooting, exam prep, job abroad"),
            ("CompTIA Network+ Certification - Networking for Aba - LAN, WiFi, Router", "Network+ - Build network for Aba cyber cafe, office, WiFi, router config, cable crimping"),
            ("CompTIA Security+ & Other Certifications - Cybersecurity Career", "Security+, CCNA, Microsoft certs, roadmap to become IT professional from Aba"),
            ("Computer Networking - Crimping, Router, Switch, WiFi Setup for Aba Office", "Networking practical - Crimp RJ45, setup router TP-Link ₦15k, extend WiFi, cyber cafe network"),
            ("Entrepreneurship in IT - How to Start Computer Business in Aba with ₦100k", "IT business ideas - Cyber cafe, phone repair, computer sales, POS, training center - Business plan"),
        ]

        # Seed renewable expanded
        try:
            cat_renew = Category.objects.get(pillar="renewable-energy-solar")
            for title, desc in renewable_courses:
                course, created = Course.objects.get_or_create(
                    category=cat_renew, title=title,
                    defaults={
                        "description": f"{desc} - Comprehensive for poor Africans, Aba-focused, practical, from scrap to earning. Simple English + Igbo. Build with local materials.",
                        "level": "beginner", "age_group": "adult", "learning_approach": "andragogic",
                        "duration_hours": 80, "learning_objectives": desc,
                        "is_active": True, "featured": True
                    }
                )
                if course.lessons.count() < 10:
                    for idx, (lt, ct) in enumerate(lessons_20, 1):
                        Lesson.objects.get_or_create(
                            course=course, order=idx,
                            defaults={
                                "title": f"{idx}. {lt} - {title[:25]}",
                                "content": f"DETAILED: {lt}. For {title}. {desc}. Includes practical build in Aba, materials from Ariaria/Cemetery Road, cost, safety, business. Poor African friendly.",
                                "content_type": ct, "duration_minutes": 45
                            }
                        )
            print("Renewable expanded seeded")
        except Exception as e:
            print(f"Renewable error: {e}")

        # Seed IT Technology 15th pillar
        try:
            cat_it = Category.objects.get(pillar="it-technology")
            for title, desc in it_courses:
                course, created = Course.objects.get_or_create(
                    category=cat_it, title=title,
                    defaults={
                        "description": f"{desc} - Comprehensive IT course for poor Africans, Aba-focused, from zero to job-ready. Practical, simple English, Igbo explanation, market prices, business ideas.",
                        "level": "beginner", "age_group": "all", "learning_approach": "heutagogic",
                        "duration_hours": 60, "learning_objectives": desc,
                        "is_active": True, "featured": True
                    }
                )
                if course.lessons.count() < 10:
                    for idx, (lt, ct) in enumerate(lessons_20, 1):
                        Lesson.objects.get_or_create(
                            course=course, order=idx,
                            defaults={
                                "title": f"{idx}. {lt}",
                                "content": f"FULL LESSON: {lt} for IT course {title}. {desc}. Step by step, tools, Aba prices, troubleshooting, how to make money. For poor Africans - no big grammar.",
                                "content_type": ct, "duration_minutes": 45
                            }
                        )
            print("IT Technology 15th pillar seeded")
        except Exception as e:
            print(f"IT error: {e}")

            print(f"\n=== TOTAL NOW: {Course.objects.filter(is_active=True).count()} courses, {Lesson.objects.count()} lessons ===")