"""English texts (Terminologia Anatomica English equivalents)."""

from __future__ import annotations

from ...model import StructureText

TEXTS: dict[str, StructureText] = {
    "H": StructureText(
        name="Heart",
        kind="Hollow muscular organ",
        region=(
            "Thorax, middle mediastinum (international division; \"anterior "
            "mediastinum\" in some French textbooks), inside the pericardium"
        ),
        count="1",
        description=(
            "Four-chambered muscular pump: two atria and two ventricles. The right "
            "heart sends oxygen-poor blood to the lungs (pulmonary circulation), the "
            "left heart sends oxygenated blood to the whole body (systemic "
            "circulation). It weighs about 250 to 300 g; two thirds lie to the left "
            "of the midline and the apex points forwards, downwards and to the left."
        ),
        sections={
            "parts": [
                "Right atrium: receives the superior and inferior venae cavae and the "
                "coronary sinus; it bears the right auricle",
                "Right ventricle: forms most of the anterior (sternocostal) surface "
                "and ejects into the pulmonary trunk",
                "Left atrium: receives the four pulmonary veins; it is the most "
                "posterior chamber",
                "Left ventricle: thickest wall (about 10 mm), forms the apex and "
                "ejects into the aorta",
                "Atrioventricular valves: tricuspid on the right, mitral (bicuspid) "
                "on the left, held by chordae tendineae and papillary muscles",
                "Arterial valves: pulmonary and aortic, each with three semilunar "
                "cusps",
                "Wall: endocardium, myocardium, epicardium (= visceral layer of serous "
                "pericardium); all surrounded by the "
                "pericardium (fibrous and serous)",
                "Conducting system: sinuatrial node, atrioventricular node, "
                "atrioventricular bundle (of His) and its branches, Purkinje network",
            ],
            "relations": [
                "In front: sternum and costal cartilages 3 to 6, pleurae and anterior "
                "borders of the lungs (cardiac notch of the left lung)",
                "Behind: oesophagus, in contact with the left atrium, and descending "
                "thoracic aorta",
                "Below: central tendon of the diaphragm (diaphragmatic surface)",
                "On each side: phrenic nerves, mediastinal pleurae and lungs",
                "Apex: left 5th intercostal space, on the midclavicular line (apex "
                "beat)",
            ],
            "vascularisation": [
                "Right coronary artery (right aortic sinus): right heart, sinuatrial "
                "node (about 60% of people) and atrioventricular node (about 80 to "
                "90%)",
                "Left coronary artery (left aortic sinus): short trunk dividing into "
                "the anterior interventricular and circumflex arteries",
                "Cardiac veins (great, middle, small) drained by the coronary sinus "
                "into the right atrium",
            ],
            "innervation": [
                "Intrinsic automaticity: the sinuatrial node sets the rhythm (60 to "
                "100 beats per minute at rest)",
                "Sympathetic (cervical and upper thoracic ganglia, T1–T4/T5): speeds up "
                "and "
                "strengthens contractions",
                "Parasympathetic (vagus nerves, X): slows the heart",
            ],
            "clinical": [
                "Myocardial infarction: occlusion of a coronary artery, often the "
                "anterior interventricular artery",
                "Auscultation areas: aortic (right 2nd intercostal space), pulmonary "
                "(left 2nd), tricuspid (left 4th-5th at the sternal border), mitral "
                "(apex)",
                "Common valve diseases: aortic stenosis, mitral regurgitation",
                "Tamponade: fluid in the pericardium that compresses the heart",
            ],
        },
        fact=(
            "The heart beats about 100,000 times a day and pumps about 5 litres of "
            "blood per minute at rest."
        ),
        old_names=["auricles (for the atria)", "sigmoid valves (for the semilunar cusps)"],
    ),
    "A": StructureText(
        name="Ascending aorta and aortic arch",
        kind="Elastic artery",
        region="Thorax: middle mediastinum (ascending aorta), then superior (arch)",
        count="1 (unpaired)",
        description=(
            "Beginning of the aorta. The ascending aorta arises from the left "
            "ventricle; the aortic arch curves backwards and to the left over the "
            "left lung root, then continues as the descending thoracic aorta (hidden "
            "behind the heart in the figure). The brachiocephalic trunk is included "
            "here."
        ),
        sections={
            "parts": [
                "Ascending aorta (about 5 cm), inside the pericardium, with the three "
                "aortic sinuses just above the aortic valve",
                "Aortic arch, in the superior mediastinum, behind the manubrium of the "
                "sternum",
                "Aortic isthmus: narrowed junction between the arch and the "
                "descending aorta, at the ligamentum arteriosum",
            ],
            "course": [
                "The ascending aorta runs upwards, forwards and to the right up to the "
                "right 2nd costal cartilage",
                "The arch runs backwards and to the left, in front of then to the left "
                "of the trachea; its top is at the middle of the manubrium",
                "It ends to the left of the body of T4, at the level of the sternal "
                "angle",
            ],
            "branches": [
                "Right and left coronary arteries, from the sinuses of the ascending "
                "aorta",
                "Brachiocephalic trunk (on the right): divides into the right "
                "subclavian and right common carotid arteries",
                "Left common carotid artery",
                "Left subclavian artery",
            ],
            "relations": [
                "Ascending aorta: pulmonary trunk in front then to the left, superior "
                "vena cava on the right",
                "The left brachiocephalic vein crosses in front of the branches of the "
                "arch",
                "Below the arch: bifurcation of the pulmonary trunk, ligamentum "
                "arteriosum and the left recurrent laryngeal nerve hooking around it",
                "On the left: left phrenic and vagus nerves; on the right and behind: "
                "trachea and oesophagus",
            ],
            "clinical": [
                "Coarctation of the aorta: congenital narrowing near the isthmus; "
                "upper-limb hypertension, weak femoral pulses",
                "Aortic dissection: tear of the intima, sudden severe chest pain "
                "radiating to the back",
                "Traumatic rupture at the isthmus in sudden deceleration (road "
                "accidents)",
                "Aneurysm of the arch: may compress the left recurrent laryngeal nerve "
                "and cause hoarseness",
            ],
        },
        fact=(
            "The ligamentum arteriosum, under the arch, is the remnant of the ductus "
            "arteriosus, which in the fetus shunted blood from the pulmonary trunk "
            "to the aorta, bypassing the lungs."
        ),
    ),
    "P": StructureText(
        name="Pulmonary trunk",
        old_names=["main pulmonary artery"],
        kind="Elastic artery (carries oxygen-poor blood)",
        region="Thorax, middle mediastinum, inside the pericardium",
        count="1 (unpaired)",
        description=(
            "Artery carrying oxygen-poor blood from the right ventricle to the lungs: "
            "it is an artery but carries \"venous\" blood, hence its blue-violet "
            "colour in the figure. The pulmonary veins then return oxygenated blood "
            "to the left atrium."
        ),
        sections={
            "course": [
                "Arises from the conus arteriosus (infundibulum) of the right "
                "ventricle, beyond the pulmonary valve",
                "Runs upwards, backwards and to the left for about 5 cm, first in "
                "front of then to the left of the ascending aorta",
                "Divides under the concavity of the aortic arch, at about T4-T5, in "
                "front of and to the left of the tracheal bifurcation",
            ],
            "branches": [
                "Right pulmonary artery: long, passes behind the ascending aorta and "
                "the superior vena cava to the right hilum",
                "Left pulmonary artery: short, passes in front of the descending aorta "
                "and the left main bronchus",
                "Ligamentum arteriosum: joins the origin of the left pulmonary artery "
                "to the underside of the aortic arch",
            ],
            "relations": [
                "Enclosed with the ascending aorta in a single sleeve of serous "
                "pericardium; the transverse pericardial sinus lies behind",
                "The pulmonary trunk and the aorta twist around each other in a spiral",
                "Right and left auricles on either side of its origin, near the "
                "coronary arteries",
            ],
            "clinical": [
                "Pulmonary embolism: blockage by a clot, most often from a deep vein "
                "thrombosis of the lower limbs",
                "Patent ductus arteriosus: shunt from the aorta to the pulmonary "
                "trunk, continuous murmur",
                "Pulmonary auscultation area: left 2nd intercostal space, at the "
                "sternal border",
                "Pulmonary hypertension: defined as mean pulmonary arterial pressure "
                "> 20 mmHg (ESC 2022; ≥ 25 mmHg formerly)",
            ],
        },
        fact=(
            "Pressure in the pulmonary trunk is about five times lower than in the "
            "aorta: the pulmonary circulation is a low-pressure circuit."
        ),
    ),
    "S": StructureText(
        name="Superior vena cava",
        kind="Large vein, without valves",
        region="Thorax, superior then middle mediastinum, on the right",
        count="1 (unpaired)",
        description=(
            "Short large vein (about 7 cm) returning blood from the head, neck, upper "
            "limbs and thoracic wall to the right atrium."
        ),
        sections={
            "course": [
                "Formed by the union of the right and left brachiocephalic veins "
                "behind the right 1st costal cartilage",
                "Runs vertically down on the right of the ascending aorta",
                "Receives the azygos vein from behind; the arch of the azygos passes "
                "over the right lung root",
                "Opens into the upper part of the right atrium, at the level of the "
                "right 3rd costal cartilage",
            ],
            "territory": [
                "Head and neck (internal and external jugular veins)",
                "Upper limbs (subclavian veins)",
                "Thoracic wall and part of the posterior abdominal wall, through the "
                "azygos system",
            ],
            "relations": [
                "On the left: ascending aorta",
                "On the right: right phrenic nerve, mediastinal pleura and right lung",
                "Behind: trachea above, then the right lung root",
            ],
            "clinical": [
                "Superior vena cava syndrome (lung cancer, lymphoma): \"cape-like\" "
                "oedema of the face and neck, collateral venous circulation",
                "The tip of central venous catheters is placed at the junction of the "
                "superior vena cava and the right atrium",
                "On a chest X-ray, it forms the upper right border of the mediastinal "
                "shadow",
            ],
        },
        fact=(
            "Because it has no valves, the central venous pressure measured in it "
            "reflects the pressure in the right atrium."
        ),
    ),
    "I": StructureText(
        name="Inferior vena cava",
        kind="Large vein",
        region="Abdomen (retroperitoneum), then thorax, to the right of the aorta",
        count="1 (unpaired)",
        description=(
            "Largest vein of the body. It returns blood from the lower limbs, pelvis, "
            "kidneys and liver to the right atrium. Blood from the gut and spleen "
            "reaches it only after crossing the liver through the portal vein."
        ),
        sections={
            "course": [
                "Formed by the union of the two common iliac veins, in front of and to "
                "the right of L5",
                "Ascends in the retroperitoneum, to the right of the abdominal aorta, "
                "in front of the right side of the vertebral bodies",
                "Runs in a groove on the posterior surface of the liver",
                "Crosses the central tendon of the diaphragm through the caval opening "
                "(T8 level)",
                "Ends almost at once in the lower part of the right atrium",
            ],
            "territory": [
                "Lower limbs and pelvis, through the common iliac veins",
                "Renal veins; the left also receives the left suprarenal and gonadal "
                "veins, the right ones drain directly into the vena cava",
                "Liver, through the hepatic veins, just below the diaphragm",
                "Posterior abdominal wall: lumbar and inferior phrenic veins",
            ],
            "relations": [
                "On the left: abdominal aorta",
                "In front: duodenum (3rd part), head of the pancreas, root of the "
                "mesentery, liver",
                "Behind: lumbar spine, right crus of the diaphragm, right sympathetic "
                "trunk",
                "The left renal vein joins it after crossing in front of the aorta, "
                "below the superior mesenteric artery",
            ],
            "clinical": [
                "Deep vein thrombosis: a vena cava filter can be placed below the renal "
                "veins when anticoagulation is contraindicated or pulmonary embolism "
                "recurs despite adequate anticoagulation",
                "Compression by the pregnant uterus when lying supine (faintness, low "
                "blood pressure): pregnant women are positioned on their left side",
                "Because it lies on the right, the right renal vein is very short: the "
                "left kidney is preferred for living-donor transplantation",
            ],
        },
        fact=(
            "Its opening lies in the central tendon of the diaphragm: the diaphragm "
            "does not squeeze it during inspiration, and the fall in thoracic "
            "pressure helps venous return."
        ),
    ),
    "C": StructureText(
        name="Common carotid artery",
        old_names=["primitive carotid artery"],
        kind="Elastic artery",
        region="Neck (and superior mediastinum for the left one)",
        count="2 (right and left)",
        description=(
            "Main artery of the head and neck. The right one arises from the "
            "brachiocephalic trunk, the left one directly from the aortic arch (so it "
            "has a thoracic part). Classically it gives no branch before dividing into "
            "the internal and external carotid arteries."
        ),
        sections={
            "course": [
                "Right: arises from the brachiocephalic trunk behind the right "
                "sternoclavicular joint",
                "Left: arises from the aortic arch and ascends in the superior "
                "mediastinum to the left sternoclavicular joint",
                "Ascends in the neck within the carotid sheath, alongside the trachea "
                "then the larynx",
                "Divides at the upper border of the thyroid cartilage, about C4 (C3 to "
                "C4 depending on the textbook)",
            ],
            "branches": [
                "No collateral branch (classically)",
                "Internal carotid artery: brain and eye; it gives no branch in the neck",
                "External carotid artery: neck, face and scalp (superior thyroid, "
                "lingual, facial, superficial temporal, maxillary...)",
            ],
            "relations": [
                "Carotid sheath: internal jugular vein laterally, vagus nerve behind, "
                "between artery and vein",
                "In front: sternocleidomastoid muscle, under its anterior border, and "
                "omohyoid muscle",
                "Behind: cervical transverse processes (carotid tubercle of C6) and "
                "cervical sympathetic trunk",
                "Medially: trachea, oesophagus, thyroid gland, then larynx and pharynx",
            ],
            "clinical": [
                "Carotid pulse: at the anterior border of the sternocleidomastoid, at "
                "the level of the thyroid cartilage",
                "Carotid sinus (baroreceptor, glossopharyngeal nerve IX) at the start "
                "of the internal carotid: massaging it slows the heart",
                "Carotid body: chemoreceptor lying in the bifurcation",
                "Atherosclerotic stenosis of the bifurcation: cause of ischaemic "
                "stroke, treated by endarterectomy",
            ],
        },
        fact=(
            "Only one carotid is felt at a time: pressing on both could reduce blood "
            "flow to the brain."
        ),
    ),
    "J": StructureText(
        name="Internal jugular vein",
        kind="Large deep vein",
        region="Neck",
        count="2 (right and left)",
        description=(
            "Main vein of the head and neck: it drains the brain (through the dural "
            "venous sinuses), the face and the neck. It runs with the internal then "
            "common carotid arteries in the carotid sheath."
        ),
        sections={
            "course": [
                "Begins at the jugular foramen as the continuation of the sigmoid "
                "sinus (superior bulb)",
                "Descends in the carotid sheath, lateral to the internal then common "
                "carotid arteries",
                "Ends behind the medial end of the clavicle by joining the subclavian "
                "vein to form the brachiocephalic vein",
            ],
            "territory": [
                "Brain and meninges, through the dural venous sinuses",
                "Face and neck: facial, lingual, pharyngeal, superior and middle "
                "thyroid veins",
            ],
            "relations": [
                "In the carotid sheath, lateral to the artery, with the vagus nerve "
                "behind, between the two",
                "Covered by the sternocleidomastoid muscle",
                "Low down, it lies in the small triangle between the sternal and "
                "clavicular heads of the sternocleidomastoid",
                "Accompanied by the deep cervical lymph nodes (jugular chain)",
                "At the jugulo-subclavian venous angle: thoracic duct (left), right "
                "lymphatic duct (right)",
            ],
            "clinical": [
                "Classic route for a central venous catheter, preferably on the right "
                "(direct path to the superior vena cava), under ultrasound guidance",
                "Jugular venous pulse (internal jugular), hepatojugular reflux and "
                "jugular distension (most visible on the external jugular): signs of "
                "raised right atrial pressure (right heart failure)",
                "Neck dissection along the jugular-carotid lymph nodes in head and "
                "neck cancers",
            ],
        },
        fact=(
            "The right internal jugular vein is in line with the superior vena cava: "
            "it is the most direct route to the heart for a catheter."
        ),
    ),
    "U": StructureText(
        name="Subclavian artery",
        kind="Elastic artery",
        region="Root of the neck and top of the thorax",
        count="2 (right and left)",
        description=(
            "Artery of the upper limb, which also supplies part of the brain, the "
            "neck and the thoracic wall. The right one arises from the "
            "brachiocephalic trunk, the left one from the aortic arch."
        ),
        sections={
            "course": [
                "Arches over the dome of the pleura and the 1st rib",
                "Passes between the anterior scalene (in front) and the middle "
                "scalene (behind): the scalene gap",
                "Three parts: medial to, behind and lateral to the anterior scalene",
                "Becomes the axillary artery at the lateral border of the 1st rib "
                "(classical French texts: middle of the clavicle)",
            ],
            "branches": [
                "Vertebral artery: ascends through the transverse foramina from C6 to "
                "C1; brainstem, cerebellum, occipital lobes",
                "Internal thoracic artery: descends behind the costal cartilages, 1 cm "
                "from the edge of the sternum",
                "Thyrocervical trunk (including the inferior thyroid artery) and "
                "costocervical trunk",
                "Dorsal scapular artery, inconstant as a direct branch",
            ],
            "relations": [
                "In front: subclavian vein, separated from the artery by the anterior "
                "scalene and the phrenic nerve lying on it",
                "Behind and above: trunks of the brachial plexus, which pass with the "
                "artery between the scalenes",
                "Below: dome of the pleura and apex of the lung, groove for the "
                "subclavian artery on the 1st rib",
            ],
            "clinical": [
                "Thoracic outlet syndrome (cervical rib, scalenes): compression of the "
                "artery and the brachial plexus",
                "Subclavian steal syndrome: stenosis before the vertebral artery; the "
                "arm \"steals\" blood from the brain through the vertebral artery",
                "Emergency compression above the clavicle, against the 1st rib, for "
                "bleeding from the upper limb",
            ],
        },
        fact=(
            "The left internal thoracic artery, a branch of the subclavian, is the "
            "reference graft for bypass of the anterior interventricular artery."
        ),
    ),
    "X": StructureText(
        name="Brachial artery",
        kind="Muscular (distributing) artery",
        region="Arm, medial side",
        count="2 (right and left)",
        description=(
            "Artery of the arm, continuing the axillary artery. It ends in the "
            "cubital fossa (front of the elbow) as the radial and ulnar arteries."
        ),
        sections={
            "course": [
                "Begins at the lower border of the teres major muscle (classical French "
                "texts: lower border of the pectoralis major)",
                "Descends on the medial side of the arm, in the medial bicipital "
                "groove, along the medial border of the biceps",
                "Ends in the cubital fossa, opposite the neck of the radius, just "
                "below the elbow crease",
            ],
            "branches": [
                "Deep artery of the arm (profunda brachii): runs with the radial "
                "nerve in the radial groove of the humerus",
                "Superior and inferior ulnar collateral arteries, for the anastomotic "
                "network of the elbow",
                "Terminal branches: radial artery and ulnar artery",
            ],
            "relations": [
                "Median nerve: lateral above, it crosses in front of the artery at "
                "mid-arm and becomes medial below",
                "Accompanied by two brachial veins",
                "At the elbow: under the bicipital aponeurosis, medial to the biceps "
                "tendon and lateral to the median nerve",
            ],
            "clinical": [
                "Blood pressure measurement: cuff on the arm, stethoscope over the "
                "artery at the elbow",
                "Brachial pulse at the elbow, medial to the biceps tendon",
                "Supracondylar fracture of the humerus in children: risk of arterial "
                "injury and compartment syndrome (Volkmann ischaemia)",
            ],
        },
        fact=(
            "The Korotkoff sounds heard with the stethoscope when taking blood "
            "pressure arise in the brachial artery under the cuff."
        ),
    ),
    "R": StructureText(
        name="Radial artery",
        kind="Muscular (distributing) artery",
        region="Forearm (lateral side), wrist and hand",
        count="2 (right and left)",
        description=(
            "Lateral terminal branch of the brachial artery. It follows the thumb "
            "side (the radius) and forms most of the deep palmar arch in the palm."
        ),
        sections={
            "course": [
                "Arises in the cubital fossa, opposite the neck of the radius",
                "Descends on the front of the forearm under the brachioradialis, then "
                "between the tendons of the brachioradialis and flexor carpi radialis",
                "Winds around the lateral side of the carpus in the anatomical "
                "snuffbox, then enters the palm between the two heads of the 1st "
                "dorsal interosseous",
            ],
            "branches": [
                "Radial recurrent artery, for the anastomotic network of the elbow",
                "Superficial palmar branch, which completes the superficial palmar "
                "arch",
                "Princeps pollicis artery; it ends as the deep palmar arch with the "
                "deep branch of the ulnar artery",
            ],
            "relations": [
                "Covered by the brachioradialis in the upper third of the forearm",
                "The superficial branch of the radial nerve is lateral to it in the "
                "middle third",
                "At the wrist, just under the skin, on the radius, lateral to the "
                "flexor carpi radialis tendon",
            ],
            "clinical": [
                "Radial pulse: the usual site for taking the pulse, at the wrist, "
                "lateral to the flexor carpi radialis tendon",
                "Puncture for arterial blood gases; radial access for coronary "
                "angiography",
                "Allen test before puncture: checks that the ulnar artery can supply "
                "the hand alone",
            ],
        },
        fact=(
            "At the wrist it lies directly on the radius: that is why the pulse is "
            "so easy to feel there."
        ),
    ),
    "N": StructureText(
        name="Ulnar artery",
        kind="Muscular (distributing) artery",
        region="Forearm (medial side), wrist and hand",
        count="2 (right and left)",
        description=(
            "Medial terminal branch, the larger one, of the brachial artery. It "
            "follows the little-finger side (the ulna) and forms mainly the "
            "superficial palmar arch."
        ),
        sections={
            "course": [
                "Arises in the cubital fossa, opposite the neck of the radius",
                "Passes deep to the pronator teres, then descends under the flexor "
                "carpi ulnaris",
                "At the wrist, passes in front of the flexor retinaculum, lateral to "
                "the pisiform, in the ulnar canal (Guyon's canal)",
            ],
            "branches": [
                "Ulnar recurrent arteries, for the anastomotic network of the elbow",
                "Common interosseous artery, giving the anterior and posterior "
                "interosseous arteries",
                "Ends as the superficial palmar arch, completed by the superficial "
                "palmar branch of the radial artery",
            ],
            "relations": [
                "The ulnar nerve joins it in the middle third of the forearm and stays "
                "medial to it down to the wrist",
                "Covered by the superficial flexor muscles of the forearm",
                "In the ulnar canal (Guyon's canal), with the ulnar nerve, lateral to "
                "the pisiform",
            ],
            "clinical": [
                "Ulnar pulse, weaker than the radial, lateral to the flexor carpi "
                "ulnaris tendon",
                "Allen test: both radial and ulnar arteries are pressed, then the "
                "ulnar is released to see the hand pink up again",
                "Hypothenar hammer syndrome: injury to the artery from repeated blows "
                "with the heel of the hand",
            ],
        },
        fact=(
            "The palmar arches link the radial and ulnar arteries: the hand usually "
            "stays well supplied if one of them is interrupted."
        ),
    ),
    "B": StructureText(
        name="Abdominal aorta",
        kind="Elastic artery",
        region="Abdomen, retroperitoneum, in front of the lumbar spine",
        count="1 (unpaired)",
        description=(
            "Part of the aorta below the diaphragm, from the aortic hiatus (T12) to "
            "its bifurcation into the common iliac arteries (L4). It gives unpaired "
            "visceral branches (gut), paired visceral branches (kidneys, suprarenal "
            "glands, gonads) and parietal branches."
        ),
        sections={
            "course": [
                "Enters the abdomen through the aortic hiatus of the diaphragm, behind, "
                "at the level of T12",
                "Descends in front of the lumbar vertebral bodies, slightly to the left "
                "of the midline",
                "Divides into the common iliac arteries in front of L4, slightly below "
                "and to the left of the umbilicus",
            ],
            "branches": [
                "Unpaired visceral: coeliac trunk (T12), superior mesenteric artery "
                "(L1), inferior mesenteric artery (L3)",
                "Paired visceral: middle suprarenal arteries, renal arteries (L1-L2), "
                "testicular or ovarian arteries",
                "Parietal: inferior phrenic arteries and four pairs of lumbar arteries",
                "Terminal: common iliac arteries, and a small median sacral artery",
            ],
            "relations": [
                "On the right: inferior vena cava",
                "In front: pancreas, left renal vein, 3rd part of the duodenum, root "
                "of the mesentery",
                "Behind: lumbar vertebral bodies and left lumbar veins",
                "Surrounded by the aortic nerve plexus and the lumbar lymph nodes",
            ],
            "clinical": [
                "Abdominal aortic aneurysm: dilatation (diameter of 3 cm or more), "
                "most often below the renal arteries; risk of rupture",
                "Risk factors: older men, smoking, hypertension; screening by "
                "ultrasound",
                "Leriche syndrome: occlusion of the aortic bifurcation (buttock "
                "claudication, absent femoral pulses, impotence)",
            ],
        },
        fact=(
            "In a slim person, the abdominal aorta can be felt pulsating by pressing "
            "deeply just above the umbilicus."
        ),
    ),
    "T": StructureText(
        name="Coeliac trunk",
        kind="Visceral artery (short trunk)",
        region="Abdomen, supramesocolic compartment",
        count="1 (unpaired)",
        description=(
            "First unpaired visceral branch of the abdominal aorta, 1 to 2 cm long. "
            "It supplies the foregut organs: stomach, duodenum down to the major "
            "papilla, "
            "liver and biliary tract, pancreas, and also the spleen."
        ),
        sections={
            "course": [
                "Arises from the front of the aorta just below the aortic hiatus, at "
                "the level of T12",
                "Runs forwards above the upper border of the pancreas",
                "Soon divides into three branches (coeliac tripod)",
            ],
            "branches": [
                "Left gastric artery: lesser curvature of the stomach and abdominal "
                "oesophagus",
                "Common hepatic artery: gives the gastroduodenal artery then becomes "
                "the hepatic artery proper (liver; cystic artery to the gallbladder, "
                "usually from the right hepatic artery)",
                "Splenic artery: runs along the upper border of the pancreas to the "
                "spleen, gives the short gastric and left gastro-omental arteries",
            ],
            "territory": [
                "Abdominal oesophagus, stomach, duodenum down to the major papilla",
                "Liver, gallbladder and biliary tract, pancreas (with the superior "
                "mesenteric), spleen",
                "Anastomoses with the superior mesenteric artery through the "
                "pancreaticoduodenal arcades",
            ],
            "clinical": [
                "Ulcer of the posterior wall of the duodenum: may erode the "
                "gastroduodenal artery and bleed heavily",
                "Median arcuate ligament syndrome: compression of the trunk by the "
                "diaphragm",
                "Frequent variations of the hepatic arteries, important in surgery and "
                "transplantation",
            ],
        },
        fact="Its name comes from the Greek koilia, the belly.",
    ),
    "K": StructureText(
        name="Renal artery",
        kind="Paired visceral artery",
        region="Abdomen, retroperitoneum",
        count="2 (right and left)",
        description=(
            "Lateral branch of the abdominal aorta running to the hilum of the "
            "kidney. The two kidneys receive about 20 to 25% of the cardiac output."
        ),
        sections={
            "course": [
                "Arises from the side of the aorta at about the L1-L2 disc, just below "
                "the superior mesenteric artery",
                "The right one, longer, passes behind the inferior vena cava",
                "Divides near the hilum into branches in front of and behind the renal "
                "pelvis, then into segmental arteries",
            ],
            "branches": [
                "Inferior suprarenal artery",
                "Ureteric branches for the upper ureter",
                "Segmental arteries: end arteries, with no anastomoses between them",
            ],
            "relations": [
                "In the renal pedicle, from front to back: renal vein, renal artery, "
                "renal pelvis",
                "The long left renal vein passes in front of the aorta, below the "
                "superior mesenteric artery",
                "Accessory (polar) renal arteries are common, arising directly from "
                "the aorta",
            ],
            "clinical": [
                "Renal artery stenosis (atheroma, fibromuscular dysplasia): secondary, "
                "so-called renovascular, hypertension",
                "Occlusion of a segmental or polar artery: infarction of its territory, "
                "because these are end arteries",
                "In transplantation, the artery of the graft is joined to the external "
                "iliac artery",
            ],
        },
        fact=(
            "Blood flows through the kidneys so fast that they filter the whole "
            "plasma about 60 times a day (180 litres of glomerular filtrate)."
        ),
    ),
    "L": StructureText(
        name="Common iliac artery",
        old_names=["primitive iliac artery"],
        kind="Large artery",
        region="Abdomen and pelvic inlet",
        count="2 (right and left)",
        description=(
            "Terminal branch of the abdominal aorta, short (4 to 5 cm). It divides "
            "into the internal iliac artery for the pelvis and the external iliac "
            "artery for the lower limb."
        ),
        sections={
            "course": [
                "Arises at the aortic bifurcation, in front of L4",
                "Runs downwards and outwards along the medial border of the psoas "
                "major",
                "Divides in front of the sacroiliac joint, at the level of the L5-S1 "
                "disc",
            ],
            "branches": [
                "No significant collateral branch",
                "Internal iliac artery: pelvic viscera, perineum, buttock (gluteal "
                "arteries)",
                "External iliac artery: passes under the inguinal ligament and becomes "
                "the femoral artery",
            ],
            "relations": [
                "The ureter crosses in front of the iliac bifurcation (often the external "
                "iliac on the right, the common iliac on the left; varies between textbooks)",
                "The left common iliac vein passes behind the right common iliac "
                "artery to reach the inferior vena cava",
                "Covered by the posterior parietal peritoneum; common iliac lymph "
                "nodes around it",
            ],
            "clinical": [
                "May-Thurner (Cockett) syndrome: the left common iliac vein squeezed "
                "by the right artery favours thrombosis on the left",
                "Iliac aneurysms, often associated with an abdominal aortic aneurysm",
                "Arterial disease: stenoses treated by angioplasty or aorto-bi-iliac "
                "or aortobifemoral bypass",
            ],
        },
        fact=(
            "The aortic bifurcation lies roughly on the line joining the highest "
            "points of the iliac crests (L4)."
        ),
    ),
    "F": StructureText(
        name="Femoral artery",
        old_names=[
            "in clinical use: common femoral artery (above the deep femoral) and "
            "superficial femoral artery (below)"
        ],
        kind="Muscular (distributing) artery",
        region="Thigh",
        count="2 (right and left)",
        description=(
            "Main artery of the lower limb, continuing the external iliac artery "
            "below the inguinal ligament. It becomes the popliteal artery by passing "
            "through the adductor hiatus."
        ),
        sections={
            "course": [
                "Begins behind the inguinal ligament, at the mid-inguinal point "
                "(between the anterior superior iliac spine and the pubic symphysis)",
                "Runs down through the femoral triangle (Scarpa's triangle)",
                "Descends in the adductor canal (Hunter's canal), under the sartorius",
                "Passes through the adductor hiatus, at the junction of the middle and "
                "lower thirds of the thigh, and becomes the popliteal artery",
            ],
            "branches": [
                "Superficial branches: superficial epigastric, superficial circumflex "
                "iliac, external pudendal arteries",
                "Deep artery of the thigh (profunda femoris), about 4 cm below the "
                "inguinal ligament, with the circumflex femoral and perforating arteries",
                "Descending genicular artery",
            ],
            "relations": [
                "In the femoral triangle, from lateral to medial: femoral nerve, "
                "femoral artery, femoral vein, then femoral canal",
                "Femoral triangle: inguinal ligament above, sartorius laterally, "
                "adductor longus medially",
                "In the adductor canal: with the femoral vein and the saphenous nerve",
            ],
            "clinical": [
                "Femoral pulse at the mid-inguinal point, just below the inguinal "
                "ligament",
                "Classic arterial access for catheterisation (coronary angiography, "
                "angioplasty); the vein, medial to it, is used for venous access",
                "Peripheral arterial disease of the lower limbs: stenoses common in "
                "the adductor canal, intermittent claudication",
                "Femoral hernia: in the femoral canal, medial to the femoral vein",
            ],
        },
        fact=(
            "The medial circumflex femoral artery, from the deep artery of the thigh, "
            "is the main supply of the femoral head: a femoral neck fracture can tear "
            "it and lead to necrosis."
        ),
    ),
    "G": StructureText(
        name="Popliteal artery",
        kind="Muscular (distributing) artery",
        region="Knee, popliteal fossa (seen here through the limb)",
        count="2 (right and left)",
        description=(
            "Continuation of the femoral artery behind the knee, it is the deepest "
            "structure of the popliteal fossa. It divides below the knee into the "
            "anterior tibial artery and the tibiofibular trunk."
        ),
        sections={
            "course": [
                "Begins at the adductor hiatus",
                "Crosses the popliteal fossa behind the femur, then behind the knee "
                "joint capsule",
                "Ends at the lower border of the popliteus muscle, under the tendinous "
                "arch of the soleus",
            ],
            "branches": [
                "Genicular arteries (superior, middle, inferior): anastomotic network "
                "of the knee",
                "Sural arteries for the gastrocnemius muscles",
                "Anterior tibial artery: anterior compartment of the leg, then dorsal "
                "artery of the foot (dorsalis pedis)",
                "Tibiofibular trunk: posterior tibial artery and fibular artery "
                "(formerly peroneal artery)",
            ],
            "relations": [
                "From deep to superficial: artery, popliteal vein, tibial nerve",
                "In front: popliteal surface of the femur and knee joint capsule",
                "Diamond-shaped popliteal fossa: biceps femoris above and laterally, "
                "semimembranosus and semitendinosus above and medially, gastrocnemius "
                "below",
            ],
            "clinical": [
                "Popliteal pulse: hard to feel, with the knee slightly bent, pressing "
                "deeply into the floor of the fossa",
                "Arterial injury must always be looked for after a knee dislocation",
                "Popliteal aneurysm: the most common peripheral aneurysm, often "
                "bilateral",
            ],
        },
        fact=(
            "Its branches give two pulses of the foot: dorsalis pedis, between the "
            "tendons of extensor hallucis longus and extensor digitorum longus, and "
            "posterior tibial, behind the medial malleolus."
        ),
        old_names=["tibioperoneal trunk (for the tibiofibular trunk)"],
    ),
    "V": StructureText(
        name="Great saphenous vein",
        old_names=["long saphenous vein"],
        kind="Superficial vein",
        region="Lower limb, medial side, subcutaneous tissue",
        count="2 (right and left)",
        description=(
            "Longest vein of the body, from the foot to the groin. Superficial vein "
            "of the medial side of the lower limb, it drains into the femoral vein "
            "below the inguinal ligament."
        ),
        sections={
            "course": [
                "Begins at the medial end of the dorsal venous arch of the foot",
                "Passes in front of the medial malleolus, where its position is "
                "constant",
                "Ascends on the medial side of the leg, passes behind the medial "
                "condyles at the knee, then on the anteromedial side of the thigh",
                "Passes through the saphenous opening about 3 to 4 cm below and "
                "lateral to the pubic tubercle and drains into the femoral vein",
            ],
            "territory": [
                "Superficial network of the foot and of the medial sides of the leg "
                "and thigh",
                "Near its end: superficial epigastric, superficial circumflex iliac "
                "and external pudendal veins",
                "Linked to the deep veins by perforating veins fitted with valves",
            ],
            "relations": [
                "Accompanied in the leg by the saphenous nerve, which can be injured "
                "when the vein is harvested",
                "In the subcutaneous tissue, above the deep fascia (fascia lata in the "
                "thigh)",
                "Many valves that direct blood upwards and towards the deep veins",
            ],
            "clinical": [
                "Varicose veins: valve failure, often at the saphenofemoral junction",
                "Emergency venous access in front of the medial malleolus",
                "Graft for coronary or limb bypass, reversed or with its valves "
                "destroyed because of the valves",
                "Deep vein thrombosis affects the deep veins; thrombosis of the "
                "saphenous vein is called superficial",
            ],
        },
        fact=(
            "In front of the medial malleolus it can be seen and felt in almost "
            "everyone: a reliable landmark even in an emergency."
        ),
    ),
}
