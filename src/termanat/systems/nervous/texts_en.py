"""English texts (same content, sections and item counts as the French ones)."""

from __future__ import annotations

from ...model import StructureText

TEXTS: dict[str, StructureText] = {
    "B": StructureText(
        name="Cerebrum (cerebral hemispheres)",
        kind="Central nervous system: telencephalon",
        region="Supratentorial compartment of the cranial cavity",
        count="2 hemispheres",
        description=(
            "Largest part of the brain, made of two hemispheres separated by the "
            "longitudinal fissure and joined by the corpus callosum. The cortex (grey "
            "matter) covers the white matter and the basal nuclei."
        ),
        sections={
            "parts": [
                "Frontal, parietal, temporal and occipital lobes, and the insula deep in the lateral sulcus",
                "Central sulcus (formerly fissure of Rolando) between the frontal and parietal lobes",
                "Lateral sulcus (formerly Sylvian fissure) above the temporal lobe",
                "Interhemispheric commissures, the corpus callosum being the largest",
                "Basal nuclei (caudate nucleus, putamen, globus pallidus) and lateral ventricles",
            ],
            "function": [
                "Precentral gyrus: primary motor area, voluntary control of the opposite half of the body",
                "Postcentral gyrus: primary somatosensory area (sensation of the opposite half of the body)",
                "Broca's area (inferior frontal gyrus): speech production, dominant hemisphere",
                "Wernicke's area (posterior part of the superior temporal gyrus): comprehension",
                "Occipital lobe: vision (primary visual cortex around the calcarine sulcus)",
            ],
            "vascularisation": [
                "Anterior and middle cerebral arteries, branches of the internal carotid artery",
                "Posterior cerebral artery, terminal branch of the basilar artery",
                "Cerebral arterial circle (circle of Willis) joining them at the base",
            ],
            "clinical": [
                "Motor pathways cross (pyramidal decussation): a lesion of one "
                "hemisphere causes hemiplegia on the opposite side",
                "Middle cerebral artery stroke: contralateral hemiplegia predominating "
                "in face and arm, aphasia if the dominant hemisphere is involved",
            ],
        },
        fact=(
            "Penfield's homunculus shows that the hand and face take up a "
            "disproportionate share of the motor and sensory cortex."
        ),
    ),
    "C": StructureText(
        name="Cerebellum",
        kind="Central nervous system: metencephalon",
        region="Posterior cranial fossa, under the tentorium cerebelli",
        count="1 (unpaired, midline)",
        description=(
            "Organ of coordination, lying behind the brainstem to which it is joined "
            "by three pairs of peduncles. It is hidden in an anterior view: it is "
            "drawn here schematically."
        ),
        sections={
            "parts": [
                "Midline vermis and two lateral cerebellar hemispheres",
                "Cortex folded into folia, and deep nuclei including the dentate nucleus",
                "Superior (midbrain), middle (pons) and inferior (medulla oblongata) peduncles",
            ],
            "relations": [
                "In front: the fourth ventricle, separating it from the pons and medulla oblongata",
                "Above: the tentorium cerebelli, separating it from the occipital lobes",
                "Supplied by the superior, anterior inferior and posterior inferior cerebellar arteries",
            ],
            "function": [
                "Balance: archicerebellum (flocculonodular lobe), or vestibulocerebellum, linked to the vestibular system",
                "Tone and posture: paleocerebellum (spinocerebellum); fine coordination: neocerebellum (cerebrocerebellum)",
                "Motor learning; it acts on the same side of the body (ipsilateral control)",
            ],
            "clinical": [
                "Ipsilateral cerebellar syndrome: ataxia, wide-based stance and gait",
                "Dysmetria, dysdiadochokinesia, intention tremor, dysarthria, nystagmus",
                "Herniation of the cerebellar tonsils into the foramen magnum compresses the medulla oblongata",
            ],
        },
        fact=(
            "The cerebellum is only about 10% of the brain's volume but contains "
            "more than half of its neurons."
        ),
    ),
    "T": StructureText(
        name="Brainstem",
        kind="Central nervous system",
        region="Posterior cranial fossa, on the clivus, between cerebrum and spinal cord",
        count="1 (unpaired, midline)",
        old_names=["bulb (medulla oblongata)", "pons Varolii (pons)"],
        description=(
            "Part of the brain linking the cerebrum to the spinal cord. The great "
            "motor and sensory pathways run through it and it holds the nuclei of "
            "most cranial nerves."
        ),
        sections={
            "parts": [
                "From top to bottom: midbrain, pons and medulla oblongata",
                "Pyramids and their decussation on the front of the medulla oblongata",
                "Superficial origin: III and IV at the midbrain, V at the pons",
                "VI, VII and VIII at the pontomedullary sulcus; IX, X, XI and XII at the medulla oblongata",
            ],
            "function": [
                "Passage of ascending (sensory) and descending (pyramidal) pathways",
                "Nuclei of cranial nerves III to XII (the nucleus of the spinal accessory lies in the cervical cord)",
                "Vital centres of the medulla oblongata: breathing, heart rate, blood pressure",
                "Reticular formation: arousal and wakefulness",
            ],
            "clinical": [
                "Crossed (alternating) syndromes: cranial nerve palsy on the side of the "
                "lesion and hemiplegia on the opposite side",
                "Wallenberg syndrome: lateral medullary infarction (vertebral or "
                "posterior inferior cerebellar artery)",
                "Absence of all brainstem reflexes is a criterion of brain death",
            ],
        },
        fact=(
            "A lesion of the medulla oblongata can be immediately fatal, because it "
            "houses the breathing centres."
        ),
    ),
    "M": StructureText(
        name="Spinal cord",
        kind="Central nervous system",
        region="Vertebral canal, from the foramen magnum to the L1-L2 vertebra",
        count="1 (unpaired, midline), 31 pairs of spinal nerves",
        description=(
            "Nerve cord about 45 cm long, wrapped in the meninges (dura mater, "
            "arachnoid, pia mater). It continues the medulla oblongata and ends as "
            "the conus medullaris, extended by the filum terminale."
        ),
        sections={
            "parts": [
                "Central H- or butterfly-shaped grey matter, surrounded by white matter",
                "Sensory posterior horn, motor anterior horn, sympathetic lateral horn (T1-L2)",
                "White matter in posterior, lateral and anterior funiculi (fibre tracts)",
                "Cervical (upper limbs) and lumbosacral (lower limbs) enlargements",
            ],
            "landmarks": [
                "In adults, the conus medullaris ends at the level of the L1-L2 disc",
                "In newborns, the cord reaches lower, around L3",
                "31 pairs of spinal nerves: 8 cervical, 12 thoracic, 5 lumbar, 5 sacral, 1 coccygeal",
                "Each spinal nerve arises from a posterior root (with a spinal "
                "ganglion) and an anterior root",
            ],
            "function": [
                "Conduction of information between the brain and the rest of the body",
                "Centres of spinal reflexes (deep tendon reflexes, visceral reflexes)",
            ],
            "clinical": [
                "Lumbar puncture is done below the cord, at L3-L4 or L4-L5 (Tuffier's "
                "line joining the iliac crests, around L4)",
                "Brown-Séquard syndrome (hemisection): motor and deep sensory loss on "
                "the side of the lesion, pain and temperature loss on the opposite side",
                "Complete transection causes paraplegia or tetraplegia below the level of the lesion",
            ],
        },
        fact=(
            "The cord is shorter than the vertebral canal: the spine grows more than "
            "the cord, hence the oblique course of the lumbar and sacral roots."
        ),
    ),
    "Q": StructureText(
        name="Cauda equina",
        kind="Spinal nerve roots",
        region="Lumbar and sacral vertebral canal, below the conus medullaris (L2 to S2)",
        description=(
            "Bundle of lumbar, sacral and coccygeal roots running down in the dural "
            "sac below the end of the cord before leaving through their "
            "intervertebral and sacral foramina. The filum terminale lies in the middle."
        ),
        sections={
            "parts": [
                "Anterior and posterior roots of nerves L2 to Co1, bathed in cerebrospinal fluid",
                "Filum terminale, an extension of the pia mater, anchored to the coccyx",
                "Dural sac (lumbar cistern), ending around S2",
            ],
            "relations": [
                "In front: lumbar vertebral bodies and intervertebral discs",
                "Behind: laminae and ligamenta flava, the route of a lumbar puncture",
            ],
            "clinical": [
                "Lumbar puncture is low-risk at this level: the floating roots move away from the needle",
                "Cauda equina syndrome (large disc herniation): saddle anaesthesia, "
                "sphincter disorders, lower limb weakness",
                "It is a surgical emergency; the deficit is of peripheral type (flaccid "
                "paralysis, areflexia)",
            ],
        },
        fact=(
            "It is named after the look of these roots which, once the dura is "
            "opened, resemble a horse's tail."
        ),
    ),
    "V": StructureText(
        name="Vagus nerve (X)",
        kind="Mixed cranial nerve (10th pair)",
        region="Neck, thorax and abdomen",
        count="2 (right and left)",
        old_names=["pneumogastric nerve"],
        description=(
            "Longest cranial nerve, with a 'wandering' course down into the abdomen. "
            "It carries most of the body's parasympathetic fibres, as well as motor "
            "and sensory fibres."
        ),
        sections={
            "course": [
                "Leaves the skull through the jugular foramen, with nerves IX and XI",
                "Runs down in the carotid sheath, posteriorly, between the internal "
                "jugular vein and the carotid artery",
                "Passes behind the root of the lung, then forms the oesophageal plexus",
                "Crosses the diaphragm through the oesophageal hiatus (T10) as anterior "
                "and posterior vagal trunks",
            ],
            "branches": [
                "Pharyngeal branches and superior laryngeal nerve",
                "Recurrent laryngeal nerve: under the subclavian artery on the right, "
                "under the aortic arch on the left",
                "Cardiac, pulmonary and oesophageal branches",
                "Gastric, coeliac and hepatic branches in the abdomen",
            ],
            "territory": [
                "Motor: muscles of the pharynx, larynx and soft palate (except tensor veli palatini)",
                "Sensory: larynx, part of the external acoustic meatus, thoracic and abdominal viscera",
                "Parasympathetic: heart, lungs, gut as far as the left colic flexure",
            ],
            "function": [
                "Slows the heart (sinoatrial node) and constricts the bronchi",
                "Stimulates peristalsis and digestive secretions",
                "Voice (laryngeal muscles) and swallowing (pharynx)",
            ],
            "clinical": [
                "Recurrent laryngeal nerve injury (thyroid surgery, left lung cancer): "
                "hoarseness, bitonal voice",
                "Vasovagal syncope: sudden bradycardia and hypotension",
                "Vagal manoeuvres (carotid sinus massage, Valsalva) to stop a supraventricular tachycardia",
            ],
        },
        fact=(
            "The left recurrent laryngeal nerve goes down under the aortic arch "
            "before climbing back to the larynx: a detour inherited from the "
            "development of the pharyngeal arches."
        ),
    ),
    "P": StructureText(
        name="Phrenic nerve",
        kind="Mixed nerve of the cervical plexus",
        region="Neck and mediastinum",
        count="2 (right and left)",
        description=(
            "Nerve of the diaphragm, from roots C3, C4 and C5 (mainly C4). It is the "
            "only motor nerve of the diaphragm, the main muscle of inspiration."
        ),
        sections={
            "course": [
                "Runs down on the anterior surface of the anterior scalene muscle, under the prevertebral fascia",
                "Enters the thorax between the subclavian artery and vein",
                "Descends in the mediastinum in front of the lung root, between the "
                "fibrous pericardium and the mediastinal pleura",
                "Along the superior vena cava on the right, over the left ventricle on "
                "the left, down to the diaphragm",
            ],
            "territory": [
                "Motor: diaphragm (each nerve supplies its own half)",
                "Sensory: pericardium, mediastinal and diaphragmatic pleura, central subdiaphragmatic peritoneum",
            ],
            "function": [
                "Contraction of the diaphragm at each inspiration",
            ],
            "clinical": [
                "Spinal cord injury at or above C3: respiratory paralysis, mechanical ventilation needed",
                "Phrenic palsy: raised hemidiaphragm on the chest X-ray",
                "Pain referred to the shoulder (C4 dermatome) when the diaphragm is irritated",
            ],
        },
        fact="Mnemonic: \"C3, 4, 5 keeps the diaphragm alive\".",
    ),
    "X": StructureText(
        name="Brachial plexus",
        kind="Somatic nerve plexus",
        region="Root of the neck, clavicular region and axilla",
        count="2 (right and left)",
        description=(
            "Network formed by the anterior rami of spinal nerves C5 to T1, giving "
            "all the nerves of the upper limb. It passes between the scalenes with the "
            "subclavian artery, then under the clavicle to the axilla."
        ),
        sections={
            "parts": [
                "Roots: anterior rami of C5, C6, C7, C8 and T1",
                "Superior (C5-C6), middle (C7) and inferior (C8-T1) trunks, in the interscalene gap",
                "Each trunk splits into anterior and posterior divisions, behind the clavicle",
                "Lateral, medial and posterior cords, named after their position around the axillary artery",
                "Former French terms: primary trunks (trunks) and secondary trunks (cords)",
            ],
            "branches": [
                "Lateral cord: musculocutaneous nerve and lateral root of the median nerve",
                "Medial cord: ulnar nerve, medial root of the median, medial cutaneous nerves of arm and forearm",
                "Posterior cord: axillary nerve and radial nerve",
                "Collateral branches, including the long thoracic nerve (C5-C7) to serratus anterior",
            ],
            "clinical": [
                "Upper palsy (Erb-Duchenne, C5-C6), often obstetric: arm adducted, "
                "medially rotated, elbow extended",
                "Lower palsy (Klumpke, C8-T1): claw hand, sometimes Horner's syndrome",
                "Interscalene block: regional anaesthesia of the upper limb",
            ],
        },
        fact=(
            "From root to branch: 5 roots, 3 trunks, 6 divisions, 3 cords. English "
            "texts count 5 terminal branches, French tradition 7 (adding the medial "
            "cutaneous nerves of the arm and forearm)."
        ),
    ),
    "K": StructureText(
        name="Musculocutaneous nerve",
        kind="Mixed nerve, terminal branch of the brachial plexus",
        region="Anterior compartment of the arm, lateral side of the forearm",
        count="2 (right and left)",
        description=(
            "Branch of the lateral cord (C5-C7), nerve of the flexor muscles of the "
            "arm. It ends as the sensory nerve of the lateral side of the forearm."
        ),
        sections={
            "course": [
                "Pierces the coracobrachialis muscle",
                "Runs down between biceps brachii and brachialis",
                "Becomes superficial at the elbow, lateral to the biceps tendon",
            ],
            "territory": [
                "Motor: coracobrachialis, biceps brachii and brachialis",
                "Sensory: lateral side of the forearm (lateral cutaneous nerve of the forearm)",
            ],
            "clinical": [
                "Rare isolated lesion: weak elbow flexion and supination",
                "Loss of the biceps reflex (C5-C6) and reduced sensation on the lateral forearm",
            ],
        },
        fact=(
            "Elbow flexion remains possible despite its palsy, thanks to "
            "brachioradialis, supplied by the radial nerve."
        ),
    ),
    "R": StructureText(
        name="Radial nerve",
        kind="Mixed nerve, terminal branch of the brachial plexus",
        region="Posterior compartment of the arm and forearm, back of the hand",
        count="2 (right and left)",
        description=(
            "Branch of the posterior cord (C5-T1), the largest of the brachial "
            "plexus. It is the nerve of extension of the elbow, wrist and fingers."
        ),
        sections={
            "course": [
                "Leaves the axilla through the triangular interval with the profunda brachii artery",
                "Winds round the back of the humerus in the radial groove",
                "Passes in front of the lateral epicondyle, between brachioradialis and brachialis",
                "Divides at the elbow into a sensory superficial branch and a motor deep branch",
            ],
            "branches": [
                "Branches to triceps brachii and anconeus, in the arm",
                "Superficial branch: sensory, to the back of the hand",
                "Deep branch: pierces supinator and becomes the posterior interosseous nerve",
            ],
            "territory": [
                "Motor: triceps, brachioradialis, wrist and finger extensors, supinator",
                "Motor: abductor pollicis longus and the thumb extensors",
                "Sensory: back of the arm and forearm, lateral back of the hand (first web space)",
            ],
            "clinical": [
                "Humeral shaft fracture: the nerve is injured in its groove",
                "Wrist drop (French 'swan neck' hand, unrelated to the rheumatoid finger deformity): "
                "the wrist and fingers cannot be extended",
                "Compression in the axilla (crutches): triceps is then also paralysed",
            ],
        },
        fact=(
            "After a humeral fracture, always test wrist extension and sensation on "
            "the back of the first web space."
        ),
    ),
    "D": StructureText(
        name="Median nerve",
        kind="Mixed nerve, terminal branch of the brachial plexus",
        region="Arm, anterior compartment of the forearm, palm of the hand",
        count="2 (right and left)",
        description=(
            "Formed by the union of two roots (lateral and medial cords, C5-T1) in "
            "front of the axillary artery. It is the nerve of pronation, finger "
            "flexion and thumb opposition."
        ),
        sections={
            "course": [
                "In the arm, it accompanies the brachial artery without giving branches",
                "At the elbow, medial to the brachial artery, passes between the two heads of pronator teres",
                "In the forearm, between flexor digitorum superficialis and profundus",
                "At the wrist, runs through the carpal tunnel under the flexor retinaculum",
            ],
            "branches": [
                "Anterior interosseous nerve, in the forearm",
                "Palmar cutaneous branch, arising before the carpal tunnel",
                "Thenar (recurrent) branch and palmar digital nerves",
            ],
            "territory": [
                "Motor: anterior forearm muscles, except flexor carpi ulnaris and the "
                "medial half of flexor digitorum profundus",
                "Motor: thenar muscles (except adductor pollicis and the deep head of flexor pollicis brevis) and the first two lumbricals",
                "Sensory: palmar side of the lateral three and a half digits, and the dorsal side of the middle and distal phalanges of those digits",
            ],
            "clinical": [
                "Carpal tunnel syndrome: night-time tingling in the lateral three "
                "digits, Tinel's and Phalen's signs",
                "Thenar wasting and loss of opposition: 'ape hand'",
                "High lesion (supracondylar fracture in children): 'hand of benediction' "
                "when the patient tries to make a fist",
            ],
        },
        fact=(
            "Carpal tunnel syndrome is the most common entrapment neuropathy; "
            "sensation of the palm is often spared."
        ),
    ),
    "U": StructureText(
        name="Ulnar nerve",
        kind="Mixed nerve, terminal branch of the brachial plexus",
        region="Medial side of the arm, forearm and hand",
        count="2 (right and left)",
        old_names=["cubital nerve"],
        description=(
            "Branch of the medial cord (C8-T1). It is the nerve of fine motor "
            "control of the hand: interossei, hypothenar muscles and adductor pollicis."
        ),
        sections={
            "course": [
                "In the arm, pierces the medial intermuscular septum",
                "Passes behind the medial epicondyle, in the groove for the ulnar nerve",
                "In the forearm, under flexor carpi ulnaris, medial to the ulnar artery",
                "At the wrist, passes lateral to the pisiform in the ulnar canal (Guyon's canal)",
            ],
            "branches": [
                "Branches to flexor carpi ulnaris and the medial half of flexor digitorum profundus",
                "Dorsal sensory branch of the hand",
                "Superficial (sensory) and deep (motor) branches in the hand",
            ],
            "territory": [
                "Motor: hypothenar muscles, all interossei, the two medial lumbricals",
                "Motor: adductor pollicis and the deep head of flexor pollicis brevis",
                "Sensory: medial border of the hand, little finger and medial half of the ring finger",
            ],
            "clinical": [
                "Knock on the elbow ('funny bone'): electric shock down to the little "
                "finger (superficial nerve behind the epicondyle)",
                "Ulnar claw of the ring and little fingers: hyperextended "
                "metacarpophalangeal and flexed interphalangeal joints",
                "Froment's sign: the thumb flexes its interphalangeal joint to pinch a sheet of paper",
            ],
        },
        fact=(
            "Ulnar paradox: the claw is less marked with a high lesion, because the "
            "deep flexor of the ring and little fingers is paralysed too."
        ),
    ),
    "I": StructureText(
        name="Intercostal nerves",
        kind="Mixed spinal nerves (thoracic anterior rami)",
        region="Intercostal spaces and anterolateral abdominal wall",
        count="11 pairs (T1 to T11), plus the subcostal nerve (T12)",
        description=(
            "Anterior rami of the thoracic spinal nerves. They form no plexus and "
            "keep a segmental arrangement."
        ),
        sections={
            "course": [
                "Each nerve runs in the costal groove, under the lower border of the rib",
                "It lies between the internal and innermost intercostal muscles",
                "From top to bottom: vein, artery, nerve",
                "Nerves T7 to T11 continue into the abdominal wall",
            ],
            "branches": [
                "Lateral cutaneous branch, at the mid-axillary line",
                "Anterior cutaneous branch, near the sternum or the midline",
                "T2 gives the intercostobrachial nerve, sensory to the medial arm",
            ],
            "territory": [
                "Motor: intercostal muscles and the flat abdominal muscles (lower nerves)",
                "Sensory: skin of thorax and abdomen in bands (dermatomes), parietal pleura and peritoneum",
                "Landmarks: T4 at the nipple, T10 at the umbilicus",
            ],
            "clinical": [
                "Pleural tap at the upper border of the lower rib, to spare the neurovascular bundle",
                "Shingles (herpes zoster): painful one-sided rash along a dermatome",
                "Intercostal neuralgia; intercostal block for pain relief of rib fractures",
            ],
        },
        fact=(
            "Shingles reactivates the chickenpox virus lying dormant in a spinal "
            "ganglion: the rash maps exactly the territory of one nerve."
        ),
    ),
    "F": StructureText(
        name="Femoral nerve (lumbar plexus)",
        kind="Mixed nerve, terminal branch of the lumbar plexus",
        region="Iliac fossa, femoral triangle, anterior compartment of the thigh",
        count="2 (right and left)",
        old_names=["anterior crural nerve"],
        description=(
            "Largest branch of the lumbar plexus (anterior rami L1 to L4, formed "
            "within psoas major). L2-L4 nerve of knee extension and of sensation on "
            "the front of the thigh."
        ),
        sections={
            "parts": [
                "Lumbar plexus: iliohypogastric, ilioinguinal and genitofemoral nerves",
                "Lumbar plexus: lateral cutaneous nerve of the thigh, obturator nerve, femoral nerve",
            ],
            "course": [
                "Emerges from the lateral border of psoas major and runs down between psoas and iliacus",
                "Passes under the inguinal ligament, lateral to the femoral artery, outside the femoral sheath",
                "Fans out at once in the femoral triangle",
            ],
            "branches": [
                "Muscular branches to quadriceps and sartorius",
                "Anterior cutaneous branches of the thigh",
                "Saphenous nerve: through the adductor canal, sensory to the medial leg and foot",
            ],
            "territory": [
                "Motor: iliacus, sartorius, pectineus (in part), quadriceps femoris",
                "Sensory: front and medial side of the thigh, medial side of the leg",
            ],
            "clinical": [
                "Weak knee extension (the knee gives way) and loss of the patellar reflex (L3-L4)",
                "Femoral neuralgia ('cruralgia'): compression of the L3 or L4 root by a disc herniation",
                "Compression by a psoas haematoma in patients on anticoagulants",
            ],
        },
        fact=(
            "At the groin, from lateral to medial: femoral nerve, artery, vein. The "
            "femoral pulse guides a femoral nerve block."
        ),
    ),
    "S": StructureText(
        name="Sciatic nerve (sacral plexus)",
        kind="Mixed nerve, terminal branch of the sacral plexus",
        region="Gluteal region and posterior compartment of the thigh",
        count="2 (right and left)",
        old_names=["great sciatic nerve"],
        description=(
            "The largest and longest nerve in the body (L4-S3), from the sacral "
            "plexus. It holds the future tibial and common fibular nerves in a "
            "single sheath."
        ),
        sections={
            "parts": [
                "Sacral plexus: lumbosacral trunk (L4-L5) and anterior rami S1 to S3, in front of piriformis",
                "Other branches: gluteal nerves and posterior cutaneous nerve of the thigh; the pudendal nerve (S2-S4) "
                "is assigned to a separate pudendal plexus in French tradition",
            ],
            "course": [
                "Leaves the pelvis through the greater sciatic foramen, below piriformis",
                "Runs under gluteus maximus, between the greater trochanter and the ischial tuberosity",
                "Descends in the posterior compartment of the thigh, on adductor magnus",
                "Usually divides at the apex of the popliteal fossa (variable level)",
            ],
            "branches": [
                "Branches to the hamstring muscles and the ischial part of adductor magnus",
                "Terminal branches: tibial nerve and common fibular nerve",
            ],
            "territory": [
                "Motor: posterior thigh muscles and all the muscles of the leg and foot",
                "Sensory: leg and foot, except the medial territory of the saphenous nerve",
            ],
            "clinical": [
                "Sciatica: compression of the L5 or S1 root by an L4-L5 or L5-S1 disc herniation",
                "Intramuscular injection in the upper outer quadrant of the buttock to spare the nerve",
                "Can be injured in posterior dislocations of the hip",
            ],
        },
        fact="As it leaves the pelvis, the sciatic nerve can be nearly 2 cm wide.",
    ),
    "N": StructureText(
        name="Tibial nerve",
        kind="Mixed nerve, terminal branch of the sciatic nerve",
        region="Popliteal fossa, posterior compartment of the leg, sole of the foot",
        count="2 (right and left)",
        old_names=["medial popliteal nerve"],
        description=(
            "Medial terminal branch of the sciatic nerve (L4-S3). It is the nerve of "
            "plantar flexion, toe flexion and sensation of the sole."
        ),
        sections={
            "course": [
                "Runs down the middle of the popliteal fossa, superficial to the popliteal vessels",
                "Passes under the tendinous arch of soleus (segment formerly called the posterior tibial nerve) "
                "and runs with the posterior tibial artery",
                "Passes behind the medial malleolus, in the tarsal tunnel",
                "Divides into medial and lateral plantar nerves",
            ],
            "branches": [
                "Medial sural cutaneous nerve, which contributes to the sural nerve",
                "Branches to gastrocnemius, soleus, popliteus, tibialis posterior and the toe flexors",
                "Medial calcaneal branches; medial and lateral plantar nerves",
            ],
            "territory": [
                "Motor: posterior compartment of the leg and the plantar muscles of the foot",
                "Sensory: sole of the foot and heel",
            ],
            "clinical": [
                "Palsy: the patient cannot walk on tiptoe",
                "Loss of the ankle (Achilles) reflex (S1)",
                "Tarsal tunnel syndrome: tingling in the sole",
            ],
        },
        fact=(
            "In the popliteal fossa, from superficial to deep: tibial nerve, "
            "popliteal vein, popliteal artery."
        ),
    ),
    "G": StructureText(
        name="Common fibular nerve",
        kind="Mixed nerve, terminal branch of the sciatic nerve",
        region="Popliteal fossa, neck of the fibula, anterior and lateral compartments of the leg",
        count="2 (right and left)",
        old_names=["common peroneal nerve", "lateral popliteal nerve"],
        description=(
            "Lateral terminal branch of the sciatic nerve (L4-S2). It is the nerve of "
            "dorsiflexion of the ankle and toes and of eversion of the foot."
        ),
        sections={
            "course": [
                "Follows the medial border of biceps femoris in the lateral part of the popliteal fossa",
                "Winds round the neck of the fibula, very superficial, under the skin",
                "Pierces fibularis longus and divides into two branches",
            ],
            "branches": [
                "Superficial fibular nerve (formerly superficial peroneal): lateral compartment",
                "Deep fibular nerve (formerly deep peroneal / anterior tibial): anterior compartment",
                "Lateral sural cutaneous nerve",
            ],
            "territory": [
                "Motor: fibularis longus and brevis (eversion) via the superficial nerve",
                "Motor: tibialis anterior and toe extensors (dorsiflexion) via the deep nerve",
                "Sensory: lateral leg, back of the foot, first web space (deep nerve)",
            ],
            "clinical": [
                "Most often injured nerve of the lower limb: fibular neck fracture, "
                "tight plaster cast, crossed legs",
                "Foot drop (steppage gait): the patient lifts the knee high so as not to catch the toes",
            ],
        },
        fact=(
            "At the neck of the fibula the nerve can be rolled under the finger, "
            "which explains its vulnerability."
        ),
    ),
}
