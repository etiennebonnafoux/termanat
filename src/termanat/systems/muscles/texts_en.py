"""English texts (international anatomical nomenclature). They say the same
thing as the French texts, section by section."""

from __future__ import annotations

from ...model import StructureText

_KIND = "Skeletal (striated) muscle"
_GROUP = "Group of skeletal muscles"

TEXTS: dict[str, StructureText] = {
    "N": StructureText(
        name="Sternocleidomastoid",
        kind=_KIND,
        region="Neck, sternocleidomastoid region",
        count="2 (paired)",
        description=(
            "Large, superficial, oblique neck muscle running from the sternum and "
            "clavicle to the mastoid process. It separates the anterior from the "
            "lateral cervical region and covers the neurovascular bundle of the neck."
        ),
        sections={
            "insertions": [
                "Sternal head: anterior surface of the manubrium of the sternum",
                "Clavicular head: superior surface of the medial third of the clavicle",
                "Insertion: lateral surface of the mastoid process and lateral half of "
                "the superior nuchal line of the occipital bone",
            ],
            "action": [
                "Unilateral contraction: tilts the head to the same side and turns the "
                "face to the opposite side",
                "Bilateral contraction: flexes the neck (brings the head forward)",
                "Accessory inspiratory muscle when the head is fixed (raises the sternum)",
            ],
            "innervation": [
                "Motor: accessory nerve (XI), through its lateral branch",
                "Proprioception: branches of the cervical plexus (C2-C3)",
            ],
            "vascularisation": [
                "Sternocleidomastoid branches of the occipital and superior thyroid "
                "arteries",
            ],
            "clinical": [
                "Congenital torticollis: fibrosis of the muscle, head tilted to the "
                "affected side and face turned to the opposite side",
                "Surgical landmark: its anterior border guides access to the common "
                "carotid artery and internal jugular vein",
                "Accessory nerve injury: weak rotation of the head to the opposite side",
            ],
        },
        fact=(
            "When you turn your head to the left, it is the right sternocleidomastoid "
            "that contracts and stands out."
        ),
    ),
    "T": StructureText(
        name="Trapezius",
        kind=_KIND,
        region="Nape, back and shoulder girdle (upper part visible from the front)",
        count="2 (paired)",
        description=(
            "Large, flat, triangular muscle, the most superficial muscle of the back. "
            "Together the two trapezius muscles form a diamond from the occiput to T12. "
            "From the front only the descending part is seen, forming the slope of the "
            "shoulders."
        ),
        sections={
            "parts": [
                "Descending (upper) part, from the occipital bone and nuchal ligament",
                "Transverse (middle) part, from the spinous processes of C7 to T3",
                "Ascending (lower) part, from the spinous processes of T4 to T12",
            ],
            "insertions": [
                "Origin: external occipital protuberance, medial third of the superior "
                "nuchal line, nuchal ligament, spinous processes of C7 to T12",
                "Insertion: lateral third of the clavicle, acromion and spine of the "
                "scapula",
            ],
            "action": [
                "Descending part: elevates the shoulder (shrugging)",
                "Transverse part: adducts (retracts) the scapula",
                "Ascending part: depresses the scapula",
                "Descending and ascending parts, with serratus anterior: upward rotation "
                "of the scapula, needed to raise the arm above 90°",
            ],
            "innervation": [
                "Motor: accessory nerve (XI)",
                "Proprioception: branches of the cervical plexus (C3-C4)",
            ],
            "vascularisation": [
                "Mainly the transverse cervical artery, with branches of the occipital "
                "and suprascapular arteries",
            ],
            "clinical": [
                "Accessory nerve injury in the lateral cervical region (lymph node "
                "dissection, biopsy): drooping shoulder",
                "Tested by asking the patient to shrug against resistance",
            ],
        },
        fact=(
            "The two trapezius muscles together outline a diamond once called the "
            "\"monk's hood\" (musculus cucullaris)."
        ),
    ),
    "D": StructureText(
        name="Deltoid",
        kind=_KIND,
        region="Shoulder",
        count="2 (paired)",
        description=(
            "Thick triangular muscle that gives the shoulder its rounded contour. It "
            "covers the glenohumeral joint in front, laterally and behind."
        ),
        sections={
            "parts": [
                "Anterior (clavicular) part",
                "Middle (acromial) part, multipennate, the strongest",
                "Posterior (spinal) part",
            ],
            "insertions": [
                "Origin: lateral third of the clavicle, lateral border of the acromion, "
                "inferior border of the spine of the scapula",
                "Insertion: deltoid tuberosity on the lateral surface of the humerus",
            ],
            "action": [
                "Main abductor of the arm, mostly between 15° and 90°, after the movement "
                "is started by the supraspinatus",
                "Anterior part: flexion and medial rotation of the arm",
                "Posterior part: extension and lateral rotation of the arm",
                "Above 90°, elevation requires rotation of the scapula (trapezius, "
                "serratus anterior)",
            ],
            "innervation": [
                "Axillary nerve (C5-C6), formerly circumflex nerve, a branch of the "
                "posterior cord of the brachial plexus",
            ],
            "vascularisation": [
                "Posterior and anterior circumflex humeral arteries, deltoid branch of "
                "the thoracoacromial artery",
            ],
            "clinical": [
                "Anteroinferior shoulder dislocation or fracture of the surgical neck of "
                "the humerus: risk of axillary nerve injury",
                "Axillary nerve palsy: abduction impossible and numbness over the "
                "shoulder (\"regimental badge\" area)",
                "Classic site for intramuscular injections (vaccines), in its upper part "
                "to avoid the axillary nerve",
            ],
        },
        fact=(
            "Its name comes from the Greek letter delta (Δ): upside down, the muscle is "
            "shaped like a triangle."
        ),
    ),
    "P": StructureText(
        name="Pectoralis major",
        kind=_KIND,
        region="Anterior chest wall",
        count="2 (paired)",
        description=(
            "Large fan-shaped muscle of the anterior chest wall, running from the "
            "thorax to the humerus. Its lower border forms the anterior axillary fold; "
            "the breast lies on its fascia."
        ),
        sections={
            "parts": [
                "Clavicular head",
                "Sternocostal head",
                "Abdominal head (inconstant, small)",
            ],
            "insertions": [
                "Origin: medial half of the clavicle, anterior surface of the sternum, "
                "costal cartilages 1 to 6, sheath of the rectus abdominis",
                "Insertion: lateral lip of the intertubercular groove of the humerus "
                "(crest of the greater tubercle), by a U-shaped folded tendon",
            ],
            "action": [
                "Adduction and medial rotation of the arm",
                "Clavicular head: flexes the arm; sternocostal head: brings the flexed "
                "arm back to the body",
                "Accessory inspiratory muscle when the arm is fixed",
            ],
            "innervation": [
                "Lateral (C5-C7) and medial (C8-T1) pectoral nerves, from the brachial "
                "plexus",
            ],
            "vascularisation": [
                "Pectoral branch of the thoracoacromial artery, perforating branches of "
                "the internal thoracic artery, lateral thoracic artery",
            ],
            "clinical": [
                "Poland syndrome: congenital absence of the sternocostal head",
                "Breast cancer: a tumour fixed to the contracted muscle suggests deep "
                "extension",
                "Used as a muscle flap in reconstructive surgery",
            ],
        },
        fact=(
            "Its fibres cross in the tendon: the lowest fibres of the muscle insert "
            "highest on the humerus."
        ),
    ),
    "S": StructureText(
        name="Serratus anterior",
        old_names=["serratus magnus"],
        kind=_KIND,
        region="Lateral chest wall",
        count="2 (paired)",
        description=(
            "Broad muscle lying flat on the lateral chest wall, between the ribs and "
            "the scapula. Its digitations, visible below the armpit in muscular "
            "people, interlock with those of the external oblique."
        ),
        sections={
            "insertions": [
                "Origin: lateral surfaces of the first 8 to 10 ribs, by digitations (the "
                "number varies between textbooks)",
                "Insertion: costal surface of the medial border of the scapula, mostly at "
                "the inferior angle",
            ],
            "action": [
                "Holds the scapula against the thorax",
                "Abduction (protraction) of the scapula: pushing, punching",
                "Upward rotation of the scapula with the trapezius, essential to raise "
                "the arm above 90°",
            ],
            "innervation": [
                "Long thoracic nerve (C5-C7), nerve of Charles Bell, running down on the "
                "lateral surface of the muscle",
            ],
            "vascularisation": [
                "Lateral thoracic artery and thoracodorsal artery",
            ],
            "clinical": [
                "Long thoracic nerve injury (axillary dissection, carrying loads on the "
                "shoulder, trauma): winged scapula",
                "Winged scapula: the medial border of the scapula lifts off when the "
                "patient pushes against a wall",
            ],
        },
        fact=(
            "It is nicknamed the \"boxer's muscle\": it drives the scapula, and so the "
            "fist, forward."
        ),
    ),
    "B": StructureText(
        name="Biceps brachii",
        kind=_KIND,
        region="Arm, anterior compartment (superficial layer)",
        count="2 (paired)",
        description=(
            "Two-headed fusiform muscle of the anterior compartment of the arm. It "
            "crosses both shoulder and elbow and is the main supinator of the forearm."
        ),
        sections={
            "parts": [
                "Long head: tendon inside the shoulder joint, runs in the intertubercular "
                "groove",
                "Short head, alongside the coracobrachialis",
            ],
            "insertions": [
                "Long head: supraglenoid tubercle of the scapula",
                "Short head: tip of the coracoid process",
                "Insertion: radial tuberosity, and bicipital aponeurosis to the medial "
                "antebrachial fascia",
            ],
            "action": [
                "Flexes the elbow",
                "Powerful supinator of the forearm, especially with the elbow flexed",
                "Weak flexor of the shoulder (long head)",
            ],
            "innervation": [
                "Musculocutaneous nerve (C5-C6)",
            ],
            "vascularisation": [
                "Muscular branches of the brachial artery",
            ],
            "clinical": [
                "Biceps reflex: tests the C5-C6 roots",
                "Rupture of the long head tendon: the belly retracts into a lump in the "
                "middle of the arm (Popeye sign)",
                "The bicipital aponeurosis covers the brachial artery and median nerve "
                "at the elbow crease",
            ],
        },
        fact=(
            "Supination is what works it hardest: it is the muscle that drives a "
            "corkscrew in (in right-handers)."
        ),
    ),
    "R": StructureText(
        name="Brachioradialis",
        old_names=["supinator longus"],
        kind=_KIND,
        region="Forearm, lateral (radial) compartment",
        count="2 (paired)",
        description=(
            "Long superficial muscle of the lateral border of the forearm. It forms "
            "the lateral boundary of the cubital fossa. It flexes the elbow although it "
            "belongs to the dorsal group supplied by the radial nerve."
        ),
        sections={
            "insertions": [
                "Origin: lateral supracondylar ridge of the humerus (upper two thirds)",
                "Insertion: base of the styloid process of the radius",
            ],
            "action": [
                "Flexes the elbow, especially with the forearm in neutral (thumb up)",
                "Brings the forearm back to neutral from pronation or supination; it is "
                "not a supinator despite its former name",
            ],
            "innervation": [
                "Radial nerve (C5-C6), before its division",
            ],
            "vascularisation": [
                "Radial recurrent artery, branches of the radial artery",
            ],
            "clinical": [
                "Brachioradialis reflex: tests the C5-C6 roots",
                "Paralysed in high radial nerve injuries (humeral shaft fracture), "
                "together with wrist drop",
            ],
        },
        fact=(
            "It is sometimes called the \"beer drinker's muscle\": it bends the elbow "
            "when you lift a glass to your mouth, thumb up."
        ),
    ),
    "F": StructureText(
        name="Medial epicondylar muscles",
        old_names=["epitrochlear muscles"],
        kind=_GROUP,
        region="Forearm, anterior compartment (superficial layer)",
        count="5 muscles on each side",
        description=(
            "Superficial muscles of the anterior compartment of the forearm, arising "
            "from the medial epicondyle (formerly epitrochlea) by a common tendon. "
            "They flex the wrist and fingers and pronate the forearm."
        ),
        sections={
            "parts": [
                "Pronator teres",
                "Flexor carpi radialis",
                "Palmaris longus, inconstant",
                "Flexor carpi ulnaris",
                "Flexor digitorum superficialis",
            ],
            "insertions": [
                "Common origin: medial epicondyle of the humerus (common flexor tendon)",
                "Pronator teres: lateral surface of the radius, mid-shaft",
                "Flexor carpi radialis: base of the 2nd metacarpal; palmaris longus: "
                "palmar aponeurosis",
                "Flexor carpi ulnaris: pisiform, hamate, base of the 5th metacarpal",
                "Flexor digitorum superficialis: middle phalanges of fingers 2 to 5",
            ],
            "action": [
                "Wrist flexion; radial deviation (flexor carpi radialis) or ulnar "
                "deviation (flexor carpi ulnaris)",
                "Finger flexion at the proximal interphalangeal joints (flexor digitorum "
                "superficialis)",
                "Pronation of the forearm (pronator teres)",
            ],
            "innervation": [
                "Median nerve (C6-T1) for all of these muscles",
                "Except flexor carpi ulnaris: ulnar nerve (C8-T1)",
            ],
            "vascularisation": [
                "Branches of the ulnar and radial arteries",
            ],
            "clinical": [
                "Medial epicondylitis (\"golfer's elbow\"): tendinopathy of the common "
                "tendon",
                "Palmaris longus, absent in about 15% of people, is used as a tendon graft",
                "Volkmann syndrome: ischaemia of the anterior compartment (supracondylar "
                "fracture in children) leading to a claw-like contracture",
            ],
        },
        fact=(
            "Make a fist and flex your wrist: the palmaris longus tendon stands out in "
            "the middle of the wrist, if you have one."
        ),
    ),
    "A": StructureText(
        name="Rectus abdominis",
        kind=_KIND,
        region="Anterior abdominal wall",
        count="2 (paired)",
        description=(
            "Long, flat, vertical muscle on each side of the linea alba, enclosed in "
            "the rectus sheath formed by the aponeuroses of the flat abdominal muscles."
        ),
        sections={
            "insertions": [
                "Inferior attachment: pubic crest and pubic symphysis",
                "Superior attachment: costal cartilages 5 to 7 and xiphoid process",
                "Interrupted by 3 to 4 tendinous intersections (the \"six-pack\")",
            ],
            "action": [
                "Flexes the trunk (curling up) and tilts the pelvis backwards",
                "Raises abdominal pressure: forced expiration, defecation, childbirth",
            ],
            "innervation": [
                "Intercostal nerves 7 to 11 and subcostal nerve (anterior rami T7-T12)",
            ],
            "vascularisation": [
                "Superior (from the internal thoracic) and inferior (from the external "
                "iliac) epigastric arteries, anastomosing in the sheath",
            ],
            "clinical": [
                "Diastasis recti: separation along the linea alba, common after pregnancy",
                "Abdominal guarding or rigidity: a sign of peritonitis",
                "Rectus sheath haematoma (rupture of the inferior epigastric artery, "
                "patient on anticoagulants)",
            ],
        },
        fact=(
            "The tendinous intersections are remnants of the embryonic segmentation of "
            "the muscle into myotomes."
        ),
    ),
    "O": StructureText(
        name="External oblique",
        kind=_KIND,
        region="Anterolateral abdominal wall",
        count="2 (paired)",
        description=(
            "The most superficial and largest of the three flat abdominal muscles. Its "
            "fibres run downwards and medially, like \"hands in the pockets\", and "
            "continue as a broad aponeurosis."
        ),
        sections={
            "insertions": [
                "Origin: outer surfaces of ribs 5 to 12, by digitations",
                "Insertion: anterior half of the outer lip of the iliac crest, linea alba "
                "(through its aponeurosis), pubic tubercle",
                "The lower border of its aponeurosis forms the inguinal ligament, from "
                "the anterior superior iliac spine to the pubic tubercle",
            ],
            "action": [
                "Unilateral: bends the trunk to the same side and turns it to the "
                "opposite side",
                "Bilateral: flexes the trunk, forced expiration, raises abdominal pressure",
            ],
            "innervation": [
                "Lower intercostal nerves and subcostal nerve (T7-T12); contribution of "
                "the iliohypogastric nerve (L1) according to some textbooks",
            ],
            "vascularisation": [
                "Lower posterior intercostal and subcostal arteries, and branches of the "
                "inferior epigastric and deep circumflex iliac arteries",
            ],
            "clinical": [
                "Its aponeurosis is pierced by the superficial inguinal ring, where "
                "inguinal hernias emerge",
                "The inguinal ligament separates abdomen and thigh: landmark for inguinal "
                "(above) and femoral (below) hernias",
                "McBurney incision (appendicectomy): its fibres are split along their "
                "direction, not cut",
            ],
        },
        fact=(
            "To turn the trunk to the right you use the left external oblique and the "
            "right internal oblique."
        ),
    ),
    "Z": StructureText(
        name="Sartorius",
        old_names=["tailor's muscle"],
        kind=_KIND,
        region="Thigh, anterior compartment",
        count="2 (paired)",
        description=(
            "Strap-like muscle, the longest in the body, crossing the thigh diagonally "
            "from the anterior superior iliac spine to the medial surface of the tibia. "
            "It crosses both hip and knee."
        ),
        sections={
            "insertions": [
                "Origin: anterior superior iliac spine",
                "Insertion: medial surface of the upper tibia, in the pes anserinus "
                "(with gracilis and semitendinosus)",
            ],
            "action": [
                "Hip: flexion, abduction and lateral rotation",
                "Knee: flexion",
                "Together: the cross-legged \"tailor\" sitting position",
            ],
            "innervation": [
                "Femoral nerve (L2-L3)",
            ],
            "vascularisation": [
                "Muscular branches of the femoral artery, descending genicular artery",
            ],
            "clinical": [
                "Lateral border of the femoral triangle (inguinal ligament above, "
                "adductor longus medially), which contains the femoral nerve, artery and vein",
                "Covers the adductor canal, through which the femoral artery and vein run",
                "Avulsion of the anterior superior iliac spine in adolescent athletes",
            ],
        },
        fact=(
            "Its name comes from the Latin sartor, \"tailor\": it allows the "
            "cross-legged position of tailors of old."
        ),
    ),
    "Q": StructureText(
        name="Quadriceps femoris",
        kind=_KIND,
        region="Thigh, anterior compartment",
        count="2 (paired), four heads",
        description=(
            "The bulkiest muscle of the anterior compartment of the thigh, made of four "
            "heads that converge on the patella. It is the only extensor of the knee."
        ),
        sections={
            "parts": [
                "Rectus femoris: the only head crossing two joints (hip and knee)",
                "Vastus lateralis",
                "Vastus medialis",
                "Vastus intermedius, deep, under the rectus femoris",
            ],
            "insertions": [
                "Rectus femoris: anterior inferior iliac spine (straight tendon) and "
                "supra-acetabular groove (reflected tendon)",
                "Vasti: femoral shaft (lips of the linea aspera, anterior and lateral "
                "surfaces)",
                "Common insertion: quadriceps tendon, patella, then patellar ligament on "
                "the tibial tuberosity",
            ],
            "action": [
                "Extends the knee (the only extensor)",
                "Rectus femoris: flexes the hip",
                "Vastus medialis: stabilises the patella and resists lateral dislocation",
            ],
            "innervation": [
                "Femoral nerve (L2-L4)",
            ],
            "vascularisation": [
                "Mainly the lateral circumflex femoral artery (from the deep femoral), "
                "and branches of the femoral artery",
            ],
            "clinical": [
                "Patellar (knee-jerk) reflex: tests mainly L4 (L3-L4)",
                "Femoral nerve palsy: knee extension impossible, falls when going down "
                "stairs",
                "Rapid wasting (especially of vastus medialis) after immobilisation or "
                "knee injury",
                "Osgood-Schlatter disease: painful traction on the tibial tuberosity in "
                "adolescents",
            ],
        },
        fact=(
            "The patella is a sesamoid bone inside the quadriceps tendon: it increases "
            "the muscle's lever arm."
        ),
    ),
    "G": StructureText(
        name="Adductor muscles of the thigh",
        kind=_GROUP,
        region="Thigh, medial compartment",
        count="5 muscles on each side",
        description=(
            "Group of muscles of the medial compartment of the thigh, running from the "
            "pubis and ischium to the femur (and to the tibia for gracilis). From the "
            "front, mainly adductor longus and gracilis are seen."
        ),
        sections={
            "parts": [
                "Pectineus",
                "Adductor longus",
                "Adductor brevis",
                "Adductor magnus",
                "Gracilis",
            ],
            "insertions": [
                "Origin: body and inferior ramus of the pubis, ramus of the ischium, "
                "ischial tuberosity (adductor magnus)",
                "Insertion: pectineal line and medial lip of the linea aspera of the "
                "femur, adductor tubercle (adductor magnus)",
                "Gracilis: medial surface of the tibia, in the pes anserinus",
            ],
            "action": [
                "Adduction of the hip (squeezing the thighs together)",
                "Help flex the hip (pectineus, adductor longus and brevis)",
                "Ischiocondylar (hamstring) part of adductor magnus: extends the hip",
            ],
            "innervation": [
                "Obturator nerve (L2-L4) for most of them",
                "Pectineus: femoral nerve (sometimes also obturator)",
                "Ischiocondylar part of adductor magnus: sciatic nerve (tibial division)",
            ],
            "vascularisation": [
                "Obturator artery, deep femoral artery (perforating arteries) and medial "
                "circumflex femoral artery",
            ],
            "clinical": [
                "Adductor longus forms the medial border of the femoral triangle",
                "Adductor hiatus: the femoral vessels become the popliteal vessels there",
                "Groin pain (pubalgia) and adductor strains, common in footballers",
                "The gracilis tendon is used as a graft to reconstruct the anterior "
                "cruciate ligament (hamstring graft with semitendinosus)",
            ],
        },
        fact=(
            "Gracilis is the only adductor that crosses the knee: it can be harvested "
            "without noticeable loss of function."
        ),
    ),
    "J": StructureText(
        name="Tibialis anterior",
        kind=_KIND,
        region="Leg, anterior compartment",
        count="2 (paired)",
        description=(
            "The most superficial and strongest muscle of the anterior compartment of "
            "the leg, against the lateral surface of the tibia. Its tendon is clearly "
            "visible in front of the ankle when the foot is raised."
        ),
        sections={
            "insertions": [
                "Origin: lateral condyle and upper two thirds of the lateral surface of "
                "the tibia, interosseous membrane",
                "Insertion: medial surface of the medial cuneiform and base of the 1st "
                "metatarsal",
            ],
            "action": [
                "Dorsiflexion of the ankle (it lifts the foot)",
                "Inversion of the foot (adduction and supination)",
                "In walking: lifts the foot during the swing phase and slows its descent "
                "after heel strike",
            ],
            "innervation": [
                "Deep fibular (peroneal) nerve (L4-L5), formerly anterior tibial nerve",
            ],
            "vascularisation": [
                "Anterior tibial artery",
            ],
            "clinical": [
                "Common fibular nerve injury at the fibular neck (cast, fracture, crossed "
                "legs): foot drop and steppage gait",
                "Anterior compartment syndrome of the leg: surgical emergency (fasciotomy)",
                "Weak dorsiflexors: walking on the heels is impossible (L4-L5 roots)",
            ],
        },
        fact=(
            "Its tendon is the most medial and most prominent of the tendons on the "
            "front of the ankle."
        ),
    ),
    "L": StructureText(
        name="Fibularis longus",
        old_names=["peroneus longus"],
        kind=_KIND,
        region="Leg, lateral (fibular) compartment",
        count="2 (paired)",
        description=(
            "Superficial muscle of the lateral compartment of the leg, against the "
            "fibula. Its tendon passes behind the lateral malleolus and then crosses "
            "the sole of the foot under the cuboid."
        ),
        sections={
            "insertions": [
                "Origin: head and upper two thirds of the lateral surface of the fibula",
                "Insertion: base of the 1st metatarsal and medial cuneiform (plantar "
                "surface), after an oblique course across the sole",
            ],
            "action": [
                "Eversion of the foot (abduction and pronation)",
                "Accessory plantar flexion of the ankle",
                "Supports the transverse arch of the foot; with tibialis anterior it forms "
                "a \"stirrup\" under the foot",
            ],
            "innervation": [
                "Superficial fibular nerve (L5-S1), formerly musculocutaneous nerve of the leg",
            ],
            "vascularisation": [
                "Branches of the fibular artery and of the anterior tibial artery",
            ],
            "clinical": [
                "Protects the ankle against inversion sprains (lateral collateral ligament)",
                "Dislocation of the fibular tendons in front of the lateral malleolus",
                "Common fibular nerve injury: foot in equinovarus (loss of evertors and "
                "dorsiflexors)",
            ],
        },
        fact=(
            "Its tendon changes direction twice, behind the lateral malleolus and under "
            "the cuboid, as if over pulleys."
        ),
    ),
    "C": StructureText(
        name="Triceps surae",
        kind=_KIND,
        region="Leg, posterior compartment (calf), seen medially from the front",
        count="2 (paired), three heads",
        description=(
            "Calf muscle made of the two heads of gastrocnemius and the soleus, joined "
            "by the calcaneal tendon. From the front, the bulge of the medial head of "
            "gastrocnemius is seen medial to the tibia."
        ),
        sections={
            "parts": [
                "Gastrocnemius, medial and lateral heads, superficial and crossing two "
                "joints",
                "Soleus, deep, crossing one joint",
            ],
            "insertions": [
                "Gastrocnemius: posterior surfaces of the medial and lateral femoral "
                "condyles",
                "Soleus: head and posterior surface of the fibula, soleal line of the "
                "tibia, tendinous arch of soleus",
                "Insertion: calcaneal (Achilles) tendon on the posterior surface of the "
                "calcaneal tuberosity",
            ],
            "action": [
                "Powerful plantar flexion of the ankle: walking, running, jumping, "
                "standing on tiptoe",
                "Gastrocnemius: helps flex the knee",
                "Soleus: postural muscle (slow fibres) and calf venous pump",
            ],
            "innervation": [
                "Tibial nerve (S1-S2)",
            ],
            "vascularisation": [
                "Sural arteries (from the popliteal artery), branches of the posterior "
                "tibial and fibular arteries",
            ],
            "clinical": [
                "Ankle (Achilles) reflex: tests the S1 root",
                "Calcaneal tendon rupture: squeezing the calf no longer produces plantar "
                "flexion (Thompson test)",
                "Tear of the medial head of gastrocnemius (\"tennis leg\")",
                "The soleal veins are a common starting point of deep vein thrombosis",
            ],
        },
        fact=(
            "The calcaneal tendon is the thickest and strongest tendon in the human body."
        ),
    ),
}
