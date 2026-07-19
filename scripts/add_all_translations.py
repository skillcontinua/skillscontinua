import os
import sys
import django

# Add project root to path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from courses.models import Category, Course

print("="*70)
print("🌍 ADDING COMPLETE TRANSLATIONS FOR ALL CATEGORIES")
print("="*70)

# Complete translations for ALL categories
translations = {
    # ===== ENGLISH (Default - already set) =====
    
    # ===== FRENCH (Français) =====
    'fr': {
        'Foundational Literacy': {'name': 'Alphabétisation Fondamentale', 'description': 'De l\'analphabétisme complet à la lecture, l\'écriture et la numératie confiantes dans votre propre langue.'},
        'Computer Literacy': {'name': 'Informatique de Base', 'description': 'Des bases aux avancées — matériel, logiciels, cybersécurité, drones, robotique et IA.'},
        'Vocational Trades': {'name': 'Métiers Professionnels', 'description': 'Menuiserie, soudure, plomberie, maçonnerie, réparations automobiles, compétences maritimes et plus.'},
        'Certifications': {'name': 'Certifications Professionnelles', 'description': 'CompTIA, Network+, Hacking Éthique, Drones, CCTV, Robotique et certifications IA.'},
        'Life Skills': {'name': 'Compétences de Vie', 'description': 'Développement cognitif, intelligence émotionnelle, gestion financière et communication.'},
        'Primary Education': {'name': 'Enseignement Primaire', 'description': 'Programmes scolaires complets — Arts, Sciences, Technologie, Commerce.'},
        'Secondary Education': {'name': 'Enseignement Secondaire', 'description': 'Études avancées en Sciences, Commerce et Technologie.'},
        'Building Construction': {'name': 'Construction et Bâtiment', 'description': 'Maçonnerie, toiture, carrelage, plomberie, peinture et compétences complètes en construction.'},
        'Housing and Appliances': {'name': 'Logement et Appareils', 'description': 'Réparation de réfrigérateurs, climatisation, TV, radio et systèmes domestiques.'},
        'Electrical Installation': {'name': 'Installation Électrique', 'description': 'Câblage, installation solaire, réparation de générateurs et systèmes électriques.'},
        'Automotive - Motorcycles': {'name': 'Automobile - Motos', 'description': 'Mécanique moto et tricycle - réparation, entretien et diagnostic.'},
        'Automotive - Cars and Vans': {'name': 'Automobile - Voitures', 'description': 'Mécanique voiture - moteur, transmission, freins et systèmes électriques.'},
        'Automotive - Heavy Vehicles': {'name': 'Automobile - Poids Lourds', 'description': 'Mécanique poids lourds - bus, camions, engins et générateurs.'},
        'Hair Care and Styling': {'name': 'Coiffure et Soins', 'description': 'Coupe, coiffure, tressage, tissage et soins capillaires.'},
        'Makeup and Beauty': {'name': 'Maquillage et Beauté', 'description': 'Maquillage professionnel - soins du visage, du corps et techniques de beauté.'},
        'Information Technology': {'name': 'Technologie de l\'Information', 'description': 'Programmation, réseaux, bases de données, cloud computing et DevOps.'},
        'Digital Skills': {'name': 'Compétences Numériques', 'description': 'Marketing numérique, médias sociaux, création de contenu et commerce en ligne.'},
        'Carpentry and Woodwork': {'name': 'Menuiserie et Bois', 'description': 'Fabrication de meubles, travail du bois, assemblage et finition.'},
        'Welding and Metalwork': {'name': 'Soudure et Métallurgie', 'description': 'Soudure à l\'arc, MIG, TIG, fabrication métallique et forge.'},
        'Agriculture and Farming': {'name': 'Agriculture', 'description': 'Culture, élevage, agrobusiness et pratiques agricoles durables.'},
        'Tailoring and Fashion': {'name': 'Couture et Mode', 'description': 'Confection, patronage, design textile africain et mode.'},
        'Financial Literacy': {'name': 'Littératie Financière', 'description': 'Budgétisation, épargne, investissement, entrepreneuriat et création de richesse.'},
        'Automotive Marine': {'name': 'Marine Automobile', 'description': 'Moteurs marins, réparation de bateaux, moteurs hors-bord et entretien des bateaux.'},
        'Secondary Education - Arts': {'name': 'Arts - Secondaire', 'description': 'Littérature, histoire, géographie, langues et arts créatifs.'},
        'Secondary Education - Commercial': {'name': 'Commercial - Secondaire', 'description': 'Études commerciales, comptabilité, économie et entrepreneuriat.'},
        'Secondary Education - Science': {'name': 'Sciences - Secondaire', 'description': 'Biologie, chimie, physique et mathématiques.'},
        'Secondary Education - Technical': {'name': 'Technique - Secondaire', 'description': 'Dessin technique, principes de conception et ingénierie.'},
        'Secondary Education - Trade': {'name': 'Commerce - Secondaire', 'description': 'Compétences professionnelles et métiers pratiques.'},
    },
    
    # ===== SPANISH (Español) =====
    'es': {
        'Foundational Literacy': {'name': 'Alfabetización Fundamental', 'description': 'Del analfabetismo total a la lectura, escritura y aritmética con confianza en tu propio idioma.'},
        'Computer Literacy': {'name': 'Alfabetización Informática', 'description': 'Desde lo básico hasta lo avanzado — hardware, software, ciberseguridad, drones, robótica e IA.'},
        'Vocational Trades': {'name': 'Oficios Profesionales', 'description': 'Carpintería, soldadura, fontanería, albañilería, reparación de automóviles, habilidades marítimas y más.'},
        'Certifications': {'name': 'Certificaciones', 'description': 'CompTIA, Network+, Hacking Ético, Drones, CCTV, Robótica y credenciales de IA.'},
        'Life Skills': {'name': 'Habilidades para la Vida', 'description': 'Desarrollo cognitivo, inteligencia emocional, gestión financiera y comunicación.'},
        'Primary Education': {'name': 'Educación Primaria', 'description': 'Currículos escolares completos — Artes, Ciencias, Tecnología, Comercio.'},
        'Secondary Education': {'name': 'Educación Secundaria', 'description': 'Estudios avanzados en Ciencias, Comercio y Tecnología.'},
        'Building Construction': {'name': 'Construcción y Edificación', 'description': 'Albañilería, techado, azulejos, fontanería, pintura y habilidades completas de construcción.'},
        'Housing and Appliances': {'name': 'Vivienda y Aparatos', 'description': 'Reparación de neveras, aire acondicionado, TV, radio y sistemas del hogar.'},
        'Electrical Installation': {'name': 'Instalación Eléctrica', 'description': 'Cableado, instalación solar, reparación de generadores y sistemas eléctricos.'},
        'Automotive - Motorcycles': {'name': 'Automotriz - Motos', 'description': 'Mecánica de motos y triciclos - reparación, mantenimiento y diagnóstico.'},
        'Automotive - Cars and Vans': {'name': 'Automotriz - Autos', 'description': 'Mecánica de autos - motor, transmisión, frenos y sistemas eléctricos.'},
        'Automotive - Heavy Vehicles': {'name': 'Automotriz - Vehículos Pesados', 'description': 'Mecánica de vehículos pesados - buses, camiones, plantas y generadores.'},
        'Hair Care and Styling': {'name': 'Cuidado y Estilismo Capilar', 'description': 'Corte, trenzado, tejido y tratamientos capilares.'},
        'Makeup and Beauty': {'name': 'Maquillaje y Belleza', 'description': 'Maquillaje profesional - cuidado facial y corporal, técnicas de belleza.'},
        'Information Technology': {'name': 'Tecnología de la Información', 'description': 'Programación, redes, bases de datos, cloud computing y DevOps.'},
        'Digital Skills': {'name': 'Habilidades Digitales', 'description': 'Marketing digital, redes sociales, creación de contenido y comercio electrónico.'},
        'Carpentry and Woodwork': {'name': 'Carpintería y Madera', 'description': 'Fabricación de muebles, carpintería, ensamblaje y acabados.'},
        'Welding and Metalwork': {'name': 'Soldadura y Metalurgia', 'description': 'Soldadura, fabricación metálica y herrería.'},
        'Agriculture and Farming': {'name': 'Agricultura', 'description': 'Cultivo, ganadería, agronegocios y prácticas agrícolas sostenibles.'},
        'Tailoring and Fashion': {'name': 'Costura y Moda', 'description': 'Confección, patronaje, diseño textil africano y moda.'},
        'Financial Literacy': {'name': 'Educación Financiera', 'description': 'Presupuesto, ahorro, inversión, emprendimiento y creación de riqueza.'},
        'Automotive Marine': {'name': 'Marina Automotriz', 'description': 'Motores marinos, reparación de botes, motores fuera de borda y mantenimiento.'},
        'Secondary Education - Arts': {'name': 'Artes - Secundaria', 'description': 'Literatura, historia, geografía, idiomas y artes creativas.'},
        'Secondary Education - Commercial': {'name': 'Comercial - Secundaria', 'description': 'Estudios comerciales, contabilidad, economía y emprendimiento.'},
        'Secondary Education - Science': {'name': 'Ciencias - Secundaria', 'description': 'Biología, química, física y matemáticas.'},
        'Secondary Education - Technical': {'name': 'Técnico - Secundaria', 'description': 'Dibujo técnico, principios de diseño e ingeniería.'},
        'Secondary Education - Trade': {'name': 'Comercio - Secundaria', 'description': 'Habilidades profesionales y oficios prácticos.'},
    },
    
    # ===== PORTUGUESE (Português) =====
    'pt': {
        'Foundational Literacy': {'name': 'Alfabetização Fundamental', 'description': 'Do analfabetismo completo à leitura, escrita e numeracia com confiança em sua própria língua.'},
        'Computer Literacy': {'name': 'Alfabetização Informática', 'description': 'Do básico ao avançado — hardware, software, cibersegurança, drones, robótica e IA.'},
        'Vocational Trades': {'name': 'Ofícios Profissionais', 'description': 'Carpintaria, soldadura, canalização, alvenaria, reparação automóvel, habilidades marítimas e mais.'},
        'Certifications': {'name': 'Certificações', 'description': 'CompTIA, Network+, Hacking Ético, Drones, CCTV, Robótica e credenciais de IA.'},
        'Life Skills': {'name': 'Habilidades para a Vida', 'description': 'Desenvolvimento cognitivo, inteligência emocional, gestão financeira e comunicação.'},
        'Primary Education': {'name': 'Ensino Primário', 'description': 'Currículos escolares completos — Artes, Ciências, Tecnologia, Comércio.'},
        'Secondary Education': {'name': 'Ensino Secundário', 'description': 'Estudos avançados em Ciências, Comércio e Tecnologia.'},
        'Building Construction': {'name': 'Construção Civil', 'description': 'Alvenaria, telhados, azulejos, canalização, pintura e habilidades completas de construção.'},
        'Housing and Appliances': {'name': 'Habitação e Eletrodomésticos', 'description': 'Reparação de frigoríficos, ar condicionado, TV, rádio e sistemas domésticos.'},
        'Electrical Installation': {'name': 'Instalação Elétrica', 'description': 'Cablagem, instalação solar, reparação de geradores e sistemas elétricos.'},
        'Automotive - Motorcycles': {'name': 'Automóvel - Motos', 'description': 'Mecânica de motos e triciclos - reparação, manutenção e diagnóstico.'},
        'Automotive - Cars and Vans': {'name': 'Automóvel - Carros', 'description': 'Mecânica de carros - motor, transmissão, travões e sistemas elétricos.'},
        'Automotive - Heavy Vehicles': {'name': 'Automóvel - Veículos Pesados', 'description': 'Mecânica de veículos pesados - autocarros, camiões, plantas e geradores.'},
        'Hair Care and Styling': {'name': 'Cuidados e Estilismo Capilar', 'description': 'Corte, tranças, tecelagem e tratamentos capilares.'},
        'Makeup and Beauty': {'name': 'Maquilhagem e Beleza', 'description': 'Maquilhagem profissional - cuidados faciais e corporais, técnicas de beleza.'},
        'Information Technology': {'name': 'Tecnologia da Informação', 'description': 'Programação, redes, bases de dados, cloud computing e DevOps.'},
        'Digital Skills': {'name': 'Habilidades Digitais', 'description': 'Marketing digital, redes sociais, criação de conteúdo e comércio eletrónico.'},
        'Carpentry and Woodwork': {'name': 'Carpintaria e Madeira', 'description': 'Fabricação de móveis, carpintaria, montagem e acabamentos.'},
        'Welding and Metalwork': {'name': 'Soldadura e Metalurgia', 'description': 'Soldadura, fabricação metálica e serralharia.'},
        'Agriculture and Farming': {'name': 'Agricultura', 'description': 'Cultivo, pecuária, agronegócio e práticas agrícolas sustentáveis.'},
        'Tailoring and Fashion': {'name': 'Costura e Moda', 'description': 'Confeção, modelagem, design têxtil africano e moda.'},
        'Financial Literacy': {'name': 'Literacia Financeira', 'description': 'Orçamento, poupança, investimento, empreendedorismo e criação de riqueza.'},
        'Automotive Marine': {'name': 'Marinha Automotiva', 'description': 'Motores marítimos, reparação de barcos, motores de popa e manutenção.'},
        'Secondary Education - Arts': {'name': 'Artes - Secundário', 'description': 'Literatura, história, geografia, línguas e artes criativas.'},
        'Secondary Education - Commercial': {'name': 'Comercial - Secundário', 'description': 'Estudos comerciais, contabilidade, economia e empreendedorismo.'},
        'Secondary Education - Science': {'name': 'Ciências - Secundário', 'description': 'Biologia, química, física e matemática.'},
        'Secondary Education - Technical': {'name': 'Técnico - Secundário', 'description': 'Desenho técnico, princípios de design e engenharia.'},
        'Secondary Education - Trade': {'name': 'Comércio - Secundário', 'description': 'Habilidades profissionais e ofícios práticos.'},
    },
    
    # ===== SWAHILI (Kiswahili) =====
    'sw': {
        'Foundational Literacy': {'name': 'Kusoma na Kuandika Msingi', 'description': 'Kutoka kutojua kusoma hadi kusoma, kuandika, na kuhesabu kwa ujasiri katika lugha yako mwenyewe.'},
        'Computer Literacy': {'name': 'Ujuzi wa Kompyuta', 'description': 'Kuanzia msingi hadi ngazi za juu — vifaa, programu, usalama wa mtandao, ndege zisizo na rubani, roboti na AI.'},
        'Vocational Trades': {'name': 'Ufundi', 'description': 'Useremala, ufundi wa chuma, mabomba, uashi, matengenezo ya magari, ujuzi wa baharini na mengine.'},
        'Certifications': {'name': 'Vyeti', 'description': 'CompTIA, Network+, Udukuzi wa Maadili, Ndege zisizo na rubani, CCTV, Roboti na vyeti vya AI.'},
        'Life Skills': {'name': 'Stadi za Maisha', 'description': 'Ukuzaji wa akili, akili ya hisia, usimamizi wa fedha na mawasiliano.'},
        'Primary Education': {'name': 'Elimu ya Msingi', 'description': 'Mitaala kamili ya shule — Sanaa, Sayansi, Teknolojia, Biashara.'},
        'Secondary Education': {'name': 'Elimu ya Sekondari', 'description': 'Masomo ya juu katika Sayansi, Biashara na Teknolojia.'},
        'Building Construction': {'name': 'Ujenzi na Uundaji', 'description': 'Uashi, paa, vigae, mabomba, rangi na ujuzi kamili wa ujenzi.'},
        'Housing and Appliances': {'name': 'Makao na Vifaa', 'description': 'Matengenezo ya jokofu, viyoyozi, TV, redio na mifumo ya nyumbani.'},
        'Electrical Installation': {'name': 'Ufungaji wa Umeme', 'description': 'Waya, ufungaji wa jua, matengenezo ya jenereta na mifumo ya umeme.'},
        'Automotive - Motorcycles': {'name': 'Magari - Pikipiki', 'description': 'Mekaniki ya pikipiki - ukarabati, matengenezo na uchunguzi.'},
        'Automotive - Cars and Vans': {'name': 'Magari - Gari na Vans', 'description': 'Mekaniki ya gari - injini, maambukizi, breki na mifumo ya umeme.'},
        'Automotive - Heavy Vehicles': {'name': 'Magari - Magari Mazito', 'description': 'Mekaniki ya magari mazito - mabasi, malori, mitambo na jenereta.'},
        'Hair Care and Styling': {'name': 'Utunzaji wa Nywele', 'description': 'Kukata, kusuka, kuweka na matibabu ya nywele.'},
        'Makeup and Beauty': {'name': 'Vipodozi na Urembo', 'description': 'Vipodozi vya kitaalamu - utunzaji wa uso na mwili, mbinu za urembo.'},
        'Information Technology': {'name': 'Teknolojia ya Habari', 'description': 'Programu, mitandao, hifadhidata, cloud computing na DevOps.'},
        'Digital Skills': {'name': 'Stadi za Kidijitali', 'description': 'Uuzaji wa kidijitali, mitandao ya kijamii, uundaji wa maudhui na biashara mtandaoni.'},
        'Carpentry and Woodwork': {'name': 'Useremala na Mbao', 'description': 'Utengenezaji wa fanicha, mbao, kusanyiko na kumalizia.'},
        'Welding and Metalwork': {'name': 'Ulehemu na Ufundi Chuma', 'description': 'Ulehemu, utengenezaji wa chuma na ufundi wa chuma.'},
        'Agriculture and Farming': {'name': 'Kilimo', 'description': 'Kilimo, ufugaji, biashara ya kilimo na mazoea endelevu.'},
        'Tailoring and Fashion': {'name': 'Ushonaji na Mitindo', 'description': 'Ushonaji, muundo wa mavazi, muundo wa nguo za Kiafrika na mitindo.'},
        'Financial Literacy': {'name': 'Elimu ya Fedha', 'description': 'Bajeti, akiba, uwekezaji, ujasiriamali na uundaji wa utajiri.'},
        'Automotive Marine': {'name': 'Bahari ya Magari', 'description': 'Injini za baharini, ukarabati wa boti, injini za nje na matengenezo.'},
        'Secondary Education - Arts': {'name': 'Sanaa - Sekondari', 'description': 'Fasihi, historia, jiografia, lugha na sanaa za ubunifu.'},
        'Secondary Education - Commercial': {'name': 'Biashara - Sekondari', 'description': 'Masomo ya biashara, uhasibu, uchumi na ujasiriamali.'},
        'Secondary Education - Science': {'name': 'Sayansi - Sekondari', 'description': 'Biolojia, kemia, fizikia na hisabati.'},
        'Secondary Education - Technical': {'name': 'Ufundi - Sekondari', 'description': 'Uchoraji wa kiufundi, kanuni za kubuni na uhandisi.'},
        'Secondary Education - Trade': {'name': 'Biashara - Sekondari', 'description': 'Stadi za kitaalamu na ujuzi wa vitendo.'},
    },
    
    # ===== ARABIC (العربية) =====
    'ar': {
        'Foundational Literacy': {'name': 'محو الأمية الأساسي', 'description': 'من الأمية الكاملة إلى القراءة والكتابة والحساب بثقة في لغتك الخاصة.'},
        'Computer Literacy': {'name': 'محو الأمية الحاسوبية', 'description': 'من الأساسي إلى المتقدم — الأجهزة والبرامج والأمن السيبراني والطائرات بدون طيار والروبوتات والذكاء الاصطناعي.'},
        'Vocational Trades': {'name': 'المهن الحرفية', 'description': 'النجارة واللحام والسباكة والبناء وإصلاح السيارات والمهارات البحرية والمزيد.'},
        'Certifications': {'name': 'الشهادات المهنية', 'description': 'CompTIA، Network+، الاختراق الأخلاقي، الطائرات بدون طيار، CCTV، الروبوتات واعتمادات الذكاء الاصطناعي.'},
        'Life Skills': {'name': 'مهارات الحياة', 'description': 'التطور المعرفي، الذكاء العاطفي، الإدارة المالية والتواصل.'},
        'Primary Education': {'name': 'التعليم الابتدائي', 'description': 'مناهج مدرسية كاملة — الفنون والعلوم والتكنولوجيا والتجارة.'},
        'Secondary Education': {'name': 'التعليم الثانوي', 'description': 'دراسات متقدمة في العلوم والتجارة والتكنولوجيا.'},
        'Building Construction': {'name': 'البناء والتشييد', 'description': 'البناء، الأسقف، البلاط، السباكة، الدهان ومهارات البناء الكاملة.'},
        'Housing and Appliances': {'name': 'الإسكان والأجهزة', 'description': 'إصلاح الثلاجات، التكييف، التلفزيون، الراديو وأنظمة المنزل.'},
        'Electrical Installation': {'name': 'التركيبات الكهربائية', 'description': 'الأسلاك، التركيبات الشمسية، إصلاح المولدات والأنظمة الكهربائية.'},
        'Automotive - Motorcycles': {'name': 'السيارات - الدراجات النارية', 'description': 'ميكانيكا الدراجات النارية والثلاثية - الإصلاح والصيانة والتشخيص.'},
        'Automotive - Cars and Vans': {'name': 'السيارات - السيارات والشاحنات', 'description': 'ميكانيكا السيارات - المحرك، ناقل الحركة، المكابح والأنظمة الكهربائية.'},
        'Automotive - Heavy Vehicles': {'name': 'السيارات - المركبات الثقيلة', 'description': 'ميكانيكا المركبات الثقيلة - الحافلات، الشاحنات، المعدات والمولدات.'},
        'Hair Care and Styling': {'name': 'العناية بالشعر وتصفيفه', 'description': 'القص، التضفير، النسيج وعلاجات الشعر.'},
        'Makeup and Beauty': {'name': 'المكياج والتجميل', 'description': 'المكياج الاحترافي - العناية بالوجه والجسم، تقنيات التجميل.'},
        'Information Technology': {'name': 'تكنولوجيا المعلومات', 'description': 'البرمجة، الشبكات، قواعد البيانات، الحوسبة السحابية و DevOps.'},
        'Digital Skills': {'name': 'المهارات الرقمية', 'description': 'التسويق الرقمي، وسائل التواصل الاجتماعي، إنشاء المحتوى والتجارة الإلكترونية.'},
        'Carpentry and Woodwork': {'name': 'النجارة والأعمال الخشبية', 'description': 'صناعة الأثاث، النجارة، التجميع والتشطيب.'},
        'Welding and Metalwork': {'name': 'اللحام والأعمال المعدنية', 'description': 'اللحام، التصنيع المعدني والحدادة.'},
        'Agriculture and Farming': {'name': 'الزراعة', 'description': 'الزراعة، تربية الماشية، الأعمال الزراعية والممارسات الزراعية المستدامة.'},
        'Tailoring and Fashion': {'name': 'الخياطة والأزياء', 'description': 'الخياطة، تصميم النماذج، تصميم المنسوجات الأفريقية والأزياء.'},
        'Financial Literacy': {'name': 'المعرفة المالية', 'description': 'الميزانية، الادخار، الاستثمار، ريادة الأعمال وبناء الثروة.'},
        'Automotive Marine': {'name': 'البحرية الآلية', 'description': 'المحركات البحرية، إصلاح القوارب، المحركات الخارجية والصيانة.'},
        'Secondary Education - Arts': {'name': 'الفنون - الثانوي', 'description': 'الأدب، التاريخ، الجغرافيا، اللغات والفنون الإبداعية.'},
        'Secondary Education - Commercial': {'name': 'التجاري - الثانوي', 'description': 'الدراسات التجارية، المحاسبة، الاقتصاد وريادة الأعمال.'},
        'Secondary Education - Science': {'name': 'العلوم - الثانوي', 'description': 'الأحياء، الكيمياء، الفيزياء والرياضيات.'},
        'Secondary Education - Technical': {'name': 'التقني - الثانوي', 'description': 'الرسم التقني، مبادئ التصميم والهندسة.'},
        'Secondary Education - Trade': {'name': 'التجاري - الثانوي', 'description': 'المهارات المهنية والحرف العملية.'},
    }
}

# Update all categories with translations
total_updated = 0
categories_updated = {}

for cat in Category.objects.all():
    print(f"\n📝 Processing: {cat.name}")
    for lang_code, lang_translations in translations.items():
        if cat.name in lang_translations:
            translation = lang_translations[cat.name]
            
            # Set the translation fields
            name_field = f'name_{lang_code}'
            desc_field = f'description_{lang_code}'
            
            setattr(cat, name_field, translation['name'])
            setattr(cat, desc_field, translation['description'])
            
            if cat.name not in categories_updated:
                categories_updated[cat.name] = []
            categories_updated[cat.name].append(lang_code)
            
            print(f"  ✅ {lang_code.upper()}: {translation['name']}")
            total_updated += 1
    
    cat.save()

print("\n" + "="*70)
print("📊 SUMMARY")
print("="*70)
print(f"✅ Total Translations Added: {total_updated}")
print(f"📚 Categories Updated: {len(categories_updated)}")

print("\n📊 Categories with Translations:")
for cat_name, langs in categories_updated.items():
    print(f"  📖 {cat_name}: {', '.join([l.upper() for l in langs])}")

print("\n🎉 Complete translations added successfully!")