# -*- coding: utf-8 -*-
"""Compact exam points — expand each bullet into 5–8 lines in the answer book."""
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor, white, black
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable, Table, TableStyle, KeepTogether
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY
import html as htmllib, os

NAVY = HexColor("#1a365d")
TEAL = HexColor("#0d7377")
GOLD = HexColor("#c9a227")

Q = []  # (n, unit, question, bullets[])

def add(n, u, q, bullets):
    Q.append((n, u, q, bullets))

add(1,1,"Concept of HRD and major objectives", [
"Def: planned continuous process to grow KSA + potential + culture (not one training day).",
"Nadler 1969: organised learning, fixed time, aimed at behavioural change.",
"T.V. Rao: (i) present & future role capabilities (ii) inner potential (iii) teamwork culture.",
"Obj: sharpen present/future job skills.",
"Obj: equity, employability, adaptability.",
"Obj: develop individual, dyad (boss–subordinate), team, whole organisation.",
"Obj: enabling climate (initiative, experiment, renew).",
"Tools: appraisal, training, counselling, OD — check they help, not just paperwork.",
])
add(2,1,"Evolution: training → strategic HRD", [
"Stage 1: welfare/personnel — files, discipline, wages; little development.",
"Stage 2: training cell — short job-skill courses, isolated from strategy.",
"Nadler 1969 names HRD as a field (training + education + development).",
"India 70s–80s: Rao/Pareek — HRD as a SYSTEM (appraisal, potential, career, OD).",
"HRM = maintenance; HRD = development; every manager responsible.",
"Liberalisation/IT/quality → need capability for competition = strategic HRD.",
"Today: competencies, talent pipeline, climate, e-learning, seat at strategy table.",
"Exam line: isolated workshop = old stage; linked to goals = strategic.",
])
add(3,1,"Relationship HRD and HRM", [
"HRM = umbrella (hire, pay, law, welfare, develop, use people).",
"HRD = development part inside HRM (learning, potential, climate).",
"HRM maintenance-oriented; HRD development-oriented.",
"HRM often money-motivation; HRD higher-order needs (growth, recognition).",
"HRM dept’s job vs HRD = ALL managers’ job.",
"They need each other: fair pay (HRM) so people can learn (HRD).",
"Data link: appraisal files → training/succession.",
"Not same word, not unrelated — complementary.",
])
add(4,1,"Importance of HRD for performance", [
"Skill: close gap (standard − actual) → fewer errors, more output.",
"Role clarity + feedback → effort not wasted.",
"Motivation/morale → extra effort, less turnover.",
"Use potential (right person in right future role).",
"Teamwork/dyads → organisation is a system, not 1+1 people.",
"Adapt + innovate in changing environment.",
"Cut waste: accidents, absence, attrition costs.",
"Long-term effectiveness, not fear-driven one-month spike.",
])
add(5,1,"HRD climate + supportive characteristics", [
"Climate = how it FEELS now regarding trust, learning, fairness (not posters).",
"OCTAPAC: Openness, Confrontation, Trust, Autonomy, Proactivity, Authenticity, Collaboration.",
"Openness: ask doubts, 2-way talk.",
"Trust/authenticity: words = actions; no mask.",
"Confrontation: solve problems, don’t hide.",
"Autonomy + initiative; collaboration across depts.",
"Top support: time, money, release for training.",
"Fair access + recognise mentoring. Soil for all HRD tools.",
])
add(6,1,"HRD climate vs organisational culture", [
"Culture = deep values/beliefs/rituals (‘who we are’) — slow to change.",
"HRD climate = current feel of development/trust — can change faster.",
"Culture = broad (power, dress, stories); climate = learning & feedback only.",
"Eg culture: family firm, seniority, owner-as-father.",
"Eg climate in same firm: seniors teach vs hide knowledge.",
"Mismatch: ‘learning culture’ on wall + punitive appraisal = cynicism.",
"HRD must FIT culture and IMPROVE climate.",
"Exam: culture = identity; climate = today’s weather for growth.",
])
add(7,1,"Role of HRD professional", [
"Not a clerk who books a hall.",
"Diagnose needs (TNA, climate, strategy) — say when training is NOT the answer.",
"Design integrated system (appraisal–career–training–counselling).",
"Facilitate learning (trainers, e-learning, mentoring) + train bosses to coach.",
"Climate/culture builder + change agent (merger, IT, quality).",
"Evaluate/audit: did behaviour change?",
"Ethics: confidentiality, fairness.",
"Shift: administrator → business partner.",
])
add(8,1,"Significance for effectiveness + long-term development", [
"Effectiveness = goals + adapt + healthy inside — done BY people.",
"Competence engine for quality/service.",
"Self-renewal even if growth has stopped (environment still changes).",
"Align IDPs to organisational goals — no random courses.",
"Leadership pipeline / succession.",
"Growth beyond present job → retention.",
"Humanistic + economic (people as assets with unlimited potential).",
"Cut HRD → short profit, long decline.",
])
add(9,1,"Growing firm: skill gaps + falling performance (apply HRD)", [
"Diagnose first: skill vs machine vs overload vs unclear goals.",
"Fix climate (fear hides gaps).",
"Developmental appraisal + counselling, not only punishment.",
"Targeted mix: OJT + short courses from TNA (no generic ‘motivation’ camp).",
"Train newly promoted bosses to coach (hidden cause).",
"Career/potential for NEW roles created by growth.",
"Urgent quality/safety gaps first, then yearly HRD cycle.",
"Evaluate errors/productivity; repeat diagnosis.",
])
add(10,1,"Measures for learning-oriented environment (apply climate)", [
"Leaders model learning and admit mistakes.",
"Psychological safety: report errors without humiliation.",
"Frequent coaching feedback, not only annual rating.",
"Time + budget + permission to practise on the job.",
"Team forums: after-action review, quality circles, mentors.",
"Fair access (not only favourites).",
"Reward knowledge-sharing, not only individual heroes.",
"Align appraisal/promotion with learning & teamwork.",
])
add(11,1,"Any two objectives of HRD (expand to 8 marks)", [
"Obj 1: acquire/sharpen capabilities for PRESENT and FUTURE roles + example.",
"How: induction, training, coaching, rotation, appraisal gaps.",
"Obj 2: develop general capabilities + inner potential (whole person).",
"How: potential appraisal, career, mentoring, education.",
"Also culture of teamwork (Rao’s 3rd pillar) — write 8 lines.",
"Also equity, employability, adaptability.",
"Also 7 system goals: individual, role, future, dyad, team, collaboration, self-renewal.",
"Don’t stop at 2 sentences — explain + example each.",
])
add(12,1,"Any two ways HRD & HRM are related", [
"Relation 1: HRD is the development CORE inside HRM umbrella.",
"Eg: hire (HRM) then induct/train/career (HRD).",
"Relation 2: complementary — maintenance vs growth need each other.",
"Shared data (appraisal → training), shared line managers, shared strategy.",
"Then 5-line DIFFERENCE so you don’t mix terms.",
"HRM money vs HRD growth-needs; HR dept vs all managers.",
"Strategic HRM is delivered THROUGH HRD.",
"Not identical, not unrelated.",
])
add(13,1,"Weak HRD climate → behaviour & performance (analyse)", [
"Chain: weak climate → behaviour → results.",
"Fear → hide mistakes → late crises/accidents.",
"No initiative → wait for orders → slow in market.",
"Training won’t transfer (‘forget classroom’).",
"Political appraisal → fake data, no improvement.",
"Silos/blame → customer delay.",
"Demotivation, absence, exit of good people.",
"Unused potential → growth plans fail. Climate = performance issue.",
])
add(14,1,"Changing role of HRD professional (analyse)", [
"From record-keeper → diagnostician.",
"From hall-organiser → learning architect (blend methods).",
"From isolated training cell → integrator of subsystems.",
"From edge → strategy table (business literacy).",
"Change agent (merger, digital, quality).",
"Developer of LINE managers as coaches.",
"From counting programmes → evaluation + ethics.",
"Why: competition + human capital. Title change ≠ role change.",
])
add(15,1,"Philosophy, climate, performance (relationship)", [
"Philosophy = leaders’ belief: people have potential, development is duty.",
"Philosophy → practices (time, coaching, fair appraisal).",
"Practices → climate (what employees FEEL).",
"Climate → behaviour (initiative vs fear).",
"Behaviour → performance (quality, service, innovation).",
"Reverse: good results strengthen philosophy; panic cuts HRD → downward spiral.",
"Worst: posters ‘people first’ + cruel bosses = cynicism.",
"Manage as ONE chain, not 3 slogans.",
])
add(16,1,"Evaluate: HRD strategic vs only training", [
"Training = short job-skill learning — necessary TOOL.",
"Training-only = calendar, smile sheets, cancelled when busy.",
"For strategic: capability, pipeline, culture execute strategy.",
"Training-only fails transfer if appraisal/career ignore it.",
"Limit: small firm may need only basic training; ‘strategic’ without data = fashion.",
"Verdict: YES strategic function; training nested inside it.",
"Implies: seat in strategy, line KRAs, evaluate behaviour/results.",
"Don’t insult trainers; don’t equate calendar with HRD.",
])
add(17,1,"Any two indicators of supportive HRD climate", [
"Ind 1: openness + free useful 2-way feedback (juniors speak; mistakes discussed to learn).",
"How see: survey item, meetings, not waiting 1 year for news.",
"Ind 2: visible management support (time, budget, release for training, leaders learn too).",
"How see: actual training days, IDPs done, distant branches included.",
"Also: trust, autonomy, collaboration, fairness, recognition of mentors.",
"Teamwork without blame-notes.",
"Indicators = observable signs, not slogans.",
"Name 2 in depth + 3 extra = 8 marks.",
])
add(18,1,"Two reasons HRD pro must understand culture", [
"Reason 1: FIT of tools — 360°/open feedback may fail in hierarchical culture (fake data).",
"Eg: start with private coaching, then widen.",
"Reason 2: pace change — read climate scores against culture; don’t shock overnight.",
"Also: who must sponsor (owner/union/CEO) for legitimacy.",
"Subcultures (plant vs IT vs region) — one design won’t fit all.",
"Strategy needs a culture (innovation vs cost) → HRD agenda.",
"Ethics: don’t crush people’s meaning of work.",
"Culture-blind HRD = neat and rejected.",
])
add(19,1,"Evaluate: HRD without culture/climate", [
"Fake data / silent classrooms.",
"Ritual forms, no behaviour change.",
"Cynicism — worse trust than doing nothing.",
"Wasted money; no transfer (levels 3–4 fail).",
"Value clash → employee stress.",
"Opportunities captured by in-groups (inequity).",
"Only ‘positive’: glossy optics for visitors — reject as true benefit.",
"Verdict: diagnose → adapt → implement → evaluate. Blind copy = unprofessional.",
])
add(20,1,"Design basic HRD framework (capability + goals)", [
"1 Policy: every manager develops people; HRD facilitates; equity.",
"2 Translate goals → role competencies (alignment hinge).",
"3 Subsystems linked: appraisal, potential, training, career, feedback, counselling.",
"4 Climate (OCTAPAC, time to practise).",
"5 TNA (org/task/person; non-training causes).",
"6 Mix: OJT, courses, mentoring; IDPs; succession.",
"7 Governance: business heads review capability vs strategy 2×/year.",
"8 Evaluate + HRD audit; redesign. Closed loop, not random courses.",
])
add(21,2,"Structure of HRD system + components", [
"System = parts working for one purpose; HRD is PROCESS not bag of forms.",
"Base: philosophy + 7 goals (individual→self-renewal).",
"Components: performance appraisal, potential, training, career.",
"Feedback + counselling (the human conversation).",
"OD / climate (teams & culture).",
"Supports: line managers, HRD cell, records, HRM links (pay/promotion).",
"Structure = LINKAGE: cycle of data from one to next.",
"Review: do mechanisms help or hinder development?",
])
add(22,2,"Performance appraisal as HRD subsystem + importance", [
"HRD appraisal = goals → review → 2-way feedback → IDP (not secret increment mark).",
"Importance: role clarity.",
"Diagnose strengths/gaps → raw material for HRD.",
"Institutionalises feedback.",
"IDP = heart (else only judgement).",
"Feeds training, career, potential, counselling.",
"Motivates + develops boss–subordinate dyad.",
"Fails if forced ranking, no talk, no follow-up — then it HARMS development.",
])
add(23,2,"Training as HRD subsystem + contribution", [
"Def: planned effort to learn job KSAs (Noe). Need ≈ standard − actual IF cause is skill.",
"Place: receives TNA/appraisal; must transfer back to job.",
"Contributes knowledge + skill + attitude (not lecture-only).",
"Present-job effectiveness + future roles/change.",
"Morale, employability, lower turnover (notes’ benefits).",
"Induction = socialisation into culture.",
"Limit: cannot fix machines/cruel bosses; not whole HRD.",
"Maximise: TNA, right method, boss support, evaluate.",
])
add(24,2,"Career planning + potential appraisal", [
"Potential = can they handle BIGGER/different job? Separate from this year’s rating.",
"Avoid Peter Principle (promote till they fail).",
"Career planning = choose goals + path; blueprint; continuous (env changes).",
"Individual’s job + org must counsel & offer chances; integrate goals.",
"Process: aspirations → opportunities → match/mismatch → strategies → review.",
"Link: potential makes paths real; career turns labels into rotation/training.",
"Benefits: succession, retain talent, morale.",
"Caution: secret lists, bias, only one ladder (allow specialist path).",
])
add(25,2,"Role of feedback and counselling", [
"Feedback = specific, timely, behaviour-based info (not ‘you are poor’).",
"Two-way: employee also reports obstacles.",
"Counselling = helping talk on emotional/work problem so PERSON decides (notes).",
"Functions: advise, reassure, communicate, release tension, clarify, reorient.",
"Aims: self-understanding, achievable goals, coping, positive self-regard.",
"Links appraisal/training/career to a living person.",
"Who: manager (trained) or specialist; confidentiality; refer serious cases.",
"Process: describe behaviour → listen → agree solution → commit → follow up.",
])
add(26,2,"Principles for designing effective HRD practices", [
"Top commitment + lived philosophy.",
"Line-manager ownership (every boss a developer).",
"Integrate subsystems (no showcase course in a silo).",
"Align with strategy (right capabilities).",
"Need-based diagnosis (no off-the-shelf).",
"Fit culture; build climate slowly.",
"Participation, fairness, transparency (equity).",
"Continuity + evaluation (help or hinder the process?).",
])
add(27,2,"How HRD subsystems are interrelated", [
"Appraisal → counselling agenda + training need.",
"Training → next appraisal checks transfer.",
"Potential → career path (leader vs specialist).",
"Career plan → which course + which rotation.",
"Feedback = blood of the system (every stage needs talk).",
"Climate/OD = soil; fear = fake data everywhere.",
"HRM consistency: if bonus kills teamwork, training of teamwork dies.",
"One competency file so the year doesn’t start from zero.",
])
add(28,2,"Need to integrate HRD with strategy", [
"People execute strategy (digital/quality/expansion fail without skill).",
"Filter waste: don’t train fashion topics.",
"Talent TIMING: 20 team leaders in 2 years must start NOW.",
"Climate type must match strategy (cost vs innovation).",
"Change support (counselling, reskill) or circulars stay on paper.",
"HRD credibility/budget depends on business link.",
"Employees learn better when they know WHY.",
"Practice: competency maps, IDPs in business reviews, drop obsolete courses.",
])
add(29,2,"Appraisal exists but doesn’t help development — improve", [
"State purpose = development (not only increment).",
"Joint goals at START of year.",
"Train bosses: incidents, not labels; listen.",
"Protect counselling time; no corridor signatures.",
"End with IDP + quarterly follow-up.",
"Link gaps to TNA/career/potential.",
"Climate: no public humiliation; some process appeal.",
"Survey ‘did this help you grow?’ — judge managers on talk quality, not form date.",
])
add(30,2,"Development path for high leadership potential", [
"Validate potential (multi-rater / assessment centre); tell the person honestly.",
"Career map 3–5 yrs + their aspirations; more than one fork.",
"Keep current job performance strong + leadership behaviours on appraisal.",
"STRETCH: rotation, project lead, deputy — main developer.",
"Training: business concepts + people skills, timed with stretch.",
"Mentor + counselling (pressure, arrogance derailers).",
"Rich feedback (360 if climate allows).",
"Yearly review; if wrong label, specialist path is also honourable.",
])
add(31,2,"Any two HRD subsystems", [
"1 Performance appraisal — developmental review + IDP + example.",
"Why ‘sub’: diagnoses, doesn’t itself create skill.",
"2 Training — planned KSA learning; TNA-based + example.",
"Why ‘sub’: not whole HRD; needs climate/career.",
"Also name: potential, career, counselling, OD.",
"One link sentence: gap → counsel → train → career → re-appraise.",
"Don’t write two words only.",
"Intro + 2 long paras + others = 8 marks.",
])
add(32,2,"Any two purposes of feedback", [
"P1: improve CURRENT performance (same-day, specific) + example.",
"Tone: respect so person stays open.",
"P2: long-term development (reinforce strengths; guide training/career).",
"Also motivation (recognition).",
"Also role clarity (dyad).",
"Also climate (openness/trust signal).",
"Also upward feedback + training evaluation.",
"Not scolding, not vague praise.",
])
add(33,2,"Poor coordination among subsystems (analyse)", [
"Rated weak every year, never trained → gap stays, trust dies.",
"Courses with no chance to use / no career → picnic.",
"High potential ignored in promotion → talent exits; HRD looks fake.",
"No counselling after rating → form without growth.",
"Conflict: train teamwork, bonus only individual → people follow pay.",
"Duplication + some roles get nothing; no memory file.",
"Chaos → worse climate → even less transfer.",
"Vicious cycle: no impact → budget cut → worse HRD.",
])
add(34,2,"Align HRD with strategy in RAPID change", [
"Every strategy shift → update competency list FAST.",
"Short TNA/climate pulses, not 3-year studies.",
"Flexible methods: JIT, OJT, e-learning, short workshops.",
"OD/counselling for mergers/new teams (not only skill).",
"Career: projects & lateral moves, review often.",
"HRD in the business meeting every quarter.",
"STOP obsolete courses/KRAs (alignment = subtraction too).",
"Measure speed of capability, not number of programmes.",
])
add(35,2,"Evaluate potential + performance appraisal together", [
"Different questions: how well NOW vs how far FUTURE.",
"Avoids wrong promotion of star specialist to bad manager.",
"4 boxes: high/high leader track; high perf/low pot specialist; etc.",
"Fairer if transparent.",
"Risks: secret lists, bias, 5-minute dual rating, no action.",
"Conditions: separate tools, trained assessors, feedback, follow-up moves.",
"Either alone is incomplete.",
"Verdict: together YES if quality; paperwork combo NO.",
])
add(36,2,"HRD designed without strategy (analyse ineffectiveness)", [
"Develop yesterday’s skills; strategy needs new ones.",
"Budget on popular courses; critical roles stay weak.",
"Career promises that don’t match future structure → anger.",
"Appraisal chases old KRAs → reinforces wrong behaviour.",
"Bosses cut HRD (no visible return).",
"Good people leave.",
"Strategy itself fails (quality/digital/expansion).",
"Activity metrics hide failure until crisis.",
])
add(37,2,"Two benefits: career planning + potential integrated", [
"B1: REALISTIC paths — less false hope/betrayal; honest counselling.",
"B2: USE talent in time — stretch, succession, money on the right people.",
"Eg: two equal engineers → leader vs designer paths; both stay.",
"Also fewer wrong promotions.",
"Also retain & motivate.",
"Also better counselling (evidence not ‘work hard and rise’).",
"Match/mismatch step in career process NEEDS potential data.",
"Labels without moves = bitterness.",
])
add(38,2,"Two features of effective HRD practice", [
"F1: developmental PURPOSE in reality (IDP/coaching happens after).",
"Test: did work behaviour change? Help or hinder process?",
"F2: INTEGRATION with other subsystems + strategy.",
"Eg: quality course → next appraisal item + boss coaches.",
"Also: need-based, line-owned, fair, funded, climate-safe, evaluated.",
"Fair access (not only favourites).",
"Features = what you OBSERVE, not brochure.",
"Two long + cluster = 8 marks.",
])
add(39,2,"Design integrated system (6 elements connected)", [
"One policy: line owns, HRD facilitates, committee 2×/year.",
"One competency language + one employee file (spine).",
"Cycle: goals → ongoing feedback → appraisal → counselling/IDP → potential → career → training/OJT → evaluate.",
"Quarterly check-ins; trained listeners; confidentiality.",
"IDPs roll into calendar; TNA still validates group courses; boss transfer brief.",
"Talent council: potential → rotation; specialist path exists; talk TO employee.",
"Climate so data isn’t fake.",
"Yearly audit of LINKS (did IDP happen? did high-pots get stretch?).",
])
add(40,2,"Evaluate strong training content, weak strategy/appraisal/career links", [
"Keep: good teaching may give high L1–L2.",
"Cost: may teach WRONG capability vs strategy.",
"No appraisal hook → no transfer (L3 dies).",
"No career credit → only self-driven apply.",
"Likely L1 high, L3/L4 poor; smile sheets mislead.",
"‘Holiday training’ cynicism.",
"May help a few individuals — not enough as org HRD.",
"Verdict: DON’T accept as-is. Remap to TNA/strategy, pre-post goals, career map, then re-evaluate.",
])
add(41,3,"TNA concept + importance", [
"Stage 1 of cycle: TNA → design → delivery → evaluate.",
"Need ≈ standard − actual ONLY if cause is KSA (not broken machine).",
"Org analysis: goals, where it hurts, will climate support?",
"Task analysis: important tasks + KSAs (content skeleton).",
"Person analysis: WHO has the gap; ‘knows but doesn’t do’ ≠ training.",
"Importance: stop off-the-shelf waste; honest diagnosis.",
"Importance: design quality, fairness, priority.",
"Importance: baseline for Kirkpatrick. Skip TNA = other 3 stages guess.",
])
add(42,3,"Steps in designing a training programme", [
"Confirm TNA, trainees, readiness (is training still the answer?).",
"Write goal + observable objectives (‘able to do X in Y minutes’).",
"Content + sequence (concept → demo → practice).",
"Methods: OJT / off-job / e-learning; internal vs vendor; site.",
"Facilities, trainer, materials, budget (notes’ matrix).",
"Design TRANSFER: boss brief, action plan, job aid.",
"Build evaluation now (tests, 30–60 day behaviour, results vs baseline).",
"Check feasibility + equity (can people attend? women/branches included?).",
])
add(43,3,"On-the-job vs off-the-job methods + examples", [
"OJT = learn while doing real work with a guide.",
"OJT eg: coaching, rotation, apprentice, understudy, JIT, live project.",
"OJT + : relevant, cheaper, transfer easy. − : bad coach, bad habits, danger.",
"Off-job = away from workstation (class/vestibule/institute).",
"Off-job eg: lecture, case, role play, games, simulation, vestibule, courses.",
"Off-job + : focus, expert, safe, concepts. − : cost, transfer gap, irrelevance.",
"Choose from objective/safety, not ‘which is best forever’.",
"HRD blend: concept off-job → skill OJT.",
])
add(44,3,"E-learning + advantages", [
"Def: LMS/modules/webinar/mobile; self-paced or live; often blended. PDF dump ≠ e-learning.",
"Adv: anytime/anywhere (shifts, many cities).",
"Adv: scale + same message fast (compliance/product update).",
"Adv: low extra cost after design; easy repeats.",
"Adv: standard quality + tracking scores.",
"Adv: replay, micro-learning, some personalisation.",
"Adv: blend with wiki/webinar/social learning (21st-c notes).",
"Limits: net/device, dropouts, weak for counselling skill, still need boss for transfer.",
])
add(45,3,"Kirkpatrick model", [
"L1 Reaction: like it? smile sheet. Useful but weak alone.",
"L2 Learning: KSA up? test/demo/pre-post.",
"L3 Behaviour: use on job after weeks? observe/boss/audit. Climate decides.",
"L4 Results: quality, errors, safety, CSAT, cost — corporate objectives.",
"Ladder: each can fail after the previous succeeded.",
"Plan measures at TNA; take baseline.",
"Use: diagnose (high L1 low L3 → transfer not trainer).",
"Limit: L4 many causes; costly; use deeper for high-risk training.",
])
add(46,3,"Importance of effective DELIVERY after design", [
"Notes: implementation = admin arrangements + carrying out training.",
"Learning happens in the room, not in the file.",
"Admin (hall, login, batch size) = respect + attention.",
"Trainer skill (adult learning, not slide-reading).",
"Adapt pace; psychological safety to practise/fail.",
"Start transfer IN class: real cases, action plan, boss at close.",
"Open/close = why it matters Monday.",
"Collect tests/reaction here or evaluation dies.",
])
add(47,3,"Relationship TNA–design–delivery–evaluation", [
"Cycle: TNA → design → delivery → evaluation → back to TNA.",
"TNA feeds objectives/content/method.",
"Design is the script delivery performs.",
"Delivery produces the evidence evaluation measures.",
"Evaluation improves next TNA and redesigns method/admin/climate.",
"Skip TNA → excellent class on WRONG need.",
"Skip evaluation → open loop, no professional HRD.",
"Budget all four, not only the visible class day.",
])
add(48,3,"Importance of evaluating training (employee + org)", [
"Employee: know what they mastered (feedback).",
"Employee: career/employability proof.",
"Employee: voice to improve next programme.",
"Org: accountability for money + lost production.",
"Org: find the break (need/design/delivery/transfer).",
"Org: prove strategy/capability (L4).",
"Avoid illusions: happy≠able; strict≠failed.",
"HRD credibility → future resources for people.",
])
add(49,3,"Repeated errors: what info to collect (apply TNA)", [
"Error facts: type, frequency, step, shift, cost (records+observe).",
"Org: goals, new machine/target, speed vs quality rewards.",
"NON-training causes first: machine, SOP, staff shortage, incentives.",
"Task: correct procedure, critical KSAs, where errors sit.",
"Person: who, new vs old, knows-but-doesn’t-do vs doesn’t-know.",
"Readiness/fear of reporting.",
"Will boss allow slower correct method after class?",
"Baseline error rate now = later evaluation. Train ONLY if KSA gap.",
])
add(50,3,"Methods for BOTH practical skill + conceptual knowledge", [
"Split objectives: explain WHY vs DO the task.",
"Concepts: short lecture, diagram, case, e-module, quiz.",
"Safe practice: simulation, vestibule, role play, dummy.",
"Then OJT + trained coach + checklist.",
"Action-learning live project binds head+hand.",
"Micro e-learning to replay concepts later.",
"Sequence: concept → demo → simulate → OJT → review. Don’t start unsupervised OJT.",
"Evaluate BOTH: knowledge test + observed job sample.",
])
add(51,3,"Any two purposes of TNA", [
"P1: find genuine KSA gaps (who/what) + example.",
"P2: stop false training when cause is system/tool/pay (notes’ caveat).",
"Also set measurable objectives for design.",
"Also pick right trainees & methods.",
"Also prioritise scarce money.",
"Also baseline for evaluation.",
"Also link to strategy (org analysis).",
"Two long paras + cluster.",
])
add(52,3,"Name any two Kirkpatrick levels", [
"Name L1 Reaction + how measured + limit.",
"Name L2 Learning + test/demo.",
"Briefly L3 Behaviour (job after lag).",
"Briefly L4 Results (org outcomes).",
"Example measures each.",
"Ladder: one doesn’t prove the next.",
"Costly/safety programmes need more than L1.",
"Two named in depth + rest brief = 8 marks.",
])
add(53,3,"Why high reaction but no job-performance gain", [
"Entertainment ≠ learning (celebrity/hill station).",
"Too easy / only theory — happy and still incompetent.",
"Wrong need (TNA missing) — training can’t fix machine/pay.",
"Boss: ‘forget class’; peers mock new method.",
"No chance to use skill for months → forgotten.",
"Rewards contradict (taught quality, paid speed).",
"No follow-up/coaching/IDP — one picnic.",
"L1 weak predictor of L3/L4. Design for transfer not applause.",
])
add(54,3,"Consequences of design without TNA", [
"Wrong content → original errors continue.",
"Wrong audience (bored experts, missing needy).",
"Wrong method (lecture where OJT needed).",
"False solution: mgmt stops looking, blames workers next time.",
"Cynicism; next HRD ignored.",
"Money + lost production wasted.",
"No baseline → evaluation is theatre.",
"Calendar ritual → strategic capability lag till crisis.",
])
add(55,3,"Evaluate usefulness of Kirkpatrick", [
"Useful: complete vs smile sheets; matches notes (learning/behaviour/impact).",
"Useful: language with managers; plan measures at design.",
"Useful: diagnose which link broke.",
"Limit: L4 many causes — don’t over-claim profit.",
"Limit: costly follow-up; firms stop at L1 (model unused).",
"Limit: not every 1-hour talk needs full L4 — proportionate.",
"Use well: baseline, transfer design, modest L4.",
"Verdict: best simple GUIDE, not a magic proof. Keep it.",
])
add(56,3,"How method choice (OJT / off-job / e-learn) affects outcomes", [
"OJT: good transfer if coach skilled; bad coach = mass wrong habits; danger.",
"Off-job: better concepts/safe practice; transfer dies if work unlike class.",
"E-learn: scale, tracking, knowledge; dropouts; weak people-skills alone.",
"FIT to objective beats fashion (motor vs info vs interpersonal).",
"Learner/context: new vs old; many cities → e-learn.",
"BLEND often best (covers each weakness).",
"Climate can kill ALL methods at L3.",
"Outcomes = fit + execution + transfer, not the method’s brand name.",
])
add(57,3,"Two reasons to evaluate at MORE than one level", [
"R1: each level = different question (like ≠ learn ≠ do ≠ results).",
"Eg fire course popular but can’t use extinguisher.",
"R2: diagnosis — know whether to fix content, trainer, or workplace.",
"Also accountability for money/time.",
"Avoid false success (high smiles) and false failure (strict but learned).",
"Gives learner further coaching data.",
"Strategic HRD cannot live on L1.",
"Two long + extras.",
])
add(58,3,"Two factors in selecting a training method", [
"F1: learning objectives (K / S / A need different methods) + example.",
"F2: nature of task (danger → simulate first; workplace teaches wrong → off-job first).",
"Also trainees (language, literacy, numbers).",
"Also cost/time/production loss.",
"Also location/facilities/trainer available.",
"Also urgency of transfer.",
"Also culture (will role-play be accepted?).",
"Systematic from TNA, not habit.",
])
add(59,3,"Design complete programme (one skill gap, full cycle)", [
"Pick gap e.g. complaint-handling (high repeat complaints).",
"TNA: org/task/person + non-training checks + baseline CSAT/repeat %.",
"Objectives: role-play 80% checklist; 8-week job metric drop.",
"Method blend: e-policy + class role play + 2-week OJT coach.",
"Delivery: batch ~12, working CRM, manager at close, action plan.",
"Transfer: weekly coach, job aid, appraisal KRA on quality.",
"Eval L1–2: form, test, observed role play.",
"Eval L3–4: 30/60-day audits vs baseline; 60-day review meeting.",
])
add(60,3,"Evaluate two programmes with Kirkpatrick + recommend", [
"Need eg: supervisors must give developmental feedback.",
"A: 2-day off-site celebrity ‘leadership’, no practice/follow-up.",
"B: TNA, role play, job assignments, boss-as-coach, 60-day follow-up, appraisal item.",
"L1: A often wins (venue). Don’t decide on L1.",
"L2: B wins (practised skill).",
"L3: B wins (workplace support); A rarely transfers.",
"L4: B likelier climate/error/engagement gain; A costly flop.",
"Recommend B + condition: top support for coaching time. Popularity ≠ effectiveness.",
])

assert len(Q) == 60

def hf(c, d):
    c.saveState()
    w, h = A4
    c.setFillColor(NAVY)
    c.rect(0, h-16, w, 16, fill=1, stroke=0)
    c.setFillColor(white)
    c.setFont("Times-Bold", 8)
    c.drawString(16*mm, h-11, "HRD (OE)  |  EXAM POINTS ONLY  |  Expand each bullet 5–8 lines")
    c.setFillColor(NAVY)
    c.rect(0, 0, w, 14, fill=1, stroke=0)
    c.setFillColor(white)
    c.setFont("Times-Roman", 8)
    c.drawString(16*mm, 5, "Yap from these points. Scholars: Nadler 1969, T.V. Rao. Cycle: TNA-design-delivery-eval. Kirkpatrick 1-4.")
    c.drawRightString(w-16*mm, 5, f"p.{d.page}")
    c.restoreState()

styles = getSampleStyleSheet()
styles.add(ParagraphStyle("T", fontName="Times-Bold", fontSize=16, leading=20, alignment=TA_CENTER, textColor=NAVY, spaceAfter=6))
styles.add(ParagraphStyle("S", fontName="Times-Italic", fontSize=10, leading=13, alignment=TA_CENTER, textColor=TEAL, spaceAfter=8))
styles.add(ParagraphStyle("QH", fontName="Times-Bold", fontSize=10.5, leading=13.5, textColor=NAVY, spaceBefore=6, spaceAfter=2))
styles.add(ParagraphStyle("B", fontName="Times-Roman", fontSize=9.5, leading=12.5, leftIndent=10, spaceAfter=1))
styles.add(ParagraphStyle("U", fontName="Times-Bold", fontSize=11, leading=14, textColor=white, alignment=TA_CENTER))
styles.add(ParagraphStyle("N", fontName="Times-Roman", fontSize=9.5, leading=13, alignment=TA_JUSTIFY, spaceAfter=6))

def banner(t):
    tb = Table([[Paragraph(t, styles["U"])]], colWidths=[178*mm])
    tb.setStyle(TableStyle([("BACKGROUND",(0,0),(-1,-1),TEAL),("TOPPADDING",(0,0),(-1,-1),5),("BOTTOMPADDING",(0,0),(-1,-1),5)]))
    return tb

def esc(s):
    return s.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;")

def build_pdf():
    out = "/home/user/HRD/HRD_Exam_Points_Only.pdf"
    doc = SimpleDocTemplate(out, pagesize=A4, leftMargin=14*mm, rightMargin=14*mm, topMargin=20*mm, bottomMargin=16*mm)
    story = []
    story.append(Paragraph("HRD (OE) — EXAM POINTS ONLY", styles["T"]))
    story.append(Paragraph("60 questions · 8 marks · memorise bullets, elaborate in the hall", styles["S"]))
    story.append(Paragraph(
        "How to yap: 4-line intro (definition + 1 scholar) → 6–8 numbered points (each 5–8 handwritten lines + tiny example) → 3-line conclusion. "
        "Must-quote: Nadler 1969; T.V. Rao 3-fold process; OCTAPAC; need = standard − actual (only if KSA); 4-stage cycle; Kirkpatrick L1–L4.",
        styles["N"]))
    cur = None
    titles = {1:"UNIT 1  Q1–20", 2:"UNIT 2  Q21–40", 3:"UNIT 3  Q41–60"}
    for n,u,q,bts in Q:
        if u != cur:
            cur = u
            story.append(Spacer(1,6))
            story.append(banner(titles[u]))
            story.append(Spacer(1,6))
        block = [Paragraph(f"Q{n}. {esc(q)}", styles["QH"])]
        for i,b in enumerate(bts,1):
            block.append(Paragraph(f"<b>{i}.</b> {esc(b)}", styles["B"]))
        story.append(KeepTogether(block))
    doc.build(story, onFirstPage=hf, onLaterPages=hf)
    print("pdf", out)

def build_html():
    parts = ["""<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"/><meta name="viewport" content="width=device-width,initial-scale=1"/>
<title>HRD Exam Points Only</title>
<style>
body{font-family:Georgia,serif;background:#efe8d8;margin:0;color:#1a202c}
header{background:#1a365d;color:#fff;padding:16px;text-align:center;position:sticky;top:0}
h1{margin:0;font-size:1.3rem} p.sub{margin:6px 0 0;opacity:.9;font-size:.9rem}
nav{margin-top:8px} nav a{color:#fff;margin:0 6px;font-size:.85rem}
main{max-width:820px;margin:16px auto 50px;padding:0 12px}
.note{background:#fff;border-left:4px solid #c9a227;padding:10px 12px;margin-bottom:14px}
.ub{background:#0d7377;color:#fff;text-align:center;padding:8px;border-radius:6px;margin:18px 0 8px;font-weight:700}
.q{background:#fffdf6;border:1px solid #e4d8bc;border-radius:8px;padding:10px 14px;margin:8px 0}
.q h2{margin:0 0 6px;font-size:1rem;color:#1a365d}
.q ol{margin:0;padding-left:20px} .q li{margin:2px 0;line-height:1.4}
</style></head><body>
<header><h1>HRD (OE) — Exam points only</h1>
<p class="sub">Memorise these. In the hall: intro → expand each point 5–8 lines → conclusion.</p>
<nav><a href="#u1">Unit 1</a> <a href="#u2">Unit 2</a> <a href="#u3">Unit 3</a></nav></header><main>
<div class="note"><b>Yap kit:</b> Nadler 1969 · T.V. Rao (present/future role + potential + culture) · OCTAPAC ·
need = standard − actual (only if skill gap) · cycle TNA→design→delivery→eval · Kirkpatrick 1 reaction 2 learning 3 behaviour 4 results.</div>
"""]
    cur=None
    ids={1:"u1",2:"u2",3:"u3"}
    titles={1:"UNIT 1 — Q1–20",2:"UNIT 2 — Q21–40",3:"UNIT 3 — Q41–60"}
    for n,u,q,bts in Q:
        if u!=cur:
            cur=u
            parts.append(f'<div class="ub" id="{ids[u]}">{titles[u]}</div>')
        lis="".join(f"<li>{htmllib.escape(b)}</li>" for b in bts)
        parts.append(f'<article class="q"><h2>Q{n}. {htmllib.escape(q)}</h2><ol>{lis}</ol></article>')
    parts.append("</main></body></html>")
    open("/home/user/HRD/HRD_Exam_Points_Only.html","w",encoding="utf-8").write("".join(parts))
    print("html ok")

if __name__ == "__main__":
    build_pdf()
    build_html()
