from django.core.management.base import BaseCommand
from courses.models import Category, Course, Lesson

class Command(BaseCommand):
    def handle(self, *args, **options):
        cat_it = Category.objects.get(pillar="it-technology")
        it_remaining = [
            ("Microsoft Excel Complete - From SUM to Shop Accounting", "Excel for Aba shops - Sales, profit, SUM IF VLOOKUP charts"),
            ("Microsoft PowerPoint Complete - Presentations", "PowerPoint for church, school, business pitch"),
            ("Internet & Email Mastery - Gmail, Search, Apply Jobs", "Create Gmail, send CV, Google search, Jobberman"),
            ("Social Media for Business - Facebook, WhatsApp Business, Instagram", "Sell via WhatsApp Status, Facebook Page"),
            ("Database Management System - Access, MySQL for Aba Shops", "Customer records, stock, tables, queries"),
            ("Software Types - Open Source vs Paid, Antivirus", "System vs application, LibreOffice, VLC, antivirus"),
            ("Operating Systems Deep Dive - Windows, Mac, Linux, Chrome OS", "Dual boot Windows + Ubuntu, Mac OS appreciation"),
            ("Graphics Design - Canva, Photoshop, CorelDRAW for Aba", "Design flyers, logos, charge ₦3k-₦20k"),
            ("Computer Assembling & Building - From Scratch", "Buy parts Computer Village, assemble, sell"),
            ("Computer Repair & Maintenance - Virus, Formatting, Blue Screen", "Repair business, slow, virus, BSOD, charge ₦5k-₦15k"),
            ("Mac OS Mastery - For Creatives", "MacBook, Finder, Final Cut, Logic, Time Machine"),
            ("Linux Mastery - Ubuntu, Mint - Free OS for Cyber Cafe", "Linux free, terminal ls cd, install software"),
            ("Cyber Security Essentials - Protect POS, Bank, Facebook", "Password, 2FA, phishing, Yahoo boys, backup"),
            ("Cloud Computing - Google Drive, Dropbox, OneDrive", "Backup shop records, photos, access anywhere"),
            ("CCTV Installation & Business - For Aba Shops", "Analog IP camera, DVR, view on phone, ₦80k-₦250k"),
            ("Drone Technology - Build, Fly, Photography, Farming", "DJI, FPV kit, aerial wedding, farm mapping"),
            ("Robotics Introduction - Arduino, Sensors, Line Follower", "Arduino IDE, LED, ultrasonic, servo, line follower"),
            ("AI Technology for Aba - ChatGPT, AI Image, AI Video", "ChatGPT proposal, AI flyer, AI video advert"),
            ("CompTIA A+ Certification Complete Prep", "A+ 1101 1102, hardware, troubleshooting, job abroad"),
            ("CompTIA Network+ Certification - LAN, WiFi, Router", "OSI, TCP IP, crimp RJ45, TP-Link router"),
            ("CompTIA Security+, CCNA, Microsoft, AWS Roadmap", "Security+, CCNA, AZ-900, AWS, career path"),
            ("Computer Networking Practical - Crimping, Router, WiFi", "Crimper, tester, straight crossover, WiFi password"),
            ("IT Entrepreneurship - Start Business with ₦100k", "Cyber cafe, sales, training, POS, business plan"),
            ("Microsoft Office Suite Mastery Combined", "Invoice, report, presentation, email, office job"),
            ("Data Entry & Typing Mastery - 50 WPM", "Mavis Beacon, Upwork, Fiverr"),
            ("Hardware Repair Advanced - Laptop Motherboard, Screen", "Screen replace ₦25k, keyboard ₦8k, battery"),
            ("Software Development Intro - HTML CSS JS Python", "HTML tags, CSS, JS alert, Python print, website"),
            ("Digital Literacy for Market Women & Elders", "Smartphone, WhatsApp video, OPay PalmPay"),
        ]
        lessons_20 = [("Intro - Market Analysis", "video"),("Tools - Ariaria Prices","pdf"),("Safety","video"),("Theory","video"),("Practical 1","video"),("Intermediate","video"),("Practical 2","video"),("Advanced","video"),("How to Charge","text"),("Where to Buy","text"),("Pricing","pdf"),("Marketing","text"),("Mobile Service","text"),("Expanding","text"),("Branding","text"),("Mistakes","text"),("Final Practical","video"),("Business Plan","pdf"),("Mentorship","text"),("Next Steps","text")]

        for title, desc in it_remaining:
            course, _ = Course.objects.get_or_create(
                category=cat_it, title=title,
                defaults={"description": desc+" - Comprehensive IT for poor Africans", "level":"beginner","age_group":"all","learning_approach":"heutagogic","duration_hours":60,"learning_objectives":desc,"is_active":True,"featured":True}
            )
            if course.lessons.count()<10:
                for idx,(lt,ct) in enumerate(lessons_20,1):
                    Lesson.objects.get_or_create(course=course, order=idx, defaults={"title": f"{idx}. {lt}", "content": f"Detailed: {lt} for {title}. {desc}. Aba-focused.", "content_type": ct, "duration_minutes":45})

        # Beauty + Gov remaining
        cat_beauty = Category.objects.get(pillar="beauty-personal-care")
        for title, desc in [("Hair Dressing & Wig Making","Wig ₦15k-₦50k"),("Makeup & Gele Tying","Makeup ₦20k-₦50k per bride"),("Manicure Pedicure Nail Fixing","Nail ₦2k-₦5k"),("Barbing Salon Business Advanced","Barbing advanced cuts")]:
            course,_=Course.objects.get_or_create(category=cat_beauty, title=title, defaults={"description":desc,"level":"beginner","age_group":"adult","learning_approach":"andragogic","duration_hours":60,"learning_objectives":desc,"is_active":True,"featured":True})
            if course.lessons.count()<10:
                for idx,(lt,ct) in enumerate(lessons_20,1):
                    Lesson.objects.get_or_create(course=course, order=idx, defaults={"title": f"{idx}. {lt}", "content": f"{lt} for {title}", "content_type": ct, "duration_minutes":45})

        cat_gov = Category.objects.get(pillar="government-social-impact")
        for title, desc in [("N-Power & Grants - Apply & Win","FG grants BOI SMEDAN"),("NGO & Community Development","Start foundation"),("Youth Leadership & Politics","Become leader Aba")]:
            course,_=Course.objects.get_or_create(category=cat_gov, title=title, defaults={"description":desc,"level":"beginner","age_group":"adult","learning_approach":"andragogic","duration_hours":40,"learning_objectives":desc,"is_active":True,"featured":True})
            if course.lessons.count()<10:
                for idx,(lt,ct) in enumerate(lessons_20,1):
                    Lesson.objects.get_or_create(course=course, order=idx, defaults={"title": f"{idx}. {lt}", "content": f"{lt} for {title}", "content_type": ct, "duration_minutes":45})

       