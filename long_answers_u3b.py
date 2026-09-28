# -*- coding: utf-8 -*-
U3B = {}

U3B[49] = {
"q": "A department is experiencing repeated performance errors. Apply the concept of TNA to identify what information should be collected before designing training.",
"intro": """This is an application of Training Needs Assessment. The department wants fewer errors. A beginner’s mistake is to announce a workshop on ‘quality’ immediately. TNA says: collect information first to decide whether training is the answer, who needs it, and what exactly must be learned. Use the three analyses — organisation, task, person — and the notes’ warning that training is not the answer to all problems.

Write the answer as a list of information to collect, with why each item matters. That is what ‘apply TNA’ means.""",
"pts": [
("Error facts, not opinions",
"""Collect type of error, frequency, process step, shift, product, cost, and whether errors cluster on certain days or machines. Use records plus observation, not only the supervisor’s anger. Without facts, TNA is gossip and design will be guesswork."""),
("Organisation-analysis information",
"""Department goals and quality standards; recent changes (new machine, new target, new software); staffing levels; whether speed is rewarded more than accuracy; whether supervisors actually support the correct method. Strategy link: is this error hurting customers or safety enough to be a priority?"""),
("Non-training causes — the most important TNA question",
"""Machine condition, missing tools, unclear or conflicting SOPs, impossible workload, incentive to rush, bad raw material. If these dominate, design a process or resource fix, not a course. The notes say apply cause-and-effect analysis before deciding that training is the answer. Write this boldly; it shows HRD maturity."""),
("Task-analysis information",
"""The correct procedure step by step; which steps are critical; knowledge, skills and attitudes required; safety points; where in the task errors actually occur. This information becomes content if training is justified."""),
("Person-analysis information",
"""Who makes the errors — new joiners, one shift, everyone? Previous training history. Can they explain the correct method (knowledge) but still fail (skill or attitude or pressure)? Language and literacy. Difference between ‘does not know’ and ‘knows but does not do’."""),
("Learner readiness and motivation",
"""Do employees believe errors matter? Are they afraid to report near-misses? Will they be punished for slowing down to be correct? If fear is high, climate work is needed along with or instead of skill training."""),
("Transfer-climate information",
"""After a possible course, will the boss allow slower correct practice? Do peers mock the official method? Is the old informal shortcut still the way to hit targets? If transfer climate is hostile, even perfect design will not reduce errors."""),
("Baseline for later evaluation",
"""Current error rate, customer complaints, rework cost. Agree what reduction in 8–12 weeks would mean success. Collecting this now is part of TNA, not something to invent after the programme. Without baseline, nobody can evaluate."""),
],
"conc": """Before designing training, collect: error data, organisation context, non-training causes, task KSAs, person gaps, readiness, transfer climate, and a baseline. Only if the gap is largely a KSA gap should you design training. That is applied TNA, not a reflex workshop."""
}

U3B[50] = {
"q": "Apply suitable training methods to design a development program for employees who need both practical job skills and conceptual knowledge.",
"intro": """The learners need two kinds of learning at once. Conceptual knowledge is understanding — why a standard exists, what the principle is, how parts of the job connect. Practical skill is being able to do the task to a standard with one’s hands, voice or software. One method rarely serves both well. Apply a blend: methods for the head, methods for the hand, a sequence, and evaluation of both.""",
"pts": [
("Split the TNA into two lists of objectives",
"""Write conceptual objectives separately (‘explain why lock-out is needed’) and practical objectives (‘perform lock-out on machine A in three minutes using the checklist’). Methods follow this split. If you mix them into one vague aim, you will lecture everything and practise nothing."""),
("Methods for conceptual knowledge",
"""Short lectures, discussion, diagrams, caselets, e-learning modules, quizzes. Example: why a bank’s KYC rule exists, not only which screen to click. Concepts travel to new situations; that is why they are needed along with skill."""),
("Safe practice methods before live work",
"""Vestibule training, simulation, dummy machines, role play, lab. Mistakes here do not harm customers or equipment. This is the bridge from concept to the job. Off-the-job practice is especially important if the real task is dangerous or costly."""),
("On-the-job coaching for real skill",
"""After simulation, OJT with a trained coach and a checklist. Job rotation if the practical skill has several contexts. The coach must be taught to teach; otherwise OJT copies bad habits."""),
("Action-learning project to bind both",
"""A live but bounded problem where they must use the concept to decide and the skill to implement, then present what they learned. This prevents ‘I understood in class but froze at work’."""),
("E-learning as a refresher for concepts",
"""Short modules they can replay after OJT, when the concept starts to fade. Useful for mixed locations. Not a substitute for practice."""),
("Sequence matters",
"""Recommended: concept → demonstration → simulated practice with feedback → OJT → review. Starting with unsupervised OJT may freeze wrong methods that later training cannot easily remove."""),
("Evaluate both kinds of learning",
"""Knowledge tests for concepts (Kirkpatrick level 2). Observed job samples for skill (levels 2 and 3). If you only give a theory exam, practical skill may still be weak, and the programme has not met the brief."""),
],
"conc": """Design a blended programme: conceptual methods (class/e-learning), safe practice (simulation/role play), then OJT coaching, plus an action project and dual evaluation. Suitable methods are a mix in a sensible sequence, not a single favourite of the trainer."""
}

U3B[51] = {
"q": "State any two purposes of Training Needs Assessment.",
"intro": """TNA is systematic finding of whether, who and what to train. For 8 marks, two purposes must be explained at length, then other purposes added. The two strongest: (1) identify genuine learning needs, (2) prevent training from being used as a false solution.""",
"pts": [
("First purpose — identify genuine KSA gaps",
"""Using organisation, task and person analysis, TNA finds what knowledge, skill or attitude is missing, in which job, and in which people, relative to the standard of performance. This purpose gives HRD a map. Without it, programmes are aimed in the dark. Example: repeated billing errors might be a software-skill gap for new clerks only, not a ‘motivation problem’ of the whole department."""),
("How this purpose is carried out",
"""Performance data, observation, interviews, tests, competency lists versus strategy. The formula standard minus actual is used carefully, only when the cause is KSA."""),
("Second purpose — prevent wrong solutions",
"""The notes warn that training is not the answer to all company problems and that firms buy off-the-shelf programmes without checking relevance. TNA’s second purpose is diagnostic honesty: if the cause is a broken machine, a bad incentive, or shortage of staff, do not design a course. This protects money, time and HRD’s reputation."""),
("Example of the second purpose",
"""A hotel’s front desk is rude because they are understaffed and punished for any delay, not because they have never heard of courtesy. A smile-training day would score well on reaction and change nothing. TNA should stop that design."""),
("Further purpose — set objectives for design",
"""TNA supplies measurable learning and performance objectives. Design cannot start professionally without them."""),
("Further purpose — select the right trainees and methods",
"""Not everyone needs the same programme. Skill vs knowledge vs attitude needs different methods. TNA guides both choices."""),
("Further purpose — prioritise and create a baseline",
"""Critical jobs and large gaps first. Pre-training performance is recorded so evaluation is possible. Organisation analysis also aligns TNA with strategy."""),
("Exam shape",
"""Two long purpose paragraphs with examples, then a cluster of design, selection, priority, baseline, strategy. Do not write two headings and one line each."""),
],
"conc": """Two main purposes of TNA are to identify real knowledge-skill-attitude gaps and to stop the organisation from using training as a false solution. Other purposes include setting objectives, choosing people and methods, prioritising, and creating an evaluation baseline. TNA is the first professional step in HRD training."""
}

U3B[52] = {
"q": "Name any two levels of the Kirkpatrick model.",
"intro": """Kirkpatrick’s model has four levels: Reaction, Learning, Behaviour and Results. The question says ‘any two’, but 8 marks require you to name two in detail, briefly explain the other two, give measures, and say why more than one level matters. Never submit only two words.""",
"pts": [
("Level 1 — Reaction (name and explain as your first)",
"""This level asks whether participants liked the programme and found it relevant. It is measured by feedback forms at the end (affective outcomes in the notes). It is useful for improving comfort and trainer style. It is a weak measure of effectiveness if used alone, because entertainment can score high."""),
("Level 2 — Learning (name and explain as your second)",
"""This level asks whether knowledge, skill or attitude actually increased. Measures: tests, demonstrations, pre–post comparison, role-play against a checklist. If people did not learn, they cannot honestly show new job behaviour later."""),
("Level 3 — Behaviour, briefly",
"""Do they apply learning on the job after a lag? Observation, supervisor ratings, audits. Transfer climate decides much of this level."""),
("Level 4 — Results, briefly",
"""Did the organisation benefit — quality, errors, safety, sales, customer measures, costs — impact on corporate objectives? Harder to prove cause, most important for the funder."""),
("Why an 8-mark answer must go beyond two names",
"""The syllabus is the whole model. Write two levels as long explanations and the other two as supporting paragraphs so the examiner sees complete knowledge."""),
("Measurement examples you can quote",
"""Reaction: form with relevance items. Learning: 20-mark skill test. Behaviour: 60-day call audit. Results: defect rate versus TNA baseline."""),
("Ladder logic",
"""Each level supports but does not guarantee the next. Positive reaction does not prove learning; learning does not prove transfer."""),
("HRD use",
"""Important or costly programmes should not stop at reaction. Short awareness talks may not need full level 4. Proportion is part of professional use."""),
],
"conc": """Name any two levels in depth — the safest pair is Reaction and Learning, or Behaviour and Results — then briefly complete the model. Kirkpatrick’s four levels together define training effectiveness; two names without explanation cannot earn 8 marks."""
}

U3B[53] = {
"q": "Analyse why a training program may receive positive participant reactions but still fail to improve job performance.",
"intro": """This is the gap between Kirkpatrick level 1 (reaction) and levels 3–4 (behaviour and results). Participants may honestly enjoy the programme — good food, charming trainer, beautiful venue, easy days away from work — and still work exactly as before on Monday. Analysis must look inside the programme, at the original need, and at the workplace. Do not write only ‘they were happy’.""",
"pts": [
("Entertainment is not learning",
"""A motivational speaker and a hill-station venue raise reaction. If skill was not practised, level 2 never happened. Job performance cannot improve from quotes in a notebook. Analysis: the programme optimised the wrong level."""),
("Learning too easy or too theoretical",
"""Content that does not stretch, or that never leaves the slide, leaves people happy and still incompetent. They liked it because it did not demand uncomfortable practice."""),
("Wrong need — TNA was missing",
"""The performance problem was a tool, a process, an impossible target, or a pay issue. Training cannot improve job performance then, however pleasant. Notes: training is not the answer to all problems. Analysis starts at Stage 1 failure."""),
("Hostile or empty transfer climate",
"""The boss says ‘forget the classroom, we have targets’. Peers mock the new method. The official SOP is not the real SOP. Behaviour cannot change. Reaction was about the classroom; performance lives in the department."""),
("No opportunity to use the skill",
"""The software is not installed, or the task comes once in six months. Skill decays. Reaction was real; performance chance never came."""),
("Conflicting appraisal and rewards",
"""Taught quality; paid only for speed. People follow pay. Analysis: organisational systems beat training. Job performance is a system outcome."""),
("No follow-up, coaching or IDP",
"""One event, no refreshers, no supervisor observation. Learning decays. Positive reaction is about a memory of a good two days, not about a changed habit."""),
("Analytical conclusion for the examiner",
"""Reaction is a weak predictor of job performance because enjoyment, learning, transfer conditions and organisational systems are different things. HRD must design for levels 2–4 and for climate, not for applause. A programme can fail at any step after a successful level 1."""),
],
"conc": """Positive reactions with no performance gain usually mean the programme was pleasant but diagnostically wrong, theoretically thin, or unsupported at work. Analyse classroom, TNA and workplace. Do not confuse smile sheets with HRD effectiveness."""
}

U3B[54] = {
"q": "Analyse the consequences of designing a training program without conducting an adequate Training Needs Assessment.",
"intro": """Consequence means what happens next, to work, to money, to people, and to HRD itself. Inadequate TNA means the designer did not properly study organisation goals, tasks, persons, and non-training causes. Design then aims at a fog. Analyse a chain of effects, not a single sentence ‘it will fail’.""",
"pts": [
("Wrong content — the original problem continues",
"""Topics miss the real KSA gaps. Errors, delays or rude service continue. Staff and customers see no benefit. Operational consequence is ‘we trained and nothing changed’."""),
("Wrong audience",
"""Skilled staff are bored (they may even give poor reaction); needy staff are absent. Development equity fails. The people who needed help remain unhelped."""),
("Wrong method",
"""A lecture is used where coaching was needed, or a two-day off-site where a one-week OJT would have worked. Learning and transfer fail even if the topic name was roughly right."""),
("Training as a false solution — the dangerous consequence",
"""System problems (machine, incentive, staffing) remain. Management thinks ‘we already trained them’ and stops looking. The next time errors occur, workers are blamed personally. This consequence is moral as well as operational."""),
("Demotivation and cynicism about HRD",
"""Employees lose faith. Future programmes suffer ‘attendance of the body but not of the mind’. Climate worsens. Later even a good TNA-based course is harder to run."""),
("Wasted budget and lost production time",
"""Direct vendor cost plus opportunity cost of people away from work. In a tight organisation this is serious. Mention both costs in the exam."""),
("Evaluation becomes theatre",
"""No true objectives or baseline, so anyone can claim success or failure. The training cycle cannot learn. HRD cannot improve."""),
("Strategic drift over time",
"""The calendar becomes a ritual disconnected from goals. Capability lag appears in a crisis — quality failure, digital lag. Consequence is long-term organisational weakness, not only one bad course."""),
],
"conc": """Without adequate TNA, design produces wrong content, people and methods; hides real causes; wastes money; creates cynicism; and blocks honest evaluation and strategy. Adequate TNA is professional risk control, not extra paperwork. Analyse this chain in the answer book."""
}

U3B[55] = {
"q": "Evaluate the usefulness of the Kirkpatrick model for judging the effectiveness of an organisational training program.",
"intro": """Evaluate = usefulness + limitations + how to use it well + a verdict. The Kirkpatrick model judges training at reaction, learning, behaviour and results. The notes already ask HRD to look beyond affective reactions to learning, behaviour and impact on corporate objectives. So the model fits the syllabus. It is not perfect science.""",
"pts": [
("Usefulness — completeness compared with smile sheets",
"""It forces attention to learning, job behaviour and organisational results. That matches professional HRD and prevents the entertainment illusion. This is its greatest use."""),
("Usefulness — a common language with managers",
"""Four levels are easy to explain to people who fund training. HRD can say: we will not claim success only on tea and venue. Communication value is real in organisations."""),
("Usefulness — helps design and diagnosis",
"""If you plan measures at TNA time, objectives become operational. If reaction is high and behaviour is low, look at transfer climate, not only the trainer. The model locates the break in the chain."""),
("Limitation — causality at level 4",
"""Sales, quality and profit have many causes. Training may be only one. Over-claiming ‘this course caused 10% profit’ is unscientific. Usefulness falls if the model is treated as proof rather than as a guide."""),
("Limitation — cost, time and incomplete use",
"""Behaviour and results need follow-up months later. Many firms stop at level 1; then the model is unused, which is not the model’s fault, but it limits usefulness in practice."""),
("Limitation — not every programme needs all four levels equally",
"""A one-hour policy briefing versus a critical safety skill should not consume the same evaluation energy. Usefulness depends on proportionate use."""),
("How to use it well",
"""Plan measures early; collect baseline; combine with transfer design (boss support); do not worship level 1; be modest at level 4; use more depth for costly or high-risk training."""),
("Verdict",
"""The Kirkpatrick model is highly useful as a guiding framework for judging organisational training effectiveness, especially compared with judging only participant happiness. It is not a mechanical proof of success. Recommend it with judgement, not as four forms to file and forget."""),
],
"conc": """Useful for completeness, communication, design and diagnosis; limited on causality, cost and one-size use. Verdict: keep Kirkpatrick as the standard HRD map of effectiveness, apply it proportionately and honestly."""
}

U3B[56] = {
"q": "Analyse how the choice among on-the-job, off-the-job, and e-learning methods can affect training outcomes.",
"intro": """Outcomes mean what happens at Kirkpatrick’s levels — did they like it, learn, change behaviour, and improve results? Method is not a decoration. On-the-job, off-the-job and e-learning create different kinds of learning experiences, different costs, and different transfer patterns. Analysis should take each method, then discuss fit, blending, and climate.""",
"pts": [
("On-the-job outcomes",
"""Typically strong relevance and transfer (good path to level 3) if the coach is skilled and has time. Outcomes become bad if the coach is busy or teaches shortcuts: then the organisation mass-produces wrong methods. OJT can also injure on dangerous tasks. Outcome quality follows coach quality more than the label ‘OJT’."""),
("Off-the-job outcomes",
"""Typically better conceptual learning and safer practice (stronger level 2 for new or risky skills). Level 3 suffers if the classroom does not resemble work or if bosses do not continue coaching. Cost and time away from work can be high; if TNA was weak, outcomes are expensive irrelevance with possibly high reaction (nice venue)."""),
("E-learning outcomes",
"""Good for consistent knowledge, scale, tracking (level 2 for information; level 1 depends on design quality). Weak completion if self-discipline or connectivity is poor. Weak for complex interpersonal skill unless blended with role play. Outcome risk: organisations think ‘we have an LMS so people are trained’ while completion and transfer are low."""),
("Fit to objective changes outcomes more than fashion",
"""Motor skill → OJT or simulation. Interpersonal skill → role play then OJT. Information update → e-learning. Wrong fit lowers outcomes regardless of budget. Analysis: choose method from TNA, not from what is trendy."""),
("Learner and context factors",
"""New employees often need structured off-the-job. Experienced staff may prefer OJT or micro e-learning. Scattered locations favour e-learning. Mismatch reduces motivation and therefore learning outcomes."""),
("Blended outcomes are often superior",
"""Concept via e-learning or class, practice off-the-job, application on-the-job with a coach. Each method covers another’s weakness. Analysis: the choice is frequently ‘how to combine’, not ‘which one winner’."""),
("Climate can cancel any method",
"""If the workplace punishes new behaviour, OJT, classroom and e-learning all fail at level 3. Method analysis without transfer climate is incomplete."""),
("Analytical close",
"""Outcomes are produced by fit + quality of execution + transfer support, not by the brand name of the method. Method choice is a strategic HRD decision because it shapes whether learning stays in the head or appears in job performance."""),
],
"conc": """OJT favours transfer but depends on coaches; off-the-job favours safe conceptual and skill practice but risks transfer failure; e-learning favours scale and knowledge consistency but risks low completion and weak people-skills. Fit, blending and climate decide outcomes. Write this analysis, not three disconnected definitions."""
}

U3B[57] = {
"q": "State any two reasons for evaluating training at more than one Kirkpatrick level.",
"intro": """One level, especially reaction only, cannot tell whether training was effective. For 8 marks, two reasons in depth, then supporting reasons. The two strongest: different levels answer different questions; and several levels are needed to diagnose where the chain broke.""",
"pts": [
("First reason — different levels answer different questions",
"""Reaction asks ‘did they like it?’ Learning asks ‘did they get the KSA?’ Behaviour asks ‘do they do it at work?’ Results ask ‘did the organisation benefit?’ Liking is not learning; learning is not doing; doing is not always business results. Evaluating at only one level answers only one of these questions and then pretends it answered all. That is why more than one level is needed."""),
("Example for the first reason",
"""A fire-safety course can be popular (level 1) while people still cannot use an extinguisher (level 2). Or they can pass a test (level 2) and still not follow procedure on the shop floor (level 3). One number cannot stand for effectiveness."""),
("Second reason — diagnosis of failure so HRD can improve",
"""If you only know that ‘performance did not improve’, you do not know whether to change content, trainer, transfer climate, or the original diagnosis. Multi-level data show the break. High reaction + low learning → redesign method. High learning + low behaviour → fix bosses and job conditions. This diagnostic purpose is why the cycle includes evaluation."""),
("Accountability reason",
"""Organisations fund training for performance, not for entertainment. More than one level is needed to be honest with those who paid in money and lost work time."""),
("Avoiding false positives and false negatives",
"""High reaction can hide zero performance change (false success). Low reaction (strict trainer, hard practice) might still mean high learning (false failure if you only measure smiles). Multiple levels protect employees and HRD from both errors."""),
("Employee development reason",
"""Learning and behaviour data guide further coaching of the same people. Evaluation is feedback to the learner, not only a report to the board."""),
("Strategic HRD reason",
"""Only higher levels show contribution to organisational goals. If HRD wants strategic status, it cannot live on level 1."""),
("Exam wrap",
"""Two reasons as long paragraphs with examples, then accountability, false success/failure, learner feedback, strategy. Conclusion: multi-level evaluation is how HRD tells the truth."""),
],
"conc": """Two main reasons: (1) each Kirkpatrick level answers a different question, so one level cannot define effectiveness; (2) several levels are needed to diagnose where training failed so that HRD can improve. Add accountability and avoiding smile-sheet illusions. Evaluating at more than one level is a professional necessity."""
}

U3B[58] = {
"q": "Mention any two factors that should be considered while selecting a training method.",
"intro": """Selecting a method means choosing OJT, lecture, case, role play, vestibule, simulation, e-learning, outdoor training, and so on — or a blend. Two headline factors for 8 marks: the learning objectives, and the nature of the task. Then list other factors (trainees, cost, location, culture) so the answer is complete.""",
"pts": [
("First factor — learning objectives",
"""What must the person be able to do after training? Knowledge, skill and attitude need different methods. You cannot lecture people into a motor skill. You cannot only give an e-module and expect counselling skill. You cannot only do a game if they must memorise a legal checklist. Objectives, written in observable language from TNA, are the first selector of method."""),
("Example",
"""Objective ‘explain three causes of defects’ can use discussion and quiz. Objective ‘replace a filter in eight minutes without leaks’ needs demonstration, simulation and OJT. Same department, different methods."""),
("Second factor — nature of the job or task",
"""Dangerous or costly tasks need simulation or vestibule before live OJT (safety, aircraft, surgery, high-voltage). Simple routine skills already done well by seniors may use OJT. Customer-facing tasks need practice with feedback (role play). If the workplace currently teaches the wrong method, off-the-job is needed first so that bad habits are not copied."""),
("Trainee characteristics",
"""Education, language, digital literacy, experience, motivation, number of people. Illiterate workers need demonstration, not dense e-text. Thousands of scattered staff favour e-learning for knowledge parts."""),
("Cost, time and production loss",
"""Can the organisation spare people for five days off-site? Is the budget enough for a simulator? Method choice is also resource choice. Cheap methods that fail are not actually cheap."""),
("Geography, facilities and trainer availability",
"""No lab means you cannot choose vestibule. No internal expert may mean a vendor or e-module. Distant plants change the choice toward e-learning plus local OJT coaches."""),
("Transfer requirements and urgency",
"""If the skill must appear tomorrow on the job, OJT with a coach and a job aid may beat a delayed residential course. If the skill is rare, off-the-job practice may be safer."""),
("Organisational culture and climate",
"""Will role play or open discussion be accepted, or seen as loss of face? Culture-blind method choice fails even if theoretically correct. Climate also decides whether any method will transfer."""),
],
"conc": """Two main factors in selecting a training method are (1) the learning objectives (knowledge/skill/attitude) and (2) the nature of the task (danger, complexity, whether the workplace already models the right way). Also consider trainees, cost, location, urgency and culture. Method selection must be systematic, from TNA, not from habit."""
}

U3B[59] = {
"q": "Design a complete training program for a clearly identified employee skill gap, covering TNA, objectives, training method, delivery, and evaluation.",
"intro": """A complete design must name a real skill gap and then walk through all four stages of the training cycle plus transfer. Use a concrete example so the examiner sees a programme, not a theory dump. Example used here: customer-service staff in a service organisation have a skill gap in handling complaints — repeat complaints are high and first-contact resolution is low. You may use another gap (machine setup, safety lock-out, classroom questioning skill) if you prefer, but you must cover TNA, objectives, method, delivery and evaluation.""",
"pts": [
("TNA",
"""Organisation: customer-retention strategy; complaints hurt repeat business. Task: listen without interrupting, log in CRM, offer SOP solution, escalate correctly, close respectfully. Person: who fails — mostly staff with less than one year? Can they recite the SOP (knowledge) but freeze on angry customers (skill/attitude)? Check non-training causes: if the CRM is down or refund policy is unclear, fix that first. Collect baseline: repeat-complaint percentage and customer satisfaction score."""),
("Objectives (observable)",
"""By end of classroom: given a recorded angry complaint, the trainee will listen, log all mandatory fields, and choose the correct SOP action or escalation in a role play scoring at least 80% on a checklist. Within eight weeks on the job: repeat complaints for trained staff fall by an agreed percentage versus baseline. Write both learning and performance objectives."""),
("Training method — blend",
"""E-module on policy and CRM screens (concept). Classroom role play with recorded calls and peer-plus-trainer feedback (skill and attitude). Then two weeks of on-the-job coaching with a checklist (transfer). This blend matches both knowledge and practical skill."""),
("Delivery",
"""Batches of about 12 so that everyone practises, not 60 people watching a lecture. Facilitator skilled in role play. Working CRM training logins. Quiet room. Manager present at the close to commit support. Admin: handouts of SOP, water, time-table that protects practice hours. Each trainee writes an action plan for Monday."""),
("Transfer support (part of a complete design)",
"""Supervisor weekly coaching for a month; a job aid near the phone; appraisal KRA includes resolution quality, not only number of calls. Without this, the design is not complete even if the class was excellent."""),
("Evaluation levels 1 and 2",
"""Reaction form with relevance items. Knowledge test on SOP. Observed role-play score versus checklist (learning of skill)."""),
("Evaluation levels 3 and 4",
"""Call audits at 30 and 60 days (behaviour). Repeat-complaint rate and CSAT versus baseline (results). If possible, compare trained group with a not-yet-trained group. Meet HRD and department head at 60 days to refine SOP or coaching."""),
("Why this counts as complete",
"""All four cycle stages are present, the gap is specified, methods match objectives, delivery is practical, transfer is designed, evaluation uses more than smile sheets. That is what the question asked you to design."""),
],
"conc": """Present one clear skill gap and a full cycle: TNA (including non-training checks and baseline), observable objectives, blended methods, careful delivery, transfer support, and multi-level evaluation. A complete programme is a process, not a one-day event with a banner."""
}

U3B[60] = {
"q": "Evaluate two alternative training programs for the same organisational need using the Kirkpatrick model and recommend the more effective program.",
"intro": """Evaluation using Kirkpatrick means judging each alternative at reaction, learning, behaviour and results, then recommending. Need used here: first-line supervisors must learn to give developmental feedback (this supports HRD climate and appraisal as a development tool). Programme A is glamorous but shallow. Programme B is TNA-based and blended. You may change the need, but you must compare two programmes level by level and give a clear recommendation.""",
"pts": [
("Programme A described",
"""Two-day off-site ‘leadership’ with a famous motivational speaker, luxury venue, little practice of feedback skill, no involvement of the supervisors’ own bosses, no follow-up, no change in appraisal forms. Marketing looks excellent."""),
("Programme B described",
"""Built from TNA: short concept module on what developmental feedback is; extensive role play with checklists; real feedback assignments on the job; the supervisors’ bosses act as coaches; 60-day follow-up workshop; an appraisal item on coaching quality. Venue is ordinary."""),
("Level 1 — Reaction",
"""A will often score higher: travel, celebrity, food. B will score adequately if participants see job relevance, but some may say it was ‘hard work’. If the organisation judged only level 1, it would wrongly buy A."""),
("Level 2 — Learning",
"""B is superior because people practise the actual skill and get feedback. A may give memorable quotes without the ability to hold a feedback conversation. Tests and role-play scores would show this if anyone measured them."""),
("Level 3 — Behaviour",
"""B is far superior: assignments, job aids, and boss support. A rarely transfers; the old habit of only scolding or only silence returns. Climate of the supervisors’ own workplace decides A’s failure."""),
("Level 4 — Results",
"""B is more likely to improve employee development climate, earlier correction of errors, and engagement in the supervisors’ teams. A is costly with little organisational result. Level 4 is why the company should care."""),
("Recommendation",
"""Recommend Programme B even if smile sheets are slightly lower. Effectiveness in HRD is behaviour and results in the service of the organisational need, not applause. State the condition: B still fails at level 3 if top management does not support coaching time — so the recommendation includes that support."""),
("What this evaluation teaches",
"""Kirkpatrick protects the organisation from buying the more popular but less effective programme. Write this meta-point; it shows you can use the model, not only recite it."""),
],
"conc": """Compare A and B at all four Kirkpatrick levels. Recommend the TNA-based blended Programme B because it can reach learning, behaviour and results, while A mainly maximises reaction. Effectiveness is not the same as popularity. Condition: workplace support must accompany B."""
}
