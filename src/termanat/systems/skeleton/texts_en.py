"""English texts (Terminologia Anatomica English equivalents)."""

from __future__ import annotations

from ...model import StructureText
from ._bone import BoneText

TEXTS: dict[str, StructureText] = {
    "S": BoneText(
        name="Skull",
        region="Head",
        count="21 fused bones: 8 neurocranial + 13 facial (mandible counted apart)",
        kind="Flat bones for the vault, irregular bones for the base and face",
        description=(
            "The neurocranium (braincase) protects the brain; the viscerocranium "
            "(facial skeleton) holds the sense organs and the start of the airway "
            "and digestive tract. Neurocranium: frontal, 2 parietals, 2 temporals, "
            "occipital, sphenoid, ethmoid. Face: 2 maxillae, 2 zygomatic, 2 nasal, "
            "2 lacrimal, 2 palatine, 2 inferior nasal conchae, vomer."
        ),
        landmarks=[
            "Coronal (frontal / parietals), sagittal (between the parietals) and "
            "lambdoid (parietals / occipital) sutures; bregma and lambda where they meet",
            "Pterion: junction of the frontal, parietal, temporal and greater wing of "
            "the sphenoid",
            "Foramen magnum and occipital condyles (occipital bone)",
            "Mastoid process and external acoustic meatus (temporal bone)",
            "Sella turcica of the sphenoid, which houses the pituitary gland",
            "Cribriform plate of the ethmoid, crossed by the olfactory nerves",
            "Orbits, nasal cavity, anterior, middle and posterior cranial fossae",
        ],
        joints=[
            "Sutures: fibrous joints (synarthroses), almost immobile",
            "Temporomandibular joint (TMJ) with the mandible",
            "Atlanto-occipital joint with the atlas (C1)",
        ],
        clinical=[
            "The pterion is thin and overlies the middle meningeal artery: a blow "
            "there can cause an extradural (epidural) haematoma",
            "Basal skull fracture: periorbital bruising (\"raccoon eyes\"), bruising "
            "behind the ear (Battle's sign), cerebrospinal fluid leaking from the "
            "nose or ear",
            "Newborn fontanelles: posterior (lambda) closes around 2 months, anterior "
            "(bregma) around 18-24 months",
        ],
        fact=(
            "Fontanelles let the skull change shape during birth and let the brain "
            "grow during the first months."
        ),
    ),
    "M": BoneText(
        name="Mandible",
        region="Head",
        count="1 (single, midline bone)",
        kind="Irregular bone",
        description=(
            "The horseshoe-shaped lower jaw. It holds the lower teeth and is the only "
            "skull bone that moves at a synovial joint (apart from the ear ossicles)."
        ),
        landmarks=[
            "Body (with the alveolar part) and two rami meeting at the angle of the "
            "mandible",
            "Condylar process (head and neck of the mandible) behind, coronoid process "
            "in front, separated by the mandibular notch",
            "Mental symphysis and mental protuberance",
            "Mental foramen (mental nerve and vessels)",
            "Mandibular foramen on the inner side of the ramus (inferior alveolar nerve)",
        ],
        joints=[
            "Temporomandibular joint (TMJ): synovial, bicondylar, with an articular "
            "disc; the head of the mandible sits in the mandibular fossa of the "
            "temporal bone",
            "Dento-alveolar joints (gomphoses) with the teeth",
        ],
        clinical=[
            "Muscles of mastication: masseter (outer ramus), temporalis (coronoid "
            "process), medial and lateral pterygoids",
            "Fractures are often double because the mandible forms a ring with the "
            "skull base: look for a second one (often condylar)",
            "TMJ dislocation: the head slips in front of the articular tubercle and "
            "the mouth is stuck open",
            "Dental anaesthesia of the inferior alveolar nerve at the mandibular foramen",
        ],
        fact="It is the largest and strongest bone of the face.",
    ),
    "C": BoneText(
        name="Cervical vertebrae",
        region="Neck",
        count="7 (C1 to C7)",
        kind="Irregular bones",
        description=(
            "The small, very mobile vertebrae of the neck. They form the cervical "
            "lordosis, carry the head and protect the cervical spinal cord."
        ),
        landmarks=[
            "Foramen transversarium in each transverse process: passage of the "
            "vertebral artery (C6 to C1)",
            "Bifid spinous processes from C3 to C6; uncinate processes on the edges "
            "of the upper endplate",
            "C1, atlas: no body and no spinous process, two lateral masses joined by "
            "anterior and posterior arches",
            "C2, axis: the dens (odontoid process), pivot of rotation",
            "C7, vertebra prominens: long, non-bifid spinous process, palpable at the "
            "base of the neck",
        ],
        joints=[
            "Atlanto-occipital (occipital condyles / lateral masses of C1): flexion "
            "and extension, the \"yes\" movement",
            "Atlanto-axial (dens of C2 / anterior arch of C1): rotation, the \"no\" "
            "movement",
            "No intervertebral disc between occiput and C1 or between C1 and C2; discs "
            "start at C2-C3",
        ],
        clinical=[
            "Jefferson fracture: burst fracture of the atlas from axial loading "
            "(diving into shallow water)",
            "Fracture of the dens; \"hangman's\" fracture of the pars of C2",
            "Whiplash injuries; cervicobrachial neuralgia from uncovertebral "
            "osteoarthritis",
        ],
        fact="Almost all mammals have 7 cervical vertebrae, giraffes and mice alike.",
    ),
    "X": BoneText(
        name="Scapula",
        region="Shoulder (shoulder girdle)",
        count="2",
        kind="Flat bone",
        description=(
            "A flat triangular bone lying on the back of the thorax, between the 2nd "
            "and 7th ribs. From the front only the acromion is visible, at the top of "
            "the shoulder."
        ),
        landmarks=[
            "Spine of the scapula, ending laterally as the acromion",
            "Supraspinous and infraspinous fossae (back), subscapular fossa (front, "
            "costal surface)",
            "Glenoid cavity, rimmed by the glenoid labrum",
            "Coracoid process: attachment of pectoralis minor, coracobrachialis and "
            "the short head of biceps",
            "Suprascapular notch (suprascapular nerve); inferior angle at the level "
            "of T7",
        ],
        joints=[
            "Glenohumeral: ball-and-socket, the most mobile joint of the body",
            "Acromioclavicular",
            "Scapulothoracic: a gliding plane, without true articular surfaces",
        ],
        clinical=[
            "Rotator cuff: supraspinatus, infraspinatus, teres minor, subscapularis",
            "Anterior shoulder dislocation (the most common): check the axillary "
            "nerve (sensation over the deltoid)",
            "Winged scapula: paralysis of serratus anterior from injury to the long "
            "thoracic nerve",
        ],
        fact=(
            "The glenoid cavity is small and shallow: the shoulder trades stability "
            "for mobility."
        ),
    ),
    "L": BoneText(
        name="Clavicle",
        region="Shoulder (shoulder girdle)",
        count="2",
        kind="Long bone (atypical: no clear medullary cavity)",
        description=(
            "An S-shaped horizontal bone between the sternum and the acromion. It "
            "holds the upper limb away from the thorax and is the only bony link "
            "between the upper limb and the trunk."
        ),
        landmarks=[
            "Sternal (medial) end and flattened acromial (lateral) end",
            "Two curves: convex forward on its medial two thirds, concave forward on "
            "its lateral third",
            "Conoid tubercle and trapezoid line (coracoclavicular ligaments)",
            "Groove for subclavius on the underside",
        ],
        joints=[
            "Sternoclavicular: saddle joint with an articular disc",
            "Acromioclavicular: plane joint",
        ],
        clinical=[
            "Very common fracture (fall on the shoulder or hand), mostly in the "
            "middle third",
            "The medial fragment is pulled up (sternocleidomastoid), the lateral "
            "fragment sags under the weight of the arm",
            "Lies just in front of the subclavian vessels and brachial plexus",
            "Acromioclavicular separation: \"piano key\" sign",
        ],
        fact=(
            "It is the first bone to ossify in the embryo (weeks 5-6), and its "
            "sternal end is one of the last to fuse, around age 25."
        ),
    ),
    "T": BoneText(
        name="Sternum",
        region="Thorax",
        count="1 (single, midline bone)",
        kind="Flat bone",
        description=(
            "The flat bone at the front of the chest, shaped like a sword: manubrium "
            "(handle), body (blade) and xiphoid process (tip)."
        ),
        landmarks=[
            "Jugular (suprasternal) notch on top of the manubrium; clavicular notches",
            "Sternal angle (of Louis), the manubrium-body junction: level of the 2nd "
            "costal cartilage and of the T4-T5 disc",
            "Costal notches for the cartilages of the first 7 ribs",
            "Xiphoid process, cartilaginous and ossifying late",
        ],
        joints=[
            "Sternoclavicular",
            "Sternocostal with costal cartilages 1 to 7 (the 1st is a synchondrosis)",
            "Manubriosternal (symphysis)",
        ],
        clinical=[
            "The sternal angle is used to count ribs: the 2nd rib attaches there. "
            "It also marks the tracheal bifurcation and the aortic arch",
            "Sternal puncture for bone marrow aspiration",
            "Median sternotomy: the usual approach for heart surgery",
            "CPR: compress the lower half of the sternum",
        ],
        fact=(
            "In adults the sternum keeps red marrow that makes blood cells "
            "throughout life."
        ),
    ),
    "R": BoneText(
        name="Ribs",
        region="Thorax",
        count="24 (12 pairs)",
        kind="Flat bones (flattened, curved long bones)",
        description=(
            "Bony arches that, with the thoracic vertebrae and sternum, form the "
            "ribcage. They protect the heart and lungs and take part in breathing."
        ),
        landmarks=[
            "True ribs (1-7): joined directly to the sternum by their cartilage",
            "False ribs (8-10 in the strict sense, 8-12 in the broad sense): their "
            "cartilage joins the one above, forming the costal margin",
            "Floating ribs (11-12): free at the front",
            "Typical rib: head (2 facets, only one for ribs 1, 11 and 12), neck, "
            "tubercle, angle, shaft",
            "Costal groove on the lower inner edge: intercostal neurovascular bundle "
            "(vein, artery, nerve from top to bottom)",
            "1st rib: short, broad and flat, scalene tubercle between the grooves for "
            "the subclavian vein and artery",
        ],
        joints=[
            "Costovertebral: the head meets the bodies of two vertebrae (same level "
            "and the one above), except ribs 1, 11 and 12 (only one)",
            "Costotransverse: the tubercle meets the transverse process (absent for "
            "ribs 11 and 12)",
            "Sternocostal and costochondral at the front",
        ],
        clinical=[
            "Pleural puncture or chest drain along the upper edge of the lower rib, "
            "to avoid the intercostal bundle",
            "Flail chest: several ribs broken in two places, the segment moves the "
            "wrong way when breathing (paradoxical breathing)",
            "Extra cervical rib: thoracic outlet syndrome",
        ],
        fact=(
            "Men and women have the same number of ribs, 12 pairs, despite an old "
            "belief."
        ),
    ),
    "H": BoneText(
        name="Humerus",
        region="Arm",
        count="2",
        kind="Long bone",
        description=(
            "The single bone of the arm, from the shoulder to the elbow. Its "
            "flattened lower end is called the humeral paddle."
        ),
        landmarks=[
            "Humeral head (faces up, in and back), anatomical neck",
            "Greater tubercle (supraspinatus, infraspinatus, teres minor) and lesser "
            "tubercle (subscapularis)",
            "Intertubercular sulcus: tendon of the long head of biceps",
            "Surgical neck, just below the tubercles",
            "Deltoid tuberosity; radial groove on the back of the shaft",
            "Capitulum (meets the radius) and trochlea (meets the ulna)",
            "Lateral and medial epicondyles; olecranon fossa (back), coronoid and "
            "radial fossae (front)",
        ],
        joints=[
            "Glenohumeral (shoulder): ball-and-socket",
            "Elbow: humero-ulnar (hinge) and humeroradial",
        ],
        clinical=[
            "Surgical neck fracture (elderly): risk to the axillary nerve",
            "Shaft fracture: the radial nerve can be injured in its groove (wrist drop)",
            "Supracondylar fracture in children: risk to the brachial artery and the "
            "median nerve",
            "Ulnar nerve behind the medial epicondyle",
        ],
        fact=(
            "Hitting your \"funny bone\" actually means pinching the ulnar nerve "
            "against the medial epicondyle of the humerus."
        ),
    ),
    "D": BoneText(
        name="Radius",
        region="Forearm",
        count="2",
        kind="Long bone",
        description=(
            "The lateral bone of the forearm (thumb side in anatomical position). It "
            "rotates around the ulna for pronation and supination, and carries the "
            "carpus."
        ),
        landmarks=[
            "Cylindrical radial head: articular fovea on top, articular circumference "
            "around",
            "Radial neck; radial tuberosity (biceps brachii attachment)",
            "Interosseous border (interosseous membrane with the ulna)",
            "Radial styloid process, about 1 cm lower than the ulnar one",
            "Ulnar notch; carpal articular surface (scaphoid and lunate)",
            "Dorsal (Lister's) tubercle",
        ],
        joints=[
            "Humeroradial (capitulum)",
            "Proximal and distal radio-ulnar, both pivot joints: at the top, the head "
            "turns in the ring formed by the radial notch of the ulna and the annular "
            "ligament",
            "Radiocarpal (wrist): ellipsoid",
        ],
        clinical=[
            "Colles fracture: distal end, dorsal displacement (\"dinner fork\" "
            "deformity), fall on the palm in an elderly osteoporotic person",
            "Smith fracture: same level, palmar displacement",
            "Pulled elbow in young children: when the arm is pulled, the head partly "
            "slips out of the annular ligament, which gets caught in the joint",
            "Galeazzi fracture: radial shaft + distal radio-ulnar dislocation",
        ],
        fact="The radial pulse is felt in front of the lower end of the radius.",
    ),
    "U": BoneText(
        name="Ulna",
        region="Forearm",
        count="2",
        kind="Long bone",
        description=(
            "The medial bone of the forearm (little-finger side). It stays still "
            "during pronation and supination and forms most of the elbow."
        ),
        landmarks=[
            "Olecranon (point of the elbow, triceps attachment) and coronoid process",
            "Trochlear notch (with the humeral trochlea)",
            "Radial notch (with the radial head)",
            "Ulnar tuberosity (brachialis attachment)",
            "Interosseous border; head of the ulna and ulnar styloid process below",
        ],
        joints=[
            "Humero-ulnar: hinge (elbow flexion and extension)",
            "Proximal and distal radio-ulnar",
            "No direct contact with the carpus: the triangular fibrocartilage complex "
            "lies in between",
        ],
        clinical=[
            "Olecranon fracture: the triceps pulls the fragments apart",
            "Monteggia fracture: ulnar shaft + dislocation of the radial head",
            "The ulnar nerve runs behind the medial epicondyle, right next to the "
            "olecranon",
        ],
        fact="The point of the elbow you lean on is the olecranon of the ulna.",
    ),
    "A": BoneText(
        name="Hand bones",
        region="Hand",
        count="54 (27 per hand): 8 carpals, 5 metacarpals, 14 phalanges",
        kind="Short bones (carpus), long bones (metacarpals and phalanges)",
        description=(
            "Carpus (wrist), metacarpus (palm) and phalanges (fingers). Each finger "
            "has 3 phalanges (proximal, middle, distal) except the thumb, which has 2."
        ),
        landmarks=[
            "Proximal carpal row, lateral to medial: scaphoid, lunate, triquetrum, "
            "pisiform",
            "Distal row: trapezium, trapezoid, capitate, hamate",
            "Ulnar (Guyon's) canal: between the pisiform (medial) and the hook of the "
            "hamate (lateral); ulnar nerve and artery",
            "Carpal tunnel: carpal groove closed by the flexor retinaculum; holds the "
            "median nerve and 9 flexor tendons",
            "Anatomical snuffbox: the scaphoid can be felt in its floor",
        ],
        joints=[
            "Radiocarpal and midcarpal (wrist)",
            "Carpometacarpal, including the saddle-shaped trapeziometacarpal joint of "
            "the thumb, which allows opposition",
            "Metacarpophalangeal, proximal and distal interphalangeal",
        ],
        clinical=[
            "Scaphoid fracture (the most common carpal fracture): snuffbox tenderness, "
            "risk of non-union and necrosis of the proximal pole (retrograde blood "
            "supply)",
            "Carpal tunnel syndrome: compression of the median nerve",
            "Fracture of the 5th metacarpal neck: \"boxer's fracture\"",
        ],
        fact=(
            "Your two hands and wrists hold more than a quarter of all the bones in "
            "your body."
        ),
    ),
    "V": BoneText(
        name="Lumbar vertebrae",
        region="Lower back",
        count="5 (L1 to L5)",
        kind="Irregular bones",
        description=(
            "The vertebrae of the lower back, the most massive because they carry the "
            "weight of the trunk. They form the lumbar lordosis. (The 12 thoracic "
            "vertebrae are hidden behind the sternum in this front view.)"
        ),
        landmarks=[
            "Large, kidney-shaped body",
            "No foramen transversarium and no costal facets",
            "Costal processes (\"transverse\" processes), remnants of ribs; mammillary "
            "and accessory processes",
            "Rectangular, horizontal spinous process",
            "Articular processes facing in the sagittal plane: little rotation",
        ],
        joints=[
            "Intervertebral discs (symphyses) between the bodies",
            "Zygapophysial (facet) joints between articular processes",
            "Lumbosacral (L5-S1)",
        ],
        clinical=[
            "The spinal cord ends around L1-L2 in adults: lumbar puncture at L3-L4 or "
            "L4-L5 (Tuffier's line, between the iliac crests, crosses L4 or the "
            "L4-L5 space)",
            "Disc herniation mostly at L4-L5 and L5-S1: L5 or S1 sciatica",
            "Spondylolisthesis: L5 slipping forward on S1, often from a pars defect",
        ],
        fact=(
            "Low back pain is one of the leading causes of sick leave and of "
            "visits to the family doctor."
        ),
    ),
    "Y": BoneText(
        name="Sacrum and coccyx",
        region="Pelvis",
        count="1 + 1 (5 sacral and 3 to 5 coccygeal vertebrae fused)",
        kind="Irregular bones",
        description=(
            "The sacrum is a triangle of 5 fused vertebrae wedged between the two hip "
            "bones. The coccyx (tailbone), remnant of a tail, extends it downward."
        ),
        landmarks=[
            "Base of the sacrum (top of S1) with the promontory; alae (wings)",
            "Pelvic surface: 4 pairs of anterior sacral foramina",
            "Dorsal surface: median sacral crest, posterior sacral foramina",
            "Auricular surfaces on the sides (sacroiliac joint)",
            "Sacral canal ending at the sacral hiatus",
        ],
        joints=[
            "Lumbosacral (L5-S1)",
            "Sacroiliac (synovial, very little movement)",
            "Sacrococcygeal",
        ],
        clinical=[
            "Promontory: obstetric landmark (obstetric conjugate of the pelvic inlet)",
            "Sacral hiatus: route for caudal epidural anaesthesia",
            "Coccydynia (tailbone pain) after a fall on the buttocks",
        ],
        fact="The coccyx is the remnant of our ancestors' tail.",
    ),
    "P": BoneText(
        name="Hip bone",
        region="Pelvis (pelvic girdle)",
        count="2",
        kind="Flat (and irregular) bone",
        description=(
            "Each hip bone is made of three bones, the ilium, ischium and pubis, which "
            "fuse at the acetabulum during adolescence (Y-shaped cartilage). With the "
            "sacrum and coccyx, the two hip bones form the pelvis."
        ),
        landmarks=[
            "Iliac crest; anterior superior iliac spine (ASIS: sartorius, inguinal "
            "ligament) and anterior inferior iliac spine (rectus femoris)",
            "Posterior superior iliac spine (dimples of Venus); iliac fossa",
            "Acetabulum: lunate surface, acetabular fossa and notch",
            "Obturator foramen, closed by the obturator membrane",
            "Ischial tuberosity (hamstrings, what you sit on); ischial spine; greater "
            "and lesser sciatic notches",
            "Pubic tubercle, symphyseal surface; arcuate line (pelvic inlet)",
        ],
        joints=[
            "Hip (coxofemoral): ball-and-socket",
            "Sacroiliac",
            "Pubic symphysis (fibrocartilage)",
        ],
        clinical=[
            "Bone marrow biopsy from the posterior iliac crest",
            "Intramuscular injection in the upper outer quadrant of the buttock, to "
            "avoid the sciatic nerve",
            "Pelvic fracture: risk of major bleeding",
            "Female pelvis: wider, rounder inlet and a wider subpubic angle",
        ],
        fact="A skeleton's sex can often be told from the pelvis alone.",
    ),
    "F": BoneText(
        name="Femur",
        region="Thigh",
        count="2",
        kind="Long bone",
        description=(
            "The single bone of the thigh, from the hip to the knee. It is the "
            "longest and strongest bone of the body."
        ),
        landmarks=[
            "Femoral head (fovea: ligament of the head of the femur), neck",
            "Neck-shaft angle of about 125-130°; neck anteversion of about 15°",
            "Greater trochanter (gluteus medius and minimus), lesser trochanter "
            "(iliopsoas)",
            "Intertrochanteric line in front, intertrochanteric crest behind",
            "Linea aspera on the back of the shaft (adductors, vasti)",
            "Medial and lateral condyles, intercondylar fossa, epicondyles, adductor "
            "tubercle, patellar surface (trochlea)",
        ],
        joints=[
            "Hip (coxofemoral)",
            "Tibiofemoral and patellofemoral (knee)",
        ],
        clinical=[
            "Femoral neck fracture in the elderly: shortened, externally rotated "
            "limb; risk of avascular necrosis of the head (circumflex arteries)",
            "Shaft fracture: heavy bleeding (1 L or more), possible shock",
            "Coxa vara / coxa valga: decreased or increased neck-shaft angle",
        ],
        fact="It is about a quarter of a person's height.",
    ),
    "K": BoneText(
        name="Patella",
        region="Knee",
        count="2",
        kind="Sesamoid bone",
        description=(
            "A triangular bone inside the quadriceps tendon, in front of the knee. It "
            "protects the joint and increases the lever arm of the quadriceps."
        ),
        landmarks=[
            "Base at the top (quadriceps tendon), apex at the bottom (patellar ligament)",
            "Front surface palpable under the skin",
            "Posterior articular surface: lateral (larger) and medial facets, "
            "separated by a ridge",
        ],
        joints=["Patellofemoral, with the patellar surface (trochlea) of the femur"],
        clinical=[
            "Lateral dislocation of the patella, especially in teenage girls",
            "Fracture from a fall on the knee; do not confuse with a bipartite "
            "patella (normal variant)",
            "Knee-jerk (patellar) reflex: tap the patellar ligament, roots L3-L4 "
            "(mainly L4)",
        ],
        fact="It is the largest sesamoid bone: a bone that grows inside a tendon.",
    ),
    "B": BoneText(
        name="Tibia",
        region="Leg",
        count="2",
        kind="Long bone",
        description=(
            "The large, medial bone of the leg. It carries the body's weight from the "
            "knee to the ankle."
        ),
        landmarks=[
            "Tibial plateau: medial and lateral condyles",
            "Intercondylar eminence (tibial spines); intercondylar areas where the "
            "cruciate ligaments attach",
            "Tibial tuberosity: attachment of the patellar ligament",
            "Anterior border (shin) and medial surface, just under the skin",
            "Soleal line on the back",
            "Medial malleolus; fibular notch below",
        ],
        joints=[
            "Tibiofemoral (knee)",
            "Proximal (synovial) and distal (syndesmosis) tibiofibular joints",
            "Talocrural (ankle) with the talus",
        ],
        clinical=[
            "Frequent fractures, often open because the medial surface is right "
            "under the skin",
            "Osgood-Schlatter disease: painful tibial tuberosity in sporty teenagers",
            "Emergency intraosseous access in the proximal tibia",
        ],
        fact=(
            "In Latin, tibia means both the shinbone and a flute, an instrument "
            "sometimes carved from bone."
        ),
    ),
    "I": BoneText(
        name="Fibula",
        region="Leg",
        count="2",
        kind="Long bone",
        description=(
            "The thin, lateral bone of the leg. It carries little weight but anchors "
            "many muscles and stabilises the ankle."
        ),
        landmarks=[
            "Head of the fibula with its apex; neck of the fibula",
            "Thin, triangular shaft",
            "Lateral malleolus: reaches lower than the medial malleolus",
        ],
        joints=[
            "Proximal and distal tibiofibular",
            "Talocrural (ankle) through the lateral malleolus",
            "Does not meet the femur: it takes no part in the knee",
        ],
        clinical=[
            "The common fibular nerve winds around the fibular neck: a fracture or a "
            "tight cast can cause foot drop (steppage gait)",
            "Ankle fractures (malleolar, bimalleolar)",
            "Vascularised fibula graft to rebuild the mandible",
        ],
        fact=(
            "A long segment can be removed without affecting walking, hence its use "
            "as a graft."
        ),
    ),
    "O": BoneText(
        name="Foot bones",
        region="Foot",
        count="52 (26 per foot): 7 tarsals, 5 metatarsals, 14 phalanges",
        kind="Short bones (tarsus), long bones (metatarsals and phalanges)",
        description=(
            "Tarsus, metatarsus and phalanges form the arches of the foot, which "
            "absorb and pass the body's weight to the ground."
        ),
        landmarks=[
            "Hindfoot: talus (no muscle attachments) and calcaneus",
            "Midfoot: navicular, cuboid, medial, intermediate and lateral cuneiforms",
            "Trochlea of the talus, held in the tibiofibular mortise",
            "Calcaneal tuberosity (calcaneal / Achilles tendon); sustentaculum tali",
            "Medial and lateral longitudinal arches, transverse arch",
        ],
        joints=[
            "Talocrural (ankle): dorsiflexion and plantarflexion",
            "Subtalar: inversion and eversion",
            "Transverse tarsal (Chopart) and tarsometatarsal (Lisfranc)",
            "Metatarsophalangeal and interphalangeal",
        ],
        clinical=[
            "Lateral ankle sprain: anterior talofibular ligament",
            "Fracture of the base of the 5th metatarsal (avulsion by fibularis brevis)",
            "Stress fracture of the 2nd-3rd metatarsals (\"march fracture\")",
            "Hallux valgus (bunion)",
        ],
        fact="The calcaneus (heel bone) is the largest bone of the foot.",
    ),
}
