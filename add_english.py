import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'skillscontinua_core.settings')
django.setup()

from courses.models import Course, Lesson

def add_lessons(title, lessons_data):
    try:
        course = Course.objects.get(title=title)
        Lesson.objects.filter(course=course).delete()
        for order, lesson_title, duration, content in lessons_data:
            Lesson.objects.create(
                course=course,
                title=lesson_title,
                content_type='text',
                content_text=content,
                order=order,
                duration_minutes=duration,
                is_active=True
            )
        print(f'OK: {title} - {course.lessons.count()} lessons')
    except Course.DoesNotExist:
        print(f'NOT FOUND: {title}')

add_lessons('English Language Skills', [
    (1, 'Reading and Vocabulary', 20,
     'Strong reading and vocabulary skills are the foundation of all communication.\n\n'
     'READING FOR MEANING:\n'
     'Reading is not just saying words - it is understanding what they mean together.\n'
     'Fluency: Reading smoothly at a natural pace with correct expression.\n'
     'Comprehension: Understanding what you have read.\n'
     'Critical reading: Evaluating what you read - is it true? Is it fair?\n\n'
     'READING STRATEGIES:\n'
     'Skimming: Reading quickly to get the general idea. Look at headings and first sentences.\n'
     'Scanning: Looking for specific information. For a date, name or fact.\n'
     'Intensive reading: Reading carefully for full understanding. Study texts.\n'
     'Extensive reading: Reading for enjoyment. Any material you choose.\n\n'
     'BUILDING VOCABULARY:\n'
     'Context clues: Use surrounding words to guess meaning.\n'
     'Word families: Knowing one form helps with others. Educate, education, educational, educationally.\n'
     'Prefixes: un (not), re (again), pre (before), mis (wrongly), dis (not).\n'
     'Suffixes: tion (noun), ful (adjective), ly (adverb), er (person who does).\n'
     'Keep a vocabulary notebook: New word, definition, example sentence, translation if helpful.\n\n'
     'TYPES OF TEXTS:\n'
     'Narrative: Stories with characters and events.\n'
     'Descriptive: Describes a person, place or thing.\n'
     'Expository: Explains facts and information.\n'
     'Persuasive: Tries to change your mind or behaviour.\n'
     'Instructional: Tells you how to do something step by step.\n\n'
     'PRACTICAL EXERCISE:\n'
     'Read one article from a newspaper or website.\n'
     'Find five words you do not know. Look up each one.\n'
     'Write the word, its meaning, and use it in your own sentence.\n'
     'Summarise the article in three sentences using your own words.'),

    (2, 'Grammar in Use', 25,
     'Grammar is the set of rules that allows us to communicate clearly and be understood correctly.\n\n'
     'TENSES IN USE:\n\n'
     'PRESENT SIMPLE:\n'
     'For habits, facts and routines.\n'
     'I work as a carpenter. Water boils at 100 degrees. She goes to market on Fridays.\n\n'
     'PRESENT CONTINUOUS:\n'
     'For actions happening now or around now.\n'
     'I am building a table. She is studying for her exams. They are planning a new project.\n\n'
     'PAST SIMPLE:\n'
     'For completed actions in the past.\n'
     'He finished the job yesterday. We visited Lagos last year.\n\n'
     'PRESENT PERFECT:\n'
     'For past actions with present relevance. Uses have or has plus past participle.\n'
     'I have completed the training. She has lived here for ten years.\n\n'
     'FUTURE:\n'
     'Will: Predictions and decisions made at the moment of speaking. It will rain tomorrow.\n'
     'Going to: Plans and intentions. I am going to start my own business.\n\n'
     'MODAL VERBS:\n'
     'Can: Ability. I can drive.\n'
     'Could: Past ability or polite request. Could you help me please?\n'
     'Must: Strong obligation. You must pay your taxes.\n'
     'Should: Advice or mild obligation. You should eat breakfast.\n'
     'May/Might: Possibility. It may rain later.\n\n'
     'ARTICLES:\n'
     'A or An: Used before singular countable nouns mentioned for the first time.\n'
     'A book. An engineer. Use an before vowel sounds.\n'
     'The: Used when the noun is already known or is specific.\n'
     'The book on the table. The president of Nigeria.\n'
     'No article: Before uncountable nouns and plural nouns used generally.\n'
     'Water is essential. Carpenters use tools.\n\n'
     'PRACTICAL EXERCISE:\n'
     'Write a paragraph about your typical working day using present simple.\n'
     'Write a paragraph about something you have achieved using present perfect.\n'
     'Write a paragraph about your plans for the next year using going to and will.\n'
     'Check that you have used articles correctly throughout.'),

    (3, 'Writing for Work and Life', 25,
     'Good writing opens doors in business and professional life.\n\n'
     'THE PROFESSIONAL EMAIL:\n'
     'Subject line: Clear and specific. Invoice for carpentry work - 15 June.\n'
     'Greeting: Dear Mr Johnson, Dear Ms Okonkwo, Dear Sir/Madam.\n'
     'Opening: State your purpose immediately. I am writing to enquire about...\n'
     'Body: One idea per paragraph. Clear and concise.\n'
     'Closing: Thank you for your time. I look forward to hearing from you.\n'
     'Sign-off: Yours sincerely (when you know their name), Yours faithfully (when you do not).\n'
     'Your name and contact details below.\n\n'
     'THE FORMAL LETTER:\n'
     'Your address: Top right.\n'
     'Date: Below your address.\n'
     'Recipient address: Left side, below date.\n'
     'Subject line: Re: Your complaint of 12 March. Makes purpose clear.\n'
     'Same structure as professional email.\n'
     'Formal letters are used for: Complaints, applications, official requests.\n\n'
     'THE REPORT:\n'
     'Title: What the report is about.\n'
     'Introduction: Purpose and scope of the report.\n'
     'Findings: What was discovered. Use headings for each section.\n'
     'Conclusions: What the findings mean.\n'
     'Recommendations: What should be done.\n'
     'Reports are factual and objective. No personal opinion unless in a separate section.\n\n'
     'CV (CURRICULUM VITAE):\n'
     'Personal details: Name, contact information.\n'
     'Personal statement: 3-4 sentences summarising your skills and goals.\n'
     'Work experience: Most recent first. Job title, employer, dates, key responsibilities.\n'
     'Education and qualifications: Most recent first.\n'
     'Skills: IT skills, languages, certifications.\n'
     'References: Two professional references or Available on request.\n\n'
     'PRACTICAL EXERCISE:\n'
     'Write a professional email applying for a job or contract.\n'
     'Write a one-page CV for yourself.\n'
     'Ask someone to review both and give honest feedback.\n'
     'Make improvements based on the feedback.'),

    (4, 'Speaking and Listening in English', 20,
     'Spoken English is essential for work, education and daily life.\n\n'
     'PRONUNCIATION:\n'
     'English pronunciation can be challenging because spelling and sound do not always match.\n'
     'Stress: In English, one syllable in each word is stressed (said more strongly).\n'
     'COMputer. carPENter. rePAIR. EDucation.\n'
     'Intonation: The rise and fall of your voice.\n'
     'Questions: Voice rises at the end. You are a carpenter?\n'
     'Statements: Voice falls at the end. I am a carpenter.\n\n'
     'CONNECTED SPEECH:\n'
     'In natural speech, words run together.\n'
     'Do you want to becomes D\'you wanna in informal speech.\n'
     'I am going to becomes I\'m gonna.\n'
     'Understanding this helps with listening comprehension.\n\n'
     'LISTENING STRATEGIES:\n'
     'Do not try to understand every word - focus on keywords.\n'
     'Listen for stressed words - they carry the main meaning.\n'
     'Use context to fill gaps in understanding.\n'
     'Ask for clarification: Could you repeat that please? What do you mean by...?\n\n'
     'CONVERSATION SKILLS:\n'
     'Turn-taking: Wait for a pause before speaking. Do not interrupt.\n'
     'Showing interest: Really? That\'s interesting. I see. Go on.\n'
     'Agreeing: Exactly. Absolutely. I couldn\'t agree more.\n'
     'Disagreeing politely: I see your point but... With respect, I think...\n'
     'Clarifying: What I mean is... In other words... Let me put it another way.\n\n'
     'PRESENTATIONS IN ENGLISH:\n'
     'Opening: Good morning everyone. Today I would like to talk about...\n'
     'Signposting: First... Then... After that... Finally...\n'
     'Summarising: To summarise... In conclusion...\n'
     'Questions: Are there any questions?\n\n'
     'PRACTICAL EXERCISE:\n'
     'Record yourself speaking for two minutes on any topic you know well.\n'
     'Listen back. Note: Pronunciation, fluency, vocabulary, clarity.\n'
     'Practice the same topic again trying to improve each area.\n'
     'Find a conversation partner and practice for 15 minutes per day.'),

    (5, 'English for Career Development', 15,
     'English is the language of global opportunity. Investing in it pays lifelong dividends.\n\n'
     'ENGLISH IN THE WORKPLACE:\n'
     'Meetings: Follow the agenda. Take notes. Summarise action points.\n'
     'Presentations: Prepare thoroughly. Speak slowly and clearly. Use examples.\n'
     'Negotiation: Listen carefully. Ask questions. Clarify terms. Confirm agreements in writing.\n'
     'Client communication: Professional tone. Prompt responses. Follow up in writing.\n\n'
     'ENGLISH FOR FURTHER EDUCATION:\n'
     'Many universities and training courses teach in English.\n'
     'Professional certifications (CompTIA, CCTV, Cloud) all require English.\n'
     'Academic writing: Formal, evidence-based, referenced.\n'
     'Research skills: Finding and evaluating English language sources.\n\n'
     'INTERNATIONAL ENGLISH QUALIFICATIONS:\n'
     'IELTS (International English Language Testing System): Required for study or migration.\n'
     'Four components: Listening, Reading, Writing, Speaking.\n'
     'Band scores 1-9. Most universities require Band 6 or 6.5.\n'
     'Cambridge English qualifications: B1, B2, C1, C2 levels.\n'
     'These qualifications are internationally recognised and valued by employers.\n\n'
     'SELF-IMPROVEMENT PLAN:\n'
     'Reading: One article or book chapter per day in English.\n'
     'Listening: English radio, podcasts or films with subtitles.\n'
     'Writing: Journal, messages, emails in English.\n'
     'Speaking: Find a language exchange partner or join an English conversation group.\n'
     'Apps: Duolingo, BBC Learning English, British Council Learn English.\n\n'
     'WEST AFRICA AND ENGLISH:\n'
     'English is the official language of Nigeria, Ghana, Sierra Leone, Liberia and Gambia.\n'
     'ECOWAS promotes multilingualism but English is the most widely used official language.\n'
     'Strong English skills significantly increase earning potential across West Africa.\n'
     'They also open doors to international remote work opportunities.\n\n'
     'PRACTICAL EXERCISE:\n'
     'Set a specific English language goal for the next three months.\n'
     'Examples: Read one English book, pass an online English test, give one presentation in English.\n'
     'Create a daily practice schedule of at least 20 minutes.\n'
     'Track your progress weekly.\n'
     'Share your goal with someone who will hold you accountable.'),
])

# Final complete check
print('\n' + '='*60)
from courses.models import Course, Lesson
total_lessons = 0
total_courses = Course.objects.count()
complete = 0
partial = 0
empty = 0

for c in Course.objects.all().order_by('title'):
    count = c.lessons.count()
    total_lessons += count
    if count >= 5:
        complete += 1
    elif count > 0:
        partial += 1
        print(f'  PARTIAL ({count}): {c.title}')
    else:
        empty += 1
        print(f'  EMPTY: {c.title}')

print(f'\nCOURSES: {total_courses} total')
print(f'  Complete (5+ lessons): {complete}')
print(f'  Partial (1-4 lessons): {partial}')
print(f'  Empty (0 lessons):     {empty}')
print(f'TOTAL LESSONS: {total_lessons}')
print(f'COMPLETION: {round(complete/total_courses*100)}%')