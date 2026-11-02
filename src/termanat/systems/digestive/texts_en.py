"""English texts (Terminologia Anatomica English equivalents). Eponyms are
given in brackets."""

from __future__ import annotations

from ...model import StructureText

TEXTS: dict[str, StructureText] = {
    "O": StructureText(
        name="Oral cavity",
        old_names=["buccal cavity", "mouth"],
        kind="Cavity (first segment of the digestive tract)",
        region="Head (lower part of the face)",
        count="1",
        description=(
            "First part of the digestive tract, bounded in front by the lips and "
            "behind by the oropharyngeal isthmus. It comprises the oral vestibule "
            "(between lips, cheeks and dental arches) and the oral cavity proper, "
            "which contains the tongue."
        ),
        sections={
            "parts": [
                "Oral vestibule and oral cavity proper, separated by the alveolar "
                "processes and dental arches",
                "Roof: hard (bony) palate in front, soft palate ending in the uvula behind",
                "Floor: mylohyoid muscles (oral diaphragm) and tongue",
                "Tongue: striated muscle; the V-shaped terminal sulcus separates the body "
                "(anterior 2/3) from the root (posterior 1/3); vallate papillae in front of the V",
                "Teeth: 20 deciduous teeth, 32 permanent teeth; per half-arch 2 incisors, "
                "1 canine, 2 premolars, 3 molars",
                "Oropharyngeal isthmus, bounded by the palatoglossal arches: passage to "
                "the oropharynx",
            ],
            "function": [
                "Chewing, mixing with saliva and forming the food bolus",
                "Oral, voluntary phase of swallowing",
                "Taste and articulation of speech",
                "Start of starch digestion by salivary amylase",
            ],
            "vascularisation": [
                "Branches of the external carotid artery: lingual, facial and maxillary "
                "arteries (alveolar and palatine arteries)",
            ],
            "innervation": [
                "Motor to the tongue: hypoglossal nerve (XII), except palatoglossus "
                "(vagus nerve, X)",
                "Body of the tongue: general sensation by the lingual nerve (V3), taste "
                "by the chorda tympani (VII)",
                "Root of the tongue: sensation and taste by the glossopharyngeal nerve (IX)",
                "Teeth: superior alveolar nerves (V2) and inferior alveolar nerve (V3)",
            ],
            "clinical": [
                "XII palsy: the protruded tongue deviates towards the paralysed side",
                "Dental caries and abscess, which can spread to the floor of the mouth "
                "(cervicofacial cellulitis)",
                "Sublingual route: fast absorption of some drugs (glyceryl trinitrate) "
                "without hepatic first pass",
            ],
        },
        fact=(
            "The vallate papillae, about ten of them, form the lingual V and carry "
            "many of the taste buds."
        ),
    ),
    "P": StructureText(
        name="Parotid gland",
        kind="Major salivary gland (exocrine, serous)",
        region="Parotid region, in front of the ear and behind the mandible",
        count="2 (paired)",
        description=(
            "The largest salivary gland, lying in the parotid bed. Its serous saliva "
            "reaches the oral vestibule through the parotid duct. The other major "
            "salivary glands are the submandibular and sublingual glands."
        ),
        sections={
            "parts": [
                "Parotid bed: ramus of the mandible in front, mastoid process and "
                "sternocleidomastoid muscle behind",
                "Parotid duct (Stensen's duct): crosses masseter, pierces buccinator, "
                "opens opposite the upper second molar",
                "Superficial and deep parts, separated by the plane of the facial nerve",
            ],
            "relations": [
                "Traversed, from superficial to deep, by the facial nerve (VII), the "
                "retromandibular vein and the external carotid artery",
                "The external carotid artery ends within it as the maxillary and "
                "superficial temporal arteries",
            ],
            "function": [
                "Secretion of a serous saliva rich in salivary amylase",
                "All glands together: about 1 to 1.5 L of saliva per day",
            ],
            "innervation": [
                "Secretomotor parasympathetic: glossopharyngeal nerve (IX), lesser "
                "petrosal nerve, otic ganglion, then auriculotemporal nerve (V3)",
                "Sympathetic: plexus around the external carotid artery",
            ],
            "clinical": [
                "Mumps: viral parotitis, often bilateral",
                "Parotidectomy: risk of peripheral facial palsy",
                "Salivary stones are more frequent in the submandibular gland than in "
                "the parotid",
            ],
        },
        fact=(
            "The facial nerve runs through the parotid without supplying it: its "
            "secretion depends on the glossopharyngeal nerve."
        ),
    ),
    "H": StructureText(
        name="Pharynx",
        kind="Musculomembranous tube (aerodigestive crossroads)",
        region="Neck, in front of the cervical spine, from the skull base to C6",
        count="1 (unpaired, midline)",
        description=(
            "Tube about 15 cm long, from the base of the skull to the lower border of "
            "the cricoid cartilage (C6), where it continues as the oesophagus. It is "
            "shared by the airway and the digestive tract."
        ),
        sections={
            "parts": [
                "Nasopharynx: behind the choanae; openings of the auditory tubes, "
                "pharyngeal tonsil",
                "Oropharynx: behind the oropharyngeal isthmus; palatine tonsils",
                "Laryngopharynx (hypopharynx): behind the larynx; piriform recesses",
                "Superior, middle and inferior constrictor muscles, and elevator muscles "
                "(including stylopharyngeus)",
            ],
            "relations": [
                "Behind: retropharyngeal space, prevertebral fascia, cervical vertebrae",
                "Laterally: parapharyngeal space, internal carotid artery, internal "
                "jugular vein and nerves IX to XII",
            ],
            "function": [
                "Pharyngeal, reflex phase of swallowing: the soft palate closes the "
                "nasopharynx and the epiglottis protects the larynx",
                "Passage of air; voice resonance; pharyngeal lymphoid ring (Waldeyer's ring)",
            ],
            "vascularisation": [
                "Ascending pharyngeal artery (external carotid) and branches of the "
                "facial, maxillary and thyroid arteries",
            ],
            "innervation": [
                "Pharyngeal plexus: glossopharyngeal nerve (IX, sensory) and vagus nerve "
                "(X, motor to the constrictors); stylopharyngeus is supplied by IX",
            ],
            "clinical": [
                "Gag reflex: afferent limb IX, efferent limb X",
                "Pharyngo-oesophageal (Zenker's) diverticulum, posteriorly, just above "
                "the cricopharyngeus muscle",
                "Foreign bodies (fish bones) lodged in the piriform recesses",
            ],
        },
        fact="The pharynx is the only segment shared by air and food.",
    ),
    "E": StructureText(
        name="Oesophagus",
        old_names=["esophagus (US spelling)"],
        kind="Hollow organ (muscular tube)",
        region="Neck, posterior mediastinum and abdomen",
        count="1",
        description=(
            "Muscular tube about 25 cm long, from C6 to the cardia (T11). It passes "
            "through the diaphragm at the oesophageal hiatus (T10). Its mucosa is a "
            "non-keratinised stratified squamous epithelium."
        ),
        sections={
            "parts": [
                "Three segments: cervical, thoracic (the longest) and abdominal (2 to 3 cm)",
                "Striated muscle in the upper third, mixed in the middle, smooth in the "
                "lower third",
                "Constrictions: oesophageal opening (C6), aortic arch, left main bronchus, "
                "diaphragmatic hiatus",
                "Upper sphincter (cricopharyngeus) and a functional lower sphincter at "
                "the gastro-oesophageal junction",
            ],
            "relations": [
                "In front: trachea, left main bronchus, then pericardium and left atrium",
                "On the left then behind: descending thoracic aorta; behind: thoracic "
                "duct and azygos vein",
                "Vagus nerves: the left becomes anterior, the right posterior, because "
                "of the rotation of the stomach",
            ],
            "function": [
                "Carries the food bolus by peristalsis (oesophageal phase of swallowing)",
                "The lower sphincter limits gastro-oesophageal reflux",
            ],
            "vascularisation": [
                "Inferior thyroid arteries (neck), oesophageal and bronchial branches of "
                "the aorta (thorax), left gastric artery (abdomen)",
                "Lower third: portocaval anastomosis between the left gastric vein "
                "(portal system) and the azygos veins (caval system)",
            ],
            "innervation": [
                "Vagus nerves (X), recurrent laryngeal nerves for the upper part, "
                "thoracic sympathetic trunk; oesophageal plexus",
            ],
            "clinical": [
                "Oesophageal varices in portal hypertension: risk of severe "
                "gastrointestinal bleeding",
                "Gastro-oesophageal reflux; Barrett's oesophagus, a glandular metaplasia "
                "predisposing to adenocarcinoma",
                "Hiatus hernia, most often sliding",
            ],
        },
        fact=(
            "The left atrium lies just in front of the oesophagus: transoesophageal "
            "echocardiography sees it at very close range."
        ),
    ),
    "S": StructureText(
        name="Stomach",
        kind="Hollow organ (dilated segment of the digestive tract)",
        region="Supramesocolic compartment: left hypochondrium and epigastrium",
        count="1",
        description=(
            "J-shaped pouch between the oesophagus (cardia) and the duodenum "
            "(pylorus), holding about 1 to 1.5 L in the adult. It is entirely "
            "covered by peritoneum (intraperitoneal)."
        ),
        sections={
            "parts": [
                "Cardia (T11), fundus above the cardia, body, antrum, pyloric canal and "
                "sphincter (L1)",
                "Lesser curvature on the right (angular incisure) and greater curvature "
                "on the left",
                "Cardial notch (angle of His) between the oesophagus and the fundus",
                "Muscular layer in three coats: longitudinal, circular and inner oblique",
            ],
            "relations": [
                "In front: left lobe of the liver, diaphragm, anterior abdominal wall",
                "Behind, across the omental bursa: pancreas, left kidney and suprarenal "
                "gland, spleen",
                "Lesser omentum at the lesser curvature; greater omentum at the greater "
                "curvature",
            ],
            "function": [
                "Reservoir and mixing; hydrochloric acid and intrinsic factor (parietal "
                "cells), pepsinogen (chief cells)",
                "Gastrin (G cells of the antrum); emptying regulated by the pylorus",
            ],
            "vascularisation": [
                "Coeliac trunk, which gives the left gastric, splenic and common hepatic "
                "arteries",
                "Lesser curvature: left and right gastric arteries; greater curvature: "
                "right and left gastro-omental arteries",
                "Fundus: short gastric arteries (from the splenic artery); veins drain "
                "to the portal vein",
            ],
            "innervation": [
                "Anterior and posterior vagal trunks (secretion, motility); sympathetic "
                "through the coeliac plexus (greater splanchnic nerves)",
            ],
            "clinical": [
                "Peptic ulcer (Helicobacter pylori, NSAIDs); complications: perforation, "
                "bleeding",
                "Infantile hypertrophic pyloric stenosis: projectile vomiting at 3 to 6 weeks",
                "Lack of intrinsic factor (pernicious anaemia, gastrectomy): vitamin B12 "
                "deficiency",
            ],
        },
        fact=(
            "Gastric pH falls to 1-2; a layer of mucus and bicarbonate stops the "
            "stomach from digesting itself."
        ),
    ),
    "D": StructureText(
        name="Duodenum",
        kind="Hollow organ (first segment of the small intestine)",
        region="Around the head of the pancreas, at the level of L1 to L3",
        count="1",
        description=(
            "C-shaped segment about 25 cm long that frames the head of the pancreas, "
            "from the pylorus to the duodenojejunal flexure. It is fixed "
            "(retroperitoneal) except for the cap. It receives bile and pancreatic juice."
        ),
        sections={
            "parts": [
                "D1, superior part: duodenal cap (bulb), mobile, at L1",
                "D2, descending part: right of L1-L3, bears the major and minor papillae",
                "D3, horizontal part: crosses L3 between the aorta behind and the "
                "superior mesenteric vessels in front",
                "D4, ascending part: up to the duodenojejunal flexure (L2), held by the "
                "suspensory muscle of the duodenum (ligament of Treitz)",
                "Major papilla (hepatopancreatic ampulla, of Vater): bile duct and main "
                "pancreatic duct, surrounded by the sphincter of Oddi",
                "Minor papilla, above it: accessory pancreatic duct",
            ],
            "relations": [
                "Head of the pancreas in the concavity of the C",
                "D1: gallbladder, hepatic pedicle, gastroduodenal artery behind",
                "D2: in front of the right kidney; crossed in front by the root of the "
                "transverse mesocolon",
            ],
            "function": [
                "Neutralises gastric acid and digests food with bile and pancreatic juice",
                "Secretes secretin and cholecystokinin; duodenal (Brunner's) glands make "
                "alkaline mucus",
            ],
            "vascularisation": [
                "Pancreaticoduodenal arcades: superior arteries (gastroduodenal artery) "
                "and inferior artery (superior mesenteric artery)",
                "Junction zone between the territories of the coeliac trunk and the "
                "superior mesenteric artery",
            ],
            "innervation": [
                "Vagus nerves (X) and sympathetic (coeliac and superior mesenteric plexuses)",
            ],
            "clinical": [
                "Duodenal cap ulcer, the most frequent site; a posterior ulcer can erode "
                "the gastroduodenal artery",
                "Stone impacted in the ampulla: jaundice and acute biliary pancreatitis",
                "Superior mesenteric artery syndrome: D3 compressed between the aorta and "
                "the superior mesenteric artery",
            ],
        },
        fact=(
            "The duodenojejunal flexure separates upper gastrointestinal bleeding "
            "(above) from lower (below)."
        ),
    ),
    "L": StructureText(
        name="Liver",
        kind="Accessory gland of the digestive tract (solid organ)",
        region="Supramesocolic compartment: right hypochondrium and epigastrium",
        count="1",
        description=(
            "Largest gland of the body (about 1.5 kg), under the right dome of the "
            "diaphragm. It receives blood from the portal vein and the hepatic "
            "artery, has many metabolic functions and secretes bile."
        ),
        sections={
            "parts": [
                "Right and left lobes separated by the falciform ligament; quadrate and "
                "caudate lobes on the visceral surface",
                "Couinaud segmentation: 8 segments (I to VIII), each with its own portal "
                "pedicle; segment I (caudate lobe) is independent",
                "Right liver (V to VIII) and left liver (II to IV) separated by the main "
                "portal fissure (Cantlie's line, middle hepatic vein)",
                "Hepatic pedicle (free edge of the lesser omentum): portal vein behind, "
                "hepatic artery proper in front on the left, bile duct in front on the right",
                "Three hepatic veins (right, middle, left) draining into the inferior "
                "vena cava",
            ],
            "relations": [
                "Diaphragmatic surface under the diaphragm; bare area, without "
                "peritoneum, against the diaphragm",
                "Visceral surface: stomach, D1, right colic flexure, right kidney, "
                "gallbladder",
                "Inferior vena cava in a groove on the posterior surface",
            ],
            "function": [
                "Secretion of bile, about 0.5 to 1 L per day",
                "Metabolism of carbohydrates (glycogen, gluconeogenesis), lipids and "
                "proteins (albumin, clotting factors)",
                "Detoxification (drugs, ammonia turned into urea) and storage (iron, "
                "vitamins A, D and B12)",
            ],
            "vascularisation": [
                "Portal vein (about 75 % of the flow, venous blood from the gut) and "
                "hepatic artery proper (about 25 %, oxygenated blood)",
                "Drainage by the hepatic veins into the inferior vena cava",
            ],
            "innervation": [
                "Hepatic plexus (vagus nerves and sympathetic from the coeliac plexus); "
                "fibrous (Glisson's) capsule sensitive to stretch",
            ],
            "clinical": [
                "Portal hypertension (cirrhosis): portocaval anastomoses (oesophageal, "
                "rectal, paraumbilical as caput medusae), ascites, splenomegaly",
                "Pringle manoeuvre: clamping the hepatic pedicle to control bleeding",
                "Segmentation allows anatomical liver resections, segment by segment",
            ],
        },
        fact=(
            "The liver regenerates: after part of it is removed, it regains a volume "
            "close to the original within a few weeks."
        ),
    ),
    "G": StructureText(
        name="Gallbladder and bile ducts",
        old_names=["common bile duct"],
        kind="Bile reservoir and extrahepatic excretory ducts",
        region="Visceral surface of the liver (right hypochondrium) and hepatic pedicle",
        count="1",
        description=(
            "The gallbladder is a pear-shaped reservoir of about 50 mL, lying in the "
            "gallbladder fossa on the visceral surface of the liver. The main bile "
            "duct carries bile from the liver to the duodenum."
        ),
        sections={
            "parts": [
                "Gallbladder: fundus, body, neck (infundibulum), then the cystic duct "
                "with its spiral fold (valves of Heister)",
                "Right and left hepatic ducts, joining as the common hepatic duct",
                "The common hepatic duct and the cystic duct form the bile duct",
                "Bile duct: in the lesser omentum, then behind D1, through the head of "
                "the pancreas, to the major papilla (D2)",
            ],
            "relations": [
                "Fundus opposite the right 9th costal cartilage, on the midclavicular line",
                "Body and neck against D1 and the right colic flexure",
                "Hepatocystic (Calot's) triangle: cystic duct, common hepatic duct and "
                "liver; it contains the cystic artery",
            ],
            "function": [
                "Stores and concentrates bile; contracts under cholecystokinin after a "
                "fatty meal",
                "Bile salts emulsify fats; enterohepatic cycle by reabsorption in the "
                "terminal ileum",
            ],
            "vascularisation": [
                "Cystic artery, most often a branch of the right hepatic artery, in "
                "Calot's triangle",
            ],
            "innervation": [
                "Hepatic plexus (vagus and coeliac sympathetic); right phrenic nerve for "
                "the nearby peritoneum",
            ],
            "clinical": [
                "Gallstones: biliary colic; acute cholecystitis with Murphy's sign "
                "(inspiration stopped by palpation)",
                "Pain referred to the right shoulder by irritation of the phrenic nerve "
                "(C3-C5)",
                "Bile duct stone: jaundice, cholangitis with Charcot's triad (pain, "
                "fever, jaundice)",
            ],
        },
        fact=(
            "In cholecystectomy, Calot's triangle is dissected before anything is "
            "cut, so as not to mistake the bile duct for the cystic duct."
        ),
    ),
    "N": StructureText(
        name="Pancreas",
        kind="Mixed (exocrine and endocrine) gland, retroperitoneal",
        region="Supramesocolic compartment, behind the stomach, at the level of L1-L2",
        count="1",
        description=(
            "Gland lying transversely (about 15 cm, 80 g), from the concavity of the "
            "duodenum to the hilum of the spleen. It secretes pancreatic juice and "
            "hormones (insulin, glucagon)."
        ),
        sections={
            "parts": [
                "Head (in the duodenal C) with the uncinate process, neck, body and tail",
                "Main pancreatic duct (of Wirsung), joining the bile duct at the major papilla",
                "Accessory pancreatic duct (of Santorini), to the minor papilla",
            ],
            "relations": [
                "In front: stomach, across the omental bursa; root of the transverse "
                "mesocolon",
                "Behind the neck: union of the superior mesenteric and splenic veins, "
                "origin of the portal vein",
                "Tail at the hilum of the spleen; splenic vessels along the upper border",
                "Uncinate process behind the superior mesenteric vessels",
            ],
            "function": [
                "Exocrine (about 98 % of the mass): 1.5 L per day of juice rich in "
                "enzymes (lipase, amylase, trypsinogen) and bicarbonate",
                "Endocrine: pancreatic islets (of Langerhans); β cells (insulin), α "
                "(glucagon), δ (somatostatin)",
            ],
            "vascularisation": [
                "Head: pancreaticoduodenal arcades (gastroduodenal and superior "
                "mesenteric arteries)",
                "Body and tail: branches of the splenic artery",
            ],
            "innervation": [
                "Vagus (secretion) and sympathetic (coeliac plexus); pancreatic pain is "
                "deep, boring, radiating to the back",
            ],
            "clinical": [
                "Acute pancreatitis, mostly gallstone or alcohol related; serum lipase "
                "above 3 times normal",
                "Cancer of the head: jaundice from bile duct compression, enlarged "
                "palpable gallbladder (Courvoisier's law)",
                "Pancreaticoduodenectomy (Whipple procedure)",
            ],
        },
        fact=(
            "The head of the pancreas and the duodenum share their blood supply: "
            "one is not removed without the other."
        ),
    ),
    "J": StructureText(
        name="Jejunum and ileum",
        old_names=["mesenteric small intestine"],
        kind="Hollow organ (mobile small intestine)",
        region="Inframesocolic compartment: umbilical region, flanks and pelvis",
        count="1",
        description=(
            "Mobile part of the small intestine, several metres long (about 5 to 6 m "
            "in the cadaver, less in life), from the duodenojejunal flexure to the "
            "ileocaecal junction. Its loops hang from the mesentery."
        ),
        sections={
            "parts": [
                "Jejunum (proximal 2/5, upper left): wider, thick wall, many circular "
                "folds, long vasa recta",
                "Ileum (distal 3/5, lower right and pelvis): narrower, Peyer's patches, "
                "multiple arcades with short vasa recta",
                "Mesentery: oblique root about 15 cm long, from the left of L2 to the "
                "right iliac fossa",
                "Circular folds, villi and microvilli that multiply the absorptive surface",
            ],
            "relations": [
                "Framed by the colon; covered in front by the greater omentum",
                "Behind, the root of the mesentery crosses D3, the aorta, the inferior "
                "vena cava and the right ureter",
            ],
            "function": [
                "Final digestion and absorption of nutrients, water and electrolytes",
                "Terminal ileum: absorption of vitamin B12 (bound to intrinsic factor) "
                "and of bile salts",
            ],
            "vascularisation": [
                "Superior mesenteric artery: jejunal and ileal arteries, arcades then "
                "vasa recta",
                "Superior mesenteric vein to the portal vein",
            ],
            "innervation": [
                "Vagus and sympathetic (superior mesenteric plexus); enteric nervous "
                "system (myenteric and submucosal plexuses)",
            ],
            "clinical": [
                "Meckel's diverticulum: remnant of the vitelline duct on the "
                "antimesenteric border of the ileum, about 60 cm from the ileocaecal valve",
                "Small bowel obstruction (adhesions, strangulated hernia); Crohn's "
                "disease, often of the terminal ileum",
                "Acute mesenteric ischaemia, from embolism of the superior mesenteric artery",
            ],
        },
        fact=(
            "Folds, villi and microvilli multiply the absorptive surface of the small "
            "intestine by about 600."
        ),
    ),
    "C": StructureText(
        name="Caecum and vermiform appendix",
        kind="Hollow organ (first segment of the colon) and lymphoid diverticulum",
        region="Right iliac fossa",
        count="1",
        description=(
            "Blind pouch of the large intestine below the opening of the ileum. The "
            "vermiform appendix, about 6 to 10 cm long, arises from its posteromedial "
            "wall, where the three taeniae coli converge."
        ),
        sections={
            "parts": [
                "Ileocaecal valve (Bauhin's valve) at the opening of the ileum",
                "Base of the appendix 2-3 cm below the valve, where the three taeniae converge",
                "Variable position of the appendix: retrocaecal (the most frequent), "
                "pelvic, subcaecal, preileal or postileal",
                "Mesoappendix containing the appendicular artery",
            ],
            "relations": [
                "Right iliac fossa, on the iliopsoas muscle",
                "McBurney's point: junction of the lateral third and medial two thirds "
                "of the line from the right anterior superior iliac spine to the umbilicus",
            ],
            "function": [
                "Reabsorption of water and electrolytes; appendix rich in lymphoid "
                "tissue (immune role)",
            ],
            "vascularisation": [
                "Ileocolic artery (branch of the superior mesenteric artery): caecal "
                "arteries and the appendicular artery, an end artery",
            ],
            "innervation": [
                "Superior mesenteric plexus; appendix pain first periumbilical (T10), "
                "then in the right iliac fossa",
            ],
            "clinical": [
                "Acute appendicitis: right iliac fossa pain, maximal at McBurney's point, "
                "with guarding",
                "Blumberg's sign (rebound tenderness); psoas sign in retrocaecal forms",
                "At appendicectomy, the base is found by following the taeniae to where "
                "they converge",
            ],
        },
        fact="Appendicitis is the most frequent abdominal surgical emergency.",
    ),
    "A": StructureText(
        name="Ascending colon",
        kind="Hollow organ (large intestine), fixed to the posterior wall",
        region="Right flank, from the caecum to the right colic flexure",
        count="1",
        description=(
            "Segment about 15 cm long that rises from the caecum to the right colic "
            "(hepatic) flexure, under the liver. It is fixed to the posterior "
            "abdominal wall by the right fusion fascia (Toldt's fascia)."
        ),
        sections={
            "parts": [
                "Features of the colon: three taeniae, haustra and omental (epiploic) "
                "appendices",
                "Right colic (hepatic) flexure, under the visceral surface of the liver",
            ],
            "relations": [
                "Behind: quadratus lumborum, lower pole of the right kidney",
                "Medially: small bowel loops; laterally: right paracolic gutter",
            ],
            "function": [
                "Reabsorption of water and electrolytes from a still liquid content; "
                "bacterial fermentation",
            ],
            "vascularisation": [
                "Superior mesenteric artery: ileocolic artery and right colic artery "
                "(inconstant)",
                "Marginal artery of the colon, linking the colic arteries",
            ],
            "innervation": [
                "Vagus nerve and sympathetic (superior mesenteric plexus)",
            ],
            "clinical": [
                "Right colon cancer, often revealed by iron-deficiency anaemia; treated "
                "by right hemicolectomy",
                "Toldt's fascia offers a bloodless plane for surgical mobilisation",
            ],
        },
        fact=(
            "The right colon comes from the embryonic midgut: like the small "
            "intestine, it is supplied by the superior mesenteric artery."
        ),
    ),
    "T": StructureText(
        name="Transverse colon",
        kind="Hollow organ (large intestine), mobile",
        region="Middle of the abdomen, between the two colic flexures",
        count="1",
        description=(
            "Longest (about 45 cm) and most mobile segment of the colon, suspended "
            "by the transverse mesocolon, which divides the peritoneal cavity into "
            "supramesocolic and inframesocolic compartments."
        ),
        sections={
            "parts": [
                "Right colic flexure, lower; left colic flexure, higher and deeper, held "
                "by the phrenicocolic ligament",
                "Transverse mesocolon, whose root crosses D2 and the pancreas",
                "Gastrocolic ligament (part of the greater omentum) linking it to the "
                "greater curvature",
            ],
            "relations": [
                "Above: liver, gallbladder, greater curvature of the stomach, spleen",
                "Below: small bowel loops; in front: greater omentum and abdominal wall",
            ],
            "function": [
                "Water absorption; mixing and propulsion by mass movements",
            ],
            "vascularisation": [
                "Right two thirds: middle colic artery (superior mesenteric); left "
                "third: left colic artery (inferior mesenteric)",
                "Superior-inferior mesenteric anastomoses through the marginal artery; "
                "the arc of Riolan is inconstant and defined differently by authors",
            ],
            "innervation": [
                "Right two thirds: vagus nerve; left third: pelvic splanchnic nerves "
                "(S2-S4); sympathetic from the mesenteric plexuses",
            ],
            "clinical": [
                "Left colic flexure: watershed between two arterial territories, "
                "prone to ischaemic colitis",
                "Accessible and mobile: classic site of a transverse colostomy",
            ],
        },
        fact=(
            "The junction of the right two thirds and the left third marks the "
            "embryonic boundary between midgut and hindgut."
        ),
    ),
    "X": StructureText(
        name="Descending colon",
        kind="Hollow organ (large intestine), fixed to the posterior wall",
        region="Left flank, from the left colic flexure to the iliac crest",
        count="1",
        description=(
            "Segment about 25 cm long, narrower than the right colon, that runs down "
            "from the left colic flexure to the left iliac crest, where it becomes "
            "the sigmoid colon. It is fixed by the left Toldt's fascia."
        ),
        sections={
            "parts": [
                "Taeniae, haustra and omental appendices; narrower lumen than the right "
                "colon",
                "Left colic (splenic) flexure, the highest, against the spleen",
            ],
            "relations": [
                "Behind: lateral border of the left kidney, quadratus lumborum",
                "Medially: jejunal loops; laterally: left paracolic gutter",
            ],
            "function": [
                "Dehydration and temporary storage of faeces",
            ],
            "vascularisation": [
                "Left colic artery, branch of the inferior mesenteric artery",
                "Inferior mesenteric vein, which joins the splenic vein and then the "
                "portal vein",
            ],
            "innervation": [
                "Sacral parasympathetic (pelvic splanchnic nerves, S2-S4); sympathetic "
                "(inferior mesenteric plexus)",
            ],
            "clinical": [
                "Left colon cancer: change in bowel habit and obstruction, as the lumen "
                "is narrow and the faeces solid",
            ],
        },
        fact=(
            "The left colon comes from the hindgut, supplied by the inferior "
            "mesenteric artery, which leaves the aorta at L3."
        ),
    ),
    "Z": StructureText(
        name="Sigmoid colon",
        old_names=["pelvic colon"],
        kind="Hollow organ (large intestine), mobile",
        region="Left iliac fossa and pelvis",
        count="1",
        description=(
            "Mobile loop of very variable length (about 40 cm), suspended by the "
            "sigmoid mesocolon, from the left iliac crest to the rectosigmoid "
            "junction (S3)."
        ),
        sections={
            "parts": [
                "Sigmoid mesocolon with an inverted-V root; the left ureter passes under "
                "the apex of the V",
                "The taeniae widen and merge at the rectosigmoid junction",
            ],
            "relations": [
                "In the pelvis: bladder, and in women the uterus and left adnexa",
                "Behind the mesocolon: left ureter and iliac vessels",
            ],
            "function": [
                "Stores faeces before they pass into the rectum",
            ],
            "vascularisation": [
                "Sigmoid arteries, branches of the inferior mesenteric artery",
            ],
            "innervation": [
                "Sacral parasympathetic (S2-S4); sympathetic (inferior mesenteric plexus)",
            ],
            "clinical": [
                "Sigmoid diverticulitis: pain and fever in the left iliac fossa "
                "(\"left-sided appendicitis\")",
                "Sigmoid volvulus, mainly in the elderly",
                "Colorectal cancer is frequent at the rectosigmoid junction; screening "
                "by colonoscopy",
            ],
        },
        fact=(
            "In Western countries, the sigmoid is the most frequent site of colonic "
            "diverticula."
        ),
    ),
    "R": StructureText(
        name="Rectum and anal canal",
        kind="Hollow organ (last segment of the digestive tract)",
        region="Pelvis (lesser pelvis) and perineum",
        count="1",
        description=(
            "The rectum (about 12 to 15 cm) runs from S3 to the anorectal junction, "
            "following the curve of the sacrum. The anal canal (3 to 4 cm) crosses "
            "the perineum to the anus."
        ),
        sections={
            "parts": [
                "Rectal ampulla (reservoir) and transverse folds; no taeniae and no haustra",
                "Anorectal angle held by the sling of the puborectalis muscle",
                "Anal canal: anal columns and pectinate line (endoderm-ectoderm junction)",
                "Internal sphincter (smooth, involuntary) and external sphincter "
                "(striated, voluntary)",
            ],
            "relations": [
                "In men: bladder, seminal glands, prostate; rectovesical pouch",
                "In women: uterus and vagina; rectouterine pouch (of Douglas), the lowest "
                "point of the peritoneal cavity",
                "Behind: sacrum, coccyx and mesorectum",
            ],
            "function": [
                "Continence and defecation: rectoanal inhibitory reflex and voluntary "
                "control of the external sphincter",
            ],
            "vascularisation": [
                "Superior rectal artery (end of the inferior mesenteric), middle rectal "
                "(internal iliac) and inferior rectal (internal pudendal) arteries",
                "Rectal venous plexuses: portocaval anastomosis (superior rectal to the "
                "portal vein, middle and inferior to the caval system)",
            ],
            "innervation": [
                "Above the pectinate line: autonomic supply, little pain sensitivity; "
                "below: pudendal nerve, very sensitive",
                "External sphincter: pudendal nerve (S2-S4)",
            ],
            "clinical": [
                "Digital rectal examination: prostate; painful pouch of Douglas in "
                "peritonitis",
                "Haemorrhoidal disease; anal fissure, painful because below the "
                "pectinate line",
                "Rectal cancer: total mesorectal excision",
            ],
        },
        fact=(
            "Across the pectinate line the epithelium, blood supply, lymphatic "
            "drainage and nerve supply all change."
        ),
    ),
}
