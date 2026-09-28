# -*- coding: utf-8 -*-
U3B = {}

U3B[49] = {
"q": "A department is experiencing repeated performance errors. Apply the concept of TNA to identify what information should be collected before designing training.",
"intro": """Application of TNA: do not jump to a workshop. Collect organisation, task and person information, and test non-training causes. List the information under headings.""",
"pts": [
("Error facts (not opinions)",
"""Type of error, frequency, process step, shift, product, cost. Interview plus records. Without facts, TNA is gossip."""),
("Organisation analysis information",
"""Department goals, quality standards, staffing, whether supervisors support correct methods, recent changes (new machine, new target). Strategy link: is speed being rewarded over accuracy?"""),
("Non-training causes",
"""Machine condition, unclear SOP, missing tools, impossible workload, incentive to rush. Notes: training is not the answer to all problems; cause-and-effect first. If these dominate, design a process fix, not training."""),
("Task analysis information",
"""Correct procedure, critical KSAs, safety points, standard of error-free work, difficult steps where errors cluster."""),
("Person analysis information",
"""Who errs (new joiners vs veterans), previous training, language/literacy, actual vs required skill tests, ‘knows but doesn’t do’ versus ‘doesn’t know’."""),
("Readiness and motivation",
"""Do employees believe errors matter? Are they afraid to report? Will they be punished for slowing down to be correct?"""),
("Transfer climate information",
"""Will the boss allow correct slower practice after training? Peer pressure? Old informal methods?"""),
("Success criteria for later evaluation",
"""What error reduction in 8 weeks would mean success? Collect baseline now. This information is part of TNA, not later."""),
],
"conc": """Information list: error data, organisation context, non-training causes, task KSAs, person gaps, readiness, transfer climate, baseline. Only then design training — if training is the right answer."""
}

U3B[50] = {
"q": "Apply suitable training methods to design a development program for employees who need both practical job skills and conceptual knowledge.",
"intro": """When both ‘hand’ and ‘head’ are needed, one method is not enough. Design a blend: off-the-job or e-learning for concepts; simulation then OJT for skills; evaluation of both.""",
"pts": [
("Start with TNA split",
"""List conceptual objectives (explain why, standards, theory) separately from practical objectives (perform the task to standard). Methods follow this split."""),
("Conceptual methods",
"""Short lectures, discussion, cases, e-modules, diagrams. Example: why a safety lock exists, not only how to click it."""),
("Safe practice methods",
"""Vestibule, simulation, role play, lab. Mistakes do not harm customers or machines. Bridge between concept and live work."""),
("OJT coaching and rotation",
"""Real skill under a trained coach with a checklist. Job rotation if multiple practical contexts exist."""),
("Action learning project",
"""A live problem where they must use concepts to decide and skills to implement. This binds both needs."""),
("E-learning refreshers",
"""Micro-modules for concepts they can repeat after OJT. Supports memory."""),
("Sequence",
"""Concept → simulated practice → OJT → review. Starting with unsupervised OJT may freeze wrong methods."""),
("Evaluation of both",
"""Knowledge tests (level 2 conceptual) and observed job samples (level 3 practical). If you only test memory, practical skill may still be weak."""),
],
"conc": """Present a blended design with sequence and evaluation. Suitable methods are a mix, not a single favourite of the trainer."""
}

U3B[51] = {
"q": "State any two purposes of Training Needs Assessment.",
"intro": """Two main purposes: identify genuine training needs, and avoid training as a wrong solution. Then add design, priority, baseline purposes.""",
"pts": [
("Purpose 1 — Identify genuine KSA gaps",
"""Using organisation, task and person analysis, find what learning is required and by whom."""),
("Purpose 2 — Prevent wrong solutions",
"""Detect system, tool, or motivation problems so the firm does not buy irrelevant training. Notes’ caveat: training is not the answer to all problems."""),
("Set measurable objectives",
"""TNA gives learning and performance objectives for design."""),
("Select the right trainees",
"""Not everyone needs the same programme — fairness and efficiency."""),
("Guide method choice",
"""Skill vs knowledge vs attitude needs different methods."""),
("Prioritise scarce resources",
"""Critical jobs and large gaps first."""),
("Create evaluation baseline",
"""Pre-training performance recorded."""),
("Align with strategy",
"""Organisation analysis keeps HRD relevant to goals."""),
],
"conc": """Two purposes: find real training needs; stop false training. Other purposes fill the 8 marks."""
}

U3B[52] = {
"q": "Name any two levels of the Kirkpatrick model.",
"intro": """Name any two, explain all four briefly for marks, and say why more than two levels matter.""",
"pts": [
("Level 1 — Reaction",
"""Satisfaction and perceived usefulness. Forms at the end of the programme."""),
("Level 2 — Learning",
"""Increase in knowledge, skill or attitude. Tests and demonstrations."""),
("Level 3 — Behaviour",
"""Transfer to the job after a lag. Observation and boss ratings."""),
("Level 4 — Results",
"""Organisational outcomes: quality, cost, safety, customer, etc."""),
("Why name more than two in an 8-mark answer",
"""The question says two; the syllabus expects the model. Write two in detail and the other two in brief."""),
("Measurement examples",
"""Smile sheet; pre–post test; 60-day audit; defect rate vs baseline."""),
("Sequence",
"""Each level supports but does not guarantee the next."""),
("HRD use",
"""Important costly programmes should not stop at reaction."""),
],
"conc": """Any two named in depth + remaining two in brief = full answer. Never leave Kirkpatrick as only two words."""
}

U3B[53] = {
"q": "Analyse why a training program may receive positive participant reactions but still fail to improve job performance.",
"intro": """This is the gap between Kirkpatrick level 1 and levels 3–4. Analyse reasons in the programme, the person, and the workplace.""",
"pts": [
("Entertainment versus learning",
"""Funny trainer, good food, hill-station venue raise reaction. Skill may not have been practised. Level 2 never happened."""),
("Learning without difficulty",
"""Content too easy or too theoretical; people leave happy and incompetent."""),
("Wrong need (TNA missing)",
"""Performance problem was tools, process, or target, not skill. Training cannot improve job performance then, however pleasant."""),
("No transfer climate",
"""Boss says ‘forget the classroom’. Peers mock new methods. Old SOP remains. Behaviour cannot change."""),
("No opportunity to use",
"""Skill unused for months is forgotten. Reaction was real; performance chance never came."""),
("Conflicting appraisal and rewards",
"""Taught quality; paid for speed. People follow pay. Analysis: systems beat training."""),
("No follow-up coaching",
"""One event without IDP, refreshers, or supervisor support. Decay of learning."""),
("Analytical conclusion",
"""Reaction is a weak predictor of job performance. HRD must design for learning, transfer support and results, not applause."""),
],
"conc": """Give workplace and design reasons, not only ‘they were happy’. Close with the level-1 versus level-3 lesson."""
}

U3B[54] = {
"q": "Analyse the consequences of designing a training program without conducting an adequate Training Needs Assessment.",
"intro": """Consequences are operational, financial, human and strategic. Analyse cause (no TNA) to these effects.""",
"pts": [
("Wrong content",
"""Topics miss actual KSA gaps; errors continue. The original problem remains."""),
("Wrong audience",
"""Skilled staff bored; needy staff absent. Reaction may even be negative from the bored group."""),
("Wrong method",
"""Lecture where coaching was needed. Learning and transfer fail."""),
("Training as false solution",
"""System problems remain; management thinks ‘we already trained them’ and stops looking. This is a dangerous consequence."""),
("Demotivation and HRD cynicism",
"""Employees lose faith; future programmes suffer attendance of the mind."""),
("Wasted budget and lost production time",
"""Direct cost plus opportunity cost. In exams, mention both."""),
("Impossible honest evaluation",
"""No baseline or true objectives, so anyone can claim success or failure. The cycle cannot learn."""),
("Strategic drift",
"""Calendar becomes ritual, disconnected from goals. Long-term capability lag."""),
],
"conc": """Consequences cascade from wrong design to wasted money, cynicism and unsolved performance problems. Adequate TNA is professional risk control, not extra paperwork."""
}

U3B[55] = {
"q": "Evaluate the usefulness of the Kirkpatrick model for judging the effectiveness of an organisational training program.",
"intro": """Evaluate usefulness + limitations + how to use it well. Verdict: useful guiding framework, not a perfect scientific proof.""",
"pts": [
("Usefulness — completeness",
"""Forces HRD beyond smile sheets to learning, behaviour and results. Matches notes’ criteria: learning, behaviour, impact on objectives."""),
("Usefulness — communication",
"""Four levels are easy to explain to managers who fund training."""),
("Usefulness — design aid",
"""Encourages measures during TNA. Makes objectives operational."""),
("Usefulness — diagnosis",
"""If reaction high and behaviour low, look at transfer climate, not only the trainer. The model locates the break."""),
("Limitation — causality at level 4",
"""Many factors affect results. Training may be only one. Do not over-claim."""),
("Limitation — cost and time",
"""Behaviour and results need follow-up. Firms may stop at level 1; the model is then unused, not useless."""),
("Limitation — one size",
"""A one-hour awareness talk does not need full level 4. Use proportionately."""),
("Verdict",
"""Highly useful if applied with judgement and transfer thinking; weak if treated as four forms to file. Still the standard HRD evaluation map."""),
],
"conc": """Balanced evaluation, clear usefulness, honest limits, proportionate use. Recommend Kirkpatrick as a guide, not a ritual."""
}

U3B[56] = {
"q": "Analyse how the choice among on-the-job, off-the-job, and e-learning methods can affect training outcomes.",
"intro": """Method choice affects learning quality, transfer, cost, motivation and therefore Kirkpatrick outcomes. Analyse each method’s outcome pattern and the idea of fit.""",
"pts": [
("OJT outcome pattern",
"""Strong transfer and relevance (good level 3 if coaching is skilled). Weak if the coach is busy or teaches wrong methods — then outcomes are bad habits at scale."""),
("Off-the-job outcome pattern",
"""Better conceptual learning and safe practice (level 2). Level 3 suffers if work does not resemble the classroom. High cost may be justified for dangerous or new skills."""),
("E-learning outcome pattern",
"""Consistent knowledge, tracking, scale (good for level 2 information). Weak completion, isolation, or poor design destroy even level 1–2. Interpersonal skills usually need extra live practice."""),
("Fit to objective",
"""Motor skill → OJT/simulation; interpersonal → role play; information update → e-learning. Wrong fit lowers outcomes regardless of budget."""),
("Learner factors",
"""New employees may need structured off-the-job; experienced staff may prefer OJT or micro e-learning. Mismatch reduces motivation and learning."""),
("Blended outcomes",
"""Combining methods often beats any single method: concept + practice + job support."""),
("Climate interaction",
"""Any method fails if workplace punishes new behaviour. Method analysis must include transfer context."""),
("Analytical point",
"""Outcomes are not determined by the label ‘OJT’ or ‘e-learning’ but by fit, quality of execution, and support. Choice is a strategic HRD decision."""),
],
"conc": """Analyse each method’s typical strengths/failures, then fit, blend, and climate. Method choice shapes whether training stays in the head or appears in job performance."""
}

U3B[57] = {
"q": "State any two reasons for evaluating training at more than one Kirkpatrick level.",
"intro": """Two main reasons: different questions, and diagnosis of where the chain broke. Then extra reasons for 8 marks.""",
"pts": [
("Reason 1 — Different levels answer different questions",
"""Liking ≠ learning ≠ doing ≠ business results. One level cannot stand for effectiveness."""),
("Reason 2 — Diagnosis of failure",
"""Multi-level data show whether to fix content, trainer, transfer climate, or job conditions."""),
("Accountability",
"""Organisations fund performance, not entertainment."""),
("Employee development",
"""Learning and behaviour data guide further coaching."""),
("Avoid false positives",
"""High reaction can hide zero performance change."""),
("Avoid false negatives",
"""Low reaction (strict trainer) might still mean high learning — need level 2."""),
("Continuous improvement",
"""Each level suggests different redesign."""),
("Strategic HRD",
"""Only higher levels show contribution to goals."""),
],
"conc": """Two reasons: different questions and diagnosis. Add accountability and avoiding false success. Multi-level evaluation is how HRD tells the truth."""
}

U3B[58] = {
"q": "Mention any two factors that should be considered while selecting a training method.",
"intro": """Two headline factors: learning objectives, and nature of the task. Then list others (trainee, cost, location, culture).""",
"pts": [
("Factor 1 — Learning objectives",
"""Knowledge, skill or attitude demand different methods. You cannot lecture people into a motor skill or only e-read them into counselling skill."""),
("Factor 2 — Nature of the job/task",
"""Dangerous or costly tasks need simulation/off-the-job first. Simple routine skills may use OJT. Customer-facing tasks need practice with feedback."""),
("Trainee characteristics",
"""Education, experience, language, digital literacy, motivation, number of people."""),
("Cost, time, production loss",
"""Budget and whether staff can leave the workplace."""),
("Geography and numbers",
"""Scattered staff → e-learning or travelling trainer."""),
("Trainer and facility availability",
"""Internal expert vs vendor; lab vs classroom."""),
("Transfer requirements",
"""How soon must the skill appear on the job? Urgent skill → OJT with coach."""),
("Organisational culture and climate",
"""Will role play or open discussion be accepted? Culture-blind method choice fails."""),
],
"conc": """Two factors: objectives and task nature. Then trainee, cost, location, transfer, culture. Method selection must be systematic."""
}

U3B[59] = {
"q": "Design a complete training program for a clearly identified employee skill gap, covering TNA, objectives, training method, delivery, and evaluation.",
"intro": """Pick a clear gap so the design is concrete. Example used here: customer-service staff have a skill gap in handling complaints (repeat complaints high, first-contact resolution low). You may use another gap if you prefer, but cover all five required parts.""",
"pts": [
("TNA",
"""Organisation: customer-retention strategy. Task: complaint process, empathy, CRM logging, escalation rules. Person: who fails — new vs old; knowledge vs skill vs attitude. Check IT and policy: if software is down, do not train. Baseline: repeat-complaint % and CSAT."""),
("Objectives",
"""By end of classroom, trainee can listen, log, resolve or escalate per SOP in a role play. Within 8 weeks, repeat complaints fall by an agreed percentage. Write objectives in observable language."""),
("Training method (blend)",
"""E-module on policy (concept); classroom role play with recorded calls (skill); two weeks OJT coaching with checklist (transfer)."""),
("Delivery",
"""Batches of about 12; skilled facilitator; CRM practice lab; manager present at close to commit support. Admin: working logins, quiet room, handouts of SOP. Action plan signed."""),
("Transfer support",
"""Supervisor weekly coaching; appraisal KRA on resolution quality; job aid near the phone."""),
("Evaluation L1–L2",
"""Reaction form; knowledge test; observed role play score vs checklist."""),
("Evaluation L3–L4",
"""Call audits at 30 and 60 days; repeat-complaint and CSAT versus baseline. Compare a trained group with untrained if possible."""),
("Review meeting",
"""HRD and department head at 60 days: refine SOP or coaching if results lag. This makes the design a cycle, not a one-day event."""),
],
"conc": """Show all parts on one example. A complete programme is TNA-based, objective-led, blended, well delivered, transfer-supported, and evaluated at several Kirkpatrick levels."""
}

U3B[60] = {
"q": "Evaluate two alternative training programs for the same organisational need using the Kirkpatrick model and recommend the more effective program.",
"intro": """Need: first-line supervisors must learn to give developmental feedback (HRD climate). Compare Programme A (glamorous but shallow) and Programme B (TNA-based blended). Evaluate each level, then recommend.""",
"pts": [
("Programme A described",
"""Two-day off-site ‘leadership’ with a motivational speaker, little practice, no boss involvement, no follow-up."""),
("Programme B described",
"""TNA-based: concept module, extensive role play, real feedback assignments, boss-as-coach, 60-day follow-up, appraisal item on coaching quality."""),
("Level 1 Reaction",
"""A may score higher (venue, speaker). B adequate if seen as relevant. Reaction would wrongly pick A."""),
("Level 2 Learning",
"""B superior: practice and feedback on the actual skill. A may give quotes, not skill."""),
("Level 3 Behaviour",
"""B superior: assignments and workplace support. A rarely transfers."""),
("Level 4 Results",
"""B more likely to improve climate, error correction, engagement. A is costly with little result."""),
("Recommendation",
"""Choose B even if smile sheets are slightly lower. Effectiveness in HRD is behaviour and results, not applause."""),
("Condition and evaluation honesty",
"""B still fails at level 3 without management support. Recommendation includes that condition. Do not implement A merely because it is popular."""),
],
"conc": """Using Kirkpatrick, recommend the programme that can reach levels 3 and 4. State that level 1 alone would mislead the organisation into buying Programme A."""
}
