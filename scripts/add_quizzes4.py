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
# BASIC NUMERACY AND MATHEMATICS
# ============================================================
create_quiz('Basic Numeracy and Mathematics', 'Basic Numeracy and Mathematics — Final Assessment',
'Numbers are the language of business and daily life. This assessment tests your ability to use arithmetic, fractions, percentages and basic problem-solving with confidence.',
25, [
('What is 15% of Le 80,000?', 'multiple_choice',
'To find 15% of any number: multiply by 15 then divide by 100. Le 80,000 times 15 = 1,200,000. Divided by 100 = Le 12,000. Alternatively: 10% of Le 80,000 is Le 8,000. 5% is Le 4,000. Add them: Le 12,000. Percentages appear in every business transaction — discounts, taxes, profit margins, interest rates. Calculating them quickly in your head is an essential life skill.',
[('Le 8,000', False), ('Le 10,000', False), ('Le 12,000', True), ('Le 15,000', False)]),
('A trader buys 12 items for Le 360,000. What is the cost per item?', 'multiple_choice',
'Le 360,000 divided by 12 = Le 30,000 per item. Division is the core skill for calculating unit costs, which every trader must do before setting a selling price. If you know the bulk cost and need to price each unit, divide total cost by quantity. Always calculate unit cost before adding your profit margin.',
[('Le 25,000', False), ('Le 28,000', False), ('Le 30,000', True), ('Le 36,000', False)]),
('What is the fraction 3/4 expressed as a percentage?', 'multiple_choice',
'Divide the numerator by the denominator: 3 divided by 4 = 0.75. Multiply by 100 = 75%. Understanding fractions and percentages are the same thing expressed differently is fundamental numeracy. Half (1/2) = 50%. Quarter (1/4) = 25%. Three-quarters (3/4) = 75%. One-third (1/3) = 33.3%. These conversions come up constantly in business and daily life.',
[('34%', False), ('57%', False), ('75%', True), ('80%', False)]),
('A phone costs Le 500,000. It is reduced by 20%. What is the sale price?', 'multiple_choice',
'20% of Le 500,000 = Le 100,000 discount. Sale price = Le 500,000 minus Le 100,000 = Le 400,000. Alternatively: if the price is reduced by 20%, the customer pays 80% of the original. Le 500,000 times 0.80 = Le 400,000. Both methods give the same answer. Understanding discounts helps you calculate whether a sale price is genuinely a bargain.',
[('Le 350,000', False), ('Le 400,000', True), ('Le 420,000', False), ('Le 450,000', False)]),
('A shop earns Le 2,400,000 in a month and spends Le 1,800,000. What is the profit margin?', 'multiple_choice',
'Profit = Le 2,400,000 minus Le 1,800,000 = Le 600,000. Profit margin = profit divided by revenue times 100 = Le 600,000 divided by Le 2,400,000 times 100 = 25%. A 25% profit margin is healthy for most retail businesses. This calculation tells you what percentage of every sale is actual profit after costs. Tracking this monthly tells you if the business is becoming more or less profitable.',
[('15%', False), ('20%', False), ('25%', True), ('30%', False)]),
('If you save Le 50,000 per week, how many weeks to save Le 650,000?', 'multiple_choice',
'Le 650,000 divided by Le 50,000 per week = 13 weeks. Simple division applied to savings planning. This type of calculation is essential for planning large purchases, equipment investment, or building a business emergency fund. Set a savings target, divide by your weekly savings capacity, and you know exactly how long it will take.',
[('10 weeks', False), ('12 weeks', False), ('13 weeks', True), ('15 weeks', False)]),
('What is the area of a rectangular room that is 5 metres by 4 metres?', 'multiple_choice',
'Area = length times width. 5 metres times 4 metres = 20 square metres. This calculation is essential for: estimating paint or tiles needed for a room, calculating how many bags of cement for a floor, pricing tiling or painting work by the square metre. Every tradesperson (mason, tiler, painter) must calculate areas quickly and accurately.',
[('9 square metres', False), ('18 square metres', False), ('20 square metres', True), ('24 square metres', False)]),
('A loan of Le 1,000,000 has a monthly interest rate of 5%. How much interest is owed after one month?', 'multiple_choice',
'Monthly interest = Principal times rate. Le 1,000,000 times 5% = Le 1,000,000 times 0.05 = Le 50,000. Total owed after one month = Le 1,050,000. Understanding loan interest is critical before borrowing. A 5% monthly rate is 60% per year — very high. Always calculate the total interest cost of a loan before accepting it. Microlenders in West Africa sometimes charge rates this high or higher.',
[('Le 5,000', False), ('Le 50,000', True), ('Le 500,000', False), ('Le 100,000', False)]),
('A recipe needs 250g of flour. You want to make 3 times the recipe. How much flour is needed?', 'multiple_choice',
'250g times 3 = 750g. Scaling recipes requires multiplying all ingredients by the same factor. This applies directly to catering businesses: if a recipe serves 10 and you need to serve 30, multiply all ingredients by 3. Getting this wrong wastes expensive ingredients or produces too little food for the event.',
[('500g', False), ('650g', False), ('750g', True), ('850g', False)]),
('You travel 180 km in 3 hours. What is your average speed in km per hour?', 'multiple_choice',
'Speed = Distance divided by Time. 180 km divided by 3 hours = 60 km/h. This formula also helps estimate journey time: if you know the speed and distance, Time = Distance divided by Speed. For transport businesses and logistics, understanding travel time calculation is practically important for scheduling deliveries and quoting collection times.',
[('45 km/h', False), ('54 km/h', False), ('60 km/h', True), ('90 km/h', False)]),
])

# ============================================================
# COMMUNICATION SKILLS
# ============================================================
create_quiz('Communication Skills', 'Communication Skills — Final Assessment',
'Effective communication is the foundation of every successful career and business relationship. This assessment tests your ability to communicate clearly, professionally and persuasively.',
20, [
('What is active listening?', 'multiple_choice',
'Active listening means fully concentrating on the speaker — not just hearing the words but understanding the message, noting non-verbal cues, asking clarifying questions, and responding thoughtfully. It means not planning your reply while the other person is still speaking. Most people are poor listeners because they are thinking about what to say next. Active listening is one of the most valued professional skills because it is so rare.',
[('Listening while taking notes on everything that is said', False), ('Fully concentrating on the speaker to understand their complete message', True), ('Listening faster than the speaker to save time in meetings', False), ('Agreeing with everything the speaker says to show respect', False)]),
('What is the most professional way to begin a formal business letter or email?', 'multiple_choice',
'Dear Mr/Ms [Surname] is the correct formal greeting when you know the recipient\'s name and gender. If you know the name but not the gender, Dear [Full Name] is acceptable. If you do not know the name, Dear Sir/Madam is correct. Never use Hey, Hi or first names only in a formal business letter unless you have an established informal relationship. The greeting sets the professional tone for everything that follows.',
[('Hey [First name] — friendly and approachable', False), ('Dear Mr/Ms [Surname] — formal and professional', True), ('To whom it may concern — always the safest option', False), ('Good day — polite and culturally appropriate', False)]),
('What does "tone" mean in written communication?', 'multiple_choice',
'Tone is the attitude or feeling conveyed in writing — formal or informal, warm or cold, assertive or passive, confident or uncertain. The same information can be communicated in many different tones. A complaint letter can be assertive and professional, or aggressive and rude. Understanding tone helps you match your writing style to the situation and reader, and recognise how your own writing might be perceived.',
[('The volume level at which a message should be read aloud', False), ('The attitude and feeling conveyed in the writing — formal, warm, assertive etc', True), ('The length and structure of a written document', False), ('The choice of font and formatting in a document', False)]),
('In a meeting, someone makes a point you strongly disagree with. What is the professional response?', 'multiple_choice',
'Listen fully without interrupting. Acknowledge their point genuinely. Then share your different view using "I" statements and evidence: "I see it differently because..." or "My experience suggests..." Avoid personal attacks, eye-rolling, or dismissive body language. Disagreement is healthy in professional settings when it focuses on ideas rather than personalities. The most respected colleagues disagree constructively.',
[('Immediately correct them in front of the group to establish the facts', False), ('Listen fully, acknowledge their view, then share your different perspective respectfully', True), ('Wait until after the meeting to tell their manager about the error', False), ('Remain silent to avoid conflict — your opinion can be shared another time', False)]),
('What is the 7-38-55 rule of communication?', 'multiple_choice',
'Albert Mehrabian\'s research suggested that in face-to-face communication, only 7% of meaning is carried by the words themselves, 38% by tone of voice, and 55% by body language and facial expression. This is why text messages and emails are so often misunderstood — you lose 93% of the communication channels. In person, your posture, eye contact, facial expression and voice carry far more than your words alone.',
[('A formula for writing: 7 sentences, 38 words, 55 characters maximum', False), ('7% words, 38% tone of voice, 55% body language in face-to-face communication', True), ('Read 7 times, edit 38%, reduce to 55% of original length', False), ('A negotiation guideline: offer 7% less, expect 38% counter, settle at 55%', False)]),
('What does "jargon" mean and why should it be avoided with general audiences?', 'multiple_choice',
'Jargon is specialised technical language used within a profession or industry — medical terms, legal language, IT terminology. It is efficient between experts who share the vocabulary but excludes and confuses people outside that group. Using jargon with a general audience signals poor communication skills and makes the speaker seem more interested in appearing expert than in being understood. Always use plain language with non-specialist audiences.',
[('Long-winded language that should always be shortened', False), ('Specialised technical vocabulary that excludes non-specialist audiences', True), ('Slang or informal language inappropriate for professional settings', False), ('Foreign words unnecessarily inserted into English sentences', False)]),
('What is a feedback sandwich?', 'multiple_choice',
'The feedback sandwich structure: positive comment first (the bread), then the constructive criticism or improvement needed (the filling), then another positive (the second bread slice). This structure makes critical feedback easier to receive without feeling attacked. It is used by managers, teachers and coaches to maintain motivation while communicating what needs to improve. The criticism must be specific and actionable, not vague.',
[('A technique for giving only positive feedback without negative criticism', False), ('Positive feedback, then constructive criticism, then positive — making feedback easier to receive', True), ('Alternating praise and criticism repeatedly throughout a performance review', False), ('Written feedback delivered in three separate emails over three days', False)]),
('When leaving a voicemail, what information should always be included?', 'multiple_choice',
'Every voicemail should include: your full name, your phone number (spoken slowly and repeated), the purpose of your call (brief), and when you are available to receive a call back. Many people rush voicemails and leave incomplete information, forcing the recipient to call back to ask basic questions. A professional voicemail is brief, clear and complete — the recipient should have everything they need to respond.',
[('Only your name — they will have your number from the missed call', False), ('Your name, phone number, purpose of call and when you are available', True), ('A detailed explanation of your full situation and all relevant history', False), ('Just say call me back — brevity is always most professional', False)]),
('What is the most effective structure for a persuasive argument?', 'multiple_choice',
'The most effective persuasive structure is: state your position clearly, provide evidence (facts, examples, statistics), anticipate and address the main objection, then conclude with a clear call to action. Addressing objections proactively is the most powerful element — it shows you have considered all sides and strengthens your credibility. This structure works for sales, proposals, negotiations and any situation where you need to change someone\'s mind.',
[('State your conclusion repeatedly until the audience accepts it', False), ('State position, provide evidence, address objections, conclude with a call to action', True), ('Ask questions to let the audience convince themselves without stating your position', False), ('Begin with objections and work backwards to your position', False)]),
('Why is it important to confirm understanding at the end of any important conversation?', 'multiple_choice',
'Summarising key points and agreements at the end of a conversation confirms both parties understood the same things. Misunderstandings in verbal communication are extremely common — what was said and what was heard often differ. "Just to confirm — you will deliver the goods on Friday and I will pay on collection. Is that correct?" prevents disputes, missed deliveries, and the frustration of discovering a misunderstanding days later when it is too late.',
[('It shows you were listening and makes the other person feel valued', False), ('It ensures both parties understood the same things and prevents later misunderstandings', True), ('It gives you an opportunity to negotiate better terms at the last moment', False), ('It is a professional formality required in all business transactions', False)]),
])

# ============================================================
# ENGLISH LANGUAGE SKILLS
# ============================================================
create_quiz('English Language Skills', 'English Language Skills — Final Assessment',
'English is the language of international business, education and professional opportunity. This assessment tests the grammar, vocabulary and writing skills that open doors.',
25, [
('Which sentence is grammatically correct?', 'multiple_choice',
'"She doesn\'t know the answer" is correct. In present tense, third-person singular (he, she, it) uses "doesn\'t" (does not) for negation. "Don\'t" is for I, you, we, they. "She don\'t" is a common spoken error but incorrect in written English. Mastering subject-verb agreement is one of the most important grammar foundations for professional English writing.',
[('She don\'t know the answer', False), ('She doesn\'t know the answer', True), ('She not know the answer', False), ('She knowing not the answer', False)]),
('What is the difference between "their", "there" and "they\'re"?', 'multiple_choice',
'"Their" shows possession (belonging to them): "Their business is growing." "There" refers to a place or introduces a clause: "The office is over there." or "There are five people." "They\'re" is a contraction of "they are": "They\'re coming tomorrow." These three words are among the most commonly confused in written English. Spell-checkers will not catch the wrong one because all three are correctly spelled.',
[('They are all interchangeable spellings of the same word', False), ('Their = possession; there = place/existence; they\'re = they are', True), ('Their is formal; there is informal; they\'re is for speech only', False), ('Only they\'re is correct in modern English; the others are archaic', False)]),
('Choose the correct sentence:', 'multiple_choice',
'"I have been working here for three years" is correct — using present perfect continuous tense to describe an action that started in the past and continues now. "I am working here since three years" is incorrect — "since" is used with a specific point in time (since 2020), not a duration. "For" is used with durations (for three years, for six months). This distinction is very common in professional written English.',
[('I am working here since three years', False), ('I have been working here for three years', True), ('I working here three years already', False), ('I work here since three years ago', False)]),
('What does "concise" mean in writing?', 'multiple_choice',
'Concise means expressing the complete idea using as few words as necessary — no padding, no repetition, no unnecessary qualifications. "Due to the fact that" can be replaced with "because." "At this point in time" becomes "now." "In the event that" becomes "if." Professional writing values conciseness because readers\' time is valuable and long-winded writing signals unclear thinking. Be brief. Be direct. Be complete.',
[('Using many long words to sound intelligent and educated', False), ('Expressing ideas fully using as few words as necessary', True), ('Writing in short sentences of five words or fewer', False), ('Omitting important details to reduce the length of a document', False)]),
('Which punctuation mark introduces a list or explanation?', 'multiple_choice',
'A colon (:) introduces a list, an explanation, or elaboration of what was just stated. "The package includes three items: a pen, a notebook and a ruler." The colon signals: what follows explains or lists what just came before. A semi-colon (;) connects two closely related independent clauses. A comma is for shorter pauses and items in a list. Correct punctuation makes writing much clearer.',
[('A semi-colon (;)', False), ('A colon (:)', True), ('A dash (—)', False), ('An apostrophe (\')', False)]),
('What is a paragraph and how long should it be?', 'multiple_choice',
'A paragraph is a group of sentences about one main idea. It begins with a topic sentence stating the main idea, followed by supporting sentences that explain, evidence or illustrate that idea, and often ends with a concluding sentence. In business writing, paragraphs should typically be 3-5 sentences. Very long paragraphs are visually intimidating and hard to follow. Very short paragraphs (one sentence) fragment ideas. Aim for 3-5 sentences per paragraph as a guide.',
[('Any group of sentences, with no specific rules on length or content', False), ('A group of sentences about one idea, typically 3-5 sentences in business writing', True), ('Exactly 5 sentences — the standard paragraph length in professional writing', False), ('A single long sentence that covers all aspects of a topic', False)]),
('The word "however" is an example of what type of word?', 'multiple_choice',
'However, therefore, furthermore, nevertheless, consequently and moreover are conjunctive adverbs (also called transition words or discourse markers). They connect ideas between sentences and show the logical relationship: contrast (however, nevertheless), addition (furthermore, moreover), consequence (therefore, consequently). Using them correctly makes writing flow logically. Incorrect use makes writing confusing.',
[('An adjective that modifies the meaning of a noun', False), ('A conjunctive adverb (transition word) showing contrast between ideas', True), ('A preposition showing the relationship between objects', False), ('A verb that describes the action of the sentence', False)]),
('What is the passive voice and when is it appropriate?', 'multiple_choice',
'Active voice: "The manager approved the report." Passive voice: "The report was approved by the manager." Passive voice emphasises the action or the object rather than the actor. It is appropriate when: the actor is unknown ("The window was broken"), the actor is obvious ("Mistakes were made"), or you want to de-emphasise the actor for diplomatic reasons ("The invoice was not paid on time"). Active voice is generally clearer and more direct. Use passive sparingly.',
[('Writing that does not use any action verbs', False), ('A construction that emphasises the action or object rather than the actor', True), ('Writing that uses very gentle language to avoid offending the reader', False), ('Sentences written entirely in past tense', False)]),
('What does proofreading involve?', 'multiple_choice',
'Proofreading is checking a completed document for errors — spelling mistakes, grammatical errors, punctuation mistakes, inconsistencies, and factual errors. It is always the final step before sending or publishing any written document. Best practice: proofread after a break (fresh eyes catch more errors), read aloud (your ear catches what your eye misses), use spell-check but do not rely on it alone (it misses context-dependent errors). Professional written work is always proofread.',
[('Checking that a document looks attractive and professionally formatted', False), ('Checking a completed document for spelling, grammar and other errors before sending', True), ('Having a colleague write feedback on the quality of your ideas', False), ('Shortening a document by removing unnecessary sections', False)]),
('Which version of this sentence is most appropriate for a professional job application?', 'multiple_choice',
'"I am writing to apply for the position of Administrative Assistant advertised on your website" is professional, specific and direct. It immediately tells the reader the purpose of the letter and shows the applicant has done their research. "I want a job" is vague and unprofessional. Application letters must be specific about the role, formal in tone, and demonstrate professionalism from the first sentence.',
[('I want a job and I think I would be good at it', False), ('I am writing to apply for the position of Administrative Assistant advertised on your website', True), ('Please find enclosed my CV as I am looking for employment opportunities', False), ('Hey, I saw you are hiring and I would love to work for you', False)]),
])

# ============================================================
# LIFE SKILLS LITERACY
# ============================================================
create_quiz('Life Skills Literacy', 'Life Skills Literacy — Final Assessment',
'Life skills are the practical abilities needed to navigate adult life successfully — from managing money to staying healthy to building relationships.',
20, [
('What is the most important habit for maintaining good physical health?', 'multiple_choice',
'Regular physical activity, adequate sleep, and a balanced diet are all essential. However, if forced to choose one, adequate sleep is the foundation that enables all others. During sleep, the body repairs itself, the immune system strengthens, and the brain consolidates learning. Most adults need 7-9 hours per night. Chronic sleep deprivation impairs decision-making, mood, immune function and physical performance — making every other health habit harder to maintain.',
[('Taking vitamin supplements daily', False), ('Adequate sleep of 7-9 hours per night as the foundation of physical health', True), ('Joining a gym and exercising for 2 hours daily', False), ('Avoiding all processed food entirely', False)]),
('What is the first step in resolving a conflict with someone at work or at home?', 'multiple_choice',
'Listen to understand their perspective fully before responding. Most conflicts escalate because both parties feel unheard and respond defensively without really understanding what the other person is saying. By genuinely listening first — without interrupting, without planning your response — you often discover the other person\'s actual concern is different from what you assumed. Understanding precedes resolution.',
[('Assert your position clearly and firmly from the beginning', False), ('Listen fully to understand their perspective before responding', True), ('Involve a third party immediately to mediate', False), ('Wait for the other person to apologise first', False)]),
('What is goal setting and why is it important?', 'multiple_choice',
'Goal setting is the process of identifying specific, achievable outcomes you want to reach within a defined time frame. Goals give direction to effort — without them, energy is scattered. SMART goals (Specific, Measurable, Achievable, Relevant, Time-bound) are far more effective than vague aspirations. "I will save Le 200,000 per month for 6 months to buy a sewing machine" is a SMART goal. "I want to be rich" is not.',
[('Making a wish list of everything you would like to have', False), ('Identifying specific achievable outcomes with defined timeframes to direct your effort', True), ('Planning the exact steps of every day for the next 10 years', False), ('Telling others what you want so they can help you achieve it', False)]),
('What is the correct way to wash hands to prevent disease?', 'multiple_choice',
'WHO-recommended handwashing: Wet hands, apply soap, rub for at least 20 seconds covering all surfaces including between fingers and under nails, rinse thoroughly, dry with clean material. 20 seconds is approximately the time to sing Happy Birthday twice. Most people wash for 6-8 seconds which is insufficient to remove pathogens. Handwashing after toilet use and before eating prevents the majority of diarrhoeal disease transmission.',
[('Rinse with water alone for 5 seconds — soap is only needed when hands are visibly dirty', False), ('Apply soap and rub all surfaces for at least 20 seconds then rinse thoroughly', True), ('Use hand sanitiser instead of soap and water for better protection', False), ('Wash once per day in the morning — this protects throughout the day', False)]),
('What is personal budgeting?', 'multiple_choice',
'A personal budget is a plan for how you will spend and save your income each month. It lists all expected income sources and allocates specific amounts to: essential expenses (food, rent, transport, bills), savings (emergency fund, goals), and discretionary spending (entertainment, non-essentials). A budget makes you intentional about money instead of reactive. People who budget consistently build savings and avoid debt more successfully than those who spend without planning.',
[('A list of everything you spent last month as a record', False), ('A plan allocating income to essential expenses, savings and discretionary spending', True), ('An agreement with a bank about how much you can spend each month', False), ('Restricting all spending to only absolute essentials', False)]),
('What is the difference between needs and wants?', 'multiple_choice',
'Needs are things required for survival and basic functioning: food, shelter, healthcare, education, clothing (basic). Wants are things that improve comfort or enjoyment but are not essential: entertainment, fashion beyond basics, luxury food, expensive phones. Financial difficulties often arise from spending on wants before all needs are covered. The discipline of meeting needs first and using remaining income for wants is fundamental to financial stability.',
[('Needs are expensive; wants are cheap', False), ('Needs are required for survival; wants improve comfort but are not essential', True), ('Needs are for adults; wants are for children', False), ('There is no meaningful difference — all spending is a choice', False)]),
('What is time management and why does it matter?', 'multiple_choice',
'Time management is organising and planning how to divide your time between specific activities to maximise effectiveness. Good time management means completing important tasks before they become urgent, avoiding procrastination, and maintaining energy by working in focused blocks with rest. Poor time management creates constant crisis management — always rushing, always late, always stressed. The most productive people are not those who work the most hours, but those who work the most effectively.',
[('Working as many hours as possible to achieve maximum output', False), ('Organising time to complete important tasks effectively while avoiding constant crisis', True), ('Using a digital calendar to schedule every minute of the day', False), ('Delegating all tasks to others to free up your own time', False)]),
('What does SMART stand for in goal setting?', 'multiple_choice',
'SMART: Specific (clearly defined, not vague), Measurable (you can track progress), Achievable (realistic given your resources), Relevant (matters to your actual priorities), Time-bound (has a deadline). A goal that meets all five criteria is far more likely to be achieved than a vague aspiration. "I will save Le 1,000,000 in 12 months by saving Le 83,333 per month" is SMART. "I want to save more money" is not.',
[('Simple, Manageable, Attainable, Realistic, Timely', False), ('Specific, Measurable, Achievable, Relevant, Time-bound', True), ('Systematic, Motivated, Active, Responsible, Thoughtful', False), ('Strategic, Meaningful, Ambitious, Rewarding, Tracked', False)]),
('What is emotional intelligence (EQ)?', 'multiple_choice',
'Emotional intelligence is the ability to recognise, understand and manage your own emotions, and to recognise and respond effectively to the emotions of others. High EQ enables better relationships, more effective conflict resolution, better leadership, and more resilient responses to setbacks. Research consistently shows that EQ is a better predictor of professional success than IQ. It can be developed through self-reflection, empathy practice and feedback.',
[('Intelligence measured by emotional brain scans rather than traditional IQ tests', False), ('The ability to recognise, understand and manage your own and others\' emotions effectively', True), ('The ability to remain emotionally neutral and unaffected by stressful situations', False), ('Intelligence related specifically to creative and artistic abilities', False)]),
('How should you respond if someone you know is showing signs of serious depression?', 'multiple_choice',
'Listen without judgment. Let them talk without trying to fix or minimise. Take expressions of hopelessness seriously. Encourage them to speak to a health professional or trusted counsellor. Stay in regular contact — isolation worsens depression. Do not leave someone alone if they express thoughts of self-harm. Mental health is health — encourage the same help-seeking that a serious physical illness would warrant. In Sierra Leone, contact a health facility or trusted community leader.',
[('Tell them to cheer up and focus on positive things', False), ('Listen without judgment, take it seriously, encourage professional help and stay in contact', True), ('Give them space as they probably want to be alone', False), ('Share your own problems so they feel less alone with theirs', False)]),
])

# ============================================================
# EMOTIONAL INTELLIGENCE
# ============================================================
create_quiz('Emotional Intelligence', 'Emotional Intelligence — Final Assessment',
'Emotional intelligence determines how effectively you relate to others, manage yourself under pressure and lead with empathy. These skills are foundational to all professional success.',
20, [
('What are the five core components of emotional intelligence according to Daniel Goleman?', 'multiple_choice',
'Daniel Goleman\'s model identifies: Self-awareness (knowing your own emotions), Self-regulation (managing your emotions), Motivation (internal drive), Empathy (understanding others\' emotions), and Social skills (managing relationships). These five components together predict professional success, effective leadership and relationship quality more reliably than technical skills or IQ alone. All five can be developed with deliberate practice.',
[('Intelligence, Creativity, Empathy, Communication and Leadership', False), ('Self-awareness, Self-regulation, Motivation, Empathy and Social skills', True), ('Happiness, Confidence, Kindness, Patience and Resilience', False), ('Thinking, Feeling, Sensing, Intuiting and Judging', False)]),
('What does self-awareness mean in the context of emotional intelligence?', 'multiple_choice',
'Self-awareness means accurately knowing your own emotions — what you are feeling, why you are feeling it, how your emotional state affects your thinking and behaviour, and how you come across to others. A self-aware person notices when stress is making them irritable before they snap at someone. They recognise their own biases. They understand their strengths and weaknesses honestly. Self-awareness is the foundation from which all other emotional intelligence develops.',
[('Being aware of your physical body and its sensations at all times', False), ('Accurately knowing your own emotions, their causes and their effect on your behaviour', True), ('Thinking about yourself often and reflecting on your achievements', False), ('Being very sensitive and easily affected by the emotions of others', False)]),
('A colleague snaps at you angrily over a minor issue. What is the emotionally intelligent response?', 'multiple_choice',
'Recognise that the anger is probably not really about you — it is likely about stress, fatigue or a situation you are unaware of. Respond calmly without escalating. Wait for a calmer moment to ask if everything is alright. This is empathy combined with self-regulation: not taking the bait, not retaliating, and looking for the human need beneath the behaviour. This approach resolves most workplace conflicts before they escalate.',
[('Assert yourself firmly and explain why their behaviour is unacceptable', False), ('Respond calmly, recognise the anger is likely not about you, and check in with them later', True), ('Report them to management immediately to protect yourself', False), ('Avoid them entirely for the rest of the day to allow things to settle', False)]),
('What is empathy and how does it differ from sympathy?', 'multiple_choice',
'Empathy is feeling with someone — putting yourself in their position and understanding their emotional experience. Sympathy is feeling for someone — acknowledging their difficulty from your own position. Empathy connects; sympathy can distance. In practice: sympathy says "I am sorry you feel that way." Empathy says "I understand why you feel that way — I can see how that situation would be very difficult." Empathy builds deeper trust and connection.',
[('Empathy is stronger than sympathy — it involves crying with the person', False), ('Empathy is feeling with someone; sympathy is feeling for someone — empathy connects more deeply', True), ('They are the same — both mean caring about how others feel', False), ('Sympathy is genuine; empathy is performed to appear caring', False)]),
('What is self-regulation in emotional intelligence?', 'multiple_choice',
'Self-regulation is the ability to manage disruptive emotions and impulses — not suppressing them, but not acting on them impulsively either. When you are angry but choose a calm response. When you are anxious but still deliver a presentation. When you are disappointed but move forward constructively. Self-regulation enables professional behaviour even when emotions are strong. It is the skill that keeps you effective under pressure.',
[('Regulating your work schedule and personal time strictly', False), ('Managing disruptive emotions so they do not control your behaviour', True), ('Suppressing all emotions to remain completely neutral at work', False), ('Setting limits on how long you will work before taking a break', False)]),
('What is the difference between a growth mindset and a fixed mindset?', 'multiple_choice',
'Carol Dweck\'s research: a growth mindset believes intelligence and ability are developed through effort, learning and persistence. A fixed mindset believes these are fixed traits you either have or do not have. Growth mindset people embrace challenges, learn from failure and improve continuously. Fixed mindset people avoid challenges that might expose their limitations. Emotional intelligence supports growth mindset by enabling resilient responses to failure.',
[('Growth mindset focuses on business expansion; fixed mindset on maintaining current position', False), ('Growth mindset believes abilities develop through effort; fixed mindset sees them as innate and unchangeable', True), ('Growth mindset is optimistic; fixed mindset is realistic', False), ('Growth mindset is for young people; fixed mindset develops naturally with age', False)]),
('When receiving critical feedback about your work, what is the emotionally intelligent response?', 'multiple_choice',
'Listen fully without becoming defensive. Separate the feedback from your self-worth — feedback is about the work, not your value as a person. Ask clarifying questions to understand what specifically could improve. Thank the person genuinely. Reflect on whether the feedback has merit and what you can learn. This response requires self-regulation (not reacting defensively), self-awareness (not being threatened by feedback), and growth mindset (seeing feedback as information for improvement).',
[('Defend your decisions thoroughly so the reviewer understands your reasoning', False), ('Listen without defensiveness, ask clarifying questions and reflect on what you can learn', True), ('Accept all feedback without question to demonstrate humility and openness', False), ('Express your disappointment so the reviewer knows the feedback was hurtful', False)]),
('What is the most effective way to build genuine rapport with someone you have just met professionally?', 'multiple_choice',
'Show genuine interest in them — ask questions about their work, their experience, what they find interesting about what they do. Listen actively to their answers rather than waiting to talk about yourself. Remember and use their name. Find common ground. People feel rapport when they feel genuinely seen and heard, not when they are impressed by the other person. The paradox of rapport: you build it by focusing on them, not on yourself.',
[('Share impressive achievements to establish your credibility', False), ('Show genuine interest in them, ask questions and listen actively', True), ('Find common ground by discussing neutral topics like the weather', False), ('Mirror their body language and speech patterns exactly', False)]),
('A team member consistently underperforms. You are their supervisor. What is the emotionally intelligent approach?', 'multiple_choice',
'Have a private, respectful conversation. Focus on specific behaviours and their impact, not the person\'s character. Listen to understand if there are obstacles you are unaware of — personal difficulties, unclear expectations, skill gaps. Agree on specific improvements and a timeline. Follow up consistently. This approach — empathy combined with accountability — is far more effective than public criticism or ignoring the problem. It also treats the team member with the dignity that motivates improvement.',
[('Address the underperformance publicly in a team meeting to motivate everyone', False), ('Have a private respectful conversation focused on specific behaviours and their impact', True), ('Transfer them to another team to avoid ongoing conflict', False), ('Ignore it — performance will improve naturally when the person is ready', False)]),
('How does emotional intelligence help in sales and customer service?', 'multiple_choice',
'Emotionally intelligent salespeople and service providers: read emotional cues to understand what the customer really needs (not just what they say), manage their own frustration when dealing with difficult customers, build genuine rapport that creates loyalty, handle objections empathetically rather than defensively, and create experiences that make customers feel valued. Research consistently shows that emotional connection drives purchasing decisions more than logic alone — particularly in West African market contexts where trust and relationship are paramount.',
[('It allows salespeople to manipulate customers\' emotions to close sales faster', False), ('It enables reading emotional cues, managing own emotions and building genuine rapport that drives loyalty', True), ('High EQ salespeople avoid emotional topics and keep all conversations factual', False), ('Emotional intelligence is irrelevant in sales — product quality and price determine everything', False)]),
])

# ============================================================
# COGNITIVE SKILLS DEVELOPMENT
# ============================================================
create_quiz('Cognitive Skills Development', 'Cognitive Skills Development — Final Assessment',
'Cognitive skills — how you think, learn, remember and solve problems — determine your effectiveness in every area of life. These skills can be deliberately developed.',
20, [
('What is critical thinking?', 'multiple_choice',
'Critical thinking is the ability to analyse information objectively, evaluate its credibility and relevance, identify assumptions and biases, consider alternative explanations, and draw well-reasoned conclusions. It means not accepting claims at face value because they come from an authority figure or because they match what you already believe. In an age of misinformation, critical thinking is one of the most important skills a person can develop.',
[('Thinking negatively about ideas in order to find their flaws', False), ('Analysing information objectively to evaluate it and draw well-reasoned conclusions', True), ('Criticising other people\'s ideas in group discussions', False), ('Thinking very carefully and slowly before making any decision', False)]),
('What is the best method for memorising and retaining new information?', 'multiple_choice',
'Spaced repetition — reviewing material at increasing intervals (after 1 day, then 3 days, then 1 week, then 1 month) — is the most scientifically supported method for long-term memory. The brain strengthens memories each time information is retrieved, especially just before forgetting. Cramming the night before creates short-term retention but the information is forgotten within days. Active recall (testing yourself) is more effective than re-reading.',
[('Re-read your notes many times until the information feels familiar', False), ('Use spaced repetition — review at increasing intervals to strengthen long-term memory', True), ('Create colourful mind maps of all information immediately after learning', False), ('Study for long unbroken sessions to maximise the time spent with the material', False)]),
('What is problem-solving and what is the recommended approach?', 'multiple_choice',
'Structured problem-solving: define the problem precisely (what exactly is wrong?), gather relevant information, generate multiple possible solutions without judging them initially, evaluate each solution against criteria, choose and implement the best solution, then review the result and adjust if needed. The most common mistake is jumping to solutions before fully understanding the problem. A well-defined problem is halfway solved.',
[('Immediately implementing the first solution that comes to mind', False), ('Define the problem precisely, generate multiple options, evaluate, implement, review', True), ('Find someone who has solved a similar problem and copy their solution', False), ('Work through all possible solutions systematically until one works', False)]),
('What is confirmation bias?', 'multiple_choice',
'Confirmation bias is the tendency to search for, interpret and remember information that confirms what you already believe, while ignoring or discounting contradictory evidence. It is one of the most powerful and universal cognitive biases. It causes people to be more certain of their beliefs than the evidence warrants. Recognising confirmation bias in yourself is the first step to thinking more objectively — deliberately seek out evidence against your own position.',
[('The bias toward confirming that you are making the right decision', False), ('The tendency to seek information that confirms existing beliefs while ignoring contradictory evidence', True), ('Overconfidence in your memory of past events', False), ('The tendency to agree with whoever you spoke to most recently', False)]),
('What is the difference between deductive and inductive reasoning?', 'multiple_choice',
'Deductive reasoning goes from general principles to specific conclusions: "All men are mortal. Kofi is a man. Therefore Kofi is mortal." The conclusion must be true if the premises are true. Inductive reasoning goes from specific observations to general conclusions: "Every swan I have seen is white, therefore all swans are probably white." The conclusion is probable, not certain. (Most swans are white, but black swans exist.) Understanding both types helps you evaluate arguments.',
[('Deductive is simple; inductive is complex', False), ('Deductive goes from general to specific (certain); inductive goes from specific to general (probable)', True), ('Deductive is used in science; inductive is used in everyday life', False), ('They are the same process described with different terms', False)]),
('What is metacognition?', 'multiple_choice',
'Metacognition is thinking about your own thinking — being aware of how you learn, what strategies work for you, when you understand something and when you are confused, what your cognitive strengths and weaknesses are. Students and professionals who practise metacognition learn faster and more effectively because they monitor their own understanding and adjust their approach. "Do I actually understand this or do I just recognise it?" is a metacognitive question.',
[('The ability to memorise large amounts of information accurately', False), ('Thinking about your own thinking — awareness of how you learn and understand', True), ('Using multiple cognitive approaches simultaneously for complex problems', False), ('The study of cognitive decline in older age', False)]),
('What habit is most effective for developing creative thinking?', 'multiple_choice',
'Deliberately exposing yourself to diverse experiences, fields, cultures and ideas is the most reliable way to develop creative thinking. Creativity largely comes from combining existing ideas in new ways — the more varied your inputs, the more novel your combinations. Reading widely outside your field, talking to people from different backgrounds, travelling, and trying new activities all build the diverse mental library from which creative connections are drawn.',
[('Spending long uninterrupted periods in quiet isolation thinking about one problem', False), ('Deliberately exposing yourself to diverse experiences, fields and ideas to build a varied mental library', True), ('Practising creative exercises like drawing and music even if you lack talent', False), ('Brainstorming alone produces better creative ideas than group brainstorming', False)]),
('What is a logical fallacy?', 'multiple_choice',
'A logical fallacy is an error in reasoning that makes an argument invalid — it appears to be logical but contains a flaw. Common examples: Ad hominem (attacking the person rather than their argument), Straw man (misrepresenting someone\'s argument to make it easier to attack), False dilemma (presenting only two options when more exist), and Slippery slope (claiming one event will lead inevitably to extreme consequences). Recognising fallacies helps you evaluate arguments critically.',
[('A mathematical calculation error that leads to the wrong answer', False), ('An error in reasoning that makes an argument appear valid when it is not', True), ('A factual mistake in a statement or claim', False), ('A deliberate lie used to mislead people', False)]),
('What is the best approach when you feel overwhelmed by a large or complex task?', 'multiple_choice',
'Break the task into the smallest possible steps and focus on just the next step. A large task is overwhelming because the brain sees the whole and cannot process it as a single action. Breaking it into small, specific steps makes each one manageable and creates a clear path forward. Starting with the very first step (even if small) creates momentum. The task that feels impossible as a whole becomes straightforward as a sequence of small steps.',
[('Push through and work intensely until the entire task is complete', False), ('Break it into the smallest possible steps and focus only on the next step', True), ('Set it aside until you feel motivated to approach it', False), ('Discuss the task with others to get their perspective before starting', False)]),
('Why is reading regularly one of the most powerful habits for cognitive development?', 'multiple_choice',
'Reading builds vocabulary (enabling more precise thinking and communication), develops the ability to follow complex arguments, exposes the mind to different perspectives and ways of thinking, and trains sustained concentration — increasingly rare in an age of constant digital distraction. Reading fiction specifically develops empathy by placing the reader in others\' perspectives. Professionals who read consistently across their career maintain cognitive sharpness and expand their knowledge base far beyond their immediate field.',
[('Reading improves eyesight through regular exercise of the visual system', False), ('Reading builds vocabulary, develops analytical ability, exposes diverse perspectives and trains concentration', True), ('Reading is only beneficial for academic subjects, not practical skills', False), ('The benefit is the same whether you read for 5 minutes or 2 hours daily', False)]),
])

# Print summary
print('\n' + '='*60)
from certifications.models import Quiz
total_q = sum(q.questions.count() for q in Quiz.objects.all())
quiz_count = Quiz.objects.count()
print(f'Total quizzes: {quiz_count}')
print(f'Total questions: {total_q}')

courses_without_quiz = []
from courses.models import Course
for c in Course.objects.all().order_by('title'):
    try:
        c.quiz
    except:
        courses_without_quiz.append(c.title)
print(f'\nCourses still needing quizzes: {len(courses_without_quiz)}')
for t in courses_without_quiz:
    print(f'  - {t}')