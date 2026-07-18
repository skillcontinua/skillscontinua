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
# SECONDARY PHYSICS
# ============================================================
create_quiz('Secondary Physics', 'Secondary Physics — Final Assessment',
'Physics explains how the universe works — from the motion of objects to electricity, waves and energy. This assessment covers the key concepts of secondary physics.',
25, [
('What is Newton\'s First Law of Motion?', 'multiple_choice',
'Newton\'s First Law (Law of Inertia): an object at rest stays at rest, and an object in motion stays in motion at the same speed and direction, unless acted upon by an unbalanced external force. Inertia is the tendency of matter to resist changes to its state of motion. This explains why passengers lurch forward when a vehicle brakes suddenly (their bodies continue moving when the vehicle stops) and why you need force to start, stop or change the direction of motion.',
[('Every action has an equal and opposite reaction', False), ('An object stays at rest or in uniform motion unless an external force acts on it', True), ('Force equals mass multiplied by acceleration', False), ('The acceleration of an object is inversely proportional to its mass', False)]),
('What is the difference between speed and velocity?', 'multiple_choice',
'Speed is a scalar quantity — it has magnitude (size) only: 60 km/h. Velocity is a vector quantity — it has both magnitude and direction: 60 km/h north. An object moving in a circle at constant speed is constantly changing velocity (because direction changes), so it is accelerating even though speed is constant. This distinction is fundamental in physics and explains circular motion, projectiles and many other phenomena.',
[('Speed is measured in km/h; velocity is measured in m/s', False), ('Speed has magnitude only; velocity has both magnitude and direction', True), ('Speed is for slow objects; velocity is for fast-moving objects', False), ('They are the same quantity measured in different units', False)]),
('What is Ohm\'s Law?', 'multiple_choice',
'Ohm\'s Law states: Voltage (V) = Current (I) × Resistance (R), or V = IR. If you know any two of these three quantities, you can calculate the third. At constant temperature, the current through a conductor is directly proportional to the voltage across it. Understanding Ohm\'s Law is fundamental to all electrical work — calculating cable sizes, fuse ratings, power consumption, and troubleshooting electrical circuits.',
[('Power equals voltage multiplied by current', False), ('Voltage equals current multiplied by resistance — V = IR', True), ('Resistance equals voltage divided by power', False), ('Current equals voltage multiplied by resistance', False)]),
('What is the difference between potential energy and kinetic energy?', 'multiple_choice',
'Potential energy is stored energy due to position or condition: a raised object has gravitational potential energy (PE = mgh), a compressed spring has elastic potential energy. Kinetic energy is energy of motion: KE = ½mv². As an object falls, PE converts to KE. At the bottom of a fall, almost all PE has become KE (minus energy lost to air resistance). The total mechanical energy (PE + KE) is conserved in an ideal system (Law of Conservation of Energy).',
[('Potential energy is electrical; kinetic energy is mechanical', False), ('Potential energy is stored (position/condition); kinetic energy is energy of motion', True), ('Potential energy is for stationary objects; kinetic energy adds when they move', False), ('They are the same energy described from different reference frames', False)]),
('What is the unit of electrical power and how is it calculated?', 'multiple_choice',
'Electrical power is measured in Watts (W). Power = Voltage × Current (P = VI). Also P = I²R = V²/R using Ohm\'s Law substitutions. A 100W bulb connected to 230V draws 100/230 = 0.43 Amps. Kilowatts (kW) = 1000W. Electricity bills are in kilowatt-hours (kWh) — power in kW multiplied by time in hours. A 2kW air conditioner running for 3 hours uses 6 kWh of electrical energy.',
[('Joules — the same unit as energy', False), ('Watts — calculated as Voltage multiplied by Current (P = VI)', True), ('Amperes — measuring the flow of electrical charge', False), ('Ohms — the unit of electrical resistance', False)]),
('What is the electromagnetic spectrum?', 'multiple_choice',
'The electromagnetic spectrum is the range of all electromagnetic radiation, ordered by wavelength (or frequency). From longest wavelength to shortest: Radio waves, Microwaves, Infrared, Visible light, Ultraviolet, X-rays, Gamma rays. All travel at the speed of light (3×10⁸ m/s) in a vacuum. Each type has different properties and applications: radio (communication), microwave (heating, communication), infrared (heat, remote controls), visible light (sight), UV (sterilisation), X-rays (medical imaging), gamma (cancer treatment).',
[('A range of colours visible to the human eye from red to violet', False), ('The full range of electromagnetic radiation from radio waves to gamma rays', True), ('The spectrum of electrical signals used in telecommunications', False), ('A measure of the frequency range of sound waves', False)]),
('What is the principle of moments?', 'multiple_choice',
'The principle of moments states that for a body in equilibrium, the sum of clockwise moments about any pivot equals the sum of anticlockwise moments. Moment = Force × perpendicular distance from pivot. A see-saw balances when: (Force 1 × distance 1) = (Force 2 × distance 2). This principle explains levers, seesaws, cranes, and is used in structural engineering to ensure stability.',
[('Objects in motion continue moving in the same direction', False), ('For equilibrium, clockwise moments equal anticlockwise moments about any pivot', True), ('Momentum is conserved in all collisions', False), ('The moment