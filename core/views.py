from django.shortcuts import render

def home(request):
    return render(request, 'en/home.html')

def pillars_overview(request):
    pillars = [
        {"slug": "digital-tech-skills", "name": "DIGITAL & TECH SKILLS", "count": 95, "icon": "💻", "desc": "Smart Campus Core - The future of Aba is digital.", "topics": ["CCTV & Surveillance", "Robotics & Automation", "AI & Data", "Cybersecurity", "Software Dev", "Networking"]},
        {"slug": "green-climate-skills", "name": "GREEN & CLIMATE SKILLS", "count": 11, "icon": "🌱", "desc": "Sustainability and climate resilience for Eastern Nigeria.", "topics": ["Cryogenics", "Recycling", "Climate Action", "Sustainable Farming"]},
        {"slug": "entrepreneurship-handiwork", "name": "ENTREPRENEURSHIP & HANDIWORK", "count": 122, "icon": "🛠️", "desc": "Job creation engine - 122 income-generating skills.", "topics": ["Fashion Design", "Catering", "Carpentry", "Beauty Tech", "Business Start-up"]},
        {"slug": "construction-technical", "name": "CONSTRUCTION & TECHNICAL", "count": 8, "icon": "🏗️", "desc": "Building the new Eastern Nigeria.", "topics": ["Bricklaying", "Plumbing", "Welding", "Tiling"]},
        {"slug": "health-social-care", "name": "HEALTH & SOCIAL CARE", "count": 14, "icon": "❤️", "desc": "Community health and social impact skills.", "topics": ["Caregiving", "First Aid", "Community Health"]},
        {"slug": "african-heritage-cultural", "name": "AFRICAN HERITAGE & CULTURAL SKILLS", "count": 6, "icon": "🎭", "desc": "Preserving Igbo heritage and cultural enterprise.", "topics": ["Bead Making", "Local Crafts", "Cultural Dance"]},
        {"slug": "school-based-career", "name": "SCHOOL-BASED & CAREER SKILLS", "count": 3, "icon": "🎓", "desc": "Academic support and career readiness.", "topics": ["Study Skills", "Career Guidance"]},
        {"slug": "returnee-reintegration", "name": "RETURNEE & REINTEGRATION", "count": 1, "icon": "✈️", "desc": "Support and skills for returnees.", "topics": ["Reintegration Support"]},
        {"slug": "energy-power-offgrid", "name": "ENERGY, POWER & OFF-GRID", "count": 57, "icon": "⚡", "desc": "ABIAPOLY PILOT FOCUS: Powering off-grid campuses.", "topics": ["Flywheel Generator", "Fuel Injection", "Carburetor", "Turbo & Supercharger", "Diagnostic", "Inverter Tech", "Solar & Wind", "Lithium Battery", "EV Technology", "Generator & Plant Maintenance"], "highlight": True},
    ]
    return render(request, 'en/pillars_overview.html', {'pillars': pillars})

def pillar_detail(request, slug):
    all_pillars_courses = {
        "energy-power-offgrid": {"name": "ENERGY, POWER & OFF-GRID", "count": 57, "icon": "⚡", "is_highlight": True, "courses": ["Flywheel Generator with DC Motor & Lithium Battery - Advanced Power Systems", "Advanced Auto Diagnostics and Repair", "Advanced Physics - Secondary", "Automotive Electrical Systems", "Electric Vehicle (EV) Technology", "Electric Vehicle Battery Systems", "Electric Vehicle Technology - Complete", "Engine Diagnostics and Troubleshooting", "Fuel Injection Systems - Advanced", "Fuel Injection Systems - Carburetor Technology", "Generator and Plant Maintenance", "Heavy Vehicle Mechanics", "Lithium Battery Technology - Modern Solutions", "Marine Engine Diagnostics", "Modern Inverter Technology - Advancements", "Modern Solar Technology - Advancements", "Modern Wind Energy Technology - Innovations", "Outboard Motor Repair - Advanced", "Turbocharger and Supercharger Systems", "Wind Energy Economics and Policy", "Wind Farm Design and Management"]},
        "digital-tech-skills": {"name": "DIGITAL & TECH SKILLS", "count": 95, "icon": "💻", "courses": ["CCTV Installation & Maintenance", "Robotics & Automation - Industrial", "Artificial Intelligence Fundamentals", "Cybersecurity Essentials"]},
        "green-climate-skills": {"name": "GREEN & CLIMATE SKILLS", "count": 11, "icon": "🌱", "courses": ["Cryogenics - Fundamentals", "Cryogenics - Advanced Applications", "Recycling & Upcycling Technology"]},
        "entrepreneurship-handiwork": {"name": "ENTREPRENEURSHIP & HANDIWORK", "count": 122, "icon": "🛠️", "courses": ["Fashion Design & Tailoring", "Catering & Baking", "Carpentry & Furniture Making"]},
        "construction-technical": {"name": "CONSTRUCTION & TECHNICAL", "count": 8, "icon": "🏗️", "courses": ["Bricklaying & Concreting", "Plumbing Systems"]},
        "health-social-care": {"name": "HEALTH & SOCIAL CARE", "count": 14, "icon": "❤️", "courses": ["Caregiving - Professional", "First Aid & Emergency Response"]},
        "african-heritage-cultural": {"name": "AFRICAN HERITAGE & CULTURAL SKILLS", "count": 6, "icon": "🎭", "courses": ["Bead Making - Igbo Heritage"]},
        "school-based-career": {"name": "SCHOOL-BASED & CAREER SKILLS", "count": 3, "icon": "🎓", "courses": ["Study Skills & Exam Prep"]},
        "returnee-reintegration": {"name": "RETURNEE & REINTEGRATION", "count": 1, "icon": "✈️", "courses": ["Returnee Reintegration & Livelihood Support"]},
    }
    pillar = all_pillars_courses.get(slug)
    if not pillar:
        from django.http import Http404
        raise Http404("Pillar not found")
    return render(request, 'en/pillar_detail.html', {'pillar': pillar, 'slug': slug})