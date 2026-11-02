"""Textes en français (nomenclature anatomique internationale francisée,
celle utilisée en PASS / L.AS). Les anciens noms et éponymes sont indiqués
à titre de correspondance."""

from __future__ import annotations

from ...model import StructureText

TEXTS: dict[str, StructureText] = {
    "O": StructureText(
        name="Cavité orale",
        old_names=["cavité buccale", "bouche"],
        kind="Cavité (segment initial du tube digestif)",
        region="Tête (étage inférieur de la face)",
        count="1",
        description=(
            "Première partie du tube digestif, limitée en avant par les lèvres et en "
            "arrière par l'isthme du gosier. Elle comprend le vestibule oral (entre "
            "lèvres, joues et arcades dentaires) et la cavité orale proprement dite, "
            "qui contient la langue."
        ),
        sections={
            "parts": [
                "Vestibule oral et cavité orale proprement dite, séparés par les arcades "
                "alvéolo-dentaires",
                "Toit : palais dur (osseux) en avant, palais mou (voile) terminé par "
                "l'uvule en arrière",
                "Plancher : muscles mylo-hyoïdiens (diaphragme oral) et langue",
                "Langue : muscle strié ; le sillon terminal en V sépare le corps (2/3 "
                "antérieurs) de la racine (1/3 postérieur) ; papilles circumvallées en "
                "avant du V",
                "Dents : 20 dents temporaires (déciduales), 32 dents permanentes ; "
                "formule par hémi-arcade 2 incisives, 1 canine, 2 prémolaires, 3 molaires",
                "Isthme du gosier, limité par les arcs palato-glosses : passage vers "
                "l'oropharynx",
            ],
            "function": [
                "Mastication, insalivation et formation du bol alimentaire",
                "Temps oral, volontaire, de la déglutition",
                "Gustation et articulation de la parole",
                "Début de la digestion de l'amidon par l'amylase salivaire",
            ],
            "vascularisation": [
                "Branches de l'artère carotide externe : artère linguale, artère faciale "
                "et artère maxillaire (artères alvéolaires et palatines)",
            ],
            "innervation": [
                "Motricité de la langue : nerf hypoglosse (XII), sauf le muscle "
                "palato-glosse (nerf vague, X)",
                "Corps de la langue : sensibilité générale par le nerf lingual (V3), goût "
                "par la corde du tympan (VII)",
                "Racine de la langue : sensibilité et goût par le nerf glosso-pharyngien (IX)",
                "Dents : nerfs alvéolaires supérieurs (V2) et nerf alvéolaire inférieur (V3)",
            ],
            "clinical": [
                "Paralysie du XII : langue tirée déviée du côté paralysé",
                "Carie et abcès dentaire, pouvant diffuser au plancher oral (cellulite "
                "cervico-faciale)",
                "Voie sublinguale : absorption rapide de certains médicaments (trinitrine) "
                "sans premier passage hépatique",
            ],
        },
        fact=(
            "Les papilles circumvallées, une dizaine, forment le V lingual et portent "
            "une grande partie des bourgeons du goût."
        ),
    ),
    "P": StructureText(
        name="Glande parotide",
        kind="Glande salivaire principale (exocrine, séreuse)",
        region="Région parotidienne, en avant de l'oreille et en arrière de la mandibule",
        count="2 (paire)",
        description=(
            "La plus volumineuse des glandes salivaires, logée dans la loge "
            "parotidienne. Sa salive séreuse rejoint le vestibule oral par le conduit "
            "parotidien. Les autres glandes salivaires principales sont les glandes "
            "submandibulaire et sublinguale."
        ),
        sections={
            "parts": [
                "Loge parotidienne : branche de la mandibule en avant, processus "
                "mastoïde et muscle sterno-cléido-mastoïdien en arrière",
                "Conduit parotidien (canal de Sténon) : croise le masséter, perfore le "
                "buccinateur, s'ouvre en regard de la 2e molaire supérieure",
                "Partie superficielle et partie profonde, séparées par le plan du nerf facial",
            ],
            "relations": [
                "Traversée, de la superficie à la profondeur, par le nerf facial (VII), la "
                "veine rétro-mandibulaire et l'artère carotide externe",
                "L'artère carotide externe s'y termine en artères maxillaire et temporale "
                "superficielle",
            ],
            "function": [
                "Sécrétion d'une salive séreuse riche en amylase salivaire",
                "Toutes glandes confondues : environ 1 à 1,5 L de salive par jour",
            ],
            "innervation": [
                "Parasympathique sécrétoire : nerf glosso-pharyngien (IX), nerf petit "
                "pétreux, ganglion otique, puis nerf auriculo-temporal (V3)",
                "Sympathique : plexus autour de l'artère carotide externe",
            ],
            "clinical": [
                "Oreillons : parotidite virale, souvent bilatérale",
                "Parotidectomie : risque de paralysie faciale périphérique",
                "Les calculs salivaires sont plus fréquents dans la glande submandibulaire "
                "que dans la parotide",
            ],
        },
        fact=(
            "Le nerf facial traverse la parotide sans l'innerver : sa sécrétion dépend "
            "du nerf glosso-pharyngien."
        ),
    ),
    "H": StructureText(
        name="Pharynx",
        kind="Conduit musculo-membraneux (carrefour aérodigestif)",
        region="Cou, en avant du rachis cervical, de la base du crâne à C6",
        count="1 (impair et médian)",
        description=(
            "Conduit d'environ 15 cm, de la base du crâne au bord inférieur du "
            "cartilage cricoïde (C6), où il se continue par l'œsophage. Il est commun "
            "aux voies aériennes et digestives."
        ),
        sections={
            "parts": [
                "Nasopharynx (rhinopharynx) : en arrière des choanes ; orifices des "
                "trompes auditives, tonsille pharyngée",
                "Oropharynx : en arrière de l'isthme du gosier ; tonsilles palatines",
                "Laryngopharynx (hypopharynx) : en arrière du larynx ; récessus "
                "piriformes",
                "Muscles constricteurs supérieur, moyen et inférieur, et muscles "
                "élévateurs (dont le stylo-pharyngien)",
            ],
            "relations": [
                "En arrière : espace rétro-pharyngien, fascia prévertébral, vertèbres "
                "cervicales",
                "Latéralement : espace latéro-pharyngien, artère carotide interne, veine "
                "jugulaire interne et nerfs IX à XII",
            ],
            "function": [
                "Temps pharyngé, réflexe, de la déglutition : fermeture du nasopharynx "
                "par le voile ; protection des voies aériennes par l'ascension et la "
                "fermeture du larynx, et la bascule de l'épiglotte",
                "Passage de l'air ; résonance de la voix ; anneau lymphatique pharyngé "
                "(de Waldeyer)",
            ],
            "vascularisation": [
                "Artère pharyngienne ascendante (carotide externe) et branches des "
                "artères faciale, maxillaire et thyroïdiennes",
            ],
            "innervation": [
                "Plexus pharyngien : nerf glosso-pharyngien (IX, sensitif) et nerf vague "
                "(X, moteur des constricteurs) ; le stylo-pharyngien est innervé par le IX (sensibilité : "
                "nasopharynx par le V2, laryngopharynx par le X)",
            ],
            "clinical": [
                "Réflexe nauséeux : afférence par le IX, efférence par le X",
                "Diverticule pharyngo-œsophagien (de Zenker), en arrière, au-dessus du "
                "muscle crico-pharyngien",
                "Corps étrangers (arêtes) bloqués dans les tonsilles palatines, les "
                "vallécules ou les récessus piriformes",
            ],
        },
        fact="Le pharynx est le seul segment partagé par l'air et les aliments.",
    ),
    "E": StructureText(
        name="Œsophage",
        kind="Organe creux (conduit musculaire)",
        region="Cou, médiastin postérieur et abdomen",
        count="1",
        description=(
            "Conduit musculaire d'environ 25 cm, de C6 au cardia (T11). Il traverse "
            "le diaphragme par le hiatus œsophagien (T10). Sa muqueuse est un "
            "épithélium pavimenteux stratifié non kératinisé."
        ),
        sections={
            "parts": [
                "Trois segments : cervical, thoracique (le plus long) et abdominal "
                "(2 à 3 cm)",
                "Musculeuse striée dans le tiers supérieur, mixte au milieu, lisse dans "
                "le tiers inférieur",
                "Rétrécissements : bouche œsophagienne (C6), arc de l'aorte, bronche "
                "principale gauche, hiatus diaphragmatique",
                "Sphincter supérieur (muscle crico-pharyngien) et sphincter inférieur, "
                "fonctionnel, à la jonction œso-gastrique",
            ],
            "relations": [
                "En avant : trachée, bronche principale gauche, puis péricarde et atrium "
                "gauche",
                "À gauche puis en arrière : aorte thoracique descendante ; en arrière : "
                "conduit thoracique et veine azygos",
                "Nerfs vagues : le gauche devient antérieur, le droit postérieur, en "
                "raison de la rotation de l'estomac",
            ],
            "function": [
                "Transport du bol alimentaire par péristaltisme (temps œsophagien de la "
                "déglutition)",
                "Le sphincter inférieur limite le reflux gastro-œsophagien",
            ],
            "vascularisation": [
                "Artères thyroïdiennes inférieures (cou), artères œsophagiennes et "
                "bronchiques de l'aorte (thorax), artère gastrique gauche (abdomen)",
                "Tiers inférieur : anastomose porto-cave entre veine gastrique gauche "
                "(système porte) et veines azygos (système cave)",
            ],
            "innervation": [
                "Nerfs vagues (X), nerfs laryngés récurrents pour la partie haute, "
                "sympathique thoracique ; plexus œsophagien",
            ],
            "clinical": [
                "Varices œsophagiennes de l'hypertension portale : risque d'hémorragie "
                "digestive grave",
                "Reflux gastro-œsophagien ; endobrachyœsophage (de Barrett), métaplasie "
                "glandulaire exposant à l'adénocarcinome",
                "Hernie hiatale, le plus souvent par glissement",
            ],
        },
        fact=(
            "L'atrium gauche est juste devant l'œsophage : l'échographie "
            "transœsophagienne le montre de très près."
        ),
    ),
    "S": StructureText(
        name="Estomac",
        kind="Organe creux (segment dilaté du tube digestif)",
        region="Étage sus-mésocolique : hypochondre gauche et épigastre",
        count="1",
        description=(
            "Poche en forme de J entre l'œsophage (cardia) et le duodénum (pylore), "
            "d'une capacité d'environ 1 à 1,5 L chez l'adulte. Il est entièrement "
            "recouvert de péritoine (intrapéritonéal)."
        ),
        sections={
            "parts": [
                "Cardia (T11), fundus au-dessus du cardia, corps, antre, canal et "
                "sphincter pyloriques (L1)",
                "Petite courbure à droite (incisure angulaire) et grande courbure à gauche",
                "Incisure cardiale (angle de His) entre l'œsophage et le fundus",
                "Musculeuse en trois couches : longitudinale, circulaire et oblique interne",
            ],
            "relations": [
                "En avant : lobe gauche du foie, diaphragme, paroi abdominale antérieure",
                "En arrière, par la bourse omentale : pancréas, rein et glande surrénale "
                "gauches, rate",
                "Petit omentum à la petite courbure ; grand omentum à la grande courbure",
            ],
            "function": [
                "Réservoir et brassage ; acide chlorhydrique et facteur intrinsèque "
                "(cellules pariétales), pepsinogène (cellules principales)",
                "Gastrine (cellules G de l'antre) ; vidange régulée par le pylore",
            ],
            "vascularisation": [
                "Tronc cœliaque, qui donne les artères gastrique gauche, splénique et "
                "hépatique commune",
                "Petite courbure : artères gastriques gauche et droite ; grande courbure : "
                "artères gastro-omentales droite et gauche",
                "Fundus : artères gastriques courtes (de l'artère splénique) ; veines "
                "vers la veine porte",
            ],
            "innervation": [
                "Troncs vagaux antérieur et postérieur (sécrétion, motricité) ; "
                "sympathique par le plexus cœliaque (nerfs grands splanchniques)",
            ],
            "clinical": [
                "Ulcère gastro-duodénal (Helicobacter pylori, AINS) ; complications : "
                "perforation, hémorragie",
                "Sténose hypertrophique du pylore du nourrisson : vomissements en jet "
                "vers 3 à 6 semaines",
                "Absence de facteur intrinsèque (maladie de Biermer, gastrectomie) : "
                "carence en vitamine B12",
            ],
        },
        fact=(
            "Le pH gastrique descend à 1-2 ; une couche de mucus et de bicarbonate "
            "empêche l'estomac de se digérer lui-même."
        ),
    ),
    "D": StructureText(
        name="Duodénum",
        kind="Organe creux (premier segment de l'intestin grêle)",
        region="Autour de la tête du pancréas, en regard de L1 à L3",
        count="1",
        description=(
            "Segment d'environ 25 cm en forme de C qui encadre la tête du pancréas, "
            "du pylore à l'angle duodéno-jéjunal. Il est fixé (rétropéritonéal), sauf "
            "le bulbe. Il reçoit la bile et le suc pancréatique."
        ),
        sections={
            "parts": [
                "D1, partie supérieure : bulbe duodénal, mobile, en regard de L1",
                "D2, partie descendante : à droite de L1-L3, porte les papilles majeure "
                "et mineure",
                "D3, partie horizontale : croise L3 entre l'aorte en arrière et les "
                "vaisseaux mésentériques supérieurs en avant",
                "D4, partie ascendante : jusqu'à l'angle duodéno-jéjunal (L2), suspendu "
                "par le muscle suspenseur du duodénum (de Treitz)",
                "Papille duodénale majeure : débouché de l'ampoule hépato-pancréatique "
                "(de Vater), où s'unissent cholédoque et conduit pancréatique principal ; "
                "sphincter de l'ampoule (d'Oddi)",
                "Papille mineure, au-dessus : conduit pancréatique accessoire",
            ],
            "relations": [
                "Tête du pancréas dans la concavité du C",
                "D1 : vésicule biliaire, pédicule hépatique, artère gastro-duodénale en "
                "arrière",
                "D2 : en avant du rein droit ; croisé en avant par la racine du "
                "mésocôlon transverse",
            ],
            "function": [
                "Neutralisation de l'acidité gastrique et digestion grâce à la bile et "
                "au suc pancréatique",
                "Sécrétion de sécrétine et de cholécystokinine ; glandes duodénales (de "
                "Brunner) à mucus alcalin",
            ],
            "vascularisation": [
                "Arcades pancréatico-duodénales : artères supérieures (artère "
                "gastro-duodénale) et inférieure (artère mésentérique supérieure)",
                "Zone de jonction entre les territoires du tronc cœliaque et de l'artère "
                "mésentérique supérieure",
            ],
            "innervation": [
                "Nerfs vagues (X) et sympathique (plexus cœliaque et mésentérique supérieur)",
            ],
            "clinical": [
                "Ulcère du bulbe, localisation la plus fréquente ; un ulcère postérieur "
                "peut éroder l'artère gastro-duodénale",
                "Calcul enclavé dans l'ampoule : ictère et pancréatite aiguë biliaire",
                "Pince aorto-mésentérique : compression de D3 entre l'aorte et l'artère "
                "mésentérique supérieure",
            ],
        },
        fact=(
            "L'angle duodéno-jéjunal sépare les hémorragies digestives hautes (en "
            "amont) des basses (en aval), selon la définition classique."
        ),
    ),
    "L": StructureText(
        name="Foie",
        kind="Glande annexe du tube digestif (organe plein)",
        region="Étage sus-mésocolique : hypochondre droit et épigastre",
        count="1",
        description=(
            "Plus grosse glande de l'organisme (environ 1,5 kg), sous la coupole "
            "diaphragmatique droite. Il reçoit le sang de la veine porte et de "
            "l'artère hépatique, assure de nombreuses fonctions métaboliques et "
            "sécrète la bile."
        ),
        sections={
            "parts": [
                "Lobes droit et gauche séparés par le ligament falciforme ; lobes carré "
                "et caudé à la face viscérale",
                "Segmentation de Couinaud : 8 segments (I à VIII), chacun avec son "
                "pédicule portal ; le segment I (lobe caudé) est autonome",
                "Foie droit (V à VIII) et foie gauche (II à IV) séparés par la scissure "
                "(fissure) portale principale (ligne de Cantlie, veine hépatique moyenne)",
                "Pédicule hépatique (bord libre du petit omentum) : veine porte en "
                "arrière, artère hépatique propre en avant à gauche, cholédoque en avant "
                "à droite",
                "Trois veines hépatiques (droite, moyenne, gauche) qui se jettent dans la "
                "veine cave inférieure",
            ],
            "relations": [
                "Face diaphragmatique sous le diaphragme ; aire nue, sans péritoine, au "
                "contact du diaphragme",
                "Face viscérale : estomac, D1, angle colique droit, rein droit, vésicule "
                "biliaire",
                "Veine cave inférieure dans un sillon de la face postérieure",
            ],
            "function": [
                "Sécrétion de la bile, environ 0,5 à 1 L par jour",
                "Métabolisme des glucides (glycogène, néoglucogenèse), des lipides et des "
                "protéines (albumine, facteurs de coagulation)",
                "Détoxication (médicaments, ammoniac transformé en urée) et stockage (fer, "
                "vitamines A, D et B12)",
            ],
            "vascularisation": [
                "Veine porte (environ 75 % du débit, sang veineux digestif) et artère "
                "hépatique propre (environ 25 %, sang oxygéné)",
                "Drainage par les veines hépatiques dans la veine cave inférieure",
            ],
            "innervation": [
                "Plexus hépatique (nerfs vagues et sympathique du plexus cœliaque) ; "
                "capsule fibreuse (de Glisson) sensible à la distension",
            ],
            "clinical": [
                "Hypertension portale (cirrhose) : anastomoses porto-caves (œsophagiennes, "
                "rectales, para-ombilicales en « tête de méduse »), ascite, splénomégalie",
                "Manœuvre de Pringle : clampage du pédicule hépatique pour contrôler un "
                "saignement",
                "La segmentation permet des hépatectomies réglées, segment par segment",
            ],
        },
        fact=(
            "Le foie régénère : après l'ablation d'une partie, il retrouve en quelques "
            "semaines un volume proche du volume initial."
        ),
    ),
    "G": StructureText(
        name="Vésicule biliaire et voies biliaires",
        old_names=["canal cystique", "canal cholédoque", "canal hépatique"],
        kind="Réservoir de bile et conduits excréteurs extra-hépatiques",
        region="Face viscérale du foie (hypochondre droit) et pédicule hépatique",
        count="1",
        description=(
            "La vésicule biliaire est un réservoir piriforme d'environ 50 mL, logé "
            "dans la fosse de la vésicule biliaire à la face viscérale du foie. La "
            "voie biliaire principale conduit la bile du foie au duodénum."
        ),
        sections={
            "parts": [
                "Vésicule : fond, corps, infundibulum puis col (poche de Hartmann), puis "
                "conduit cystique à plis spiraux (valvules de Heister)",
                "Conduits hépatiques droit et gauche, réunis en conduit hépatique commun",
                "Conduit hépatique commun et conduit cystique forment le conduit "
                "cholédoque",
                "Cholédoque : dans le petit omentum, puis en arrière de D1, dans la tête "
                "du pancréas, jusqu'à la papille majeure (D2)",
            ],
            "relations": [
                "Fond en regard du 9e cartilage costal droit, sur la ligne "
                "médio-claviculaire",
                "Corps et col au contact de D1 et de l'angle colique droit",
                "Triangle hépato-cystique (de Calot) : conduit cystique, conduit hépatique "
                "commun et foie ; il contient l'artère cystique (le triangle original de Calot "
                "avait l'artère cystique pour bord supérieur ; le triangle "
                "hépato-cystique en est la version moderne, plus grande)",
            ],
            "function": [
                "Stockage et concentration de la bile ; contraction sous l'effet de la "
                "cholécystokinine après un repas gras",
                "Les sels biliaires émulsionnent les graisses ; cycle entéro-hépatique "
                "par réabsorption dans l'iléum terminal",
            ],
            "vascularisation": [
                "Artère cystique, le plus souvent branche de l'artère hépatique droite, "
                "dans le triangle de Calot",
            ],
            "innervation": [
                "Plexus hépatique (vague et sympathique cœliaque) ; nerf phrénique droit "
                "pour le péritoine voisin",
            ],
            "clinical": [
                "Lithiase biliaire : colique hépatique ; cholécystite aiguë avec signe de "
                "Murphy (inspiration bloquée à la palpation)",
                "Douleur projetée à l'épaule droite par irritation du nerf phrénique "
                "(C3-C5)",
                "Calcul du cholédoque : ictère, angiocholite avec la triade de Charcot "
                "(douleur, fièvre, ictère)",
            ],
        },
        fact=(
            "En cholécystectomie, le triangle de Calot est disséqué avant toute section "
            "pour ne pas confondre cystique et cholédoque."
        ),
    ),
    "N": StructureText(
        name="Pancréas",
        kind="Glande mixte (exocrine et endocrine), rétropéritonéale (sauf la queue)",
        region="Étage sus-mésocolique, en arrière de l'estomac, en regard de L1-L2",
        count="1",
        description=(
            "Glande allongée transversalement (environ 15 cm, 80 g), de la concavité "
            "du duodénum jusqu'au hile de la rate. Elle sécrète le suc pancréatique "
            "et des hormones (insuline, glucagon)."
        ),
        sections={
            "parts": [
                "Tête (dans le cadre duodénal) avec le processus unciné, col (isthme), "
                "corps et queue",
                "Conduit pancréatique principal (de Wirsung), qui rejoint le cholédoque à "
                "la papille majeure",
                "Conduit pancréatique accessoire (de Santorini), vers la papille mineure",
            ],
            "relations": [
                "En avant : estomac, séparé par la bourse omentale ; racine du mésocôlon "
                "transverse",
                "En arrière du col : confluent des veines mésentérique supérieure et "
                "splénique, origine de la veine porte",
                "Queue au hile de la rate ; vaisseaux spléniques le long du bord "
                "supérieur",
                "Processus unciné en arrière des vaisseaux mésentériques supérieurs",
            ],
            "function": [
                "Exocrine (environ 98 % de la masse) : 1,5 L par jour d'un suc riche en "
                "enzymes (lipase, amylase, trypsinogène) et en bicarbonates",
                "Endocrine : îlots pancréatiques (de Langerhans) ; cellules β (insuline), "
                "α (glucagon), δ (somatostatine)",
            ],
            "vascularisation": [
                "Tête : arcades pancréatico-duodénales (artère gastro-duodénale et artère "
                "mésentérique supérieure)",
                "Corps et queue : branches de l'artère splénique",
            ],
            "innervation": [
                "Vague (sécrétion) et sympathique (plexus cœliaque) ; douleur "
                "pancréatique transfixiante, irradiant dans le dos",
            ],
            "clinical": [
                "Pancréatite aiguë, surtout biliaire ou alcoolique ; lipasémie supérieure "
                "à 3 fois la normale",
                "Cancer de la tête : ictère par compression du cholédoque, grosse "
                "vésicule palpable (loi de Courvoisier-Terrier)",
                "Duodéno-pancréatectomie céphalique (intervention de Whipple)",
            ],
        },
        fact=(
            "La tête du pancréas et le duodénum partagent leur vascularisation : on "
            "n'enlève pas l'une sans l'autre."
        ),
    ),
    "J": StructureText(
        name="Jéjunum et iléum",
        old_names=["iléon", "intestin grêle mésentérique"],
        kind="Organe creux (intestin grêle mobile)",
        region="Étage sous-mésocolique : région ombilicale, flancs et pelvis",
        count="1",
        description=(
            "Partie mobile de l'intestin grêle, longue de plusieurs mètres (environ "
            "5 à 6 m sur le cadavre, moins in vivo), de l'angle duodéno-jéjunal à la "
            "jonction iléo-cæcale. Ses anses sont suspendues au mésentère."
        ),
        sections={
            "parts": [
                "Jéjunum (2/5 proximaux, en haut à gauche) : plus large, paroi épaisse, "
                "nombreux plis circulaires, longs vaisseaux droits",
                "Iléum (3/5 distaux, en bas à droite et dans le pelvis) : plus étroit, "
                "plaques de Peyer, arcades multiples à vaisseaux droits courts",
                "Mésentère : racine oblique d'environ 15 cm, de la gauche de L2 à la "
                "fosse iliaque droite",
                "Plis circulaires, villosités et microvillosités qui multiplient la "
                "surface d'absorption",
            ],
            "relations": [
                "Encadré par le côlon ; recouvert en avant par le grand omentum",
                "En arrière, la racine du mésentère croise D3, l'aorte, la veine cave "
                "inférieure et l'uretère droit",
            ],
            "function": [
                "Digestion terminale et absorption des nutriments, de l'eau et des "
                "électrolytes",
                "Iléum terminal : absorption de la vitamine B12 (liée au facteur "
                "intrinsèque) et des sels biliaires",
            ],
            "vascularisation": [
                "Artère mésentérique supérieure : artères jéjunales et iléales, arcades "
                "puis vaisseaux droits",
                "Veine mésentérique supérieure vers la veine porte",
            ],
            "innervation": [
                "Vague et sympathique (plexus mésentérique supérieur) ; système nerveux "
                "entérique (plexus myentérique et sous-muqueux)",
            ],
            "clinical": [
                "Diverticule de Meckel : reliquat du conduit vitellin sur le bord "
                "anti-mésentérique de l'iléum, à environ 60 cm de la valve iléo-cæcale",
                "Occlusion du grêle (brides, hernie étranglée) ; maladie de Crohn, "
                "souvent iléale terminale",
                "Ischémie mésentérique aiguë, par embolie de l'artère mésentérique "
                "supérieure",
            ],
        },
        fact=(
            "Plis, villosités et microvillosités multiplient la surface d'absorption "
            "du grêle par environ 600."
        ),
    ),
    "C": StructureText(
        name="Cæcum et appendice vermiforme",
        kind="Organe creux (segment initial du côlon) et diverticule lymphoïde",
        region="Fosse iliaque droite",
        count="1",
        description=(
            "Cul-de-sac du gros intestin situé sous l'abouchement de l'iléum. "
            "L'appendice vermiforme, long d'environ 6 à 10 cm, naît de sa face "
            "postéro-médiale, là où convergent les trois ténias du côlon."
        ),
        sections={
            "parts": [
                "Valve iléo-cæcale (de Bauhin) à l'abouchement de l'iléum",
                "Base de l'appendice à 2-3 cm sous la valve, à la convergence des trois "
                "ténias",
                "Position de l'appendice variable : rétro-cæcale (la plus fréquente selon "
                "la plupart des séries), pelvienne, sous-cæcale, pré-iléale, rétro-iléale "
                "(méso-cœliaque)",
                "Méso-appendice contenant l'artère appendiculaire",
            ],
            "relations": [
                "Fosse iliaque droite, sur le muscle ilio-psoas",
                "Point de McBurney : union du tiers latéral et des deux tiers médiaux de "
                "la ligne épine iliaque antéro-supérieure droite - ombilic",
            ],
            "function": [
                "Réabsorption d'eau et d'électrolytes ; appendice riche en tissu "
                "lymphoïde (rôle immunitaire)",
            ],
            "vascularisation": [
                "Artère iléo-colique (branche de l'artère mésentérique supérieure) : "
                "artères cæcales et artère appendiculaire, terminale",
            ],
            "innervation": [
                "Plexus mésentérique supérieur ; douleur appendiculaire d'abord "
                "péri-ombilicale (T10), puis en fosse iliaque droite",
            ],
            "clinical": [
                "Appendicite aiguë : douleur de la fosse iliaque droite, maximale au "
                "point de McBurney, avec défense",
                "Signe de Blumberg (douleur à la décompression) ; signe du psoas dans les "
                "formes rétro-cæcales",
                "En appendicectomie, la base est retrouvée en suivant les ténias jusqu'à "
                "leur convergence",
            ],
        },
        fact="L'appendicite est l'urgence chirurgicale abdominale la plus fréquente.",
    ),
    "A": StructureText(
        name="Côlon ascendant",
        kind="Organe creux (gros intestin), accolé à la paroi postérieure",
        region="Flanc droit, du cæcum à l'angle colique droit",
        count="1",
        description=(
            "Segment d'environ 15 cm qui monte du cæcum à l'angle colique droit "
            "(hépatique), sous le foie. Il est accolé à la paroi abdominale "
            "postérieure par le fascia d'accolement (de Toldt) droit."
        ),
        sections={
            "parts": [
                "Caractères du côlon : trois ténias, haustrations et appendices omentaux "
                "(épiploïques)",
                "Angle colique droit (hépatique), sous la face viscérale du foie",
            ],
            "relations": [
                "En arrière : muscle carré des lombes, pôle inférieur du rein droit",
                "En dedans : anses grêles ; en dehors : gouttière pariéto-colique droite",
            ],
            "function": [
                "Réabsorption d'eau et d'électrolytes d'un contenu encore liquide ; "
                "fermentation bactérienne",
            ],
            "vascularisation": [
                "Artère mésentérique supérieure : artère iléo-colique et artère colique "
                "droite (inconstante)",
                "Arcade marginale du côlon, qui relie les artères coliques",
            ],
            "innervation": [
                "Nerf vague et sympathique (plexus mésentérique supérieur)",
            ],
            "clinical": [
                "Cancer du côlon droit, souvent révélé par une anémie ferriprive ; "
                "traitement par hémicolectomie droite",
                "Le fascia de Toldt offre un plan de décollement avasculaire en chirurgie",
            ],
        },
        fact=(
            "Le côlon droit dérive de l'intestin moyen embryonnaire : il est "
            "vascularisé, comme le grêle, par l'artère mésentérique supérieure."
        ),
    ),
    "T": StructureText(
        name="Côlon transverse",
        kind="Organe creux (gros intestin), mobile",
        region="Partie moyenne de l'abdomen, entre les deux angles coliques",
        count="1",
        description=(
            "Segment le plus long (environ 45 cm) et le plus mobile du côlon, "
            "suspendu par le mésocôlon transverse, qui sépare les étages sus- et "
            "sous-mésocoliques de la cavité péritonéale."
        ),
        sections={
            "parts": [
                "Angle colique droit, plus bas ; angle colique gauche, plus haut et plus "
                "profond, fixé par le ligament phrénico-colique",
                "Mésocôlon transverse, dont la racine croise D2 et le pancréas",
                "Ligament gastro-colique (partie du grand omentum) qui le relie à la "
                "grande courbure",
            ],
            "relations": [
                "Au-dessus : foie, vésicule biliaire, grande courbure de l'estomac, rate",
                "En dessous : anses grêles ; en avant : grand omentum et paroi abdominale",
            ],
            "function": [
                "Absorption d'eau ; brassage et propulsion par des contractions de masse",
            ],
            "vascularisation": [
                "Deux tiers droits : artère colique moyenne (mésentérique supérieure) ; "
                "tiers gauche : artère colique gauche (mésentérique inférieure)",
                "Anastomoses entre mésentériques supérieure et inférieure par l'arcade "
                "marginale ; l'arcade de Riolan est inconstante et diversement définie",
            ],
            "innervation": [
                "Deux tiers droits : nerf vague ; tiers gauche : nerfs splanchniques "
                "pelviens (S2-S4) ; sympathique des plexus mésentériques",
            ],
            "clinical": [
                "Angle colique gauche : zone frontière entre deux territoires artériels, "
                "exposée à la colite ischémique",
                "Accessible et mobile : site classique de colostomie transverse",
            ],
        },
        fact=(
            "La jonction des deux tiers droits et du tiers gauche marque la limite "
            "embryonnaire entre intestin moyen et intestin postérieur."
        ),
    ),
    "X": StructureText(
        name="Côlon descendant",
        kind="Organe creux (gros intestin), accolé à la paroi postérieure",
        region="Flanc gauche, de l'angle colique gauche à la crête iliaque",
        count="1",
        description=(
            "Segment d'environ 25 cm, plus étroit que le côlon droit, qui descend de "
            "l'angle colique gauche à la crête iliaque gauche, où il devient le côlon "
            "sigmoïde (limite variable selon les auteurs : crête iliaque ou détroit "
            "supérieur). Il est accolé par le fascia de Toldt gauche."
        ),
        sections={
            "parts": [
                "Ténias, haustrations et appendices omentaux ; calibre plus étroit que "
                "celui du côlon droit",
                "Angle colique gauche (splénique), le plus haut, au contact de la rate",
            ],
            "relations": [
                "En arrière : bord latéral du rein gauche, muscle carré des lombes",
                "En dedans : anses jéjunales ; en dehors : gouttière pariéto-colique gauche",
            ],
            "function": [
                "Déshydratation et stockage temporaire des selles",
            ],
            "vascularisation": [
                "Artère colique gauche, branche de l'artère mésentérique inférieure",
                "Veine mésentérique inférieure, qui rejoint la veine splénique puis la "
                "veine porte",
            ],
            "innervation": [
                "Parasympathique sacré (nerfs splanchniques pelviens, S2-S4) ; "
                "sympathique (plexus mésentérique inférieur)",
            ],
            "clinical": [
                "Cancer du côlon gauche : troubles du transit et occlusion, car la "
                "lumière est étroite et les selles solides",
            ],
        },
        fact=(
            "Le côlon gauche dérive de l'intestin postérieur, vascularisé par "
            "l'artère mésentérique inférieure, née de l'aorte en regard de L3."
        ),
    ),
    "Z": StructureText(
        name="Côlon sigmoïde",
        old_names=["côlon pelvien", "côlon ilio-pelvien"],
        kind="Organe creux (gros intestin), mobile",
        region="Fosse iliaque gauche et pelvis",
        count="1",
        description=(
            "Anse mobile de longueur très variable (environ 40 cm), suspendue par le "
            "mésocôlon sigmoïde, de la crête iliaque gauche (limite variable selon les "
            "auteurs : crête iliaque ou détroit supérieur) à la jonction "
            "recto-sigmoïdienne (S3)."
        ),
        sections={
            "parts": [
                "Mésocôlon sigmoïde à racine en V renversé ; l'uretère gauche passe sous "
                "le sommet du V",
                "Les ténias s'élargissent et fusionnent à la jonction recto-sigmoïdienne",
            ],
            "relations": [
                "Dans le pelvis : vessie, et chez la femme utérus et annexes gauches",
                "En arrière du mésocôlon : uretère et vaisseaux iliaques gauches",
            ],
            "function": [
                "Stockage des selles avant leur passage dans le rectum",
            ],
            "vascularisation": [
                "Artères sigmoïdiennes, branches de l'artère mésentérique inférieure",
            ],
            "innervation": [
                "Parasympathique sacré (S2-S4) ; sympathique (plexus mésentérique "
                "inférieur)",
            ],
            "clinical": [
                "Diverticulite sigmoïdienne : douleur et fièvre en fosse iliaque gauche "
                "(« appendicite à gauche »)",
                "Volvulus du sigmoïde, surtout chez le sujet âgé",
                "Cancer colorectal fréquent à la jonction recto-sigmoïdienne ; dépistage "
                "par coloscopie",
            ],
        },
        fact=(
            "Dans les pays occidentaux, le sigmoïde est le siège le plus fréquent des "
            "diverticules du côlon."
        ),
    ),
    "R": StructureText(
        name="Rectum et canal anal",
        kind="Organe creux (segment terminal du tube digestif)",
        region="Pelvis (petit bassin) et périnée",
        count="1",
        description=(
            "Le rectum (environ 12 à 15 cm) va de S3 à la jonction ano-rectale en "
            "suivant la concavité du sacrum. Le canal anal (3 à 4 cm) traverse le "
            "périnée jusqu'à l'anus."
        ),
        sections={
            "parts": [
                "Ampoule rectale (réservoir) et plis transversaux ; pas de ténias ni "
                "d'haustrations",
                "Angle ano-rectal maintenu par la sangle du muscle pubo-rectal",
                "Canal anal : colonnes anales et ligne pectinée (jonction "
                "endoderme-ectoderme)",
                "Sphincter interne (lisse, involontaire) et sphincter externe (strié, "
                "volontaire)",
            ],
            "relations": [
                "Chez l'homme : vessie, glandes séminales (vésicules séminales), prostate ; cul-de-sac "
                "recto-vésical",
                "Chez la femme : utérus et vagin ; cul-de-sac recto-utérin (de Douglas), "
                "point le plus bas de la cavité péritonéale",
                "En arrière : sacrum, coccyx et mésorectum",
            ],
            "function": [
                "Continence et défécation : réflexe recto-anal inhibiteur et contrôle "
                "volontaire du sphincter externe",
            ],
            "vascularisation": [
                "Artère rectale supérieure (fin de la mésentérique inférieure), artères "
                "rectales moyennes (iliaques internes) et inférieures (pudendales "
                "internes)",
                "Plexus veineux rectaux : anastomose porto-cave (rectale supérieure vers "
                "la porte, moyennes et inférieures vers la cave)",
            ],
            "innervation": [
                "Au-dessus de la ligne pectinée : innervation autonome, peu sensible à la "
                "douleur ; en dessous : nerf pudendal, très sensible",
                "Sphincter externe : nerf pudendal (S2-S4)",
            ],
            "clinical": [
                "Toucher rectal : prostate ; cul-de-sac de Douglas douloureux en cas de "
                "péritonite",
                "Maladie hémorroïdaire ; fissure anale, douloureuse car sous la ligne "
                "pectinée",
                "Cancer du rectum : exérèse totale du mésorectum",
            ],
        },
        fact=(
            "De part et d'autre de la ligne pectinée changent l'épithélium, la "
            "vascularisation, le drainage lymphatique et l'innervation."
        ),
    ),
}
