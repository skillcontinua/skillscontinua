from django.shortcuts import render
from django.http import Http404

def index(request):
    """Home page - alias for home"""
    return home(request)

def home(request):
    return render(request, 'core/index.html')

def dashboard(request):
    return render(request, 'core/dashboard.html')

def community(request):
    # Your perfect community.html
    return render(request, 'courses/community.html')

def pillars_overview(request):
    pillars = [
        {"slug": "renewable-energy-solar", "name": "RENEWABLE ENERGY & SOLAR", "count": 20, "icon": "☀️", "desc": "Solar Installation, Inverter & Battery, Solar Business"},
        {"slug": "technology-software", "name": "TECHNOLOGY & SOFTWARE", "count": 35, "icon": "💻", "desc": "Web Dev, Mobile App, UI/UX, AI & ChatGPT"},
        {"slug": "trades-craftsmanship", "name": "TRADES & CRAFTSMANSHIP", "count": 40, "icon": "🛠️", "desc": "Tailoring, Carpentry, Welding, Plumbing, Electrical"},
        {"slug": "agriculture-agro-business", "name": "AGRICULTURE & AGRO-BUSINESS", "count": 25, "icon": "🌾", "desc": "Poultry, Fish Farming, Snail, Export Business"},
        {"slug": "business-entrepreneurship", "name": "BUSINESS & ENTREPRENEURSHIP", "count": 30, "icon": "💼", "desc": "Start Business, Sales, Import/Export, E-commerce"},
        {"slug": "digital-marketing-content", "name": "DIGITAL MARKETING & CONTENT", "count": 28, "icon": "📱", "desc": "Facebook Ads, Google Ads, TikTok, Content Creation"},
        {"slug": "health-wellness", "name": "HEALTH & WELLNESS", "count": 22, "icon": "❤️", "desc": "First Aid, Nursing Assistant, Fitness, Nutrition"},
        {"slug": "education-teaching", "name": "EDUCATION & TEACHING", "count": 18, "icon": "🎓", "desc": "Nursery Teaching, JAMB Tutoring, Online Teaching"},
        {"slug": "finance-professional", "name": "FINANCE & PROFESSIONAL SERVICES", "count": 20, "icon": "💰", "desc": "Accounting, Tax, Investment, Real Estate"},
        {"slug": "media-creative-arts", "name": "MEDIA & CREATIVE ARTS", "count": 15, "icon": "🎭", "desc": "Music, Photography, African Heritage"},
        {"slug": "transport-logistics", "name": "TRANSPORT & LOGISTICS", "count": 15, "icon": "🚚", "desc": "Ride Hailing, Trucking, Shipping, Delivery"},
        {"slug": "beauty-personal-care", "name": "BEAUTY & PERSONAL CARE", "count": 20, "icon": "💄", "desc": "Barbering, Hairdressing, Makeup, Nail Tech"},
        {"slug": "government-social-impact", "name": "GOVERNMENT & SOCIAL IMPACT", "count": 12, "icon": "🤝", "desc": "NGO Management, Grant Writing, Leadership"},
        {"slug": "automotive-repairs-maintenance", "name": "AUTOMOTIVE REPAIRS & MAINTENANCE", "count": 15, "icon": "🚗", "desc": "ABIAPOLY PILOT FOCUS: Keke, Okada, Diagnostics - Most Profitable!", "highlight": True},
    ]
    return render(request, 'en/pillars_overview.html', {'pillars': pillars})

def pillar_detail(request, slug):
    all_pillars_courses = {
        "energy-power-offgrid": {"name": "ENERGY, POWER & OFF-GRID", "count": 57, "icon": "⚡", "is_highlight": True, "courses": ["Flywheel Generator with DC Motor & Lithium Battery - Advanced Power Systems", "Advanced Auto Diagnostics and Repair", "Advanced Physics - Secondary", "Automotive Electrical Systems", "Electric Vehicle (EV) Technology", "Electric Vehicle Battery Systems", "Electric Vehicle Technology - Complete", "Engine Diagnostics and Troubleshooting", "Fuel Injection Systems - Advanced", "Fuel Injection Systems - Carburetor Technology", "Generator and Plant Maintenance", "Heavy Vehicle Mechanics", "Lithium Battery Technology - Modern Solutions", "Marine Engine Diagnostics", "Modern Inverter Technology - Advancements", "Modern Solar Technology - Advancements", "Modern Wind Energy Technology - Innovations", "Outboard Motor Repair - Advanced", "Turbocharger and Supercharger Systems", "Wind Energy Economics and Policy", "Wind Farm Design and Management"]},
        "digital-tech-skills": {"name": "DIGITAL & TECH SKILLS", "count": 95, "icon": "💻", "courses": ["CCTV Installation & Maintenance", "Robotics & Automation - Industrial", "Artificial Intelligence Fundamentals", "Cybersecurity Essentials"]},
        "green-climate-skills": {"name": "GREEN & CLIMATE SKILLS", "count": 11, "icon": "🌱", "courses": ["Cryogenics - Fundamentals", "Cryogenics - Advanced Applications", "Recycling & Upcycling Technology"]},
        "entrepreneurship-handiwork": {"name": "ENTREPRENEURSHIP & HANDIWORK", "count": 122, "icon": "🛠", "courses": ["Fashion Design & Tailoring", "Catering & Baking", "Carpentry & Furniture Making"]},
        "construction-technical": {"name": "CONSTRUCTION & TECHNICAL", "count": 8, "icon": "🏗", "courses": ["Bricklaying & Concreting", "Plumbing Systems"]},
        "health-social-care": {"name": "HEALTH & SOCIAL CARE", "count": 14, "icon": "❤", "courses": ["Caregiving - Professional", "First Aid & Emergency Response"]},
        "african-heritage-cultural": {"name": "AFRICAN HERITAGE & CULTURAL SKILLS", "count": 6, "icon": "🎭", "courses": ["Bead Making - Igbo Heritage"]},
        "school-based-career": {"name": "SCHOOL-BASED & CAREER SKILLS", "count": 3, "icon": "🎓", "courses": ["Study Skills & Exam Prep"]},
        "returnee-reintegration": {"name": "RETURNEE & REINTEGRATION", "count": 1, "icon": "✈", "courses": ["Returnee Reintegration & Livelihood Support"]},
    }
    pillar = all_pillars_courses.get(slug)
    if not pillar:
        raise Http404("Pillar not found")
    return render(request, 'en/pillar_detail.html', {'pillar': pillar, 'slug': slug})