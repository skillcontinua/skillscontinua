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
            defaults={'title': quiz_title, 'description': description,
                      'pass_mark': 60, 'time_limit_minutes': time_limit, 'is_active': True}
        )
        if not created:
            quiz.title = quiz_title
            quiz.description = description
            quiz.time_limit_minutes = time_limit
            quiz.save()
            quiz.questions.all().delete()
        for order, (qtext, qtype, explanation, answers) in enumerate(questions_data, 1):
            q = Question.objects.create(quiz=quiz, question_text=qtext, question_type=qtype,
                                        order=order, marks=1, explanation=explanation)
            for atext, correct in answers:
                Answer.objects.create(question=q, answer_text=atext, is_correct=correct)
        print(f'OK: {course_title} — {quiz.questions.count()} questions')
    except Course.DoesNotExist:
        print(f'NOT FOUND: {course_title}')

# ============================================================
# MAC AND LINUX OPERATING SYSTEMS
# ============================================================
create_quiz('Mac and Linux Operating Systems', 'Mac and Linux Operating Systems — Final Assessment',
'This assessment covers both macOS and Linux. These two operating systems power the professional technology world — from creative studios to the internet itself.',
30, [
('What is the keyboard shortcut to open Spotlight Search on a Mac?', 'multiple_choice',
'Spotlight (Command + Space) is the fastest way to find anything on a Mac — files, apps, calculations, conversions and web searches. It is one of the most productive habits a Mac user can develop. Type the first few letters of anything and it appears instantly.',
[('Control + Space', False), ('Command + Space', True), ('Option + Space', False), ('Command + F', False)]),
('On a Mac, what does Command + Q do?', 'multiple_choice',
'Command + Q completely quits the active application. This is different from clicking the red X button, which only closes the window but leaves the app running in the background. Mac apps that are still running show a small dot under their icon in the Dock. Use Command + Q to fully close apps you are finished with.',
[('Closes the current window only', False), ('Completely quits the active application', True), ('Opens the Quick Look preview', False), ('Minimises the window to the Dock', False)]),
('What is Time Machine on Mac?', 'multiple_choice',
'Time Machine is Mac\'s built-in automatic backup system. Connect an external hard drive and Time Machine automatically backs up your Mac hourly, daily and weekly. If files are accidentally deleted or your Mac fails, Time Machine lets you travel back in time and restore any file. It is the most important Mac maintenance habit — always run Time Machine.',
[('A productivity app for time tracking', False), ('Mac\'s built-in automatic backup system requiring an external drive', True), ('A system performance optimisation tool', False), ('The Mac clock and calendar application', False)]),
('What is Gatekeeper on Mac?', 'multiple_choice',
'Gatekeeper is a macOS security feature that prevents apps from unidentified developers from opening automatically. If you download an app from outside the App Store and see a security warning, you can override it in System Settings > Privacy & Security by clicking Open Anyway. Only do this for software from developers you trust. Gatekeeper protects against malicious software.',
[('A password manager built into Safari', False), ('A security feature that blocks apps from unidentified developers', True), ('The Mac firewall for network connections', False), ('A parental control system for restricting app access', False)]),
('Linux powers approximately what percentage of the world\'s web servers?', 'multiple_choice',
'Approximately 96% of the world\'s web servers run Linux. This is why Linux knowledge is essential for any web developer, system administrator or cloud engineer. When you host a website, your files almost certainly live on a Linux server. Understanding Linux means understanding the environment where your work ultimately runs.',
[('About 40%', False), ('About 60%', False), ('About 80%', False), ('About 96%', True)]),
('What does "sudo" mean in Linux?', 'multiple_choice',
'sudo stands for "superuser do" — it runs a command with administrator (root) privileges. It is equivalent to "Run as Administrator" in Windows. Linux requires you to explicitly use sudo for system-level changes, which protects the system from accidental or malicious modifications. You will be asked for your password. Never run sudo commands from the internet without understanding what they do.',
[('Super User Download Operation', False), ('Superuser Do — runs a command with administrator privileges', True), ('System Update and Download Operations', False), ('Secure Unix Default Override', False)]),
('What command in Linux shows you the current directory you are in?', 'multiple_choice',
'pwd stands for Print Working Directory. It tells you exactly where you are in the Linux file system. This is one of the first commands every Linux user learns. When navigating the file system via terminal, pwd confirms your location before you run other commands. Combine it with ls (list) to see your location and its contents.',
[('ls', False), ('cd', False), ('pwd', True), ('dir', False)]),
('What does "sudo apt install firefox" do on Ubuntu Linux?', 'multiple_choice',
'apt is Ubuntu\'s package manager. sudo apt install firefox downloads Firefox from Ubuntu\'s official software repositories and installs it automatically, including all dependencies. This is far more organised than Windows where you must find, download and run installers manually. The package manager ensures software comes from trusted sources and can be updated with a single command.',
[('Updates the Firefox browser if already installed', False), ('Downloads and installs Firefox from official Ubuntu repositories', True), ('Searches for Firefox in the App Store', False), ('Removes Firefox and replaces it with a newer version', False)]),
('What is FileVault on Mac?', 'multiple_choice',
'FileVault encrypts your entire Mac hard drive. If your Mac is stolen, the thief cannot access your files without your login password — the data appears as meaningless encrypted information without the decryption key. It is strongly recommended for any Mac containing sensitive business or client data. Enable it in System Settings > Privacy & Security > FileVault.',
[('A secure cloud storage service for large files', False), ('Full disk encryption that protects your data if your Mac is stolen', True), ('A file compression tool to save disk space', False), ('An Apple subscription service for additional storage', False)]),
('What is the LAMP stack in Linux web hosting?', 'multiple_choice',
'LAMP stands for Linux, Apache, MySQL and PHP — the four components that together power most of the world\'s websites. Linux is the operating system, Apache is the web server software, MySQL is the database, and PHP is the programming language. Understanding LAMP is the foundation of web server administration. A Sierra Leonean who can manage a LAMP server can work anywhere in the world.',
[('A software development framework for mobile apps', False), ('Linux, Apache, MySQL, PHP — the standard web server software stack', True), ('A Linux command for managing lamp and display settings', False), ('Linux Automated Management Protocol — a server monitoring system', False)]),
])

# ============================================================
# SPREADSHEETS AND NUMBERS
# ============================================================
create_quiz('Spreadsheets and Numbers', 'Spreadsheets and Numbers — Final Assessment',
'Spreadsheet skills are among the most valued in any workplace. This assessment tests your ability to use spreadsheets productively and professionally.',
25, [
('What must every formula in a spreadsheet begin with?', 'multiple_choice',
'Every formula in Excel, LibreOffice Calc or Google Sheets must begin with the equals sign (=). This tells the spreadsheet that what follows is a calculation, not just text. Without the =, the formula is treated as text and displayed literally rather than calculated. This is one of the most fundamental rules of spreadsheet use.',
[('A plus sign (+)', False), ('An equals sign (=)', True), ('A dollar sign ($)', False), ('A hash sign (#)', False)]),
('What does the SUM function do?', 'multiple_choice',
'SUM adds together all the numbers in a specified range of cells. For example, =SUM(A1:A10) adds all values in cells A1 through A10. It is the most commonly used function in spreadsheets. SUM is far faster and less error-prone than manually adding cells with + signs, especially for long lists. It automatically updates if you change any value in the range.',
[('Finds the highest value in a range', False), ('Adds all values in a specified range of cells', True), ('Counts the number of cells containing numbers', False), ('Calculates the average of values in a range', False)]),
('What does VLOOKUP do?', 'multiple_choice',
'VLOOKUP (Vertical Lookup) searches for a value in the first column of a table and returns a corresponding value from another column in the same row. It is used for looking up product prices, finding customer details, matching stock codes to descriptions and many other tasks. It is one of the most powerful and commonly used functions in business spreadsheets.',
[('Sorts data vertically from A to Z', False), ('Searches a column for a value and returns data from the same row', True), ('Calculates vertical totals for each column', False), ('Locks rows so they do not scroll when you move down', False)]),
('What does the $ symbol do in a cell reference like $A$1?', 'multiple_choice',
'The $ sign makes a cell reference absolute — it does not change when you copy the formula to other cells. Without $, references are relative and shift when copied. $A$1 always refers to cell A1 regardless of where you copy the formula. $A1 locks the column but lets the row change. A$1 locks the row but lets the column change. This is essential for formulas that always refer to a fixed cell, like a tax rate or exchange rate.',
[('Formats the cell to display currency', False), ('Makes the cell reference absolute so it does not change when copied', True), ('Protects the cell from being edited', False), ('Multiplies the cell value by 100 to show as percentage', False)]),
('What is conditional formatting?', 'multiple_choice',
'Conditional formatting automatically changes the appearance of cells (colour, font, borders) based on the value they contain. For example: colour all sales above a target in green, all below in red. This makes important information immediately visible without reading every number. It is one of the most powerful ways to make a spreadsheet communicate clearly.',
[('Formatting that only applies when the document is printed', False), ('Automatically changing cell appearance based on the value it contains', True), ('A way to protect certain cells from being changed', False), ('Formatting that switches between different styles on different days', False)]),
('A business owner wants to see total sales by month. What feature is most useful?', 'multiple_choice',
'A PivotTable summarises large amounts of data quickly and flexibly. You can drag fields to group, filter and aggregate data in any way. Summarising sales by month, by product, by region or any combination is done in seconds with a PivotTable. It is one of the most powerful features of Excel and LibreOffice Calc for business analysis.',
[('Cell comments to note the monthly figures', False), ('A PivotTable to summarise and group the sales data', True), ('The SORT function to arrange sales in date order', False), ('Conditional formatting to colour monthly totals', False)]),
('What is the keyboard shortcut to select an entire column in Excel or LibreOffice?', 'multiple_choice',
'Ctrl+Space selects the entire column of the current cell. Shift+Space selects the entire row. Ctrl+A selects all cells. These shortcuts are faster than clicking column headers. When you need to format, delete or copy an entire column, these shortcuts save significant time compared to scrolling and clicking.',
[('Ctrl+A', False), ('Shift+Space', False), ('Ctrl+Space', True), ('Alt+C', False)]),
('What does freezing rows or columns do in a spreadsheet?', 'multiple_choice',
'Freeze Panes keeps header rows or identifier columns visible as you scroll through large spreadsheets. If you have 500 rows of data, without freezing the header row you lose track of what each column means as you scroll down. With frozen headers, the column labels stay visible no matter how far you scroll. Access it through View > Freeze Panes.',
[('Prevents any changes to those rows or columns', False), ('Keeps selected rows or columns visible while scrolling through large datasets', True), ('Saves the spreadsheet automatically when those cells change', False), ('Locks the row height and column width to prevent resizing', False)]),
('What is the difference between a bar chart and a line chart?', 'multiple_choice',
'Bar charts compare values between different categories at a single point in time (sales by product, income by department). Line charts show how a value changes over time (monthly revenue, daily temperatures). Using the wrong chart type misleads the reader. Always choose the chart type that best represents the story in your data.',
[('Bar charts are for large data sets; line charts are for small data sets', False), ('Bar charts compare categories; line charts show change over time', True), ('They are interchangeable — the choice is purely aesthetic', False), ('Line charts are more accurate than bar charts for any data', False)]),
('What should you always do before sharing a spreadsheet with a client?', 'multiple_choice',
'Before sharing any spreadsheet, protect cells containing formulas to prevent accidental deletion or overwriting. In Excel: Review > Protect Sheet. This locks all cells except those you specifically unlock for data entry. It also prevents clients from accidentally seeing or changing your formulas. Professional spreadsheets always protect their structure while leaving data entry cells accessible.',
[('Delete all formulas and replace with the calculated values', False), ('Protect formula cells to prevent accidental deletion or modification', True), ('Convert it to PDF so it cannot be edited at all', False), ('Add a password to the entire file so only you can open it', False)]),
])

# ============================================================
# GRAPHICS AND MEDIA PRODUCTION
# ============================================================
create_quiz('Graphics and Media Production', 'Graphics and Media Production — Final Assessment',
'Graphics and media skills open doors in marketing, design, social media, printing and content creation. This assessment tests your understanding of design principles and production tools.',
25, [
('What does RGB stand for in digital design?', 'multiple_choice',
'RGB stands for Red, Green, Blue — the three colours of light used in digital displays. Every colour on a screen is created by mixing these three. RGB is used for anything viewed on screens: websites, social media graphics, digital photos. CMYK (Cyan, Magenta, Yellow, Key/Black) is used for print. Designing in RGB and sending to print can cause colour shifts — always check which colour mode your project requires.',
[('Red, Grey, Brown', False), ('Red, Green, Blue — the colour model used for screen display', True), ('Raster, Gradient, Bitmap — types of digital image files', False), ('Resolution, Grain, Brightness — image quality settings', False)]),
('What is the difference between a vector and a raster image?', 'multiple_choice',
'Raster images (JPEG, PNG, BMP) are made of pixels. Enlarging them beyond their original size causes pixelation (blurring). Vector images (SVG, AI, EPS) are made of mathematical paths. They can be scaled to any size — from a business card to a billboard — without any loss of quality. Logos, icons and print graphics should always be created as vectors.',
[('Vectors are higher resolution than rasters', False), ('Rasters are pixel-based and pixelate when enlarged; vectors are path-based and scale infinitely', True), ('Raster images are larger file sizes than vectors in all cases', False), ('Vectors are only suitable for photographs; rasters for illustrations', False)]),
('What is DPI and why does it matter for print?', 'multiple_choice',
'DPI stands for Dots Per Inch — the resolution of a printed image. 72 DPI is standard for screens. 300 DPI is required for professional print quality. An image that looks sharp on screen at 72 DPI will look blurry and pixelated when printed at A4 size. Always design print materials at 300 DPI minimum. This is why you cannot simply screenshot a web image and use it for printing.',
[('Digital Processing Interface — how a file is formatted for output devices', False), ('Dots Per Inch — print resolution. 300 DPI minimum for professional print quality', True), ('Display Pixel Index — a measure of screen sharpness', False), ('Document Print Information — metadata embedded in print files', False)]),
('Adobe Photoshop is primarily used for:', 'multiple_choice',
'Photoshop is a raster image editor — designed for editing photographs and pixel-based artwork. It is the industry standard for photo retouching, colour correction, compositing and digital painting. For logo design and illustrations, Adobe Illustrator (vector-based) is more appropriate. Understanding which tool to use for which task is essential professional knowledge.',
[('Creating and editing vector logos and illustrations', False), ('Editing photographs and pixel-based raster artwork', True), ('Designing multi-page layouts like brochures and magazines', False), ('Creating animated videos and motion graphics', False)]),
('What is Canva and why is it valuable for small businesses in West Africa?', 'multiple_choice',
'Canva is a free web-based graphic design platform with templates for social media posts, flyers, business cards, presentations and more. It requires no design training to produce professional-looking materials. For small businesses and individuals who cannot afford Adobe software or a professional designer, Canva democratises design. It runs in a browser on any device including smartphones.',
[('A paid professional design tool equivalent to Adobe Illustrator', False), ('A free web-based design platform with templates usable without design training', True), ('A photo editing app primarily for retouching portraits', False), ('A video editing tool for creating YouTube content', False)]),
('What file format should you use when saving a logo for use on both web and print?', 'multiple_choice',
'SVG (Scalable Vector Graphics) is the ideal format for logos because it is vector-based (scales without quality loss) and works on both web and print. For web-only use, PNG with transparent background works well. Never save a logo as JPEG — JPEG compression adds artefacts and JPEG does not support transparency. A professional logo should always be available as a vector file (SVG, AI or EPS).',
[('JPEG — the most widely supported image format', False), ('SVG for web; EPS or AI for print — vector formats that scale without loss', True), ('BMP — the highest quality uncompressed format', False), ('GIF — supports both still images and animation', False)]),
('What is kerning in typography?', 'multiple_choice',
'Kerning is the adjustment of space between individual pairs of characters. Certain letter combinations (like AV, To, We) have gaps that look too large or too small with standard spacing. Professional designers kern these pairs manually for a polished result. Poor kerning is one of the most noticeable signs of amateur design work. It is distinct from tracking (overall letter spacing) and leading (line spacing).',
[('The process of making text bold and italic simultaneously', False), ('Adjusting space between specific pairs of characters for visual balance', True), ('Setting the overall size and weight of a typeface', False), ('The alignment of text to left, right, centre or justified', False)]),
('What is the rule of thirds in visual design?', 'multiple_choice',
'The rule of thirds divides the frame into a 3x3 grid. Placing subjects and key visual elements at the intersections of these grid lines (rather than dead centre) creates more dynamic, visually interesting compositions. It works for photography, graphic design, video and illustration. Most cameras and design applications have a grid overlay to help apply it.',
[('Never use more than three colours in a single design', False), ('Divide the frame into a 3x3 grid and place subjects at the intersections', True), ('Reserve one third of a design for empty white space always', False), ('Use three typefaces maximum in any design project', False)]),
('What is a brand style guide?', 'multiple_choice',
'A brand style guide (or brand guidelines) documents all the visual and communication standards for a brand: the exact logo versions and how to use them, the official colour palette with precise colour codes (hex, RGB, CMYK), the approved typefaces and their usage, and the tone of voice for communications. It ensures consistency across all materials regardless of who creates them. Every professional brand should have one.',
[('A portfolio of all designs ever created for a client', False), ('A document defining logo, colours, fonts and visual standards for consistent brand application', True), ('A legal document protecting a brand\'s intellectual property', False), ('A template file containing all pre-designed marketing materials', False)]),
('A client asks you to design a flyer for printing at A4 size. What resolution should your document be?', 'multiple_choice',
'300 DPI is the professional standard for print. At A4 size (210mm x 297mm), 300 DPI means the image has 2480 x 3508 pixels — enough detail for sharp, clean printing. 72 DPI is for screens only. Starting at 300 DPI and reducing is possible; starting at 72 DPI and trying to enlarge to 300 DPI will not recover the missing detail — the result will be blurry.',
[('72 DPI — the standard for all digital media', False), ('150 DPI — a good compromise between file size and quality', False), ('300 DPI — the professional minimum for print quality', True), ('600 DPI — always use the highest possible resolution', False)]),
])

# ============================================================
# SOCIAL MEDIA FOR BUSINESS
# ============================================================
create_quiz('Social Media for Business', 'Social Media for Business — Final Assessment',
'Social media is where West African businesses build their brands and find customers. This assessment tests your ability to use social media professionally and strategically.',
20, [
('Which social media platform is most effective for B2B (business-to-business) professional networking?', 'multiple_choice',
'LinkedIn is the professional social network — used by businesses, professionals, recruiters and decision makers. For B2B marketing, job seeking and professional brand building, LinkedIn is the most effective platform. For consumer brands, Instagram and Facebook reach larger audiences. Choosing the right platform for your audience is the first strategic decision in social media marketing.',
[('Instagram — the largest photo-sharing platform', False), ('LinkedIn — the professional network for B2B and career development', True), ('Twitter/X — for real-time news and conversations', False), ('TikTok — the fastest growing platform globally', False)]),
('What is an algorithm in the context of social media?', 'multiple_choice',
'Social media algorithms are systems that decide which content each user sees in their feed, and in what order. They prioritise content that generates engagement (likes, comments, shares, saves) — because engaged users spend more time on the platform. Understanding algorithms helps you create content that gets shown to more people without paying for advertising.',
[('A method of scheduling posts automatically at optimal times', False), ('The system that decides which content users see based on engagement signals', True), ('A tool for analysing competitor social media strategies', False), ('The process of converting followers to paying customers', False)]),
('What is the most important metric to track for a business social media account?', 'multiple_choice',
'Reach and engagement rate are more meaningful than follower count. A page with 500 engaged followers who buy from you is worth more than 50,000 followers who never interact. The conversion rate — how many social media interactions lead to actual sales or enquiries — is the ultimate measure of business value. Vanity metrics (high follower count) without engagement indicate a disconnected audience.',
[('Total number of followers — the more the better', False), ('Engagement rate and conversion to actual business outcomes', True), ('Number of posts published per week', False), ('Number of hashtags used per post', False)]),
('WhatsApp Business differs from regular WhatsApp because it:', 'multiple_choice',
'WhatsApp Business provides: a business profile with opening hours, address, description and website; a product catalogue for showing what you sell; quick replies for common questions; labels to organise chats; automated away messages and greeting messages. In West Africa, WhatsApp Business is one of the most effective tools for small business marketing — almost everyone uses WhatsApp.',
[('Allows sending messages to unlimited people simultaneously for free', False), ('Provides a business profile, product catalogue and automated messaging tools', True), ('Has better security and encryption than personal WhatsApp', False), ('Allows businesses to advertise within the WhatsApp platform', False)]),
('What does "organic reach" mean on social media?', 'multiple_choice',
'Organic reach is the number of people who see your content without you paying to promote it. Paid reach comes from advertising spend. Organic reach has declined significantly on most platforms as they prioritise paid content. High-quality, engaging content that generates comments and shares receives greater organic reach from the algorithm as a reward for generating user engagement.',
[('Reach from accounts that only post natural, authentic content', False), ('The number of people who see your content without paid promotion', True), ('Reach from accounts that do not use scheduled posting tools', False), ('Views from users in your own country rather than internationally', False)]),
('What is a content calendar?', 'multiple_choice',
'A content calendar is a planning document (usually a spreadsheet or app) that schedules what content you will post, on which platform, on which date and time. It ensures consistent posting (algorithms reward consistency), prevents running out of ideas, allows for planning around events and promotions, and makes it easier to maintain multiple platforms. Businesses without content calendars post inconsistently and lose audience momentum.',
[('An app that automatically generates content based on your business type', False), ('A planning document scheduling what to post, where and when', True), ('A record of all content that has been posted in the past', False), ('A tool that tracks the performance of each post automatically', False)]),
('What is the best practice for responding to negative comments on a business social media page?', 'multiple_choice',
'Respond promptly, professionally and empathetically to all negative comments in public — then take the resolution offline (ask them to DM you or call). Never delete negative comments (this escalates anger and damages trust). Never respond defensively or aggressively. A well-handled complaint publicly demonstrates excellent customer service to everyone who sees it. Handled poorly, one negative exchange can go viral.',
[('Delete the comment immediately to protect the brand image', False), ('Respond professionally in public, then take resolution offline via private message', True), ('Ignore negative comments as responding draws more attention to them', False), ('Report the comment to the platform for removal as abusive content', False)]),
('Instagram Reels, TikTok videos and YouTube Shorts are all examples of:', 'multiple_choice',
'Short-form video (typically under 60-90 seconds) is currently the highest-reach content format on all major platforms. Algorithms strongly favour it because it generates high engagement and keeps users on the platform. For small businesses in West Africa, short videos showing products, processes, before-and-after results, and behind-the-scenes content consistently outperform photo posts in reach.',
[('Paid advertising formats requiring a marketing budget', False), ('Short-form video — the highest-reach organic content format on current platforms', True), ('Live streaming features for real-time audience interaction', False), ('Stories format that disappears after 24 hours', False)]),
('Why should businesses never buy followers?', 'multiple_choice',
'Bought followers are fake or inactive accounts. They inflate your follower count but generate no engagement, never buy your products and damage your engagement rate (the ratio of interactions to followers). Platforms detect and remove fake followers. Potential clients and partners who inspect your account will see high follower counts with very low engagement — a clear signal of fake followers that damages credibility.',
[('Buying followers violates the terms of service of most platforms', False), ('Bought followers are fake, generate no engagement and damage credibility', True), ('Bought followers are expensive and rarely worth the cost', False), ('Platforms charge businesses extra fees when bought followers are detected', False)]),
('A Sierra Leonean food business wants to reach local customers. Which combination is most effective?', 'multiple_choice',
'WhatsApp Business for direct customer communication and orders, combined with Facebook and Instagram for visual content and local advertising, is the most effective combination for reaching Sierra Leonean consumers. WhatsApp is the primary communication channel. Facebook has the largest Sierra Leonean user base. Instagram is ideal for food photography. TikTok is growing rapidly among younger consumers.',
[('LinkedIn and Twitter for professional reach', False), ('WhatsApp Business, Facebook and Instagram — the dominant platforms in Sierra Leone', True), ('Only TikTok — it has the fastest growth rate globally', False), ('YouTube only — video content always outperforms other formats', False)]),
])

# ============================================================
# PRESENTATIONS
# ============================================================
create_quiz('Presentations', 'Presentations — Final Assessment',
'Professional presentation skills combine design, communication and technology. This assessment tests your ability to create and deliver presentations that inform and persuade.',
20, [
('What is the maximum recommended number of bullet points per slide?', 'multiple_choice',
'The professional standard is a maximum of three to five bullet points per slide, and many presentation experts advocate for fewer. Each bullet point should be a short phrase, not a full sentence. Slides covered in dense text cause audiences to read rather than listen. The presenter should know the details — the slide should support and prompt, not reproduce the entire speech.',
[('As many as needed to cover the topic fully', False), ('Three to five bullet points maximum per slide', True), ('Ten — one for each minute of speaking time', False), ('Two — slides should be mostly visual', False)]),
('What font size is generally the minimum recommended for presentation slides?', 'multiple_choice',
'24pt is the generally recommended minimum font size for body text on presentation slides. Text smaller than 24pt becomes difficult to read from the back of a room. Headings should be larger — 36pt to 44pt. If you cannot fit your content on a slide at 24pt, you have too much text. Reduce the content, not the font size.',
[('12pt — the standard document font size', False), ('18pt — readable from a normal viewing distance', False), ('24pt — the generally recommended minimum for readability from a distance', True), ('36pt — all text should be at least heading size', False)]),
('What is the 10-20-30 rule of PowerPoint presentations?', 'multiple_choice',
'Venture capitalist Guy Kawasaki popularised the 10-20-30 rule: a presentation should have no more than 10 slides, last no more than 20 minutes, and use no font smaller than 30pt. The principle behind it is powerful regardless of whether you follow it exactly: fewer slides, shorter time, larger text. Most presenters use too many slides, speak too long, and use text that is too small.',
[('Ten colours, twenty images, thirty words per slide maximum', False), ('Ten slides maximum, twenty minutes maximum, thirty point font minimum', True), ('Ten minutes preparation per slide, twenty rehearsals minimum, thirty audience maximum', False), ('A presentation rule specific to sales pitches to investors only', False)]),
('What should you do if the projector fails at the start of your presentation?', 'multiple_choice',
'Technical problems are inevitable in presentations. The professional response is to continue without the slides if necessary — you prepared the content, not just the slides. Have a backup: your presentation on a USB drive, saved to cloud storage and emailed to yourself. Know your material well enough that slides are a support, not a crutch. Audiences respect presenters who handle adversity calmly.',
[('Apologise and reschedule the presentation for another day', False), ('Continue confidently without slides — you know your material, slides are just a support', True), ('Read the slides aloud from your laptop screen instead', False), ('Ask the audience to read the presentation document you printed', False)]),
('What is the purpose of a slide master?', 'multiple_choice',
'The slide master is the master template that controls the design of all slides — background, fonts, colours, logo placement and layout. Changes made to the slide master apply automatically to every slide in the presentation. Using a slide master ensures consistency throughout, makes branding changes quick (change once, updates everywhere), and is far more efficient than formatting each slide individually.',
[('A tool for creating animated transitions between slides', False), ('A master template that controls design elements across all slides simultaneously', True), ('The first slide of a presentation containing the title and agenda', False), ('A feature that automatically generates slides from a text document', False)]),
('When presenting to a small group in a meeting room, which approach is most effective?', 'multiple_choice',
'Small group settings benefit from a conversational, interactive approach rather than a formal lecture style. Use fewer slides, allow questions throughout rather than saving them for the end, make eye contact with individuals, and be prepared to skip slides or go deeper based on what the group responds to. The most effective small group presentations feel like expert conversations, not one-way broadcasts.',
[('Present exactly as you would to a large audience for consistency', False), ('Use a conversational interactive style — fewer slides, questions throughout, flexible', True), ('Read your notes carefully to ensure accuracy and completeness', False), ('Project the slides on the largest screen available to maximise impact', False)]),
('What is the most common mistake presenters make with slide animations?', 'multiple_choice',
'Overuse of animations and transitions is the most common presentation mistake. Elaborate animations (spinning text, exploding slides, bouncing bullet points) distract from the content and signal inexperience. Simple, minimal animations — text appearing as you discuss it (Build effect) or a simple fade transition — serve the content. The rule: if the animation does not serve the audience\'s understanding, remove it.',
[('Not using enough animations to keep the audience engaged', False), ('Overusing complex animations that distract from the content', True), ('Using the same animation for every element rather than varying them', False), ('Animating photos but not text, causing inconsistency', False)]),
('What is the recommended aspect ratio for modern presentations?', 'multiple_choice',
'16:9 (widescreen) is the standard for modern presentations, matching current widescreen monitors, projectors and displays. The older 4:3 ratio (standard/square) is still used but leaves black bars on widescreen displays. Always check which ratio the venue\'s projector uses before designing your slides. For online presentations and video calls, 16:9 is universally correct.',
[('4:3 — the universal standard for all presentation software', False), ('16:9 — widescreen, matching modern displays and projectors', True), ('1:1 — square format for compatibility across all devices', False), ('21:9 — ultrawide for maximum visual impact', False)]),
('What makes a strong opening to a presentation?', 'multiple_choice',
'The first 30 seconds are the most important. Strong openings include: a surprising statistic, a thought-provoking question, a brief story or anecdote, a bold statement, or a relevant image without words. What does not work: "Good morning everyone, my name is... today I am going to tell you about..." Audiences decide in the first minute whether to pay attention. Give them a reason immediately.',
[('Introduce yourself fully with your credentials and experience', False), ('Start with a surprising fact, question, story or bold statement to capture attention', True), ('Begin with a detailed agenda so the audience knows what to expect', False), ('Open with a joke to establish rapport and relax the audience', False)]),
('How should you handle a question you cannot answer during a presentation?', 'multiple_choice',
'The professional response to a question you cannot answer is: acknowledge it genuinely, commit to finding the answer and following up, and move on. Do not guess (you may be wrong and undermine your credibility), do not apologise excessively, do not try to deflect. "That is an excellent question — I do not have that data with me but I will find out and get back to you by tomorrow" is a perfectly professional response.',
[('Answer with your best guess so the audience has something to work with', False), ('Acknowledge you do not know, commit to finding out and following up', True), ('Ask if anyone in the audience knows the answer', False), ('Move to the next question without addressing it directly', False)]),
])

# ============================================================
# TRADING AND PETTY BUSINESS MANAGEMENT
# ============================================================
create_quiz('Trading and Petty Business Management', 'Trading and Petty Business Management — Final Assessment',
'This assessment tests your understanding of the principles that make a trading business profitable. Every question is based on real situations Sierra Leonean traders face every day.',
25, [
('Fatima buys tomatoes for Le 30,000 and sells them for Le 40,000. She paid Le 3,000 transport and Le 1,500 market fee. What is her REAL profit?', 'multiple_choice',
'True profit = Selling price minus ALL costs. Le 40,000 minus Le 30,000 (purchase) minus Le 3,000 (transport) minus Le 1,500 (market fee) = Le 5,500 real profit. Not Le 10,000. This is the most important concept in this course — always calculate ALL costs before claiming profit. Many traders believe they are making much more than they actually are because they only subtract the purchase price.',
[('Le 10,000 — selling price minus purchase price', False), ('Le 5,500 — selling price minus ALL costs including transport and fees', True), ('Le 7,000 — selling price minus purchase price and transport only', False), ('Le 8,500 — the market fee is not a real cost', False)]),
('What is the TRUE COST of goods in trading?', 'multiple_choice',
'True cost includes every expense incurred to get the goods to the point of sale: purchase price, transport, handling fees, market fees, storage, spoilage losses, mobile money transaction fees, loan interest if applicable, and the value of your own time. Most traders only count the purchase price and lose money without knowing why. Calculating true cost before setting a selling price is the foundation of profitable trading.',
[('Only the price paid to the supplier for the goods', False), ('Purchase price plus ALL costs to bring goods to the point of sale', True), ('The price competitors charge for the same goods', False), ('The replacement cost minus transport if you collect it yourself', False)]),
('A trader has goods worth Le 500,000 in stock and Le 100,000 cash. She owes Le 150,000 to a supplier. What is the net worth of her business?', 'multiple_choice',
'Net worth = Total assets minus Total liabilities. Assets: Stock (Le 500,000) + Cash (Le 100,000) = Le 600,000. Liabilities: Debt to supplier (Le 150,000). Net worth: Le 600,000 minus Le 150,000 = Le 450,000. Understanding this simple calculation allows any trader to know whether their business is growing, stable or shrinking from one month to the next.',
[('Le 600,000 — total of stock and cash', False), ('Le 350,000 — cash minus what is owed', False), ('Le 450,000 — total assets minus total liabilities', True), ('Le 500,000 — the stock value only', False)]),
('What is the MIXING TRAP in cash flow management?', 'multiple_choice',
'The mixing trap is when traders combine business money with personal money — using the business cash box for household expenses and then putting money back when they earn. This makes it impossible to know the true cash position of the business. Over time, personal withdrawals from the business steadily reduce its capital without the trader noticing. The solution is strict separation: a dedicated business cash box or account that personal expenses never touch.',
[('Mixing different products in one display to attract more customers', False), ('Combining business and personal money making it impossible to track business cash', True), ('Mixing credit and cash sales in the same daily records', False), ('Mixing stock from different suppliers causing quality confusion', False)]),
('If your supplier raises the price of rice by 15%, what should you do immediately?', 'multiple_choice',
'Raise your selling price immediately by at least 15% to maintain your margin. Absorbing a supplier price increase means your profit margin shrinks. If you absorb several such increases over a year, your margin disappears entirely — you are working for nothing. Customers understand price increases when they happen for clear reasons. Explain: "My supplier price has risen — I must adjust." Most customers accept this.',
[('Wait and see if the price comes back down before raising your price', False), ('Raise your selling price immediately to maintain your profit margin', True), ('Absorb the increase for one month to maintain customer loyalty', False), ('Stop selling rice and switch to a different product immediately', False)]),
('What is the difference between profit and cash flow?', 'multiple_choice',
'Profit is what you made over a period of time — it is a calculation. Cash flow is the actual money available to you right now. You can be profitable on paper but have no cash if customers owe you money, if you have bought more stock than you have sold, or if you have given credit. Many businesses that appear profitable fail because of cash flow problems. Always know both your profit AND your cash position.',
[('They are the same — profit is always the cash you have', False), ('Profit is what you made over a period; cash flow is the money available right now', True), ('Cash flow is always higher than profit because it includes borrowings', False), ('Profit applies to large businesses; cash flow is for small traders', False)]),
('What is the recommended split of business profits?', 'multiple_choice',
'The recommended split is: 50% reinvested in the business (more and better stock), 20% saved as business emergency reserve, 30% taken as personal income. This ratio keeps the business growing while paying the owner fairly. Taking too much for personal use starves the business of capital for growth. Taking too little means the business owner is not rewarding themselves appropriately for their work and risk.',
[('100% reinvested to grow the business as fast as possible', False), ('50% reinvest, 20% save, 30% personal income', True), ('50% personal income, 50% restocking', False), ('Split equally three ways — 33% each for reinvestment, savings and personal', False)]),
('A customer asks for Le 200,000 of goods on credit. They have always paid before. What is the safest approach?', 'multiple_choice',
'Always agree a specific repayment date before handing over goods on credit. Record the debt in your credit book with date, goods description, amount and agreed payment date. Charge a slightly higher price for credit sales to compensate for waiting and the risk of non-payment. Do not give further credit until this debt is settled. Even trusted customers should have formal written agreements for significant amounts.',
[('Refuse all credit to protect your cash flow', False), ('Agree a specific repayment date, record in your credit book and charge a credit premium', True), ('Give the goods and trust they will pay when they can', False), ('Only give credit to family members who you can chase up easily', False)]),
('What should a trader do at the end of every trading day?', 'multiple_choice',
'End-of-day routine: Count all cash. Record all sales and expenses in your cash book. Count remaining stock. Calculate today\'s net profit or loss. Plan tomorrow — what needs restocking, who owes you money, what expenses are coming. This 10-15 minute habit gives you accurate financial data, reveals problems early, and ensures your records are always up to date. Traders who do this consistently know their business inside out.',
[('Count cash only and lock it away securely', False), ('Record sales, expenses, count cash and stock, calculate profit, plan tomorrow', True), ('Check social media for new customer enquiries', False), ('Review competitor prices for the following day', False)]),
('What is the GROWTH STAGE a trader reaches when they consistently make profit and have an emergency cash reserve?', 'multiple_choice',
'The Stable stage is when consistent profit and a cash reserve are maintained. The four stages are: Surviving (day to day, no savings), Stable (consistent profit, small reserve), Growing (reinvesting profit, expanding stock or customers), Thriving (consistent income, employing others, planning for the future). Most Sierra Leonean traders are in the Surviving stage — moving to Stable requires applying the principles of this course consistently for 3 months.',
[('Surviving — every business with profit is in survival mode', False), ('Stable — consistent profit plus an emergency cash reserve', True), ('Growing — the stage immediately after making any profit', False), ('Thriving — any trader who makes daily profit has reached this level', False)]),
])

# ============================================================
# SIMPLE BOOKKEEPING FOR SMALL BUSINESSES
# ============================================================
create_quiz('Simple Bookkeeping for Small Businesses', 'Simple Bookkeeping — Final Assessment',
'Accurate records are the foundation of every successful business. This assessment tests your ability to keep, read and use simple financial records.',
25, [
('What is the golden rule of bookkeeping?', 'multiple_choice',
'Write it down today. Not tomorrow, not when you remember. Every transaction — every sale, every purchase, every expense — must be recorded on the day it happens. Memory is unreliable for financial records. Delayed recording leads to forgotten transactions, inaccurate totals and business decisions based on wrong information. The discipline of same-day recording is what separates reliable records from guesswork.',
[('Always use a professional accountant to keep your books', False), ('Record every transaction on the day it happens — not later', True), ('Only record transactions above a minimum threshold amount', False), ('Review and update records at the end of each week', False)]),
('What is the difference between a cash sale and a credit sale?', 'multiple_choice',
'A cash sale is completed immediately — goods are handed over and payment is received at the same time. Record as income today. A credit sale means goods are given now and payment will come later. Record as a debtor entry (money owed to you) when goods are given, and only transfer to income when actual payment is received. Counting credit sales as income before payment leads to overestimated income and cash flow problems.',
[('Cash sales are for large amounts; credit sales are for small ones', False), ('Cash sale = payment received now; credit sale = payment to come later, record separately', True), ('They are treated the same in bookkeeping — both recorded as income immediately', False), ('Credit sales are not recorded until the customer confirms they received the goods', False)]),
('You had 10 bags of rice at the start of the week. You bought 20 more. You sold 18. How many should remain?', 'multiple_choice',
'Opening stock (10) + Purchases (20) = 30 bags available. Sold (18). Closing stock = 30 minus 18 = 12 bags. If you count and find only 10 bags, 2 bags are unaccounted for — possibly stolen, spoiled or recorded incorrectly. Stock reconciliation (comparing calculated closing stock to physical count) is the key tool for detecting losses and theft.',
[('8 bags', False), ('10 bags', False), ('12 bags', True), ('18 bags', False)]),
('What is the purpose of a debtor record?', 'multiple_choice',
'A debtor record tracks everyone who owes your business money — their name, what they bought, the amount owed, when it was agreed, and the repayment date. Without a debtor record, you forget who owes you what, debts go uncollected, and your cash flow suffers. Total debtors should be reviewed every week. Growing total debtors is an early warning sign of cash flow problems ahead.',
[('To record all your purchases from suppliers', False), ('To track all money owed to your business by customers', True), ('To monitor your business cash balance daily', False), ('To calculate the tax you owe at the end of the year', False)]),
('A business has: income Le 800,000, cost of goods Le 400,000, transport Le 30,000, market fees Le 20,000, stall rent Le 50,000. What is the net profit?', 'multiple_choice',
'Net profit = Income minus all costs. Le 800,000 minus Le 400,000 (goods) minus Le 30,000 (transport) minus Le 20,000 (market fees) minus Le 50,000 (stall rent) = Le 300,000. This is a net profit margin of 37.5% (Le 300,000 divided by Le 800,000 times 100) — healthy for a trading business. If the business owner forgot transport, fees and rent, they would think profit was Le 400,000 — more than 33% wrong.',
[('Le 400,000 — income minus cost of goods only', False), ('Le 350,000 — forgetting stall rent', False), ('Le 300,000 — income minus all costs', True), ('Le 450,000 — cost of goods is not a real expense', False)]),
('What does FIFO mean in stock management?', 'multiple_choice',
'FIFO stands for First In, First Out — sell the oldest stock before the newer stock. This is critical for perishable goods (food, vegetables, fish) where older stock spoils first. It is also important for goods where prices are rising — selling older (cheaper) stock first maintains your margin calculation accuracy. Ignoring FIFO with perishables leads to spoilage losses and waste.',
[('Find and Identify any Faulty or Old stock', False), ('First In, First Out — sell oldest stock before newer stock', True), ('Fixed Income, Fixed Outgoings — a budgeting principle', False), ('File Income and Financial Outgoings — a recording method', False)]),
('If a business shows profit of Le 500,000 but has only Le 50,000 cash, what is the most likely explanation?', 'multiple_choice',
'When profit is high but cash is low, the most likely causes are: significant amounts owed by debtors (profit recorded but not yet collected), large stock purchases (profit reinvested in stock, not sitting as cash), or mixing of business and personal funds (profit withdrawn for personal use without recording). Review debtors, check stock value, and verify no unrecorded personal withdrawals occurred.',
[('The business is making a loss despite what the records show', False), ('Profit is owed by debtors, tied up in stock, or withdrawn for personal use', True), ('The books are incorrect and must be completely restarted', False), ('Cash payment received is being stolen before it is recorded', False)]),
('How often should a trader do a monthly review of their business records?', 'multiple_choice',
'Every month without fail. The monthly review — checking income, expenses, profit, cash position, stock value, debtors and creditors — takes 30 minutes and provides the complete financial picture. Businesses that review monthly catch problems early: declining margins, growing debts, cash flow risks. Businesses that never review discover problems only when they become crises. Monthly review is the habit that separates managed businesses from drifting ones.',
[('Only when applying for a loan or at year end', False), ('Every month without fail — 30 minutes that shows the complete financial picture', True), ('Quarterly — monthly is too frequent for a small business', False), ('Whenever the business seems to be doing poorly', False)]),
('What is a creditor in business terms?', 'multiple_choice',
'A creditor is a person or organisation your business owes money to — typically a supplier from whom you bought goods on credit. Creditors are liabilities. Knowing your total creditors tells you how much your business owes and when it must be paid. Ignoring creditors leads to late payment, damaged supplier relationships, loss of credit terms and potential legal action. Always know exactly what you owe and when it is due.',
[('A customer who pays promptly and reliably', False), ('A person or organisation your business owes money to', True), ('Any person who has lent money to your business', False), ('A government tax authority to whom taxes are owed', False)]),
('Why do banks and microfinance institutions require financial records before giving loans?', 'multiple_choice',
'Financial records prove that the business exists, is generating income, and can repay the loan. Without records, the lender cannot assess the risk. With 6-12 months of clear income and expense records, even an informal trader can demonstrate creditworthiness. Good records are the passport to formal financing — which is often the difference between a trader who stays small and one who grows into a real business.',
[('It is a legal formality with no practical purpose', False), ('Records prove the business generates income and has capacity to repay the loan', True), ('Banks use records to calculate the tax the business owes', False), ('Records allow banks to take ownership of stock as collateral', False)]),
])

# Print summary
print('\n' + '='*60)
from certifications.models import Quiz
total_q = 0
quiz_count = Quiz.objects.count()
for q in Quiz.objects.all():
    total_q += q.questions.count()
print(f'Total quizzes: {quiz_count}')
print(f'Total questions: {total_q}')

courses_without_quiz = []
from courses.models import Course
for c in Course.objects.all().order_by('title'):
    if not hasattr(c, 'quiz'):
        try:
            c.quiz
        except:
            courses_without_quiz.append(c.title)

print(f'\nCourses still needing quizzes: {len(courses_without_quiz)}')
for t in courses_without_quiz[:20]:
    print(f'  - {t}')
if len(courses_without_quiz) > 20:
    print(f'  ... and {len(courses_without_quiz) - 20} more')