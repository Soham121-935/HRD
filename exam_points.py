# -*- coding: utf-8 -*-
"""Exam points with a short concept line so you understand, then bullets to expand."""
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor, white
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, KeepTogether
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY
import html as htmllib

NAVY = HexColor("#1a365d")
TEAL = HexColor("#0d7377")
Q = []

def add(n, u, title, idea, pts):
    Q.append((n, u, title, idea, pts))

add(1,1,"Concept of HRD and major objectives",
"HRD means the organisation helps employees grow in knowledge, skill, attitude and potential, and builds a culture of teamwork. It is a continuous planned process, not a one-day training camp. Machines have a fixed limit; people can keep growing if the climate allows it.",
["Leonard Nadler (1969): HRD = organised learning experiences, for a set time, designed to change behaviour at work.",
"T.V. Rao: help employees in a planned way to (i) do present and future roles (ii) discover inner potential (iii) build collaboration and pride.",
"Objective 1 — sharpen capabilities for today’s job and tomorrow’s job (new machine, new market, promotion).",
"Objective 2 — develop the whole person (communication, judgement, leadership), not only one task.",
"Objective 3 — equity (fair chance), employability (stay valuable), adaptability (handle change).",
"Objective 4 — develop many levels: individual, boss–subordinate pair (dyad), team, whole organisation.",
"Objective 5 — enabling climate: people take initiative, experiment, and the organisation can renew itself.",
"Tools (appraisal, training, counselling, OD) only work if they actually help development, not if they are empty forms."])

add(2,1,"Evolution from traditional training to strategic HRD",
"HRD did not start as a board-level function. It grew from welfare and skill classes into a system linked to business goals. Write this as stages.",
["Welfare/personnel era: attendance, wages, discipline, files — people were controlled, not developed.",
"Training-cell era: short job-skill courses (how to run a machine), often cancelled when production was busy, not linked to strategy.",
"1969 Nadler names HRD as a field: training + education + development for behaviour change.",
"India 1970s–80s (Rao, Pareek): HRD as a SYSTEM — appraisal, potential, career, counselling, OD together.",
"Difference crystallises: HRM maintains the workforce; HRD develops it; every manager (not only HR) is responsible.",
"Competition, IT, quality, liberalisation forced firms to ask ‘what capabilities do we need next year?’ = strategic HRD.",
"Today: competency maps, talent pipeline, climate, e-learning, HRD sitting in strategy meetings.",
"Exam punch: a random workshop = old stage; development tied to organisational goals = strategic."])

add(3,1,"Relationship between HRD and HRM",
"Both deal with people, but they are not the same word. HRM is the whole house (hire, pay, law, welfare, use people). HRD is the room where people grow. They need each other.",
["HRM umbrella includes procurement, compensation, IR, welfare AND development; HRD is mainly that development part.",
"HRM is maintenance-oriented (keep the system running); HRD is development-oriented (change behaviour and capability).",
"HRM often motivates with money; HRD uses higher-order needs — growth, recognition, achievement.",
"HRM is typically the HR department’s job; HRD is every manager’s job, with specialists only helping.",
"They complement: unpaid, unsafe staff will not learn; well-paid untrained staff produce scrap.",
"Data link: appraisal and manpower files (HRM) feed training and succession (HRD).",
"Strategic HRM (‘people as competitive resource’) is actually delivered through HRD systems.",
"Do not write they are identical; do not write they are unrelated."])

add(4,1,"Importance of HRD for individual and organisational performance",
"Performance = desired results. HRD raises it by ability, clarity, motivation and teamwork — not by shouting ‘work harder’.",
["Closes skill gaps (when the gap really is knowledge/skill) so errors fall and output rises.",
"Appraisal + feedback make the role clear, so effort is not wasted on the wrong things.",
"Growth opportunities raise morale; people give extra effort and leave less.",
"Potential and career put people where they can contribute more (person–job fit).",
"Teams and boss–subordinate pairs improve; organisation performance is a system, not 1+1 isolated people.",
"Enabling climate → initiative and innovation when the environment changes.",
"Cuts hidden drains: accidents, absence, attrition, unused talent.",
"Builds long-term effectiveness (pipeline, self-renewal), not a fear-driven one-month spike."])

add(5,1,"HRD climate and characteristics of a supportive climate",
"Climate is the ‘weather’ of the workplace — how it feels regarding trust, learning and fairness. Posters are not climate; daily boss behaviour is. Supportive climate is the soil; HRD tools are seeds.",
["OCTAPAC values (Indian HRD): Openness, Confrontation of problems, Trust, Autonomy, Proactivity, Authenticity, Collaboration.",
"Openness: you can ask a doubt and disagree without being labelled negative; talk is two-way.",
"Trust and authenticity: management’s words match actions; people need not wear a mask.",
"Confrontation: problems are discussed and solved, not buried to look peaceful.",
"Autonomy and proactivity: reasonable freedom; people act before being told every step.",
"Collaboration: departments help each other instead of writing blame notes.",
"Top support is visible: time, money, people actually released for learning.",
"Fair access and recognition of mentoring — not only favourite employees and not only individual heroes."])

add(6,1,"Differentiate HRD climate and organisational culture",
"Culture is who we are over years (deep values, rituals, unwritten rules). HRD climate is how developmental it feels this year. Related, not twins.",
["Culture = shared beliefs (‘elders decide’, ‘customer is king’) — often unconscious, slow to change.",
"HRD climate = current perception of openness, coaching, fair training chances — can improve or crash in months.",
"Culture is broad (power, dress, festivals); climate is the development slice only.",
"Example of culture: family business, loyalty, seniority, owner as father.",
"Example of climate in the same firm: seniors patiently teach juniors vs they hide knowledge so they cannot be replaced.",
"Mismatch: wall says ‘learning culture’ but appraisal is punitive → employees become cynical.",
"HRD must fit tools to culture (don’t dump 360° overnight in a very hierarchical place) AND deliberately improve climate.",
"Exam line: culture = identity; climate = today’s weather for growth."])

add(7,1,"Role and responsibilities of an HRD professional",
"Not a clerk who books a hall and orders tea. Designer of people-systems and partner to managers.",
["Diagnose: what capability gap is blocking work? Is the problem even training (or a broken machine)?",
"Design the HRD system so appraisal, career, training and counselling share one purpose.",
"Facilitate learning: methods, internal trainers, e-learning, mentoring — and teach bosses to coach.",
"Build climate/culture and act as change agent in mergers, computerisation, quality drives.",
"Evaluate and audit: did behaviour and results change, or only attendance?",
"Ethics: keep counselling confidential; keep opportunities fair.",
"Old role = files and training calendar; new role = business partner who understands strategy.",
"Success = managers developing their teams daily, not a fat training brochure."])

add(8,1,"Significance for organisational effectiveness and long-term employee development",
"Effectiveness = achieve goals, adapt, stay healthy inside. Long-term development = people keep growing for years. They are two sides of one HRD coin.",
["Goals (quality, service, cost) are achieved through what people can do — HRD is the competence engine.",
"Even a firm that has stopped growing still needs HRD, because the outside world keeps changing (self-renewal).",
"IDPs must point at organisational goals so development is not random courses.",
"Career + potential = leadership pipeline; without it, one resignation collapses effectiveness.",
"Growth beyond the present job retains people and builds employability.",
"Cuts human wastage (turnover, unused talent) which is expensive.",
"Both humanistic (people first, equity) and economic (human capital).",
"Cutting HRD for a quarter’s profit usually means long-term decline."])

add(9,1,"Growing org: skill gaps + falling performance (apply HRD)",
"Don’t only write ‘conduct training’. HRD approach = diagnose, climate, all subsystems, line managers, evaluate. Growth stretches bosses and creates new roles faster than people are prepared.",
["Diagnose: which jobs, which errors, new vs old staff; skill vs tools vs overload vs unclear targets.",
"Restore climate — busy, angry bosses make people hide gaps.",
"Use appraisal for improvement plans, not only low ratings (rating without help increases decline).",
"Targeted learning from TNA: OJT + short courses; no generic 5-day ‘motivation’ picnic.",
"Train recently promoted supervisors to coach — often the hidden cause of team skill gaps.",
"Map future roles created by growth; start developing before the vacancy becomes a crisis.",
"Fix urgent safety/quality/customer gaps first, then install a yearly HRD cycle so it doesn’t return.",
"Measure whether errors and output recover; if not, go back to diagnosis."])

add(10,1,"Measures for a learning-oriented work environment",
"Learning environment = people learn from work, from each other, and from programmes, then apply it. That is HRD climate made daily, not a circular ‘please learn’.",
["Leaders model: share their own learning, admit mistakes; if the head never learns, juniors won’t.",
"Psychological safety: report errors and ask doubts without humiliation (e.g. ‘what we learned from defects’ without name-shame).",
"Frequent coaching feedback, not only one fearful annual rating.",
"Give time, budget, e-learning/library, and permission to practise new methods on the job.",
"Structures: after-action reviews, quality circles, mentors, cross-functional projects.",
"Fair access — stretch jobs and courses not only for those close to the boss.",
"Recognise knowledge-sharing and mentoring, not only individual heroes.",
"Align appraisal and promotion with teamwork and improvement, or the climate message is cancelled by the bonus."])

add(11,1,"Any two objectives of HRD (write as 8 marks)",
"Question says ‘two’ but marks are 8, so explain fully + mention others. Safest pair = Rao’s first two.",
["Obj 1: acquire/sharpen capabilities for present AND future roles. Acquire = new; sharpen = improve what is half-known.",
"Example: bank clerk must learn computers when the branch is digitised, not only paper ledgers.",
"How: induction, job training, coaching, rotation, using appraisal to find the weak skill.",
"Obj 2: develop general capabilities and inner potential (the whole person) for self and organisation.",
"Example: quiet technician with analytical talent given a process-improvement project becomes a leader.",
"How: potential appraisal, career talks, education, mentoring, stretch work.",
"Also write 8 lines on culture of teamwork (Rao’s third pillar) and equity/employability/adaptability.",
"Never submit two one-line sentences."])

add(12,1,"Any two ways HRD and HRM are related",
"Relation = how they connect, not only how they differ. Then add a short contrast so you don’t mix the words.",
["Relation 1: HRD is the developmental core inside the HRM umbrella (whole and part).",
"Example: recruit 50 operators (HRM) → induct, safety train, later make some supervisors (HRD).",
"Relation 2: they complement — HRM keeps people staffed and paid; HRD makes that payroll capable.",
"Shared data: appraisal files feed training; shared line managers; shared strategy.",
"Then 5-line difference: maintenance vs development; money vs growth needs; HR dept vs all managers.",
"Strategic HRM is delivered through HRD (capability building).",
"Incomplete HRM = hire and pay undeveloped people; incomplete HRD = courses with no stable employment conditions.",
"Not the same word, not unrelated."])

add(13,1,"Weak HRD climate → behaviour and performance (analyse)",
"Analyse = chain. Weak climate (fear, closed talk, no learning support) changes behaviour; behaviour hits results. Not a ‘soft’ topic.",
["Fear → hide mistakes and don’t ask doubts → defects/accidents reach the customer late.",
"No autonomy → wait for orders → organisation is slow in a changing market.",
"Even good training fails: ‘forget the classroom, do it the old way’ → no transfer.",
"Appraisal becomes politics; people manage impressions, not work; nobody improves.",
"Departments blame each other; customer sees delay and contradiction.",
"Demotivation: minimum work, absence, good people leave; who stays may be less marketable.",
"Potential unused (knowledge hoarded) → growth plans fail because nobody inside is ready.",
"Write one linking sentence: weak climate → fearful uncooperative behaviour → worse quality/speed/innovation/human capital."])

add(14,1,"Changing role of HRD professional (personnel → strategic HRD)",
"Analyse from-what-to-what, why, and new skills. Renaming the door ‘HRD’ while still only booking halls is not a role change.",
["From record-keeper (leave files, attendance) → diagnostician (capability vs strategy, climate data).",
"From classroom organiser → learning architect (OJT + e-learning + coaching mix).",
"From isolated training cell → integrator of appraisal, career, counselling, OD.",
"From the edge of the firm → strategy table (must understand customers/tech enough to translate goals into skills).",
"Change agent in mergers, digitalisation, quality — not only transfer orders.",
"Developer of line managers as coaches; success = their teams grow.",
"From counting programmes → evaluation, audit, ethics (no leaked counselling).",
"Why: competition and human-capital idea. Role changes fully only if top management means it."])

add(15,1,"Relationship: HRD philosophy, climate, performance",
"Three are a chain, not three definitions. Philosophy = what leaders believe. Climate = what staff feel. Performance = what the org achieves.",
["Philosophy: people have potential; developing them is a duty, not a cost to cut first.",
"Philosophy shapes practices: time for learning, developmental appraisal, real counselling — or the opposite.",
"Practices create climate: employees don’t read booklets, they experience the boss.",
"Climate shapes behaviour: initiative and honesty vs fear and hiding.",
"Behaviour produces performance: quality, service, innovation, speed.",
"Reverse loop: good results confirm ‘investment in people paid off’; panic-cuts start a downward spiral.",
"Dangerous case: high-sounding philosophy + cruel climate = extra cynicism (worse than silence).",
"To raise performance, live the philosophy; don’t start with a poster or only with a target."])

add(16,1,"Evaluate: HRD as strategic function vs only training",
"Evaluate = both sides + verdict. Training is necessary. The question is whether HRD should be only a course calendar.",
["Training-only looks like: annual calendar, attendance, smile sheets, cancelled when busy.",
"For strategic: capability, leadership pipeline and culture decide if strategy can be executed.",
"Nadler and Rao already defined HRD wider than a class.",
"A popular course can leave job performance unchanged if bosses and careers ignore it.",
"Counter: tiny firms may only need basic skill training; calling every picnic ‘strategic’ without data is fashion.",
"Do not abolish training — nest it inside a strategic system.",
"Strategic in practice: seat in strategy talks, line KRAs for development, evaluate behaviour/results.",
"Verdict: YES treat HRD as strategic; training is a vital instrument, not the whole function."])

add(17,1,"Any two indicators of a supportive HRD climate",
"Indicator = sign you can see or measure. Name two in depth, then extras.",
["Indicator 1 — openness and useful two-way feedback: juniors speak; mistakes discussed to learn, not only to punish.",
"How you see it: meetings, survey ‘I can discuss problems with my boss’, people don’t wait a year to know how they’re doing.",
"Indicator 2 — visible management support: time, money, people actually released for training; leaders themselves learn.",
"How you see it: training days really happened, IDPs completed, distant-branch staff also get chances.",
"Also: trust (words=actions), autonomy, collaboration, fairness, recognition of mentors.",
"Teamwork without a war of blame-notes is a practical sign.",
"If every course is cancelled because ‘work is busy’, support is fake whatever the poster says.",
"Don’t only list OCTAPAC as seven words — show behavioural signs."])

add(18,1,"Two reasons the HRD professional must understand culture",
"Culture is the context of every tool. Ignore it and people fake or reject HRD.",
["Reason 1 — FIT: 360° or blunt public feedback can be seen as insult in a hierarchical culture → fake praise, later used as a weapon.",
"Culture-aware start: private coaching and boss-supported feedback, then slowly more openness.",
"Reason 2 — pace of change: the same ‘low openness’ score means different things in the army vs a start-up; don’t shock overnight.",
"Also: who must sponsor HRD (owner, union, CEO) for it to be believed.",
"Subcultures (plant, sales, IT, regions) — one national design may fit none well.",
"Strategy needs a culture (innovation vs cost-cutting) → that gap becomes the HRD agenda.",
"Ethics: imposing a culture by force through HR tools can harm dignity.",
"Culture-blind HRD is technically neat and socially rejected."])

add(19,1,"Evaluate implementing HRD without culture and climate",
"Judgement question. Mostly bad consequences. Sequence should be diagnose → adapt → implement → evaluate.",
["People fill forms the ‘safe’ way: fake 360 data, silent classrooms — worse than no data.",
"Ritual: attendance complete, nobody learns; staff become skilled at looking developed.",
"Cynicism: ‘people first’ then used to punish → trust worse than if nothing was announced.",
"Money and workdays wasted; Kirkpatrick levels 3–4 fail even if the class was fun.",
"Value clash (speak up vs never embarrass the boss) → stress and withdrawal.",
"New ‘opportunities’ captured by in-groups → HRD increases inequality.",
"Only weak ‘plus’: glossy optics for visitors/accreditation — not real effectiveness.",
"Verdict: predominantly negative. Blind copy of foreign tools is unprofessional."])

add(20,1,"Design a basic HRD framework (capability + aligned to goals)",
"Design = labelled blocks, not a speech on importance. Pipeline: goals → competencies → diagnosis → actions → climate → check.",
["Block 1 — policy: development is strategic; every manager develops people; HRD cell facilitates; fair access.",
"Block 2 — translate this year’s and next years’ goals into role competencies (the alignment hinge).",
"Block 3 — linked subsystems: appraisal, potential, training, career, feedback, counselling; one language.",
"Block 4 — climate (openness, time to practise) or Block 3 won’t stick.",
"Block 5 — TNA: organisation, task, person; also check non-training causes.",
"Block 6 — mix OJT, courses, mentoring; IDPs; succession for growth roles.",
"Block 7 — governance: business heads + HRD review twice a year: right capabilities?",
"Block 8 — evaluation + simple HRD audit; feed back into Block 2. Closed loop, not random courses."])

add(21,2,"Structure of an HRD system and major components",
"A system = parts working for one purpose. HRD is a process, not a training calendar. Structure = how parts are arranged and linked.",
["Foundation: philosophy (people have potential) + goals from notes (individual, present role, future role, dyad, team, collaboration, self-renewal).",
"Performance appraisal: developmental review of results and behaviour — not only an increment mark.",
"Potential appraisal: can this person take a bigger/different job?",
"Training and development: planned learning for gaps and future work.",
"Career planning: path from entry toward later roles; individual + organisation goals.",
"Feedback and counselling: conversations that turn data into change; OD/climate for teams and culture.",
"Supports: line managers as developers, HRD staff, records, links to pay/promotion so messages don’t contradict.",
"Interrelation is structure: output of one is input of another; periodically ask if mechanisms help or hinder development."])

add(22,2,"Performance appraisal as HRD subsystem + importance",
"As HRD, appraisal is a cycle: agree the job → review → two-way feedback → development plan. If it doesn’t grow the person, it is only a ritual.",
["Starts with role clarity and joint goals — people cannot grow if ‘good work’ is unknown.",
"Diagnoses strengths and gaps — this map is the raw material of all other HRD.",
"Makes feedback regular instead of accidental.",
"Importance peaks at the IDP: 2–3 actions with dates (course, project, coaching). No IDP = only judgement.",
"Feeds training needs, career talks, potential, counselling — often drawn at the centre of HRD diagrams.",
"Fair recognition motivates; the talk also develops the boss–subordinate relationship (a Unit 1 goal).",
"Fails as HRD when forced ranking, surprise ratings, corridor signatures, no follow-up — then it creates fear.",
"Importance exists only if managers are trained and climate allows honesty."])

add(23,2,"Training as an HRD subsystem + contribution to development",
"Training = planned effort so people learn job knowledge, skills, attitudes. It is one subsystem, not all of HRD. Formula: need ≈ standard − actual, only if the cause is lack of KSA.",
["Receives needs from TNA and appraisal; must return people to a workplace that allows transfer.",
"Contributes at three levels: know, do, feel (respect, safety). Lecture-only under-develops.",
"Present-job: fewer errors, more confidence (e.g. new machine).",
"Future: prepare for tech, law, quality, promotion — preventive development.",
"Notes’ benefits: satisfaction, motivation, lower turnover, better image, adopt new methods.",
"Induction socialises people into purpose, customers, rules — they become members, not only hands.",
"Cannot fix broken machines, impossible targets, or cruel bosses; off-the-shelf programmes are a trap.",
"Maximise contribution: TNA, right method, good delivery, boss support, evaluate behaviour not only tea."])

add(24,2,"Career planning and potential appraisal",
"Both look at tomorrow. Performance = how well this year. Potential = how far can they go. Career = what path shall we walk together.",
["Potential: systematic estimate for higher/different responsibility; keep it separate from this year’s rating so a star specialist isn’t auto-made a manager.",
"Purpose: find talent, avoid Peter Principle (promote until they fail), invest development money wisely.",
"Career planning: process of choosing goals and a path; a blueprint; continuous because the environment changes; a means, not an end.",
"Mainly the individual’s job; organisation must give info, counselling and chances; integrate both sides’ goals.",
"Process in notes: aspirations → opportunities → match/mismatch → strategies (training/rotation) → review.",
"Join them: potential makes paths realistic; career turns a label into actual stretch jobs. Label without action = bitterness.",
"Benefits: succession, retention, better promotions, morale, stable workforce.",
"Cautions: secret lists, bias, only one managerial ladder — allow a specialist excellence path too."])

add(25,2,"Role of feedback and counselling in the HRD system",
"Forms don’t change people; conversations do. Feedback = usable information about work. Counselling = helping talk so the person can decide and cope.",
["Good feedback is specific, timely, about behaviour (‘you interrupted twice, we missed their concern’), not ‘you are poor’.",
"Must be two-way: employee also reports missing tools and unclear orders — that improves the system.",
"Notes: counselling discusses an emotional problem to reduce it; purpose is to help the person choose among options, not to scold softly.",
"Triggers: dissatisfaction, resistance to change, conflict, stress, withdrawal, etc. (on or off the job).",
"Functions: advise, reassure, communicate, release tension, clarify thinking, reorient. Aims include self-understanding, achievable goals, coping, positive self-regard.",
"Without counselling, appraisal is a signature; after training, feedback checks transfer; career counselling stops wild hopes.",
"Who: trained manager or specialist; confidentiality or climate dies; refer serious mental-health cases.",
"Simple process: describe behaviour → listen → agree solution → summarise commitment → follow up. Keep criticism on performance, not character."])

add(26,2,"Principles for designing effective HRD practices",
"Principles = design rules so practices grow people instead of creating fear or paperwork. Copying another firm’s form is not design.",
["Top management must believe it, fund it, and model it — or staff learn HRD is optional.",
"Line managers must own it daily; design tools they can actually use; train them.",
"Integrate subsystems: a beautiful course that never talks to appraisal is a showcase, not HRD.",
"Align with strategy: build the capabilities the next two years need, not a vendor’s favourite topic.",
"Need-based diagnosis (TNA, climate); notes warn against off-the-shelf; first ask if it is even a training problem.",
"Fit culture; build climate slowly. Shock 360° in a fearful place produces fake data.",
"Participation, fairness, transparency — equity is an HRD objective; developing only favourites is not effective HRD.",
"Continuity and evaluation: follow up; ask whether the mechanism helps or hinders the process; redesign rituals."])

add(27,2,"How major HRD subsystems are interrelated",
"Interrelated = output of one is input of another. Listing six names is not the answer. Draw a cycle in words.",
["Appraisal finds ‘weak listening’ → that becomes counselling agenda and, if it is skill, a training need.",
"After training, next appraisal should look for transfer — otherwise the course was a picnic between two forms.",
"Potential suggests leader track vs specialist track; career without potential is guesswork; potential without career moves is a broken promise.",
"Career plan specifies which course and which rotation; calendars should partly come from IDPs, not only vendor catalogues.",
"Feedback is the blood: every subsystem needs a conversation or files move and people don’t.",
"Climate/OD is the soil: fear makes every other subsystem process fake data.",
"HRM must be consistent: train teamwork but bonus only individual → people follow the bonus.",
"One shared competency file so each year doesn’t start from zero — that is how the process stays continuous."])

add(28,2,"Need to integrate HRD practices with organisational strategy",
"Strategy = chosen path (which market, quality, technology). HRD builds the people who walk it. Unconnected HRD can be busy and still useless.",
["Strategy is implemented by people, not by PowerPoint — digital branches fail if staff can’t use the system.",
"Need as a filter: limited money/time; don’t train fashion topics while critical roles stay weak.",
"Talent takes time: 20 team leaders in 2 years must start development now.",
"Different strategies need different climates (cost-discipline vs psychological safety for innovation).",
"Change creates fear; integrated communication, reskill, counselling or the strategy stays a circular.",
"HRD’s own budget/credibility depends on showing business outcomes.",
"Employees learn better when they see why (‘rural branches next year’ beats ‘please attend’).",
"Looks like: competency maps from strategy, IDPs in business reviews, dropping obsolete courses."])

add(29,2,"Appraisal exists but employees say it doesn’t help — improve it",
"Application: they already have a system. Typical disease: increment-only, untrained bosses, no talk, no follow-up. Apply HRD principles to redesign.",
["Write and say the purpose is development; rewards may use data but the conversation is about growth.",
"At the start of the year, jointly set KRAs — unclear jobs make review feel random and unfair.",
"Train managers: incidents and impact, not labels like ‘attitude problem’; teach listening.",
"Protect a real counselling slot; ban signing forms in the corridor; self-appraisal first; confidentiality.",
"End with an IDP (2–3 actions + dates) and a quarterly check — no IDP = judgement not development.",
"Send gaps to TNA; aspirations to career; leadership behaviours to potential — something must HAPPEN after the form.",
"Climate: no public humiliation of ratings; some appeal on process; moderate unfair bosses.",
"Ask staff yearly ‘did this help you grow?’; judge managers on conversation quality, not only form submitted on time."])

add(30,2,"Development path for someone with future leadership potential",
"Don’t only write MBA or instant promotion. Potential = maybe they can handle larger people/decision work later. Use all subsystems over 2–4 years.",
["Validate with more than one source (results, people behaviour, assessment centre); tell them honestly what was seen and what the risks are (e.g. impatience).",
"Career map 3–5 years with their aspirations; more than one fork, not a promised throne.",
"Keep present-job performance strong; add leadership behaviours (coaching, decisions, integrity) on appraisal. Potential is not a holiday.",
"Main developer = stretch experience: rotation, project lead, deputy, cross-functional task — each with a learning goal.",
"Training/education timed with stretch: how the business makes money + feedback/conflict skills.",
"Mentor (often not the direct boss) + counselling for pressure, loneliness, arrogance derailers.",
"Rich feedback from subordinates/peers/customers (360 only if climate is safe).",
"Yearly review by a talent group; if the label was wrong, a specialist path is still honourable; if good, next stretch."])

add(31,2,"Any two HRD subsystems",
"Name two, explain like a beginner, example, then list others + one link. Best pair: appraisal + training.",
["Subsystem 1 — performance appraisal: planned review vs agreed work/behaviour, ending in an IDP. Example: teacher + principal agree goals in June, review in March, then a workshop + coaching.",
"Why ‘sub’: it diagnoses and plans; it does not by itself create skill.",
"Subsystem 2 — training: planned learning of job KSAs, on-job or off-job, from a real need. Example: technicians practise on a dummy then work under a senior.",
"Why ‘sub’: not the whole of HRD; climate and career must support transfer or it is a picnic.",
"Also name potential, career, feedback/counselling, OD/climate.",
"Link: gap → counsel → train → use in career move → re-appraise.",
"Don’t write two words. Don’t say training = HRD.",
"Intro + two long explanations + others = 8 marks."])

add(32,2,"Any two purposes of feedback in HRD",
"Feedback = specific information so learning can happen. Not scolding, not vague praise.",
["Purpose 1 — improve current performance in time to correct. Cook told today ‘gravy too salty’ can fix tonight; ‘food average’ once a year cannot.",
"Tone matters: humiliation makes people defend, not improve — then even correct information fails.",
"Purpose 2 — long-term development: reinforce what is going well; point the next training or stretch. ‘You explain products clearly; you freeze when the customer is angry.’",
"Also motivation: honest praise meets growth/esteem needs that HRD stresses vs only money.",
"Also role clarity: often boss and employee didn’t share the same picture of the job.",
"Also climate: open respectful two-way talk signals trust; only negative talk signals fear.",
"Also upward feedback (broken processes) and after-training feedback (improve HRD design).",
"Write two long + cluster of others."])

add(33,2,"Poor coordination among subsystems reduces development (analyse)",
"Silos: each part works alone. Effectiveness = people actually become more capable. Show broken links → contradiction → waste → lost credibility.",
["Rated ‘weak communication’ every year but never trained/coached → gap stays; staff think HRD is dishonest.",
"Courses with no chance to practise and no career use → attendance without capability.",
"‘High potential’ ignored at promotion time → talent leaves; others see politics.",
"No counselling after the rating → numbers without insight; emotional blocks remain.",
"Train teamwork but bonus only individual targets → people follow pay; collaboration can get worse after ‘HRD’.",
"Two cells run similar programmes; some roles get nothing; no shared file → year starts from zero.",
"Chaos feels political → climate falls → remaining good practices transfer even less.",
"Vicious cycle: no impact → budget cut → even less HRD. Coordination is a condition of effectiveness, not a luxury."])

add(34,2,"Align HRD with strategy in a rapidly changing organisation",
"Strategy itself is revised often. Alignment cannot be a frozen 5-year training list. Need agility with direction.",
["Every strategy shift (new product, digital, new city) → quickly update ‘what people must be able to do’.",
"Short TNA and climate pulses; a giant study every three years trains yesterday’s need.",
"Flexible methods: just-in-time, OJT, e-learning, short workshops — people can’t leave a crisis for two-week camps every time software changes.",
"OD and counselling for new teams/mergers/lost roles — change is emotional, not only a skill list.",
"Career: projects and lateral moves; review paths often (notes already say career planning is continuous).",
"HRD in the quarterly business meeting: market shift → capability risk → action this quarter.",
"Alignment is also subtraction: drop old KRAs and courses so people aren’t pulled two ways.",
"Measure speed of capability building, not number of programmes."])

add(35,2,"Evaluate using potential appraisal together with performance appraisal",
"Evaluate combined vs either alone. Performance = how well now. Potential = how far. Development needs both.",
["They answer different questions; one number hides information (excellent today ≠ ready to lead people).",
"Avoids the classic wrong promotion: best salesperson becomes worst sales manager (Peter Principle).",
"Richer paths: high/high → leadership stretch; high performance/limited managerial potential → specialist excellence; low now/high potential → coaching or role fit.",
"Fairer when transparent: people understand why some get stretch roles.",
"Risks: secret lists, bias, both judgements in five minutes by one untrained boss, no feedback, no action — then it is politics.",
"Conditions: separate tools/time, trained assessors, multiple inputs, tell the employee, career/training actually follow, review as people grow.",
"Performance-only over-invests in today’s job; potential-only may ignore today’s customers.",
"Verdict: together is highly effective IF quality and follow-up; otherwise damaging. Recommend combined use with quality, not two extra forms."])

add(36,2,"HRD system ineffective when designed without strategy alignment",
"Ineffective = looks busy (forms, courses) but wrong capabilities and no business readiness. Trace the chain.",
["People become excellent at yesterday’s work while strategy needs new skills (digital, new market).",
"Popular programmes eat budget; critical roles for the plan stay weak — opportunity cost.",
"Career promises that don’t match future structure (many rungs while the firm is flattening) → anger and broken climate.",
"Appraisal chases old KRAs (volume without quality) → HRD actively teaches the wrong behaviour.",
"Business heads see no return and cut HRD; rituals shrink further.",
"High performers leave for firms where growth matches the business; remaining audience is weaker.",
"The organisation then cannot execute its own strategy (quality failure, digital lag, failed expansion).",
"High training-day counts hide irrelevance until a crisis. Activity ≠ effectiveness."])

add(37,2,"Two benefits of integrating career planning with potential appraisal",
"Integration = paths based on real potential judgement, and labels followed by real moves (rotation, training), not a secret stamp.",
["Benefit 1 — realistic paths: don’t promise GM in three years if potential shows little people-leadership; less betrayal later; counselling can be truthful.",
"Notes already say career planning must find match/mismatch; potential supplies the evidence so the person can plan effort that will actually pay.",
"Benefit 2 — better use of talent: high-pots get timely stretch instead of waiting behind seniority; succession for key jobs; money on the right people.",
"Example: two equally good engineers → one people-leader path, one deep-designer fellowship; both stay; you don’t ruin a designer by forcing him to be a boss.",
"Also fewer wrong promotions (customers and teams protected).",
"Also motivation and retention — growth paths become believable.",
"Also better counselling: not generic ‘work hard and you will rise’.",
"A label without a move creates bitterness; a path without potential creates false hope."])

add(38,2,"Two features of an effective HRD practice",
"Feature = quality you would look for. Effective = actually helps development, not only control or a brochure.",
["Feature 1 — developmental purpose in real operation: after the practice, an IDP, coaching, or chance to practise exists. Five-minute increment signing is not HRD even if the heading says so.",
"Test (Rao): does this mechanism promote or hinder the development process? Ask employees whether anything at work changed.",
"Feature 2 — integration with other subsystems and with strategy. Training comes from gaps and goals, not a vendor catalogue.",
"Example: quality course → next appraisal includes quality behaviour + boss coaches weekly + a live project uses the method.",
"Also: need-based, line-manager owned, fair/transparent, funded by the top, climate-safe (doesn’t terrify), evaluated.",
"Fair access (not only favourites) is both an objective and a feature — unfair practice kills climate then nothing transfers.",
"Evaluation/review is itself a feature; unreviewed practices rot into paperwork.",
"Write two features with ‘how you would recognise them’, then a cluster. Not two adjectives like ‘good’."])

add(39,2,"Design an integrated HRD system connecting the six elements",
"Don’t write six mini-essays. One cycle, one language, line managers own, HRD facilitates.",
["Policy: performance, potential, training, career, feedback, counselling are ONE cycle; talent committee of business heads twice a year.",
"Spine: one competency framework + one employee file (goals, appraisals, IDP, courses, career notes).",
"Sequence: joint goals → ongoing feedback → performance appraisal → counselling + IDP → potential (if relevant) → career talk → training/OJT plan → evaluate → next goals.",
"Feedback/counselling: quarterly check-ins; trained listening; criticism on performance not character; confidentiality; follow-up dates.",
"Training: IDPs aggregated to calendar; group courses still pass TNA; bosses get a transfer brief; unused training reported.",
"Potential/career: talent council uses data for rotation/succession then TALKS to the employee; specialist path exists; review when strategy changes.",
"Climate work so people don’t fake every form — otherwise integration processes lies.",
"Yearly audit of links: did IDP actions happen? did training match gaps? did high-pots get stretch? Repair breaks."])

add(40,2,"Evaluate strong training content but weak strategy/appraisal/career links",
"Keep good teaching. Reject isolation. Strong content = good classroom. Weak links = maybe wrong topic, bosses don’t use it, course doesn’t count for growth.",
["Strength: may still get high reaction and some real learning (Kirkpatrick 1–2). Keep content if the topic can be aligned.",
"Weakness: may teach a fashionable capability while strategy needs something else — opportunity cost.",
"No appraisal hook: bosses don’t expect the new behaviour → level 3 (job use) dies. Content cannot jump this gap alone.",
"No career credit: only highly self-driven staff practise; others treat it as a break.",
"Likely pattern: L1 high, L3/L4 poor. A manager who only reads smile sheets will wrongly approve it.",
"Repeated isolated ‘excellent’ courses create holiday-training cynicism; later even good HRD is harder.",
"May still help a few individuals as general education — not enough to accept as organisational HRD.",
"Verdict: don’t accept as-is. Remap to TNA/strategy, add pre/post goals and boss coaching, put it on career maps, evaluate behaviour/results, then keep the content."])

add(41,3,"TNA: concept and importance in HRD",
"TNA (Training Needs Assessment) is Stage 1 of the cycle: TNA → design → delivery → evaluation. It asks whether people need training, who, in what — and whether training is even the right medicine.",
["Simple formula in notes: need = standard performance − actual, BUT only when the cause is lack of knowledge/skill/attitude.",
"If the machine is broken or the target is impossible, that is not a training need. Cause-and-effect first (notes’ caveat).",
"Organisation analysis: link to goals; where it hurts; will bosses support use of learning?",
"Task analysis: important tasks and the KSAs needed — this becomes the content skeleton.",
"Person analysis: who has the gap; two people with the same title may differ; ‘knows but doesn’t do’ may be climate, not training.",
"Importance: stops off-the-shelf waste and cynicism; honest diagnosis so management doesn’t say ‘we already trained them’ while the real cause remains.",
"Importance: better design, fair who-gets-help, priority when money is scarce.",
"Importance: baseline so later evaluation is possible. Skip TNA = other three stages are guesswork."])

add(42,3,"Major steps in designing a training programme",
"Design is Stage 2 — convert TNA into a blueprint. Notes’ matrix: goal, objectives, methods, facilities/trainers, budget. More than a lecture timetable.",
["Confirm TNA, who attends, readiness (literacy, motivation), and that training is still the right solution.",
"Write an overall goal and observable objectives: ‘able to log a complaint correctly in five minutes’ — vague ‘appreciate quality’ produces vague courses.",
"Select content and sequence, usually concept → demo → practice → feedback; cut anything that doesn’t serve an objective.",
"Choose methods from the type of objective (practice for skill, discussion for attitude) and decide on-job vs off-job, internal vs vendor, on-site vs off-site.",
"Plan venue, AV, materials, trainer, costs accounts will accept — poor admin later looks like poor training.",
"Design transfer now: brief the boss, action plans, job aids, time to practise at work. Transfer is not a hope.",
"Build evaluation into the plan: reaction, test, 30–60 day behaviour, results vs TNA baseline.",
"Check feasibility and equity: can production release people? are women and distant branches included? un-attendable design is a wish."])

add(43,3,"On-the-job and off-the-job methods with examples",
"Method = how learning is organised. OJT = learn while doing real work. Off-the-job = away from the daily workstation so attention is on learning. Neither is always best.",
["OJT meaning: actual workplace, real tools, guided by supervisor or experienced worker; learning and producing together.",
"OJT examples: coaching, job rotation, apprenticeship, internship, understudy/shadowing, job-instruction training, live action-learning project.",
"OJT plus: relevant, extra cost often low, transfer easier. OJT minus: busy/unskilled coach, bad habits copied, danger on machines. Train the coaches.",
"Off-the-job meaning: classroom, workshop, vestibule (dummy workplace near factory), institute, conference — not answering production calls every five minutes.",
"Off-the-job examples: lecture, discussion, case, role play, games, sensitivity lab, simulation, vestibule, formal courses.",
"Off-job plus: focus, expert faculty, safer practice, concepts, mix with other departments. Minus: cost, time away, classroom unlike job, irrelevance if TNA was weak.",
"Choose from objective and safety: routine existing skills → OJT; new/dangerous/concepts or workplace teaches wrong method → off-job first.",
"HRD usually blends: concept and safe practice off-job, then OJT coaching, then review. Method serves TNA, not fashion."])

add(44,3,"E-learning as a method and major advantages",
"E-learning = training through LMS, online modules, webinars, video, quizzes, mobile. Self-paced or live. Can stand alone or blend. Uploading a PDF is not good e-learning. 21st-century notes mention web, mobile, wikis, communities of practice.",
["Good e-learning uses instructional design: small chunks, practice questions, feedback, sometimes simulation, and tracking of completion/scores.",
"Advantage — flexibility: night shifts, many cities, no travel to head office; short spells of learning.",
"Advantage — speed and scale: same compliance or product update to thousands in days, same message (classroom would take months and vary by trainer).",
"Advantage — cost over time: expensive to build, cheap per extra learner; yearly repeats cheaper than residential camps.",
"Advantage — standard quality + tracking for evaluation/audit; managers see who is behind.",
"Advantage — replay difficult parts, micro-learning, some personalisation for mixed ability.",
"Advantage — blend with webinars, mobile, internal wikis, social learning (notes’ 21st-c tools).",
"Limits (write 2 for balance): devices/connectivity; dropouts need discipline; poor design bores; not enough alone for counselling/surgery skills; transfer still needs a boss."])

add(45,3,"Kirkpatrick model for evaluating training",
"Stage 4: effectiveness vs objectives. Notes: not only feelings — learning, behaviour, impact on corporate objectives. Kirkpatrick = four levels, a ladder. Liking ≠ organisational results.",
["Level 1 Reaction: did they like it / find it relevant? Smile sheet. Useful for tea, timing, trainer style. Danger: hill-station + funny speaker scores 9/10 with no skill.",
"Level 2 Learning: did KSA actually increase? Test, demo, pre–post, role-play vs checklist. If L2 is weak, later levels cannot honestly succeed.",
"Level 3 Behaviour: do they use it at work after weeks? Observation, boss ratings, audits. Most programmes die here because old habits and rewards pull back. Climate decides a lot.",
"Level 4 Results: quality, errors, safety, sales, CSAT, cost — why the company paid. Hard to prove training alone caused it.",
"Logic: each step can fail even if the previous succeeded — so don’t stop at L1.",
"Decide measures during TNA, take baseline before training, plan 30–60 day follow-up.",
"Use: diagnose (high L1 low L3 → transfer/climate, not only slides). Supports HRD’s professional status.",
"Limits: L4 has many causes; full 4-level is costly — go deeper for safety/high-cost programmes than for a one-hour talk."])

add(46,3,"Importance of delivering training effectively after it is designed",
"Delivery = Stage 3. Notes split it: practical admin + actually carrying out training. Design is the recipe; delivery is the cooking. Learning happens in those hours, not in the HRD file.",
["If the trainer skips practice because time ran out, the skill objective is dead — delivery is the product employees experience.",
"Admin (venue, logins, batch size, handouts, travel) shapes attention and respect; chaos says ‘this learning is not important’.",
"Trainer needs subject knowledge PLUS adult-learning skill (questions, their world, managing talkers). Slide-reading is not delivery.",
"Adapt pace to a weaker/stronger group without abandoning objectives.",
"Psychological safety to practise, fail, and ask basic questions — especially for skills and attitudes.",
"Start transfer in the room: real cases, action plan, boss at closing, practise on actual software.",
"Opening (why this, what Monday will look like) and closing (commitment) create motivation to try.",
"Tests and reaction data are collected here; sloppy implementation makes later evaluation unusable and breaks the cycle."])

add(47,3,"Relationship among TNA, design, delivery, evaluation",
"Four stages of one cycle, sequential and circular. Matches Nadler: organised learning for behaviour change. Break a link → training becomes an event, not HRD.",
["TNA feeds design: who, what, method, whether training is the solution. Design without TNA is a decorated guess / off-the-shelf trap.",
"Design feeds delivery: sequence, facilities, trainer brief, transfer tasks, tests. Delivery without design = improvisation; design without delivery = a drawer document.",
"Delivery feeds evaluation: you measure what actually happened (if practice was skipped, skill scores should be honest and low).",
"Evaluation feeds next TNA: remaining gaps, new errors, or the discovery that it was never a training need.",
"Evaluation also redesigns method/admin/climate (poor L2 → change method; poor L3 → bosses/job conditions).",
"Skip TNA: excellent class on the wrong need — failure started at Stage 1.",
"Skip evaluation: open loop; next year is guesswork again; HRD cannot claim professional/strategic status.",
"Picture: TNA → Design → Delivery → Evaluation → back to TNA. Budget all four, not only the visible class day."])

add(48,3,"Importance of evaluating training for employees and organisations",
"Evaluation = did it do what it was supposed to? Importance differs slightly for people vs the firm, but both need truth, not only certificates.",
["For employees: tests and coaching show what they mastered and what to practise — feedback as an HRD right, not only a certificate.",
"For employees: documented competence supports career talks and employability (an HRD objective).",
"For employees: their reaction/suggestions, if used, improve the next programme; asking ‘did this help work?’ also signals climate.",
"For organisations: accountability for money and lost production hours — stewardship, not cruelty.",
"For organisations: find the break (wrong need, weak design, poor delivery, or no transfer) so the same bad course isn’t repeated.",
"For organisations: L4-type questions show whether capability for strategy increased — needed if HRD wants strategic status.",
"Avoid two illusions: happy people who can’t perform; strict trainer with low smiles but high learning.",
"Credibility: evaluation moves HRD from ‘picnic department’ to a professional function, which then wins resources for people again."])

add(49,3,"Repeated performance errors: what TNA information to collect",
"Apply TNA: do not announce a ‘quality workshop’ first. Collect info to decide if training is the answer, who, and what. Write as an information list.",
["Error facts: type, frequency, process step, shift, product, cost — records + observation, not only the supervisor’s anger.",
"Organisation analysis: quality standards, new machine/target/software, staffing, whether speed is rewarded more than accuracy, whether this error hurts customers/safety enough to be a priority.",
"Non-training causes FIRST: machine, missing tools, conflicting SOPs, impossible workload, incentive to rush. If these dominate, fix process, don’t design a course. Notes: training is not the answer to all problems.",
"Task analysis: correct procedure, critical steps, KSAs, where errors cluster — this becomes content IF training is justified.",
"Person analysis: who (new vs everyone), past training, can they explain the method but still fail (skill/attitude/pressure vs knowledge), language/literacy.",
"Readiness: do they believe errors matter? fear of reporting near-misses? punished for slowing down to be correct? Fear means climate work too.",
"Transfer climate: after a course, will the boss allow slower correct practice? do peers mock the official method? is the shortcut still how you hit targets?",
"Baseline now (error rate, rework, complaints) and agree what reduction in 8–12 weeks means success — otherwise later evaluation is invented."])

add(50,3,"Methods for employees who need practical skills AND conceptual knowledge",
"Head = understand why/principle. Hand = do the task to standard. One method rarely does both. Design a blend and a sequence.",
["Split TNA into two objective lists: ‘explain why lock-out exists’ vs ‘perform lock-out on machine A in 3 minutes using the checklist’.",
"Conceptual methods: short lecture, diagram, case, e-module, quiz — concepts travel to new situations.",
"Safe practice before live work: vestibule, simulation, dummy, role play, lab — mistakes don’t harm customers/machines. Especially if the real task is dangerous/costly.",
"Then OJT with a trained coach and checklist; rotation if the skill has several contexts. Untrained seniors copy bad habits.",
"Action-learning project: live but bounded problem using the concept to decide and the skill to implement — binds head and hand.",
"Micro e-learning to replay concepts after OJT when memory fades; not a substitute for practice.",
"Sequence: concept → demo → simulated practice with feedback → OJT → review. Unsupervised OJT first can freeze wrong methods.",
"Evaluate both: knowledge test for concepts AND observed job sample for skill. A theory exam alone misses the brief."])

add(51,3,"Any two purposes of TNA",
"Two in depth, then extras. Strongest: find real learning needs, and stop training as a fake solution.",
["Purpose 1: identify genuine KSA gaps — what, in which job, in which people — so HRD has a map instead of aiming in the dark.",
"Example: billing errors may be software skill of new clerks only, not a ‘motivation problem’ of the whole department.",
"Purpose 2: prevent wrong solutions. Notes warn training is not the answer to all problems and against off-the-shelf buys. If cause is machine/incentive/staffing, don’t design a course.",
"Example: rude front desk because understaffed and punished for delay — a smile-training day won’t change performance.",
"Also: give measurable objectives so design can start professionally.",
"Also: choose the right trainees and the right method (skill vs knowledge vs attitude).",
"Also: prioritise scarce money; record baseline; org analysis keeps TNA tied to strategy.",
"Two long paragraphs with examples + cluster."])

add(52,3,"Name any two levels of the Kirkpatrick model",
"Four levels exist. For 8 marks name two in detail, briefly the other two, measures, why more than one level matters. Never two words only.",
["Level 1 Reaction: liked it / relevant? End-form. Useful for comfort/trainer; weak alone because entertainment scores high.",
"Level 2 Learning: did knowledge/skill/attitude rise? Tests, demos, pre–post, role-play checklist. No L2 → later levels cannot honestly succeed.",
"Briefly Level 3 Behaviour: use on the job after a lag; observation/audits; climate decides a lot.",
"Briefly Level 4 Results: org outcomes (quality, errors, safety, CSAT, cost) — impact on corporate objectives.",
"Example measures: smile sheet; 20-mark skill test; 60-day call audit; defect rate vs baseline.",
"Ladder: one level does not prove the next (popular ≠ able; able ≠ doing it at work).",
"Costly or safety programmes should not stop at reaction; a one-hour talk may not need full L4.",
"Write two in depth + rest brief so the examiner sees the whole model."])

add(53,3,"Why positive reactions but no job-performance improvement (analyse)",
"Gap between Kirkpatrick L1 and L3/L4. People may honestly enjoy the programme and work the same on Monday. Look at class, original need, and workplace.",
["Entertainment ≠ learning: celebrity + hill station raise smiles; skill never practised so L2 never happened.",
"Content too easy or only slides — they liked it because it didn’t demand uncomfortable practice; still incompetent.",
"Wrong need (no TNA): problem was tool, process, target, or pay. Training cannot improve that job. Notes: not the answer to all problems.",
"Hostile transfer: boss says forget class; peers mock new method; unofficial shortcut is how you hit targets.",
"No opportunity to use: software not installed, or task comes once in six months — skill forgotten.",
"Rewards contradict: taught quality, paid only for speed — people follow pay. Systems beat training.",
"No follow-up, coaching, IDP — one good memory of two days, not a changed habit.",
"Conclusion: L1 is a weak predictor of job performance. Design for learning + transfer + climate, not applause."])

add(54,3,"Consequences of designing training without adequate TNA",
"Consequence chain: work, money, people, HRD itself. Inadequate TNA = didn’t study goals, tasks, persons, non-training causes. Design aims at fog.",
["Wrong content → original errors continue; staff and customers see no benefit (‘we trained and nothing changed’).",
"Wrong audience: bored experts give poor reaction; needy people absent; equity fails.",
"Wrong method: lecture where coaching was needed → learning/transfer fail even if the topic name was roughly right.",
"Dangerous: training as false solution — real cause remains; management stops looking and next time blames workers personally.",
"Cynicism: future programmes get bodies in chairs but not minds; climate worsens.",
"Direct vendor cost PLUS lost production time (mention both).",
"No true objectives/baseline → evaluation is theatre; the cycle cannot learn.",
"Over years the calendar becomes ritual; capability lag shows up in a crisis (quality, digital). Long-term org weakness, not only one bad course."])

add(55,3,"Evaluate usefulness of Kirkpatrick for judging training",
"Usefulness + limits + how to use + verdict. Fits the notes (beyond feelings → learning, behaviour, corporate impact). Not perfect science.",
["Useful: complete vs smile sheets — biggest value; stops the entertainment illusion.",
"Useful: easy language with managers who fund training; HRD can refuse to claim success on tea and venue.",
"Useful for design and diagnosis: plan measures at TNA; high L1 + low L3 → look at transfer climate, not only the trainer.",
"Limit: L4 causality messy (sales/profit have many causes) — over-claiming ‘this course caused 10% profit’ is unscientific.",
"Limit: behaviour/results need months of follow-up; many firms stop at L1 so the model is unused (not the model’s fault).",
"Limit: not every one-hour briefing needs full L4 energy — usefulness depends on proportionate use.",
"Use well: baseline, combine with boss support for transfer, don’t worship L1, be modest at L4, go deeper when risk/cost is high.",
"Verdict: highly useful as a GUIDE for organisational training effectiveness; not a mechanical proof. Keep it; don’t file four empty forms."])

add(56,3,"How choosing OJT / off-the-job / e-learning affects outcomes",
"Outcomes = like, learn, do, results. Method creates different experiences, costs, transfer patterns. Then fit, blend, climate.",
["OJT: strong relevance/transfer if the coach is skilled and has time (path to L3). Bad/busy coach = mass-produced wrong methods; can injure on dangerous tasks. Outcome follows coach quality more than the label OJT.",
"Off-the-job: better concepts and safer practice (L2 for new/risky skills). L3 suffers if class ≠ work or bosses don’t continue coaching. High reaction possible from a nice venue even when TNA was weak — expensive irrelevance.",
"E-learning: scale, consistent knowledge, tracking (L2 for information). Dropout if no discipline/net. Weak alone for interpersonal skill. Risk: ‘we have an LMS so people are trained’ while completion and transfer are low.",
"Fit beats fashion: motor skill → OJT/simulation; interpersonal → role play then OJT; info update → e-learning. Wrong fit lowers outcomes regardless of budget.",
"Learner/context: new staff often need structured off-job; experienced may prefer OJT or micro e-learn; many cities favour e-learn for knowledge.",
"Blended outcomes often best — each method covers another’s weakness (concept + practice + job coach).",
"Climate can cancel ALL methods at L3 if new behaviour is punished.",
"Analytical close: outcomes = fit + execution quality + transfer support, not the brand name of the method. Choice is a strategic HRD decision."])

add(57,3,"Two reasons to evaluate at more than one Kirkpatrick level",
"One level, especially reaction, cannot define effectiveness. Two reasons in depth, then extras.",
["Reason 1: different levels answer different questions — like ≠ learn ≠ do at work ≠ business results. One number pretends to answer all.",
"Example: fire course can be popular (L1) while people still cannot use an extinguisher (L2); or they pass a test and still don’t follow procedure on the floor (L3).",
"Reason 2: diagnosis so HRD can improve. Knowing only ‘performance didn’t improve’ doesn’t tell you whether to change content, trainer, or workplace. Multi-level data show the break.",
"High reaction + low learning → redesign method. High learning + low behaviour → fix bosses and job conditions.",
"Also accountability: the organisation funded performance, not entertainment.",
"Avoid false success (high smiles, zero job change) and false failure (strict trainer, low smiles, high learning).",
"Also feedback to the same learners for further coaching; and strategic HRD cannot live on L1.",
"Two long reasons with examples + cluster."])

add(58,3,"Two factors while selecting a training method",
"Selecting = OJT, lecture, case, role play, vestibule, simulation, e-learning, outdoor… or a blend. Headlines: objectives, and nature of the task.",
["Factor 1 — learning objectives: what must they be able to DO after? Knowledge, skill, attitude need different methods. You cannot lecture a motor skill or only e-read someone into counselling skill.",
"Example: ‘explain three causes of defects’ → discussion/quiz. ‘Replace a filter in 8 minutes without leaks’ → demo, simulation, OJT. Same department, different methods.",
"Factor 2 — nature of the task: dangerous/costly → simulate/vestibule before live OJT. Simple routine already modelled well by seniors → OJT. If the workplace currently teaches the wrong method, off-job first so bad habits aren’t copied. Customer tasks need practice with feedback (role play).",
"Also trainees: education, language, digital literacy, numbers. Illiterate workers need demonstration, not dense e-text.",
"Also cost, time, production loss — cheap methods that fail are not actually cheap.",
"Also geography, lab/trainer availability (no lab → no vestibule; scattered plants → e-learn + local coaches).",
"Also urgency: skill needed tomorrow → OJT + job aid may beat a delayed residential course.",
"Also culture: will role play be seen as loss of face? Climate decides transfer of any method. Choose from TNA, not habit."])

add(59,3,"Design a complete programme for one skill gap (full cycle)",
"Name a concrete gap and walk TNA, objectives, method, delivery, evaluation + transfer. Example: complaint-handling — high repeat complaints, low first-contact resolution. Another gap is fine if all parts are covered.",
["TNA: org = customer retention; task = listen, log CRM, SOP solution, escalate; person = who fails, know vs freeze on angry customers; check CRM/policy first; baseline repeat-% and CSAT.",
"Objectives observable: end of class, role-play angry complaint, 80% on checklist; within 8 weeks on job, repeat complaints fall by agreed %.",
"Method blend: e-module on policy/screens (concept) + classroom role play with recorded calls (skill/attitude) + two weeks OJT coaching with checklist (transfer).",
"Delivery: batches ~12 so everyone practises; working CRM logins; quiet room; manager at close to commit support; action plan for Monday.",
"Transfer: supervisor weekly coaching a month; job aid near phone; appraisal KRA on resolution quality not only call count — without this the design is incomplete.",
"Eval L1–2: relevance form; SOP test; observed role-play vs checklist.",
"Eval L3–4: call audits day 30 and 60; repeat-complaint and CSAT vs baseline; maybe trained vs not-yet-trained group; 60-day HRD + dept review.",
"Complete = all four cycle stages + specified gap + methods matching objectives + transfer + more than smile sheets."])

add(60,3,"Evaluate two alternative programmes with Kirkpatrick and recommend",
"Same need, two designs, judge each level, recommend. Need here: first-line supervisors must give developmental feedback (helps HRD climate). Change the need if you like, but compare level by level.",
["Programme A: two-day off-site ‘leadership’ with a celebrity speaker, luxury venue, little practice, no boss involvement, no follow-up. Looks expensive and fun.",
"Programme B: from TNA — concept on developmental feedback, lots of role play, real job assignments, their bosses as coaches, 60-day follow-up, appraisal item on coaching quality. Ordinary venue.",
"L1 Reaction: A often wins (travel, celebrity). If you decide on L1 you wrongly buy A. B scores OK if seen as relevant, some say it was hard work.",
"L2 Learning: B superior — they practise the actual conversation. A gives quotes without skill. Role-play scores would show this.",
"L3 Behaviour: B far better (assignments + job support). A rarely transfers; old scolding/silence returns.",
"L4 Results: B more likely to improve team climate, earlier error-correction, engagement. A costly with little organisational result.",
"Recommend B even if smile sheets are slightly lower. Effectiveness = behaviour and results for the need, not applause. Condition: B still fails at L3 without top support for coaching time.",
"Meta-point: Kirkpatrick protects the organisation from buying the more popular but less effective programme. Popularity ≠ effectiveness."])

assert len(Q)==60

def hf(c, d):
    c.saveState()
    w,h=A4
    c.setFillColor(NAVY); c.rect(0,h-16,w,16,fill=1,stroke=0)
    c.setFillColor(white); c.setFont("Times-Bold",8)
    c.drawString(14*mm,h-11,"HRD (OE)  |  Understand + expand  |  8-mark exam points")
    c.setFillColor(NAVY); c.rect(0,0,w,14,fill=1,stroke=0)
    c.setFillColor(white); c.setFont("Times-Roman",7.5)
    c.drawString(14*mm,5,"Intro 4 lines → expand each point → 3-line conclusion.  Nadler 1969 · T.V. Rao · OCTAPAC · TNA cycle · Kirkpatrick 1–4")
    c.drawRightString(w-14*mm,5,f"p.{d.page}")
    c.restoreState()

styles=getSampleStyleSheet()
styles.add(ParagraphStyle("T",fontName="Times-Bold",fontSize=15,leading=18,alignment=TA_CENTER,textColor=NAVY,spaceAfter=4))
styles.add(ParagraphStyle("S",fontName="Times-Italic",fontSize=9.5,leading=12,alignment=TA_CENTER,textColor=TEAL,spaceAfter=6))
styles.add(ParagraphStyle("N",fontName="Times-Roman",fontSize=9,leading=12,alignment=TA_JUSTIFY,spaceAfter=6))
styles.add(ParagraphStyle("QH",fontName="Times-Bold",fontSize=10,leading=13,textColor=NAVY,spaceBefore=5,spaceAfter=2))
styles.add(ParagraphStyle("I",fontName="Times-Italic",fontSize=9,leading=12,alignment=TA_JUSTIFY,textColor=HexColor("#2d4a4a"),spaceAfter=3))
styles.add(ParagraphStyle("B",fontName="Times-Roman",fontSize=9,leading=11.8,leftIndent=8,spaceAfter=1.5))
styles.add(ParagraphStyle("U",fontName="Times-Bold",fontSize=11,leading=14,textColor=white,alignment=TA_CENTER))

def banner(t):
    tb=Table([[Paragraph(t,styles["U"])]],colWidths=[180*mm])
    tb.setStyle(TableStyle([("BACKGROUND",(0,0),(-1,-1),TEAL),("TOPPADDING",(0,0),(-1,-1),5),("BOTTOMPADDING",(0,0),(-1,-1),5)]))
    return tb

def esc(s):
    return s.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;")

def build_pdf():
    out="/home/user/HRD/HRD_Exam_Points_Only.pdf"
    doc=SimpleDocTemplate(out,pagesize=A4,leftMargin=13*mm,rightMargin=13*mm,topMargin=20*mm,bottomMargin=16*mm)
    story=[Paragraph("HRD (OE) — EXAM POINTS (understandable)",styles["T"]),
           Paragraph("Short concept + points you can expand in the hall",styles["S"]),
           Paragraph("How to write 8 marks: 4-line intro from the concept box → 6–8 numbered points (each 5–8 handwritten lines + tiny example) → 3-line conclusion.",styles["N"])]
    cur=None
    titles={1:"UNIT 1  Q1–20  Concept, climate, roles",2:"UNIT 2  Q21–40  HRD system & subsystems",3:"UNIT 3  Q41–60  Training cycle & Kirkpatrick"}
    for n,u,title,idea,pts in Q:
        if u!=cur:
            cur=u
            story+=[Spacer(1,6),banner(titles[u]),Spacer(1,5)]
        block=[Paragraph(f"Q{n}. {esc(title)}",styles["QH"]),
               Paragraph(f"<b>Concept.</b> {esc(idea)}",styles["I"])]
        for i,b in enumerate(pts,1):
            block.append(Paragraph(f"<b>{i}.</b> {esc(b)}",styles["B"]))
        story.append(KeepTogether(block))
    doc.build(story,onFirstPage=hf,onLaterPages=hf)
    print("pdf",out)

def build_html():
    parts=["""<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"/><meta name="viewport" content="width=device-width,initial-scale=1"/>
<title>HRD Exam Points</title>
<style>
body{font-family:Georgia,serif;background:#efe8d8;margin:0;color:#1a202c}
header{background:#1a365d;color:#fff;padding:14px;text-align:center;position:sticky;top:0;z-index:2}
h1{margin:0;font-size:1.25rem} .sub{margin:6px 0 0;font-size:.88rem;opacity:.95}
nav a{color:#fff;margin:0 8px;font-size:.85rem}
main{max-width:840px;margin:14px auto 48px;padding:0 12px}
.note{background:#fff;border-left:4px solid #c9a227;padding:10px 12px;margin-bottom:12px;font-size:.95rem}
.ub{background:#0d7377;color:#fff;text-align:center;padding:8px;border-radius:6px;margin:16px 0 8px;font-weight:700}
.q{background:#fffdf6;border:1px solid #e4d8bc;border-radius:8px;padding:12px 14px;margin:10px 0}
.q h2{margin:0 0 6px;font-size:1.02rem;color:#1a365d}
.idea{font-style:italic;color:#2d4a4a;margin:0 0 8px;line-height:1.45}
ol{margin:0;padding-left:20px} li{margin:3px 0;line-height:1.45}
</style></head><body>
<header><h1>HRD (OE) — Exam points you can understand</h1>
<p class="sub">Concept in italics. Then points — expand each to 5–8 lines in the answer book.</p>
<nav><a href="#u1">Unit 1</a><a href="#u2">Unit 2</a><a href="#u3">Unit 3</a></nav></header><main>
<div class="note"><b>Yap kit:</b> Nadler 1969 organised learning → behaviour change. T.V. Rao: present/future roles + potential + teamwork culture.
OCTAPAC climate. Need = standard − actual <i>only if</i> skill gap. Cycle TNA → design → delivery → eval. Kirkpatrick 1 reaction 2 learning 3 behaviour 4 results.</div>
"""]
    cur=None
    ids={1:"u1",2:"u2",3:"u3"}
    titles={1:"UNIT 1 — Q1–20",2:"UNIT 2 — Q21–40",3:"UNIT 3 — Q41–60"}
    for n,u,title,idea,pts in Q:
        if u!=cur:
            cur=u
            parts.append(f'<div class="ub" id="{ids[u]}">{titles[u]}</div>')
        lis="".join(f"<li>{htmllib.escape(b)}</li>" for b in pts)
        parts.append(f'<article class="q"><h2>Q{n}. {htmllib.escape(title)}</h2><p class="idea">{htmllib.escape(idea)}</p><ol>{lis}</ol></article>')
    parts.append("</main></body></html>")
    open("/home/user/HRD/HRD_Exam_Points_Only.html","w",encoding="utf-8").write("".join(parts))
    print("html ok")

if __name__=="__main__":
    build_pdf(); build_html()
