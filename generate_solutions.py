#!/usr/bin/env python3
"""Generate HRD Question Bank solutions PDF (8-mark, point-wise)."""
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch, mm
from reportlab.lib.colors import HexColor, white, black
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak, ListFlowable, ListItem,
    KeepTogether, HRFlowable, Table, TableStyle
)
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT, TA_RIGHT

OUT = "/home/user/HRD/HRD_QB_Solutions_8Marks.pdf"

NAVY = HexColor("#1a365d")
TEAL = HexColor("#0d7377")
GOLD = HexColor("#c9a227")
LIGHT = HexColor("#f4f7fb")
GRAY = HexColor("#4a5568")

def header_footer(canvas, doc):
    canvas.saveState()
    w, h = A4
    canvas.setFillColor(NAVY)
    canvas.rect(0, h - 18, w, 18, fill=1, stroke=0)
    canvas.setFillColor(white)
    canvas.setFont("Times-Bold", 8)
    canvas.drawString(20 * mm, h - 13, "HRD (OE)  |  Question Bank Solutions  |  8 Marks each")
    canvas.drawRightString(w - 20 * mm, h - 13, "Point-wise Theoretical Answers")
    canvas.setFillColor(NAVY)
    canvas.rect(0, 0, w, 16, fill=1, stroke=0)
    canvas.setFillColor(white)
    canvas.setFont("Times-Roman", 8)
    canvas.drawString(20 * mm, 6, "Human Resource Development  —  Open Elective")
    canvas.drawRightString(w - 20 * mm, 6, f"Page {doc.page}")
    canvas.restoreState()


styles = getSampleStyleSheet()
styles.add(ParagraphStyle(
    name="CoverTitle", fontName="Times-Bold", fontSize=22, leading=26,
    alignment=TA_CENTER, textColor=NAVY, spaceAfter=8
))
styles.add(ParagraphStyle(
    name="CoverSub", fontName="Times-Italic", fontSize=12, leading=16,
    alignment=TA_CENTER, textColor=TEAL, spaceAfter=6
))
styles.add(ParagraphStyle(
    name="QHead", fontName="Times-Bold", fontSize=12, leading=16,
    textColor=NAVY, spaceBefore=10, spaceAfter=4
))
styles.add(ParagraphStyle(
    name="QText", fontName="Times-Bold", fontSize=11, leading=15,
    textColor=HexColor("#1a202c"), spaceAfter=6, alignment=TA_JUSTIFY
))
styles.add(ParagraphStyle(
    name="Meta", fontName="Times-Italic", fontSize=9, leading=12,
    textColor=TEAL, spaceAfter=8
))
styles.add(ParagraphStyle(
    name="Body", fontName="Times-Roman", fontSize=10.5, leading=14.5,
    alignment=TA_JUSTIFY, textColor=black, spaceAfter=3
))
styles.add(ParagraphStyle(
    name="PtBullet", fontName="Times-Roman", fontSize=10.5, leading=14.5,
    alignment=TA_JUSTIFY, textColor=black, leftIndent=14, firstLineIndent=0,
    spaceAfter=5, spaceBefore=1
))
styles.add(ParagraphStyle(
    name="Conc", fontName="Times-Italic", fontSize=10.5, leading=14.5,
    alignment=TA_JUSTIFY, textColor=GRAY, spaceBefore=6, spaceAfter=8
))
styles.add(ParagraphStyle(
    name="Sec", fontName="Times-Bold", fontSize=14, leading=18,
    textColor=white, alignment=TA_CENTER
))
styles.add(ParagraphStyle(
    name="Intro", fontName="Times-Roman", fontSize=11, leading=15,
    alignment=TA_JUSTIFY, spaceAfter=8
))

# Each item: (qno, unit, question, intro, [bullets], conclusion)
QA = []

def add(n, u, q, intro, pts, conc):
    QA.append((n, u, q, intro, pts, conc))

# ========== UNIT 1 ==========
add(1, 1,
"Explain the concept of Human Resource Development (HRD) and state its major objectives.",
"Human Resource Development (HRD) is a planned, continuous organisational process that helps employees acquire capabilities, realise potential, and build a culture of collaboration. Leonard Nadler (1969) defined HRD as organised learning experiences, conducted within a specified time, designed to produce behavioural change. Prof. T.V. Rao described HRD as a process by which employees are helped in a continuous and planned way to develop role-related and general capabilities and a healthy work culture.",
[
"<b>Capability for present and future roles:</b> HRD aims to help employees acquire or sharpen knowledge, skills and attitudes needed for current jobs and expected future roles.",
"<b>Development of inner potential:</b> A major objective is to help individuals discover and use their potential for personal growth as well as organisational development.",
"<b>Culture building:</b> HRD seeks a culture of strong superior–subordinate relations, teamwork and collaboration among units, contributing to motivation and professional pride.",
"<b>Continuous planned learning:</b> Unlike one-off training, HRD is ongoing. Mechanisms such as appraisal, counselling, training and OD are used to keep the process alive.",
"<b>Individual, dyad, group and organisation:</b> Development covers the person, the boss–subordinate pair, teams/committees, departments and the whole organisation.",
"<b>Enabling climate:</b> HRD aims to create a climate that identifies, nurtures and uses human potential, because unlike other resources people have relatively unlimited capability.",
"<b>Performance and growth orientation:</b> Objectives include higher individual effectiveness, organisational dynamism, adaptability and long-term competitiveness.",
"<b>Formal and informal modes:</b> Classroom training, coaching, mentoring, career development, succession planning and OD interventions all serve HRD objectives.",
],
"Thus, HRD is not merely training; it is a philosophy and process that develops people, climate and organisation together so that both individual and organisational goals are achieved.")

add(2, 1,
"Describe the evolution of Human Resource Development from traditional employee training to a strategic organisational function.",
"HRD evolved from welfare and training activities into a strategic function linked to business goals, culture and competitive advantage.",
[
"<b>Welfare and personnel era:</b> Early industrial organisations emphasised welfare, discipline, record-keeping and industrial relations. Development of people was incidental.",
"<b>Training as a discrete activity:</b> After World War II and with scientific management, organisations ran job-skill training. Learning was short-term, job-specific and often isolated from strategy.",
"<b>Nadler’s HRD concept (1969):</b> Leonard Nadler introduced HRD as organised learning for behavioural change, widening the field beyond classroom instruction to development and education.",
"<b>T.V. Rao and Indian HRD movement:</b> In India, HRD was institutionalised as a system of appraisal, feedback, potential appraisal, career planning, training and OD, especially after the 1970s–80s.",
"<b>From maintenance to development:</b> HRM remained largely maintenance-oriented (staffing, compensation, IR). HRD became development-oriented, focusing on competence, climate and culture.",
"<b>Integration with organisational strategy:</b> Later, HRD was expected to support change, quality, technology and global competition. Training needs, career paths and talent pipelines were aligned with strategy.",
"<b>Strategic HRD:</b> Today HRD includes competency mapping, leadership pipelines, learning organisations, knowledge management and human capital. HRD professionals advise top management on capability building.",
"<b>Line-manager partnership:</b> Evolution also shifted responsibility from the training cell alone to all managers, making development a shared strategic duty.",
],
"The journey from isolated training to strategic HRD reflects the recognition that people capability is a core source of organisational effectiveness and long-term survival.")

add(3, 1,
"Explain the relationship between Human Resource Development and Human Resource Management.",
"HRM and HRD are related but not identical. HRM is the broader management of people; HRD is the developmental subset (and philosophy) within or alongside HRM.",
[
"<b>HRM as umbrella:</b> HRM covers procurement, compensation, industrial relations, welfare, compliance and development. HRD specifically deals with training, career, potential, climate and learning.",
"<b>Maintenance vs development:</b> HRM is largely maintenance-oriented (keeping the system running). HRD is development-oriented (growing people and the organisation).",
"<b>Structure:</b> HRM structures tend to be independent functional units. HRD requires interdependent, inter-related structures because development cuts across departments.",
"<b>Aims:</b> HRM emphasises efficiency, utilisation and control of human resources. HRD emphasises employee growth plus organisational effectiveness.",
"<b>Responsibility:</b> HRM is typically the personnel/HR department’s job. HRD responsibility rests with all managers at all levels, supported by HRD specialists.",
"<b>Motivation:</b> HRM often uses monetary incentives. HRD stresses higher-order needs—recognition, achievement, learning and self-actualisation.",
"<b>Complementarity:</b> Sound HRM policies (fair pay, security) create conditions in which HRD can work. HRD in turn improves the quality of HRM outcomes (performance, retention, succession).",
"<b>Strategic linkage:</b> Modern strategic HRM treats HRD as a key lever: without HRD, HRM cannot build a future-ready workforce.",
],
"Hence HRD and HRM are interdependent: HRM provides the employment framework; HRD develops people within that framework toward organisational goals.")

add(4, 1,
"Discuss the importance of HRD in improving individual and organisational performance.",
"HRD improves performance by building competence, motivation, climate and alignment between people and goals.",
[
"<b>Skill and knowledge enhancement:</b> Training, coaching and job experiences close performance gaps (standard minus actual) and raise job proficiency.",
"<b>Role clarity through appraisal and feedback:</b> Developmental appraisal and counselling help employees know expectations and how to improve.",
"<b>Motivation and morale:</b> Growth opportunities, recognition of potential and a supportive climate increase commitment and discretionary effort.",
"<b>Better utilisation of potential:</b> Potential appraisal and career planning place people in roles where they can contribute more.",
"<b>Teamwork and collaboration:</b> HRD culture strengthens dyads and teams, improving coordination and decision quality—key to organisational performance.",
"<b>Adaptability and innovation:</b> An enabling culture encourages initiative, experimentation and learning, which organisations need in changing environments.",
"<b>Reduced waste of human capital:</b> Without HRD, capability remains unused; with HRD, human resources (unlike other resources) can expand in value.",
"<b>Strategic capability:</b> Integrated HRD supports quality, customer service, leadership pipelines and long-term competitiveness, not only short-term output.",
],
"Therefore HRD is important because individual competence and a developmental climate together raise organisational performance in a sustainable way.")

add(5, 1,
"Explain the concept of HRD climate and identify the major characteristics of a supportive HRD climate.",
"HRD climate is the general feeling, atmosphere and practices in an organisation that indicate how much it values people and their development. It is a subset of organisational climate, focused on openness, trust, authenticity, proactivity, autonomy, confrontation and collaboration (OCTAPAC-related values popularised in Indian HRD literature).",
[
"<b>Openness:</b> Employees can share ideas, feelings and feedback without fear. Communication is two-way.",
"<b>Trust and authenticity:</b> People believe management’s intentions and behave genuinely rather than politically.",
"<b>Confrontation of problems:</b> Issues are discussed and solved rather than avoided or blamed.",
"<b>Autonomy and proactivity:</b> Employees have reasonable freedom and are encouraged to take initiative and experiment.",
"<b>Collaboration and teamwork:</b> Help-seeking and help-giving across levels and units are normal.",
"<b>Support from top management:</b> Leaders invest time and resources in development and model learning behaviour.",
"<b>Fair developmental practices:</b> Appraisal, training opportunities and career support are perceived as just and available.",
"<b>Recognition of development:</b> Learning, mentoring and improvement are rewarded, not only short-term results.",
],
"A supportive HRD climate is thus open, trusting, developmental and collaborative; it is the soil in which HRD mechanisms actually work.")

add(6, 1,
"Differentiate between HRD climate and organisational culture with suitable examples.",
"Climate and culture are related but distinct. Culture is deeper and more enduring; climate is the current, felt atmosphere that employees experience.",
[
"<b>Definition:</b> Organisational culture is shared values, beliefs, assumptions and symbols (e.g., ‘customers first’, hierarchy, innovation). HRD climate is the perceived environment for learning, trust, openness and development.",
"<b>Depth:</b> Culture is deep and often unconscious. Climate is more surface-level and can be surveyed as current perceptions.",
"<b>Stability:</b> Culture changes slowly. HRD climate can improve or worsen relatively faster with leadership and HR practices.",
"<b>Scope:</b> Culture covers all organisational life (power, rituals, stories). HRD climate specifically concerns development, feedback, collaboration and growth.",
"<b>Example – culture:</b> A family-owned firm may have a paternalistic culture of loyalty and seniority. That is culture.",
"<b>Example – climate:</b> In the same firm, if bosses regularly coach juniors, share feedback and sponsor training, the HRD climate is supportive even within that culture.",
"<b>Example of mismatch:</b> An organisation may proclaim a ‘learning culture’ in vision statements, yet employees may report a poor HRD climate if appraisals are punitive and training is denied.",
"<b>Implication:</b> HRD interventions must respect culture while deliberately shaping climate; ignoring culture makes climate programmes cosmetic.",
],
"In short, culture is ‘who we are’; HRD climate is ‘how developmental it feels to work here now’. Both must be aligned for HRD success.")

add(7, 1,
"Explain the role and responsibilities of an HRD professional in an organisation.",
"An HRD professional designs, facilitates and evaluates learning and development systems, and acts as a partner to line managers and top management.",
[
"<b>Diagnosing development needs:</b> Identifying individual, team and organisational capability gaps through TNA, climate surveys and performance data.",
"<b>Designing HRD systems:</b> Structuring appraisal, potential appraisal, training, career planning, feedback, counselling and OD so they work as one system.",
"<b>Facilitating learning:</b> Arranging training, coaching, mentoring and on-the-job learning; not doing all teaching personally but enabling it.",
"<b>Culture and climate building:</b> Promoting OCTAPAC values, trust and collaboration through interventions and role modelling.",
"<b>Advisor and change agent:</b> Helping management handle change, technology, quality and restructuring by preparing people.",
"<b>Developing line managers as developers:</b> Training bosses to appraise, counsel and coach, because HRD is every manager’s job.",
"<b>Evaluation and HRD audit:</b> Checking whether mechanisms actually develop people and contribute to business results.",
"<b>Ethical stewardship:</b> Ensuring fairness in opportunities, confidentiality in counselling, and respect for employee dignity.",
],
"The HRD professional is therefore a system designer, facilitator, consultant and conscience-keeper of people development, not merely a training administrator.")

add(8, 1,
"Discuss the significance of HRD for achieving organisational effectiveness and long-term employee development.",
"Organisational effectiveness (goal achievement, adaptability, health) and long-term employee development are two sides of the same HRD coin.",
[
"<b>Competence as a performance driver:</b> Effective organisations need skilled, motivated people; HRD continuously upgrades competence.",
"<b>Enabling culture:</b> Effectiveness requires initiative, innovation and teamwork—outcomes of a strong HRD climate.",
"<b>Alignment with goals:</b> HRD links individual development plans to organisational strategy so effort is not wasted.",
"<b>Leadership pipeline:</b> Career planning, potential appraisal and succession ensure long-term continuity of effectiveness.",
"<b>Employee growth beyond the present job:</b> Long-term development covers general capabilities, not only current task skills, preparing people for future roles.",
"<b>Retention and commitment:</b> Employees stay and contribute when they see a future; HRD reduces turnover costs and knowledge loss.",
"<b>Renewal capability:</b> Even stable organisations must adapt; HRD provides processes of learning and renewal.",
"<b>Humanistic and economic value:</b> HRD treats people as assets with unlimited potential, which is both ethically sound and economically productive.",
],
"Hence HRD is significant because organisational effectiveness cannot be sustained without systematic, long-term development of employees.")

add(9, 1,
"A growing organisation is facing skill gaps and declining employee performance. Suggest an HRD-oriented approach to address these issues.",
"An HRD-oriented approach treats skill gaps and falling performance as development problems, not only control or punishment problems.",
[
"<b>Diagnose systematically:</b> Conduct organisation, task and person analysis. Separate skill gaps from motivation, process or resource problems.",
"<b>Strengthen HRD climate:</b> Restore trust, feedback and support so employees will admit gaps and learn. Punitive climate hides problems.",
"<b>Developmental performance appraisal:</b> Use appraisal to identify specific KSA gaps and agree on improvement plans, not only to rate people.",
"<b>Targeted training and on-the-job learning:</b> Design training from TNA; combine coaching, job rotation and formal programmes.",
"<b>Counselling and feedback:</b> Managers should counsel poor performers, set goals and review progress.",
"<b>Career and potential focus:</b> For a growing firm, map future roles and start developing people for expansion, not only current jobs.",
"<b>Involve line managers:</b> Make every supervisor responsible for developing their team; HRD specialist supports them.",
"<b>Evaluate and iterate:</b> Measure behaviour and results (Kirkpatrick-type evaluation), then refine interventions.",
],
"This HRD approach closes skill gaps through diagnosis, climate, appraisal, learning and follow-up, which is more sustainable than hiring or firing alone.")

add(10, 1,
"Apply the concept of HRD climate to suggest measures for creating a learning-oriented work environment.",
"A learning-oriented environment is a practical expression of a supportive HRD climate. Measures should shape day-to-day experience of openness, trust and development.",
[
"<b>Top-management modelling:</b> Leaders should share their own learning, admit mistakes and sponsor development visibly.",
"<b>Psychological safety:</b> Encourage questions, experiments and reporting of errors without humiliation.",
"<b>Regular developmental feedback:</b> Replace once-a-year judgment with frequent coaching conversations.",
"<b>Time and resources for learning:</b> Budget, learning hours, libraries/e-learning and permission to practise new skills on the job.",
"<b>Team learning forums:</b> After-action reviews, quality circles, mentoring pairs and cross-functional projects.",
"<b>Fair access:</b> Training and stretch assignments should not be limited to favourites; equity builds climate.",
"<b>Recognition of learning:</b> Reward knowledge sharing, mentoring and improvement, not only individual heroics.",
"<b>Align systems:</b> Appraisal, promotion and job design should value collaboration and capability growth.",
],
"These measures convert HRD climate from a slogan into daily practices that make the workplace a learning system.")

add(11, 1,
"State any two objectives of Human Resource Development.",
"HRD has several objectives; two core ones (with explanation suitable for an 8-mark theoretical answer) are highlighted and supported by related points.",
[
"<b>Objective 1 – Develop role-related capabilities:</b> Help employees acquire or sharpen skills and knowledge for present and future roles (T.V. Rao).",
"<b>Explanation:</b> This includes induction, job training, multi-skilling and preparation for expected responsibilities.",
"<b>Objective 2 – Develop general capabilities and potential:</b> Help individuals discover inner potential for their own and the organisation’s development.",
"<b>Explanation:</b> This goes beyond the current job to personality, leadership and career growth.",
"<b>Related objective – culture:</b> Build superior–subordinate relations, teamwork and collaboration.",
"<b>Related objective – climate:</b> Create an enabling climate that continuously identifies and uses human potential.",
"<b>Related objective – organisational dynamism:</b> Make the organisation adaptive and growth-oriented through people.",
"<b>Related objective – behavioural change:</b> Nadler’s aim of organised learning leading to changed behaviour on the job.",
],
"Any two of the above may be stated as primary objectives; together they show HRD’s dual concern for people and the organisation.")

add(12, 1,
"State any two ways in which HRD and HRM are related.",
"HRD and HRM are distinct yet closely related parts of managing people.",
[
"<b>Relation 1 – HRD as a core function within HRM:</b> Training, development, career and performance development are developmental activities of the HRM function.",
"<b>Explanation:</b> HRM cannot achieve utilisation of people without developing them.",
"<b>Relation 2 – Complementary aims:</b> HRM provides employment conditions (pay, staffing, IR); HRD develops competence and climate so those people perform and grow.",
"<b>Shared concern for people:</b> Both deal with human resources; they differ in emphasis (maintenance vs development).",
"<b>Policy linkage:</b> Promotion, transfer, reward and appraisal policies of HRM must support HRD, or development fails.",
"<b>Shared responsibility with line managers:</b> Modern HRM and HRD both require line ownership.",
"<b>Strategic HRM uses HRD:</b> Capability building is a strategic HRM tool implemented through HRD systems.",
"<b>Data linkage:</b> HRM information (manpower plans, appraisals) feeds HRD decisions (training, succession).",
],
"Thus HRD and HRM are related as overlapping, mutually dependent systems focused on people, with HRD supplying the developmental engine.")

add(13, 1,
"Analyse how a weak HRD climate can affect employee behaviour and organisational performance.",
"A weak HRD climate (low trust, closed communication, little support for learning) systematically distorts behaviour and damages results.",
[
"<b>Fear and silence:</b> Employees hide mistakes and withhold ideas, so problems grow and innovation falls.",
"<b>Low initiative:</b> Without autonomy and support, people wait for orders; proactivity and ownership decline.",
"<b>Poor learning transfer:</b> Even good training fails because the workplace does not allow practice or coaching.",
"<b>Defensive appraisal behaviour:</b> Ratings become political; feedback is rejected or never given honestly.",
"<b>Reduced collaboration:</b> Units compete or blame each other; teamwork and quality of decisions suffer.",
"<b>Demotivation and withdrawal:</b> Higher-order needs are frustrated; absenteeism, turnover and inner resignation rise.",
"<b>Wasted human potential:</b> Capabilities are neither identified nor used; the organisation stagnates despite hiring.",
"<b>Performance decline:</b> Combined effect is lower productivity, poorer customer outcomes and weak adaptability—directly hitting organisational performance.",
],
"Therefore a weak HRD climate is not a ‘soft’ issue; it is a performance risk because behaviour follows climate.")

add(14, 1,
"Analyse the changing role of an HRD professional as organisations move from traditional personnel administration toward strategic human resource development.",
"The HRD role has shifted from administrative trainer to strategic business partner and change agent.",
[
"<b>From record-keeper to diagnostician:</b> Earlier focus on training calendars and files; now diagnosis of capability versus strategy.",
"<b>From classroom organiser to learning architect:</b> Designing blended, on-the-job, coaching and e-learning systems, not only courses.",
"<b>From isolated training cell to integrator:</b> Linking appraisal, potential, career, feedback and OD into one HRD system.",
"<b>Business literacy:</b> The professional must understand markets, technology and strategy to align development.",
"<b>Partner to line and top management:</b> Influencing decisions on structure, culture and talent, not waiting for training requests.",
"<b>Change and OD role:</b> Facilitating mergers, digitalisation and culture change through people processes.",
"<b>Metrics and accountability:</b> Using evaluation, climate surveys and HRD audit to show impact, not activity counts.",
"<b>Ethical and employee-advocate role:</b> Balancing organisational strategy with employee growth and fairness—more complex than old personnel welfare.",
],
"The changing role demands higher competence: consulting, analytics, facilitation and strategic thinking, far beyond traditional personnel administration.")

add(15, 1,
"Analyse the relationship among HRD philosophy, HRD climate, and organisational performance.",
"Philosophy, climate and performance form a causal chain. Philosophy shapes practices; practices shape climate; climate shapes behaviour and thus performance.",
[
"<b>HRD philosophy:</b> Belief that people have potential, deserve development, and that development is a managerial duty—not a cost to minimise.",
"<b>Philosophy drives mechanisms:</b> If philosophy is genuine, appraisal is developmental, training is need-based, and bosses counsel rather than only control.",
"<b>Mechanisms create climate:</b> Consistent practices produce perceptions of openness, trust and support (HRD climate).",
"<b>Climate shapes behaviour:</b> Employees take initiative, learn, collaborate and persist when climate is supportive.",
"<b>Behaviour produces performance:</b> Quality, productivity, innovation and customer service improve.",
"<b>Reverse effect:</b> High performance can reinforce philosophy (‘investment in people pays’). Poor results with no reflection may wrongly kill HRD budgets.",
"<b>Inconsistency problem:</b> Stated philosophy without matching climate (e.g., slogans vs punitive bosses) creates cynicism and hurts performance.",
"<b>Strategic implication:</b> Sustainable performance requires all three: believed philosophy, felt climate, and results—not isolated training events.",
],
"Hence organisational performance is strongest when a true HRD philosophy is lived as climate, not merely written in HR manuals.")

add(16, 1,
"Evaluate whether HRD should be treated as a strategic function rather than only as an employee training activity.",
"Evaluation supports treating HRD as strategic. Training is necessary but insufficient.",
[
"<b>Limited view of training:</b> Training is one mechanism, usually short-term and job-specific. HRD also includes potential, career, climate, OD and culture.",
"<b>Strategic contribution:</b> Capability, leadership pipelines and learning agility are sources of competitive advantage—strategic issues.",
"<b>Alignment need:</b> Without strategy linkage, training may be popular yet irrelevant (activity without impact).",
"<b>Evidence from evolution:</b> Organisations that remain at ‘calendar training’ fail to handle change; those that integrate HRD with strategy adapt better.",
"<b>Counter-argument:</b> Some firms see HRD as a cost centre and prefer buying short courses. This may work for simple skill gaps but not for culture or leadership.",
"<b>Risk of over-claiming:</b> Calling HRD ‘strategic’ without metrics or CEO support is empty. Strategy status must be earned through diagnosis and results.",
"<b>Balanced evaluation:</b> Training remains a core tool; the evaluation is not to abolish training but to nest it inside a strategic HRD system.",
"<b>Conclusion of evaluation:</b> Yes—HRD should be a strategic function, with training as one subsystem, because people capability determines long-term organisational success.",
],
"Therefore HRD must be positioned and resourced as a strategic function, while retaining excellence in training as one of its instruments.")

add(17, 1,
"Identify any two indicators of a supportive HRD climate.",
"Indicators are observable signs that the climate supports development. Two primary indicators are elaborated with supporting points.",
[
"<b>Indicator 1 – Openness and free feedback:</b> Employees can discuss problems with superiors; feedback is regular, two-way and used for improvement.",
"<b>Behavioural signs:</b> Meetings allow dissent; mistakes are analysed; suggestion schemes are used.",
"<b>Indicator 2 – Management support for development:</b> Time, budget and sponsorship for training, coaching and career discussions are visible.",
"<b>Behavioural signs:</b> Bosses release people for learning; development is discussed in appraisals.",
"<b>Other valid indicators:</b> Trust, authenticity, autonomy, collaboration, confrontation of issues, and recognition of learners/mentors.",
"<b>Teamwork:</b> Cross-unit help and low inter-departmental hostility indicate collaborative climate.",
"<b>Fairness:</b> Equitable access to opportunities indicates a healthy climate.",
"<b>Proactivity:</b> Employees taking initiative without fear is a strong climate indicator.",
],
"Any two such indicators, explained with workplace signs, demonstrate a supportive HRD climate.")

add(18, 1,
"State any two reasons why an HRD professional needs to understand organisational culture.",
"Culture is the context in which HRD mechanisms succeed or fail; hence the professional must understand it.",
[
"<b>Reason 1 – Fit of interventions:</b> Training, appraisal and OD must fit existing values. A highly hierarchical culture will reject blunt 360-degree feedback unless adapted.",
"<b>Explanation:</b> Culture-blind HRD creates resistance and wasted investment.",
"<b>Reason 2 – Climate vs culture gap:</b> The professional must know deep culture to interpret climate survey results and to change climate realistically.",
"<b>Change management:</b> Culture knowledge helps sequence change—what to preserve, what to challenge.",
"<b>Communication:</b> Messages about development must use the organisation’s language, stories and heroes.",
"<b>Power and politics:</b> Culture reveals who must sponsor HRD for it to be legitimate.",
"<b>Ethics and inclusion:</b> Understanding subcultures (functions, regions, generations) prevents one-size-fits-all programmes.",
"<b>Strategy alignment:</b> Desired culture (e.g., innovation) tells HRD which competencies and behaviours to develop.",
],
"Thus understanding culture is essential for designing acceptable, effective and ethical HRD, not optional background knowledge.")

add(19, 1,
"Evaluate the likely consequences of implementing HRD practices without considering the existing organisational culture and climate.",
"Implementing HRD in a culture/climate vacuum typically produces failure, cynicism and sometimes harm.",
[
"<b>Rejection of practices:</b> Forced openness or 360-degree feedback in a closed, fear-based climate is seen as a trap; people give fake data.",
"<b>Ritualism:</b> Appraisal forms and training attendance occur, but no behavioural change—HRD becomes a ritual.",
"<b>Cynicism:</b> Employees conclude that management is hypocritical, damaging trust further.",
"<b>Wasted resources:</b> High training spend with no transfer because climate does not support application.",
"<b>Conflict:</b> New HRD values (autonomy, confrontation) clash with old culture (obedience, avoidance), creating role stress.",
"<b>Inequity and politics:</b> Without climate fairness, development opportunities are captured by in-groups.",
"<b>Possible short-term optics:</b> A few visible programmes may impress outsiders, but evaluation at behaviour and results levels will fail.",
"<b>Evaluative conclusion:</b> Consequences are predominantly negative. HRD practices must be sequenced with climate-building and culture-sensitive design.",
],
"Evaluation shows that HRD without culture and climate analysis is likely to be ineffective and may worsen trust; diagnosis must precede design.")

add(20, 1,
"Design a basic HRD framework for an organisation that wants to improve employee capability while aligning development efforts with organisational goals.",
"A basic HRD framework links organisational strategy to people systems and to results.",
[
"<b>1. HRD philosophy and policy:</b> State that people development is strategic; assign responsibility to all managers, with an HRD cell as facilitator.",
"<b>2. Strategy and competency translation:</b> Convert organisational goals into required competencies for roles and future roles.",
"<b>3. HRD subsystems:</b> Interlinked performance appraisal, potential appraisal, training, career planning, feedback and counselling.",
"<b>4. Climate building:</b> OCTAPAC-oriented practices, top-management support, and learning time.",
"<b>5. Need diagnosis:</b> Organisation, task and person analysis so capability building is evidence-based.",
"<b>6. Development interventions:</b> Mix of on-the-job learning, formal training, mentoring and OD for teams.",
"<b>7. Alignment mechanisms:</b> Individual development plans reviewed against business goals; succession for critical roles.",
"<b>8. Evaluation and audit:</b> Reaction to results, climate surveys, and periodic HRD audit to improve the system.",
],
"This framework ensures capability improvement is not random training but a closed-loop system aligned with organisational goals.")

# ========== UNIT 2 ==========
add(21, 2,
"Explain the structure of an HRD system and describe its major components.",
"An HRD system is an integrated set of subsystems and processes designed to develop individuals, dyads, teams and the organisation. Structure means how these parts are arranged and linked, not a mere list of training courses.",
[
"<b>HRD philosophy and goals:</b> The foundation—beliefs about people and the aims of development.",
"<b>Performance appraisal:</b> Periodic assessment used for development (strengths, gaps, goals), not only for rewards.",
"<b>Potential appraisal:</b> Assessment of future capability for higher or different roles.",
"<b>Training and development:</b> Planned learning to close gaps and prepare for future work.",
"<b>Career planning and development:</b> Matching individual aspirations with organisational paths.",
"<b>Feedback and counselling:</b> Dialogue that turns appraisal data into insight and action.",
"<b>OD and climate mechanisms:</b> Team building, culture work, employee surveys—system-level development.",
"<b>Supporting structure:</b> HRD staff, line-manager roles, information system, and links to HRM (rewards, placement). Components must be interrelated so data from one feeds another.",
],
"A well-structured HRD system is therefore a network of subsystems around a developmental philosophy, not isolated HR activities.")

add(22, 2,
"Explain performance appraisal as an HRD subsystem and state its importance for employee development.",
"As an HRD subsystem, performance appraisal is a developmental process of reviewing results and behaviours, identifying learning needs, and planning improvement—not merely a confidential rating for salary.",
[
"<b>Role analysis and goal setting:</b> Clarifies what is expected, which is the starting point of development.",
"<b>Identification of strengths and gaps:</b> Appraisal data feed training needs and coaching agendas.",
"<b>Feedback:</b> Employees cannot improve what they do not understand; appraisal institutionalises feedback.",
"<b>Development planning:</b> Jointly agreed IDPs (individual development plans) convert appraisal into action.",
"<b>Motivation:</b> Recognition of achievement and a fair review process support higher-order motivation.",
"<b>Data for other subsystems:</b> Feeds potential appraisal, career moves, and training calendars.",
"<b>Manager as developer:</b> The appraisal discussion trains bosses to take HRD responsibility.",
"<b>Importance:</b> Without developmental appraisal, HRD lacks a regular, organisation-wide mechanism to diagnose and guide employee growth.",
],
"Thus performance appraisal is central to HRD because it continuously connects actual work to learning and future capability.")

add(23, 2,
"Describe training as an HRD subsystem and explain how it contributes to employee development.",
"Training is a planned organisational effort to help employees learn job-related competencies. Within HRD it is one subsystem, linked to needs from appraisal and to career/potential plans.",
[
"<b>Need-based learning:</b> Training should follow TNA so it develops real deficiencies, not generic topics.",
"<b>Skill, knowledge and attitude:</b> It contributes at all three levels required for role performance.",
"<b>Present-job effectiveness:</b> Improves current performance (training need = standard − actual).",
"<b>Preparation for change:</b> New technology, quality systems and products require training as a development tool.",
"<b>Confidence and morale:</b> Mastery experiences increase self-efficacy and job satisfaction.",
"<b>Link to career:</b> Training for future roles (e.g., supervisory skills) is developmental, not only remedial.",
"<b>Socialisation:</b> Induction training develops organisational understanding and culture fit.",
"<b>Limits:</b> Training alone does not develop people if climate, appraisal and job design do not allow transfer—hence it must stay a subsystem, not the whole HRD.",
],
"Training contributes to employee development by systematically building competencies, provided it is integrated with other HRD subsystems.")

add(24, 2,
"Explain career planning and potential appraisal as HRD subsystems.",
"Career planning and potential appraisal look forward. They develop people for tomorrow’s roles, complementing performance appraisal which looks mainly at yesterday and today.",
[
"<b>Potential appraisal – meaning:</b> Systematic judgement of an employee’s capability to take up higher or different responsibilities, using tools such as review discussions, assessment centres, and psychological tests where appropriate.",
"<b>Purpose:</b> Identify talent, avoid promoting only on current-job performance (the ‘Peter Principle’ risk), and guide development investments.",
"<b>Career planning – meaning:</b> A joint process of mapping possible paths (vertical, lateral, specialist) and the experiences/skills needed.",
"<b>Individual side:</b> Helps employees understand options, aspirations and development actions.",
"<b>Organisational side:</b> Ensures succession, reduces vacancy risk, and aligns talent with strategy.",
"<b>Interrelation:</b> Potential data inform career moves; career plans specify training, job rotation and mentoring.",
"<b>Counselling link:</b> Career counselling prevents unrealistic expectations and frustration.",
"<b>HRD contribution:</b> Together they institutionalise long-term employee development rather than ad-hoc promotions.",
],
"Career planning and potential appraisal are therefore forward-looking HRD subsystems that build a talent pipeline and meaningful employee growth.")

add(25, 2,
"Explain the role of feedback and counselling in an HRD system.",
"Feedback and counselling convert data (appraisal, potential, training results) into understanding and behavioural change. They are the human process that makes other subsystems work.",
[
"<b>Feedback – information for improvement:</b> Specific, timely, behaviour-focused information on what was effective and what was not.",
"<b>Two-way nature:</b> Employees also feed back on resources, role clarity and support needed.",
"<b>Counselling – helping relationship:</b> A manager or counsellor helps the employee explore problems, feelings, career issues and action plans in a confidential, respectful setting.",
"<b>Link to appraisal:</b> Without a counselling discussion, appraisal is a form, not development.",
"<b>Motivation and trust:</b> Skilled counselling builds HRD climate; harsh or absent feedback destroys it.",
"<b>Corrective and developmental:</b> Addresses performance problems early and also stretches high performers.",
"<b>Career counselling:</b> Aligns aspirations with organisational reality.",
"<b>Skill requirement:</b> Listening, empathy, confrontation of issues, and goal setting—HRD must train managers in these skills.",
],
"Feedback and counselling are the heart of an HRD system because development happens through dialogue, not through forms alone.")

add(26, 2,
"Describe the major principles for designing effective HRD practices.",
"Effective HRD practices are designed on principles that keep them developmental, integrated and context-sensitive.",
[
"<b>Top-management commitment:</b> Practices fail without visible leadership support and resources.",
"<b>Line-manager ownership:</b> HRD is every manager’s job; design must involve and skill line managers.",
"<b>Integration of subsystems:</b> Appraisal, training, career, potential and counselling should share data and purpose.",
"<b>Strategy alignment:</b> Practices must serve organisational goals and future competencies.",
"<b>Need-based and scientific:</b> Design from diagnosis (TNA, climate, role analysis), not fads or copies of other firms.",
"<b>Culture and climate fit:</b> Adapt tools to existing culture while gradually building OCTAPAC values.",
"<b>Participation and fairness:</b> Employees should understand criteria and have voice; equity of opportunity is essential.",
"<b>Continuity and evaluation:</b> HRD is a process without a finish line; practices must be reviewed for whether they help or hinder development.",
],
"Designing on these principles makes HRD practices effective instruments of development rather than isolated administrative routines.")

add(27, 2,
"Explain how the major HRD subsystems are interrelated within an organisation.",
"HRD subsystems are interrelated like organs of one body: output of one is input of another. Isolation reduces effectiveness.",
[
"<b>Appraisal → training:</b> Performance gaps become training needs.",
"<b>Appraisal → counselling:</b> Ratings and incidents become discussion agenda.",
"<b>Potential → career planning:</b> High-potential employees enter accelerated paths; others get realistic alternative paths.",
"<b>Career plans → training and job experiences:</b> Required competencies specify programmes, rotation and mentoring.",
"<b>Feedback loops:</b> Training evaluation and on-the-job results should update the next appraisal.",
"<b>Climate as context:</b> All subsystems depend on a climate of trust; OD/climate work enables honest appraisal and counselling.",
"<b>HRM links:</b> Placement, promotion and rewards should be consistent with HRD data, or employees ignore development messages.",
"<b>Information system:</b> A shared HRD information base (competencies, IDPs, history) makes interrelation operational.",
],
"Interrelated subsystems create a coherent development cycle; without links, each practice works below potential.")

add(28, 2,
"Explain the need for integrating HRD practices with organisational strategy.",
"Strategy states where the organisation is going; HRD builds the people capability to get there. Integration is therefore a necessity, not a luxury.",
[
"<b>Capability as strategy implementation:</b> New products, markets, quality or digitalisation fail if people lack competencies.",
"<b>Avoiding irrelevant training:</b> Unintegrated HRD produces popular courses that do not serve business priorities.",
"<b>Talent for future structure:</b> Strategy may need new roles; career and potential systems must prepare them in time.",
"<b>Culture required by strategy:</b> Cost leadership vs innovation need different climates; HRD must shape accordingly.",
"<b>Resource efficiency:</b> Development budgets are limited; strategy tells what to prioritise.",
"<b>Change readiness:</b> Strategic change is mainly a people process; integrated HRD reduces resistance.",
"<b>Measurement:</b> Integration allows HRD to be judged on strategic outcomes, raising its credibility.",
"<b>Employee meaning:</b> People see why they are developed, which increases engagement with HRD practices.",
],
"Hence integrating HRD with strategy ensures that development efforts create the right capabilities at the right time for organisational success.")

add(29, 2,
"An organisation has an appraisal system but employees report that it does not help their development. Apply HRD principles to improve the appraisal process.",
"The problem is typically an administrative/evaluative appraisal without developmental design. HRD principles suggest redesign, not merely a new form.",
[
"<b>Clarify purpose:</b> State that appraisal is primarily for development (goals, feedback, IDP), with rewards as a separate but linked use.",
"<b>Role clarity and joint goal setting:</b> Begin with agreed KRAs/competencies so review is fair and learning-focused.",
"<b>Behavioural, evidence-based feedback:</b> Train managers to give specific examples, not vague labels.",
"<b>Mandatory counselling discussion:</b> Protect time for two-way dialogue; ban ‘form-signing in the corridor’.",
"<b>Individual development plan:</b> Every review must end with training, coaching or stretch-job actions and follow-up dates.",
"<b>Link to other subsystems:</b> Feed gaps to TNA; use potential data for career talk.",
"<b>Climate safeguards:</b> Reduce fear (no public humiliation, some self-appraisal, appeal on process).",
"<b>Evaluate the appraisal itself:</b> Survey whether employees found it useful; hold managers accountable for development quality, not only timely form submission.",
],
"Applying these HRD principles converts appraisal from a ritual of judgement into a genuine development subsystem.")

add(30, 2,
"Apply the concept of HRD subsystems to propose a development path for an employee identified as having future leadership potential.",
"A high-potential employee needs an integrated path using all major HRD subsystems, not a single training programme.",
[
"<b>Potential appraisal confirmation:</b> Use multiple inputs (boss, assessment centre, track record) so the label is valid.",
"<b>Career planning:</b> Map 3–5 year possible leadership roles and competency gaps versus those roles.",
"<b>Performance appraisal:</b> Keep current-job excellence while adding leadership behaviour goals (delegation, coaching, decision quality).",
"<b>Training and education:</b> Mix of conceptual programmes (strategy, finance) and skill workshops (communication, conflict).",
"<b>On-the-job stretch:</b> Job rotation, project leadership, deputy roles—potential is developed mainly through experience.",
"<b>Mentoring and counselling:</b> Senior mentor plus regular counselling to handle transition stress and derailers.",
"<b>Feedback:</b> 360-degree or frequent stakeholder feedback to correct early.",
"<b>Review:</b> Annual potential re-appraisal; if progress stalls, revise path. Align rewards so development effort is recognised.",
],
"This path uses interrelated HRD subsystems to convert identified potential into ready leadership capability.")

add(31, 2,
"State any two HRD subsystems.",
"An HRD system comprises several subsystems. Two are stated first; others complete an 8-mark theoretical discussion.",
[
"<b>Subsystem 1 – Performance appraisal:</b> Developmental review of results and behaviours to guide improvement.",
"<b>Subsystem 2 – Training:</b> Planned learning to build job-related and future competencies.",
"<b>Potential appraisal:</b> Judging future capability for higher roles.",
"<b>Career planning:</b> Mapping growth paths for individual and organisation.",
"<b>Feedback and counselling:</b> Dialogue that produces insight and change.",
"<b>Organisation development:</b> Interventions for teams, culture and structure.",
"<b>HRD climate mechanisms:</b> Surveys, communication and trust-building practices.",
"<b>Interrelation:</b> Naming two is not enough for practice—they must exchange data and share a developmental philosophy.",
],
"Any two subsystems may be stated; theoretically they exist as parts of one HRD system, not as standalone activities.")

add(32, 2,
"State any two purposes of feedback in HRD practices.",
"Feedback is purposeful information for development. Two core purposes are explained along with related purposes.",
[
"<b>Purpose 1 – Improve current performance:</b> Let employees know where they stand against expectations so they can correct behaviour and results.",
"<b>Purpose 2 – Support learning and development:</b> Reinforce effective behaviour and guide training, coaching and career choices.",
"<b>Motivation:</b> Recognition through positive feedback satisfies higher-order needs.",
"<b>Role clarification:</b> Feedback reveals misunderstood expectations.",
"<b>Climate building:</b> Open, respectful feedback signals trust and openness.",
"<b>System improvement:</b> Upward feedback helps the organisation fix processes, not only people.",
"<b>Potential development:</b> Feedback on leadership behaviours prepares future roles.",
"<b>Evaluation of training:</b> Feedback after programmes (reaction and behaviour) improves HRD design.",
],
"Thus the purposes of feedback in HRD are corrective, developmental, motivational and systemic—not merely criticism.")

add(33, 2,
"Analyse how poor coordination among HRD subsystems can reduce the effectiveness of employee development.",
"When subsystems work in silos, development becomes fragmented, contradictory and low-impact.",
[
"<b>Appraisal not feeding training:</b> People are rated low on a skill but never trained; frustration rises.",
"<b>Training unrelated to career:</b> Employees attend courses that do not lead to growth; motivation to learn falls.",
"<b>Potential ignored in promotion:</b> High potentials leave; others see HRD as dishonest.",
"<b>No counselling after appraisal:</b> Data exist but no insight or IDP; forms replace development.",
"<b>Conflicting messages:</b> Training teaches teamwork while rewards and appraisal honour only individual targets.",
"<b>Duplication and gaps:</b> Multiple agencies run overlapping programmes while some roles get nothing.",
"<b>Weak information:</b> Without a shared database, each subsystem starts from zero each year.",
"<b>Result:</b> Employee development is slow, unfair and unstrategic; HRD loses credibility and budget.",
],
"Analysis shows coordination is a design requirement: unlinked subsystems cancel each other and waste human potential.")

add(34, 2,
"Analyse how HRD practices can be aligned with organisational strategy in a rapidly changing organisation.",
"Rapid change (markets, technology, structure) requires HRD that is agile and tightly coupled to strategy.",
[
"<b>Continuous strategy–competency translation:</b> Each strategic shift should update competency maps quickly.",
"<b>Shorter diagnosis cycles:</b> Frequent TNA and pulse climate surveys rather than once-in-three-years studies.",
"<b>Flexible learning:</b> Blended, just-in-time, on-the-job and e-learning instead of only long residential courses.",
"<b>Change and OD capability:</b> HRD facilitates restructuring, new teams and culture, not only skill training.",
"<b>Talent mobility:</b> Career systems allow lateral moves and project roles, not rigid ladders.",
"<b>Line partnership:</b> Business leaders and HRD jointly review capability risks in strategy meetings.",
"<b>Let-go of obsolete practices:</b> Drop training and appraisal items that no longer match strategy.",
"<b>Evaluate on adaptability:</b> Judge HRD by speed of capability building and change readiness, not by number of programmes.",
],
"Alignment in a fast-changing context is an ongoing process of translating strategy into people systems that can themselves change quickly.")

add(35, 2,
"Evaluate the effectiveness of using potential appraisal together with performance appraisal for employee development.",
"Using both is more effective than using either alone, provided they are distinct yet linked.",
[
"<b>Different questions:</b> Performance appraisal asks ‘How well is the present job done?’ Potential appraisal asks ‘How far can the person go?’",
"<b>Avoids the star-performer trap:</b> Excellent specialists may fail as managers if promoted only on performance.",
"<b>Richer development plans:</b> High performance + high potential → leadership path; high performance + limited potential → specialist excellence path; low performance + high potential → coaching and role fit.",
"<b>Fairness:</b> Employees understand why some get stretch roles; criteria are dual, not arbitrary.",
"<b>Risks:</b> If potential is secretive or biased, it creates politics. If both are done by the same untrained boss in one sitting, they collapse into one rating.",
"<b>Conditions for effectiveness:</b> Separate tools/time, trained assessors, feedback to the employee, and career actions that follow.",
"<b>Evidence logic:</b> Combined use supports succession accuracy and targeted training ROI.",
"<b>Evaluative conclusion:</b> Joint use is highly effective for development when methodologically separated and ethically feedback-based; otherwise it is ineffective or harmful.",
],
"Evaluation therefore favours combined performance-plus-potential appraisal as a superior HRD design when quality and transparency are ensured.")

add(36, 2,
"Analyse how an HRD system can become ineffective when its practices are designed without organisational strategy alignment.",
"An unaligned HRD system may be busy and even popular, yet ineffective for the organisation and eventually for employees.",
[
"<b>Wrong competencies:</b> People are developed for yesterday’s jobs while strategy needs new capabilities.",
"<b>Misallocated budget:</b> High spend on peripheral programmes; critical roles remain weak.",
"<b>Career paths to nowhere:</b> Plans that do not match future structure create broken promises.",
"<b>Appraisal of irrelevant KRAs:</b> Employees chase measures that no longer matter.",
"<b>Loss of top-management support:</b> Leaders see no business return and cut HRD.",
"<b>Employee cynicism:</b> Development feels decorative; talent leaves for firms with clearer growth linked to business.",
"<b>Change failure:</b> Strategy implementation stalls because HRD did not prepare people.",
"<b>Illusion of effectiveness:</b> High training days and completed forms hide strategic irrelevance until a crisis.",
],
"Analysis concludes that strategy alignment is a condition of HRD effectiveness; design without it produces activity, not impact.")

add(37, 2,
"State any two benefits of integrating career planning with potential appraisal.",
"Integration of these two forward-looking subsystems yields several benefits; two are primary.",
[
"<b>Benefit 1 – Realistic career paths:</b> Career plans are based on assessed potential, reducing false hopes and later frustration.",
"<b>Benefit 2 – Better talent utilisation:</b> High-potential employees receive timely stretch roles, rotation and training instead of waiting in the queue.",
"<b>Succession security:</b> The organisation knows who can fill key jobs and how to prepare them.",
"<b>Targeted investment:</b> Development money goes where potential and organisational need meet.",
"<b>Motivation:</b> Employees see a transparent link between their growth and organisational judgement of potential.",
"<b>Reduced wrong promotions:</b> Potential data qualify career moves beyond current performance.",
"<b>Retention:</b> Visible, fair growth paths reduce exit of capable staff.",
"<b>Feedback quality:</b> Career counselling becomes evidence-based rather than generic advice.",
],
"Integrating career planning with potential appraisal therefore benefits both the individual and the organisation’s future capability.")

add(38, 2,
"Mention any two features of an effective HRD practice.",
"Effective HRD practices share identifiable features. Two are stated and others support the answer.",
[
"<b>Feature 1 – Developmental purpose:</b> The practice helps people learn and grow; it is not only administrative control.",
"<b>Feature 2 – Integration:</b> It links with other subsystems and with organisational strategy.",
"<b>Need-based:</b> Built on diagnosis rather than fashion.",
"<b>Line-manager involvement:</b> Bosses own the practice day to day.",
"<b>Fairness and transparency:</b> Criteria and opportunities are understood.",
"<b>Top support and resources:</b> Time, money and sponsorship exist.",
"<b>Climate consistency:</b> The practice matches and builds trust and openness.",
"<b>Evaluated and improved:</b> Impact is reviewed; the practice is redesigned when it hinders the HRD process.",
],
"Any two features, explained, characterise effective HRD practice; in combination they distinguish genuine development from ritual.")

add(39, 2,
"Design an integrated HRD system for an organisation that wants to connect performance, potential, training, career planning, feedback, and counselling.",
"An integrated design specifies purpose, process links, roles and review for all six elements.",
[
"<b>Architecture:</b> One HRD policy stating that the six subsystems form a single cycle owned by line managers, facilitated by HRD.",
"<b>Annual cycle:</b> Goal setting → ongoing feedback → performance appraisal → counselling and IDP → potential review (for relevant employees) → career discussion → training/job-experience plan → evaluation.",
"<b>Data spine:</b> A common competency framework and employee development file shared across subsystems.",
"<b>Feedback and counselling:</b> Quarterly check-ins plus appraisal counselling; trained managers; optional specialist counsellor.",
"<b>Training link:</b> IDPs aggregate into the training calendar; TNA validates group programmes.",
"<b>Potential and career:</b> Assessment centres/reviews feed a talent council that decides rotations and succession, then communicates paths to employees.",
"<b>Governance:</b> HRD committee of business heads reviews alignment with strategy twice a year.",
"<b>Climate and audit:</b> Climate survey and HRD audit test whether the connections work in employees’ experience, not only on paper.",
],
"This design makes the six elements one system: each conversation and record triggers the next developmental action.")

add(40, 2,
"Evaluate a proposed HRD practice that has strong training content but weak linkage with organisational strategy, performance appraisal, and career planning.",
"Strong content is a necessary but not sufficient condition. Evaluation must judge likely transfer, relevance and developmental impact.",
[
"<b>Strength:</b> Sound pedagogy, expert trainers and good materials may produce high reaction and some learning (Kirkpatrick levels 1–2).",
"<b>Strategy weakness:</b> Content may not build capabilities the business actually needs; opportunity cost is high.",
"<b>Appraisal disconnect:</b> Bosses may not expect or reinforce new behaviours; employees return to old KRAs.",
"<b>Career disconnect:</b> Learning does not count toward growth; motivation to apply and continue learning falls.",
"<b>Transfer failure risk:</b> Without workplace linkage, level 3 (behaviour) and 4 (results) will likely be poor.",
"<b>Climate signal:</b> Isolated excellent training can still create cynicism (‘holiday training’) if unrelated to real work.",
"<b>Conditional value:</b> The practice may still help as general education for a few motivated individuals, but as an organisational HRD practice it is weak.",
"<b>Evaluative verdict:</b> Do not accept as-is. Keep the strong content only after remapping to strategy, inserting pre/post appraisal goals, and placing the programme on career/competency maps.",
],
"Evaluation concludes that content quality cannot compensate for missing strategic, appraisal and career linkages; redesign is required.")

# ========== UNIT 3 ==========
add(41, 3,
"Explain the concept of Training Needs Assessment (TNA) and state its importance in HRD.",
"Training Needs Assessment (TNA) is the systematic process of identifying gaps between required and actual competencies at organisation, task and person levels, and deciding whether training is the right solution. Need ≈ Standard performance − Actual performance, but only when the cause is a lack of KSA.",
[
"<b>Organisation analysis:</b> Links firm strategy/goals to where training is needed and whether climate will support it.",
"<b>Task analysis:</b> Identifies important tasks and the knowledge, skills and attitudes required.",
"<b>Person analysis:</b> Identifies who needs training by comparing employee KSAs with job requirements.",
"<b>Importance – relevance:</b> Prevents ‘off-the-shelf’ programmes that do not fit.",
"<b>Importance – diagnosis:</b> Distinguishes training needs from problems of motivation, tools, or process design.",
"<b>Importance – priority and budget:</b> Directs scarce HRD resources to critical gaps.",
"<b>Importance – design quality:</b> Supplies objectives, content and method choices for the training plan.",
"<b>Importance – evaluation baseline:</b> Defines what success will look like, enabling later Kirkpatrick evaluation.",
],
"TNA is therefore the foundation of HRD training: without it, design, delivery and evaluation rest on guesswork.")

add(42, 3,
"Describe the major steps involved in designing a training program.",
"Design follows TNA and converts needs into a coherent plan of objectives, content, methods, resources and evaluation.",
[
"<b>Confirm needs and trainees:</b> Use TNA outputs; ensure learners are ready (basic skills, motivation).",
"<b>Set training goals and learning objectives:</b> Overall capability to be achieved and specific, observable learning outcomes.",
"<b>Select content and sequence:</b> What will be taught, in what order, with theory–practice balance.",
"<b>Choose methods and activities:</b> Lectures, cases, workshops, OJT, e-learning, simulations—matched to objectives.",
"<b>Decide on-the-job vs off-the-job, internal vs outsourced, on-site vs off-site.</b>",
"<b>Plan facilities, trainers, materials and budget:</b> Venue, AV, handouts, resource persons, costs.",
"<b>Design transfer support:</b> Pre-briefing of bosses, action plans, post-training projects.",
"<b>Build evaluation into design:</b> Reaction sheets, learning tests, behaviour follow-up and result measures agreed in advance.",
],
"These steps produce a training plan that is need-based, feasible and evaluable, not merely a timetable of lectures.")

add(43, 3,
"Explain on-the-job and off-the-job training methods with suitable examples.",
"Training methods are broadly on-the-job (learning in the actual work setting) and off-the-job (learning away from daily work). Each suits different objectives.",
[
"<b>On-the-job training (OJT):</b> Learning while performing real work under guidance.",
"<b>Examples of OJT:</b> Coaching by supervisor, job rotation, apprenticeship, understudy, internships, action learning projects.",
"<b>Advantages of OJT:</b> High relevance, lower extra cost, easier transfer, real equipment and customers.",
"<b>Limitations of OJT:</b> Quality depends on the boss; production pressure; possible learning of bad habits; safety risks.",
"<b>Off-the-job training:</b> Learning away from the workstation in classroom, workshop or external institute.",
"<b>Examples:</b> Lectures, case study, role play, vestibule training, simulations, sensitivity training, conferences, MBA-type courses.",
"<b>Advantages:</b> Focused attention, safer practice, expert faculty, conceptual depth, mixing with other participants.",
"<b>Limitations:</b> Transfer problems, higher cost, possible irrelevance if not designed from TNA. A complete HRD approach often blends both.",
],
"On-the-job methods excel for practical skills; off-the-job methods excel for concepts and safe practice. Choice should follow objectives.")

add(44, 3,
"Explain e-learning as a training method and state its major advantages.",
"E-learning is training delivered through electronic media (LMS, online modules, virtual classrooms, mobile learning, webinars). It can be self-paced or live, standalone or blended with classroom and OJT.",
[
"<b>Nature:</b> Uses digital content, interactivity, tracking and often multimedia to achieve learning objectives.",
"<b>Advantage – flexibility:</b> Anytime, anywhere access; useful for dispersed or shift workers.",
"<b>Advantage – scale and speed:</b> Same content to many employees quickly (e.g., compliance, product updates).",
"<b>Advantage – cost over time:</b> After development, marginal cost per extra learner is low.",
"<b>Advantage – standardisation:</b> Consistent quality versus variable classroom trainers.",
"<b>Advantage – tracking:</b> LMS records completion, scores and time, aiding evaluation.",
"<b>Advantage – personalisation:</b> Adaptive paths, micro-learning, replay of difficult parts.",
"<b>Cautions:</b> Needs self-discipline, digital access, instructional design quality, and workplace support for transfer; not ideal alone for all complex interpersonal skills.",
],
"E-learning is a powerful HRD method when content, technology and learner support are sound; its advantages are flexibility, scale, consistency and data.")

add(45, 3,
"Explain the Kirkpatrick model for evaluating training effectiveness.",
"Donald Kirkpatrick’s model evaluates training at four sequential levels, from immediate reaction to organisational results. It is the most widely used framework in HRD.",
[
"<b>Level 1 – Reaction:</b> Did participants like the programme? (satisfaction, perceived relevance, trainer quality). Measured by feedback forms.",
"<b>Level 2 – Learning:</b> Did they acquire intended knowledge, skills or attitudes? Measured by tests, demonstrations, pre–post scores.",
"<b>Level 3 – Behaviour:</b> Do they apply learning on the job? Measured by observation, boss ratings, 360 feedback after a lag.",
"<b>Level 4 – Results:</b> Did the organisation benefit (quality, productivity, errors, sales, safety, customer satisfaction)?",
"<b>Logic of the hierarchy:</b> Favourable reaction helps learning; learning is needed for behaviour; behaviour should drive results—but each step can fail even if the previous succeeded.",
"<b>Importance of higher levels:</b> Many programmes stop at smile sheets; HRD effectiveness requires behaviour and results.",
"<b>Design implication:</b> Evaluation criteria should be set during TNA and design, not after delivery.",
"<b>Limitations:</b> Causality at level 4 is hard; not all outcomes are numeric. Still, the model forces a complete view of effectiveness.",
],
"The Kirkpatrick model thus provides a simple, comprehensive ladder for judging whether training merely pleased people or actually improved work and organisational outcomes.")

add(46, 3,
"Describe the importance of delivering a training program effectively after it has been designed.",
"Design is a plan; delivery (implementation) is putting the plan into effect. Poor delivery can ruin an excellent design.",
[
"<b>Learning happens at delivery:</b> Objectives are achieved only if facilitation, activities and timing actually engage learners.",
"<b>Administrative readiness:</b> Venue, materials, IT, travel and batching affect attention and respect for the programme.",
"<b>Trainer competence:</b> Subject knowledge plus adult-learning skills determine credibility and clarity.",
"<b>Adaptation:</b> Effective delivery adjusts to the group’s level without abandoning objectives.",
"<b>Psychological climate:</b> Safety to practise, ask and fail in the room is essential for skill learning.",
"<b>Transfer start:</b> Delivery should include action planning and boss involvement so learning does not stay in the classroom.",
"<b>Motivation:</b> Opening (why this training) and closing (next steps) influence whether employees try new behaviour.",
"<b>Evaluation data:</b> Delivery is when reaction and learning data are captured; sloppy implementation yields unusable evaluation.",
],
"Therefore effective delivery is as important as design: HRD impact depends on how the programme is actually carried out.")

add(47, 3,
"Explain the relationship among Training Needs Assessment, training design, training delivery, and training evaluation.",
"These four stages form the training cycle. Each stage feeds the next, and evaluation feeds back to TNA and design.",
[
"<b>TNA → Design:</b> Identified gaps, trainees and constraints become objectives, content, methods and budget.",
"<b>Design → Delivery:</b> The plan (sequence, methods, resources) guides implementation; delivery without design is improvisation.",
"<b>Delivery → Evaluation:</b> Implementation produces the experiences and data (tests, behaviour) to be judged.",
"<b>Evaluation → TNA:</b> Results show remaining gaps, wrong diagnoses, or new needs—restarting the cycle.",
"<b>Evaluation → Design/Delivery:</b> Poor learning suggests redesign; poor reaction may suggest trainer or admin fixes.",
"<b>If TNA is skipped:</b> Design aims at the wrong target; evaluation cannot show ‘success’ meaningfully.",
"<b>If evaluation is skipped:</b> The organisation never knows whether delivery was worth it; the cycle is open-loop.",
"<b>HRD view:</b> The four are one process of planned learning, matching Nadler’s organised learning for behavioural change.",
],
"TNA, design, delivery and evaluation are interdependent stages of a single cycle; breaking the chain reduces training to an event.")

add(48, 3,
"Discuss the importance of evaluating training effectiveness for employees and organisations.",
"Evaluation asks whether training achieved its objectives for people and for the firm. It is a duty of HRD, not an optional extra.",
[
"<b>For employees – feedback on learning:</b> Tests and coaching after training show what was mastered and what to practise.",
"<b>For employees – career evidence:</b> Documented new competence supports growth discussions.",
"<b>For employees – better future programmes:</b> Their reaction data improve later learning experiences.",
"<b>For organisations – accountability:</b> Training consumes money and work time; results must be justified.",
"<b>For organisations – improvement:</b> Evaluation locates whether failure was need, design, delivery or transfer climate.",
"<b>For organisations – strategy:</b> Level 4 data show if capability for strategy actually increased.",
"<b>Avoiding false security:</b> Happy participants (level 1) may still not perform; evaluation prevents this illusion.",
"<b>HRD credibility:</b> Systematic evaluation raises HRD from a cost centre image to a professional function.",
],
"Evaluating training is important because it protects employee development quality and organisational return on learning investment.")

add(49, 3,
"A department is experiencing repeated performance errors. Apply the concept of TNA to identify what information should be collected before designing training.",
"TNA must first test whether training is the right response, then collect organisation, task and person information.",
[
"<b>Error pattern data:</b> Type, frequency, process step, shift, product—facts, not impressions.",
"<b>Organisation analysis:</b> Targets, quality policy, whether supervisors support correct methods, and if staffing/tools are adequate.",
"<b>Non-training causes:</b> Faulty machines, unclear SOPs, unrealistic speed, poor incentives—if these dominate, do not design training yet.",
"<b>Task analysis:</b> Correct procedure, critical KSAs, safety points, and standards of error-free performance.",
"<b>Person analysis:</b> Who makes errors (new vs old staff), existing skill tests, and prior training history.",
"<b>Learner readiness:</b> Literacy, language, motivation, and whether they already ‘know but don’t do’.",
"<b>Climate for transfer:</b> Will the boss allow slower correct practice after training?",
"<b>Success criteria:</b> What error reduction would mean the programme worked—needed for later evaluation.",
],
"Applying TNA means collecting evidence on causes, tasks and people before any training design; otherwise the department may train for the wrong problem.")

add(50, 3,
"Apply suitable training methods to design a development program for employees who need both practical job skills and conceptual knowledge.",
"When both practice and concepts are needed, a blended design is appropriate rather than a single method.",
[
"<b>Start with TNA:</b> List practical skills vs conceptual knowledge objectives separately.",
"<b>Off-the-job for concepts:</b> Short lectures, discussion, cases and e-modules to build understanding of principles, standards and ‘why’.",
"<b>Simulations/role play/vestibule:</b> Safe practice of procedures before live work.",
"<b>On-the-job coaching and job rotation:</b> Real skill under a trained coach with checklists.",
"<b>Action learning project:</b> Apply concepts to a live departmental problem to bind theory and practice.",
"<b>E-learning micro-modules:</b> For conceptual refreshers that employees can repeat.",
"<b>Sequence:</b> Concept → simulated practice → OJT → review. Reverse sequence (pure OJT first) may entrench errors.",
"<b>Evaluation:</b> Knowledge tests (level 2) plus observed job samples (level 3) so both needs are checked.",
],
"A blended programme using off-the-job conceptual methods plus OJT and practice methods develops both the head and the hand.")

add(51, 3,
"State any two purposes of Training Needs Assessment.",
"TNA serves several purposes; two are primary for an 8-mark answer.",
[
"<b>Purpose 1 – Identify genuine training needs:</b> Find KSA gaps that training can close, using organisation, task and person analysis.",
"<b>Purpose 2 – Avoid wrong solutions:</b> Detect when errors come from systems, tools or motivation so the firm does not buy irrelevant training.",
"<b>Set objectives:</b> TNA provides measurable learning and performance objectives.",
"<b>Select trainees:</b> Not everyone needs the same programme.",
"<b>Choose methods:</b> Nature of the need (skill vs knowledge) guides OJT, classroom or e-learning.",
"<b>Prioritise resources:</b> Critical jobs and large gaps come first.",
"<b>Create evaluation baseline:</b> Pre-training performance is recorded.",
"<b>Align with strategy:</b> Organisation analysis keeps HRD relevant to goals.",
],
"The purposes of TNA are diagnostic, preventive, design-related and strategic—making it the first professional step in training.")

add(52, 3,
"Name any two levels of the Kirkpatrick model.",
"Kirkpatrick’s four levels are Reaction, Learning, Behaviour and Results. Two are named and all four explained for a full theoretical answer.",
[
"<b>Level named 1 – Reaction:</b> Participants’ satisfaction and perceived usefulness of training.",
"<b>Level named 2 – Learning:</b> Increase in knowledge, skill or attitude due to the programme.",
"<b>Level 3 – Behaviour:</b> Transfer of learning to the job.",
"<b>Level 4 – Results:</b> Organisational outcomes attributable to training.",
"<b>Why name more than two:</b> Effectiveness cannot be judged by reaction alone.",
"<b>Measurement examples:</b> Smile sheets; tests; observation; quality/productivity data.",
"<b>Sequence:</b> Each level supports but does not guarantee the next.",
"<b>HRD use:</b> Design evaluation at all levels when the programme is important and costly.",
],
"Naming any two levels is the direct answer; theoretically all four levels together define training effectiveness.")

add(53, 3,
"Analyse why a training program may receive positive participant reactions but still fail to improve job performance.",
"This is the classic gap between Kirkpatrick level 1 and levels 3–4. Positive reaction is not performance.",
[
"<b>Entertainment vs learning:</b> Enjoyable trainers and venues raise reaction without building skill.",
"<b>No real learning (level 2 fail):</b> Content too easy, too hard, or not practised; people leave happy but incompetent.",
"<b>Wrong need:</b> TNA missing—performance problem was not a skill gap (tools, workload, process).",
"<b>No transfer climate:</b> Bosses do not allow new methods; old SOPs and peer pressure restore old behaviour.",
"<b>No opportunity:</b> Skills unused for months are forgotten.",
"<b>Conflicting appraisal/rewards:</b> Employees are measured on speed, not the quality method taught.",
"<b>Lack of follow-up:</b> No coaching, action plan or refresher after the event.",
"<b>Analytical conclusion:</b> Reaction is a weak predictor of job performance; HRD must design for learning, behaviour support and results, not applause.",
],
"Positive reactions with no performance gain usually mean the programme was pleasant but diagnostically or contextually wrong.")

add(54, 3,
"Analyse the consequences of designing a training program without conducting an adequate Training Needs Assessment.",
"Skipping TNA is a major cause of HRD waste and can worsen operational problems.",
[
"<b>Wrong content:</b> Topics do not match actual KSA gaps; errors continue.",
"<b>Wrong audience:</b> Skilled staff are bored; those who need help are absent.",
"<b>Wrong method:</b> Lecture used where coaching was needed, or vice versa.",
"<b>Training as false solution:</b> System problems remain; management thinks ‘we already trained them’.",
"<b>Demotivation:</b> Employees lose faith in HRD; future programmes suffer.",
"<b>Wasted budget and lost production time:</b> Direct cost plus opportunity cost.",
"<b>Impossible evaluation:</b> No baseline or objectives, so success cannot be judged.",
"<b>Strategic drift:</b> Training calendar becomes a ritual disconnected from organisational goals.",
],
"Consequences are operational, financial and cultural. Adequate TNA is therefore not bureaucracy but professional risk control.")

add(55, 3,
"Evaluate the usefulness of the Kirkpatrick model for judging the effectiveness of an organisational training program.",
"The model is useful as a comprehensive framework, with known limitations that HRD professionals should manage.",
[
"<b>Usefulness – completeness:</b> Forces attention beyond smile sheets to learning, behaviour and results.",
"<b>Usefulness – communication:</b> Four levels are easy to explain to managers and trainees.",
"<b>Usefulness – design aid:</b> Encourages setting measures during TNA and design.",
"<b>Usefulness – diagnosis:</b> If reaction is high but behaviour low, look at transfer climate, not only the trainer.",
"<b>Limitation – causality:</b> Level 4 results have many causes; training may be only one.",
"<b>Limitation – cost and time:</b> Behaviour and results evaluation is harder; firms may stop at level 1.",
"<b>Limitation – not all programmes need full 4 levels:</b> Short awareness talks vs critical safety training differ.",
"<b>Evaluative conclusion:</b> Highly useful as a guiding model if applied proportionately and supplemented with transfer and ROI thinking; not a mechanical proof of training success.",
],
"Overall, Kirkpatrick remains a valuable HRD tool for judging effectiveness when used thoughtfully rather than as a paperwork ritual.")

add(56, 3,
"Analyse how the choice among on-the-job, off-the-job, and e-learning methods can affect training outcomes.",
"Method choice affects learning quality, transfer, cost, motivation and therefore outcomes at all Kirkpatrick levels.",
[
"<b>OJT outcomes:</b> Strong transfer and job relevance; outcomes suffer if coaches are unskilled or production pressure blocks practice.",
"<b>Off-the-job outcomes:</b> Better conceptual learning and safe practice; outcomes suffer if the classroom is isolated from work (low level 3).",
"<b>E-learning outcomes:</b> Consistent knowledge delivery and tracking; outcomes suffer with poor design, no interaction, or low completion.",
"<b>Match to objective:</b> Motor skills favour OJT/simulation; interpersonal skills favour role play; information updates favour e-learning.",
"<b>Learner factors:</b> New employees may need structured off-the-job; experienced staff may prefer OJT or micro e-learning.",
"<b>Blended superiority:</b> Combining methods often yields better learning and behaviour than any single method.",
"<b>Climate interaction:</b> Even the best method fails if the workplace punishes new behaviour.",
"<b>Analytical point:</b> Outcomes are not determined by method labels but by fit to need, quality of execution, and transfer support.",
],
"Method choice is a strategic HRD decision: it shapes what is learned and whether it appears in job performance.")

add(57, 3,
"State any two reasons for evaluating training at more than one Kirkpatrick level.",
"Single-level evaluation, especially reaction only, is misleading. Two reasons are central.",
[
"<b>Reason 1 – Different levels answer different questions:</b> Liking is not learning; learning is not doing; doing is not business results.",
"<b>Reason 2 – Diagnosis of failure:</b> Multi-level data show where the chain broke (content vs transfer vs job conditions).",
"<b>Accountability:</b> Organisations fund training for performance, not entertainment.",
"<b>Employee development:</b> Learning and behaviour data guide further coaching.",
"<b>Avoiding false positives:</b> High reaction can hide zero performance change.",
"<b>Avoiding false negatives:</b> Low reaction (strict trainer) might still produce high learning—need level 2.",
"<b>Continuous improvement:</b> Each level suggests different redesign actions.",
"<b>Strategic HRD:</b> Only higher levels show contribution to organisational goals.",
],
"Hence evaluating at more than one level is required for truth, diagnosis and improvement of training.")

add(58, 3,
"Mention any two factors that should be considered while selecting a training method.",
"Method selection should be systematic. Two factors are stated; others complete the theory.",
[
"<b>Factor 1 – Learning objectives:</b> Knowledge, skill or attitude outcomes demand different methods (lecture vs practice vs role play).",
"<b>Factor 2 – Nature of the job/task:</b> Dangerous or costly tasks need simulation/off-the-job first; simple routine skills may use OJT.",
"<b>Trainee characteristics:</b> Education, experience, language, digital literacy, motivation.",
"<b>Cost and time:</b> Budget, opportunity cost of absence from work.",
"<b>Number and location of trainees:</b> Scattered staff may need e-learning.",
"<b>Trainer and facility availability:</b> Internal experts vs external; lab vs classroom.",
"<b>Transfer requirements:</b> How soon must skill appear on the job?",
"<b>Organisational culture:</b> Acceptance of outdoor training, e-learning, or open discussion methods.",
],
"Selecting a method on at least these factors makes training design professional and raises the chance of effective outcomes.")

add(59, 3,
"Design a complete training program for a clearly identified employee skill gap, covering TNA, objectives, training method, delivery, and evaluation.",
"Illustration: customer-service staff show a skill gap in handling complaints (high repeat complaints, low first-contact resolution). The design follows the full cycle.",
[
"<b>TNA:</b> Organisation analysis (customer strategy); task analysis (complaint process, empathy, system use); person analysis (who fails, knowledge vs skill vs attitude). Confirm it is a skill gap, not a policy/IT problem.",
"<b>Objectives:</b> By end of programme, trainees will listen, log, resolve or escalate complaints as per SOP, and reduce repeat complaints by an agreed percentage within 8 weeks.",
"<b>Method:</b> Blended—e-module on policy; classroom role play; OJT coaching with checklist for two weeks.",
"<b>Delivery:</b> 12-person batches, trained facilitator, recorded calls for practice, manager present at close for transfer commitments. Admin: lab with CRM access.",
"<b>Transfer:</b> Supervisor weekly coaching; updated appraisal KRA on resolution quality.",
"<b>Evaluation L1–L2:</b> Reaction form; knowledge test and observed role play.",
"<b>Evaluation L3–L4:</b> Call audits after 30–60 days; repeat-complaint and CSAT metrics versus baseline.",
"<b>Review:</b> HRD and department head meet at 60 days to refine SOP or coaching if results lag.",
],
"This complete design shows TNA-driven objectives, blended methods, careful delivery and multi-level evaluation for a specific skill gap.")

add(60, 3,
"Evaluate two alternative training programs for the same organisational need using the Kirkpatrick model and recommend the more effective program.",
"Organisational need: first-line supervisors must learn to give developmental feedback (linked to HRD climate). Two alternatives are evaluated.",
[
"<b>Programme A – Two-day off-site lecture on ‘leadership’ with motivational speaker.</b> Likely high Level 1 (reaction). Level 2 uncertain (few skill practices). Level 3 weak (no on-job tools). Level 4 unlikely (climate/appraisal unchanged).",
"<b>Programme B – TNA-based blended design:</b> concept module, extensive role play, real feedback assignments, boss-as-coach, 60-day follow-up, appraisal item on coaching quality.",
"<b>Level 1:</b> A may beat B (entertainment). B still adequate if relevant.",
"<b>Level 2:</b> B superior due to practice and feedback on skill.",
"<b>Level 3:</b> B superior due to assignments and climate support; A rarely transfers.",
"<b>Level 4:</b> B more likely to improve employee development climate, error correction and engagement; A is costly with little result.",
"<b>Recommendation:</b> Choose Programme B even if reaction scores are slightly lower.",
"<b>Condition:</b> B must keep quality facilitation and management support; otherwise it also fails at level 3.",
],
"Using Kirkpatrick, the more effective programme is the one that can reach behaviour and results, not the one that only maximises participant happiness.")


def section_banner(title):
    data = [[Paragraph(title, styles["Sec"])]]
    t = Table(data, colWidths=[160*mm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), TEAL),
        ("TOPPADDING", (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
    ]))
    return t


def build():
    doc = SimpleDocTemplate(
        OUT, pagesize=A4,
        leftMargin=18*mm, rightMargin=18*mm,
        topMargin=24*mm, bottomMargin=20*mm,
        title="HRD (OE) Question Bank Solutions — 8 Marks",
        author="HRD Solutions",
    )
    story = []

    story.append(Spacer(1, 40))
    story.append(Paragraph("HUMAN RESOURCE DEVELOPMENT", styles["CoverTitle"]))
    story.append(Paragraph("(Open Elective)", styles["CoverSub"]))
    story.append(Spacer(1, 8))
    story.append(HRFlowable(width="80%", thickness=2, color=GOLD, spaceBefore=4, spaceAfter=8, hAlign="CENTER"))
    story.append(Paragraph("QUESTION BANK SOLUTIONS", styles["CoverTitle"]))
    story.append(Paragraph("Point-wise Theoretical Answers  |  8 Marks each  |  60 Questions", styles["CoverSub"]))
    story.append(Spacer(1, 16))
    story.append(Paragraph(
        "This document provides examination-oriented, point-wise theoretical solutions for the complete HRD (OE) "
        "question bank. Answers are written to the 8-mark standard: a short introduction, eight developed points, "
        "and a brief conclusion. Content is aligned with the prescribed notes (HRD concept and climate; HRD systems "
        "and subsystems; Training Needs Assessment, design, methods and Kirkpatrick evaluation).",
        styles["Intro"],
    ))
    story.append(Paragraph(
        "<b>How to use in the exam:</b> Write the introduction in 3–5 lines, present 6–8 numbered points with "
        "brief explanation (not one-line bullets only), and close with a 2-line conclusion. Short questions in the "
        "bank (e.g., ‘state any two…’) are expanded to 8-mark depth by explaining the two items and adding related theory.",
        styles["Intro"],
    ))
    story.append(Spacer(1, 10))
    story.append(Paragraph("Unit 1 — Questions 1–20 &nbsp;&nbsp;|&nbsp;&nbsp; Unit 2 — Questions 21–40 &nbsp;&nbsp;|&nbsp;&nbsp; Unit 3 — Questions 41–60", styles["CoverSub"]))
    story.append(PageBreak())

    current_unit = None
    unit_titles = {
        1: "UNIT 1 — Concept of HRD, Climate, Roles and Strategic Importance",
        2: "UNIT 2 — HRD System, Subsystems and Design Principles",
        3: "UNIT 3 — Training: TNA, Design, Methods, Delivery and Evaluation",
    }

    for n, u, q, intro, pts, conc in QA:
        if u != current_unit:
            current_unit = u
            story.append(section_banner(unit_titles[u]))
            story.append(Spacer(1, 12))

        block = []
        block.append(Paragraph(f"Question {n}  &nbsp;·&nbsp;  Unit {u}  &nbsp;·&nbsp;  8 Marks", styles["QHead"]))
        block.append(HRFlowable(width="100%", thickness=0.6, color=GOLD, spaceAfter=6))
        block.append(Paragraph(q, styles["QText"]))
        block.append(Paragraph("<b>Answer</b>", styles["Meta"]))
        block.append(Paragraph(intro, styles["Body"]))
        for i, p in enumerate(pts, 1):
            block.append(Paragraph(f"<b>{i}.</b>  {p}", styles["PtBullet"]))
        block.append(Paragraph(f"<b>Conclusion.</b> {conc}", styles["Conc"]))
        story.append(KeepTogether(block))
        story.append(Spacer(1, 6))

    story.append(Spacer(1, 12))
    story.append(HRFlowable(width="100%", thickness=1.2, color=NAVY, spaceBefore=8, spaceAfter=8))
    story.append(Paragraph(
        "— End of solutions. Revise definitions (Nadler, T.V. Rao), OCTAPAC climate, HRD vs HRM, six major subsystems, "
        "the four-stage training cycle, and Kirkpatrick’s four levels for a complete 8-mark presentation. —",
        styles["CoverSub"],
    ))

    doc.build(story, onFirstPage=header_footer, onLaterPages=header_footer)
    print("Wrote", OUT)

    import os
    outdir = "/home/user/HRD/solutions_by_question"
    os.makedirs(outdir, exist_ok=True)
    for n, u, q, intro, pts, conc in QA:
        path = os.path.join(outdir, f"Q{n:02d}_Unit{u}_8Marks.pdf")

        def hf(canvas, doc, n=n, u=u):
            canvas.saveState()
            w, h = A4
            canvas.setFillColor(NAVY)
            canvas.rect(0, h - 18, w, 18, fill=1, stroke=0)
            canvas.setFillColor(white)
            canvas.setFont("Times-Bold", 8)
            canvas.drawString(20 * mm, h - 13, f"HRD (OE)  |  Q{n}  |  Unit {u}  |  8 Marks")
            canvas.drawRightString(w - 20 * mm, h - 13, "Point-wise Theoretical Answer")
            canvas.setFillColor(NAVY)
            canvas.rect(0, 0, w, 16, fill=1, stroke=0)
            canvas.setFillColor(white)
            canvas.setFont("Times-Roman", 8)
            canvas.drawString(20 * mm, 6, "Human Resource Development — Open Elective")
            canvas.drawRightString(w - 20 * mm, 6, f"Page {doc.page}")
            canvas.restoreState()

        d = SimpleDocTemplate(
            path, pagesize=A4,
            leftMargin=18*mm, rightMargin=18*mm,
            topMargin=24*mm, bottomMargin=20*mm,
            title=f"HRD Q{n} Solution — 8 Marks",
            author="HRD Solutions",
        )
        st = []
        st.append(Paragraph(f"Question {n}  &nbsp;·&nbsp;  Unit {u}  &nbsp;·&nbsp;  8 Marks", styles["QHead"]))
        st.append(HRFlowable(width="100%", thickness=0.6, color=GOLD, spaceAfter=6))
        st.append(Paragraph(q, styles["QText"]))
        st.append(Paragraph("<b>Answer</b>", styles["Meta"]))
        st.append(Paragraph(intro, styles["Body"]))
        for i, p in enumerate(pts, 1):
            st.append(Paragraph(f"<b>{i}.</b>  {p}", styles["PtBullet"]))
        st.append(Paragraph(f"<b>Conclusion.</b> {conc}", styles["Conc"]))
        d.build(st, onFirstPage=hf, onLaterPages=hf)
    print("Wrote 60 individual PDFs in", outdir)

if __name__ == "__main__":
    build()
