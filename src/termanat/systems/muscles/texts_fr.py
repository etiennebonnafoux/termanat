"""Textes en français (nomenclature anatomique internationale francisée,
celle utilisée en PASS / L.AS). Les anciens noms sont indiqués à titre de
correspondance."""

from __future__ import annotations

from ...model import StructureText

_KIND = "Muscle strié squelettique"
_GROUP = "Groupe de muscles striés squelettiques"

TEXTS: dict[str, StructureText] = {
    "N": StructureText(
        name="Muscle sterno-cléido-mastoïdien",
        kind=_KIND,
        region="Cou, région sterno-cléido-mastoïdienne",
        count="2 (pair)",
        description=(
            "Gros muscle superficiel et oblique du cou, tendu du sternum et de la "
            "clavicule jusqu'au processus mastoïde. Il sépare la région cervicale "
            "antérieure de la région cervicale latérale et recouvre le paquet "
            "vasculo-nerveux du cou."
        ),
        sections={
            "insertions": [
                "Chef sternal : face antérieure du manubrium sternal",
                "Chef claviculaire : face supérieure du tiers médial de la clavicule",
                "Terminaison : face latérale du processus mastoïde et moitié latérale "
                "de la ligne nuchale supérieure de l'occipital",
            ],
            "action": [
                "Contraction unilatérale : inclinaison de la tête du même côté et "
                "rotation de la face vers le côté opposé",
                "Contraction bilatérale : flexion du cou (antéflexion de la tête)",
                "Inspirateur accessoire quand la tête est fixée (élève le sternum)",
            ],
            "innervation": [
                "Motricité : nerf accessoire (XI), par sa branche latérale",
                "Proprioception : rameaux du plexus cervical (C2-C3)",
            ],
            "vascularisation": [
                "Branches sterno-cléido-mastoïdiennes des artères occipitale et "
                "thyroïdienne supérieure",
            ],
            "clinical": [
                "Torticolis congénital : fibrose du muscle, tête inclinée du côté atteint "
                "et face tournée du côté opposé",
                "Repère chirurgical : son bord antérieur guide l'abord de l'artère "
                "carotide commune et de la veine jugulaire interne",
                "Lésion du nerf accessoire : faiblesse de la rotation de la tête vers le "
                "côté opposé",
            ],
        },
        fact=(
            "Quand on tourne la tête vers la gauche, c'est le sterno-cléido-mastoïdien "
            "droit qui se contracte et devient bien visible."
        ),
    ),
    "T": StructureText(
        name="Muscle trapèze",
        kind=_KIND,
        region="Nuque, dos et ceinture scapulaire (partie supérieure visible de face)",
        count="2 (pair)",
        description=(
            "Grand muscle plat et triangulaire, le plus superficiel du dos. Les deux "
            "trapèzes forment un losange de l'occiput à T12. De face, on ne voit que "
            "sa partie descendante, qui forme la pente des épaules."
        ),
        sections={
            "parts": [
                "Partie descendante (supérieure), de l'occipital et du ligament nuchal",
                "Partie transverse (moyenne), des processus épineux de C7 à T3",
                "Partie ascendante (inférieure), des processus épineux de T4 à T12",
            ],
            "insertions": [
                "Origine : protubérance occipitale externe, tiers médial de la ligne "
                "nuchale supérieure, ligament nuchal, processus épineux de C7 à T12",
                "Terminaison : tiers latéral de la clavicule, acromion et épine de la "
                "scapula",
            ],
            "action": [
                "Partie descendante : élévation du moignon de l'épaule (hausser les épaules)",
                "Partie transverse : adduction (rétraction) de la scapula",
                "Partie ascendante : abaissement de la scapula",
                "Parties descendante et ascendante, avec le dentelé antérieur : sonnette "
                "latérale, nécessaire à l'élévation du bras au-delà de 90°",
            ],
            "innervation": [
                "Motricité : nerf accessoire (XI)",
                "Proprioception : rameaux du plexus cervical (C3-C4)",
            ],
            "vascularisation": [
                "Artère cervicale transverse principalement, avec des branches des "
                "artères occipitale et supra-scapulaire",
            ],
            "clinical": [
                "Lésion du nerf accessoire dans la région cervicale latérale (curage "
                "ganglionnaire, biopsie) : chute du moignon de l'épaule",
                "Testé en demandant de hausser les épaules contre résistance",
            ],
        },
        fact=(
            "Les deux trapèzes réunis dessinent un losange que l'on appelait autrefois "
            "le « capuchon de moine » (muscle cucullaire)."
        ),
    ),
    "D": StructureText(
        name="Muscle deltoïde",
        kind=_KIND,
        region="Épaule (moignon de l'épaule)",
        count="2 (pair)",
        description=(
            "Muscle épais et triangulaire qui donne son galbe arrondi à l'épaule. Il "
            "coiffe l'articulation scapulo-humérale en avant, en dehors et en arrière."
        ),
        sections={
            "parts": [
                "Faisceau antérieur (claviculaire)",
                "Faisceau moyen (acromial), multipenné, le plus puissant",
                "Faisceau postérieur (spinal)",
            ],
            "insertions": [
                "Origine : tiers latéral de la clavicule, bord latéral de l'acromion, "
                "bord inférieur de l'épine de la scapula",
                "Terminaison : tubérosité deltoïdienne (« V deltoïdien ») de la face "
                "latérale de l'humérus",
            ],
            "action": [
                "Abducteur principal du bras, surtout entre 15° et 90°, le "
                "supra-épineux l'assistant surtout en début de mouvement",
                "Faisceau antérieur : flexion et rotation médiale du bras",
                "Faisceau postérieur : extension et rotation latérale du bras",
                "Au-delà de 90°, l'élévation nécessite la bascule de la scapula "
                "(trapèze, dentelé antérieur)",
            ],
            "innervation": [
                "Nerf axillaire (C5-C6), ancien nerf circonflexe, branche du faisceau "
                "postérieur du plexus brachial",
            ],
            "vascularisation": [
                "Artères circonflexes humérales postérieure et antérieure, branche "
                "deltoïdienne de l'artère thoraco-acromiale",
            ],
            "clinical": [
                "Luxation antéro-inférieure de l'épaule ou fracture du col chirurgical "
                "de l'humérus : risque de lésion du nerf axillaire",
                "Paralysie axillaire : abduction très affaiblie et hypoesthésie du "
                "moignon de l'épaule (en épaulette)",
                "Site classique des injections intramusculaires (vaccins), dans sa "
                "partie haute pour éviter le nerf axillaire",
            ],
        },
        fact=(
            "Son nom vient de la lettre grecque delta (Δ) : le muscle a la forme d'un "
            "delta renversé."
        ),
    ),
    "P": StructureText(
        name="Muscle grand pectoral",
        kind=_KIND,
        region="Paroi antérieure du thorax",
        count="2 (pair)",
        description=(
            "Grand muscle en éventail de la paroi thoracique antérieure, tendu du "
            "thorax à l'humérus. Son bord inférieur forme le pli axillaire antérieur ; "
            "la glande mammaire repose sur son fascia."
        ),
        sections={
            "parts": [
                "Chef claviculaire",
                "Chef sterno-costal",
                "Partie abdominale (petite, variable)",
            ],
            "insertions": [
                "Origine : moitié médiale de la clavicule, face antérieure du sternum, "
                "cartilages costaux 1 à 6, gaine du muscle droit de l'abdomen",
                "Terminaison : lèvre latérale du sillon intertuberculaire de l'humérus "
                "(crête du tubercule majeur), par un tendon replié en U",
            ],
            "action": [
                "Adduction et rotation médiale du bras",
                "Chef claviculaire : flexion du bras ; chef sterno-costal : ramène le "
                "bras fléchi vers le corps",
                "Inspirateur accessoire quand le bras est fixé",
            ],
            "innervation": [
                "Nerfs pectoraux latéral (C5-C7) et médial (C8-T1), issus du plexus brachial",
            ],
            "vascularisation": [
                "Branche pectorale de l'artère thoraco-acromiale, perforantes de "
                "l'artère thoracique interne, artère thoracique latérale",
            ],
            "clinical": [
                "Syndrome de Poland : absence congénitale du chef sterno-costal",
                "Cancer du sein : la fixité de la tumeur au muscle (bras en contraction) "
                "évoque une extension en profondeur",
                "Utilisé comme lambeau musculaire en chirurgie reconstructrice",
            ],
        },
        fact=(
            "Ses fibres se croisent dans le tendon : les fibres les plus basses du "
            "muscle se fixent le plus haut sur l'humérus."
        ),
    ),
    "S": StructureText(
        name="Muscle dentelé antérieur",
        old_names=["grand dentelé"],
        kind=_KIND,
        region="Paroi latérale du thorax",
        count="2 (pair)",
        description=(
            "Muscle large plaqué sur la paroi latérale du thorax, entre les côtes et "
            "la scapula. Ses digitations, visibles sous l'aisselle chez le sujet "
            "musclé, s'engrènent avec celles du muscle oblique externe."
        ),
        sections={
            "insertions": [
                "Origine : faces latérales des 8 à 10 premières côtes, par des "
                "digitations (le nombre varie selon les auteurs)",
                "Terminaison : face costale du bord médial de la scapula, surtout à "
                "l'angle inférieur",
            ],
            "action": [
                "Plaque la scapula contre le thorax",
                "Abduction (protraction) de la scapula : pousser, donner un coup de poing",
                "Sonnette latérale avec le trapèze, indispensable à l'élévation du bras "
                "au-delà de 90°",
            ],
            "innervation": [
                "Nerf thoracique long (C5-C7), ancien nerf de Charles Bell, qui descend "
                "sur la face latérale du muscle",
            ],
            "vascularisation": [
                "Artère thoracique latérale et artère thoraco-dorsale",
            ],
            "clinical": [
                "Lésion du nerf thoracique long (curage axillaire, port de charge sur "
                "l'épaule, traumatisme) : scapula alata",
                "Scapula alata : le bord médial de la scapula se décolle quand le patient "
                "pousse contre un mur",
            ],
        },
        fact=(
            "On le surnomme le « muscle du boxeur » : il projette la scapula, donc le "
            "poing, vers l'avant."
        ),
    ),
    "B": StructureText(
        name="Muscle biceps brachial",
        kind=_KIND,
        region="Bras, loge antérieure (plan superficiel)",
        count="2 (pair)",
        description=(
            "Muscle fusiforme à deux chefs de la loge antérieure du bras. Biarticulaire, "
            "il croise l'épaule et le coude ; c'est le grand supinateur de l'avant-bras."
        ),
        sections={
            "parts": [
                "Chef long : tendon intra-articulaire de l'épaule, passe dans le sillon "
                "intertuberculaire",
                "Chef court, accolé au muscle coraco-brachial",
            ],
            "insertions": [
                "Chef long : tubercule supra-glénoïdal de la scapula",
                "Chef court : apex du processus coracoïde",
                "Terminaison : tubérosité du radius, et aponévrose bicipitale vers le "
                "fascia antébrachial médial",
            ],
            "action": [
                "Fléchisseur du coude",
                "Supinateur puissant de l'avant-bras, surtout coude fléchi",
                "Faible fléchisseur de l'épaule (chef long)",
            ],
            "innervation": [
                "Nerf musculo-cutané (C5-C6)",
            ],
            "vascularisation": [
                "Branches musculaires de l'artère brachiale",
            ],
            "clinical": [
                "Réflexe bicipital : explore les racines C5-C6",
                "Rupture du tendon du chef long : le ventre musculaire se rétracte en "
                "boule dans la moitié inférieure du bras (signe de Popeye)",
                "L'aponévrose bicipitale recouvre l'artère brachiale et le nerf médian au "
                "pli du coude",
            ],
        },
        fact=(
            "C'est la supination qui le fait le plus travailler : c'est le muscle qui "
            "visse un tire-bouchon (chez le droitier)."
        ),
    ),
    "R": StructureText(
        name="Muscle brachio-radial",
        old_names=["long supinateur"],
        kind=_KIND,
        region="Avant-bras, loge latérale (antébrachiale latérale)",
        count="2 (pair)",
        description=(
            "Muscle long et superficiel du bord latéral de l'avant-bras. Il forme la "
            "limite latérale de la fosse cubitale. Fléchisseur du coude bien qu'il "
            "appartienne au groupe dorsal innervé par le nerf radial."
        ),
        sections={
            "insertions": [
                "Origine : crête supra-épicondylaire latérale de l'humérus (deux tiers "
                "supérieurs)",
                "Terminaison : base du processus styloïde du radius",
            ],
            "action": [
                "Fléchisseur du coude, surtout avant-bras en position neutre (pouce en haut)",
                "Ramène l'avant-bras en position neutre depuis la pronation ou la "
                "supination ; il n'est pas supinateur malgré son ancien nom",
            ],
            "innervation": [
                "Nerf radial (C5-C6), avant sa division",
            ],
            "vascularisation": [
                "Artère récurrente radiale, branches de l'artère radiale",
            ],
            "clinical": [
                "Réflexe stylo-radial : explore les racines C5-C6",
                "Paralysé dans les lésions hautes du nerf radial (fracture de la diaphyse "
                "humérale), avec la main tombante",
            ],
        },
        fact=(
            "On l'appelle parfois le « muscle du buveur de bière » : il plie le coude "
            "quand on "
            "porte un verre à la bouche, pouce en haut."
        ),
    ),
    "F": StructureText(
        name="Muscles épicondyliens médiaux",
        old_names=["muscles épitrochléens"],
        kind=_GROUP,
        region="Avant-bras, loge antérieure (plan superficiel)",
        count="5 muscles de chaque côté",
        description=(
            "Muscles superficiels de la loge antérieure de l'avant-bras, nés de "
            "l'épicondyle médial (ancienne épitrochlée) par un tendon commun. Ce sont "
            "des fléchisseurs du poignet et des doigts et des pronateurs."
        ),
        sections={
            "parts": [
                "Muscle rond pronateur (pronateur, non fléchisseur, mais classé dans ce groupe)",
                "Muscle fléchisseur radial du carpe (ancien grand palmaire)",
                "Muscle long palmaire (ancien petit palmaire), inconstant",
                "Muscle fléchisseur ulnaire du carpe (ancien cubital antérieur)",
                "Muscle fléchisseur superficiel des doigts (plan intermédiaire)",
            ],
            "insertions": [
                "Origine commune : épicondyle médial de l'humérus (tendon commun des "
                "fléchisseurs)",
                "Rond pronateur : face latérale du radius, au milieu de la diaphyse",
                "Fléchisseur radial du carpe : base du 2e métacarpien ; long palmaire : "
                "aponévrose palmaire",
                "Fléchisseur ulnaire du carpe : pisiforme, hamatum, base du 5e métacarpien",
                "Fléchisseur superficiel des doigts : phalanges moyennes des doigts 2 à 5",
            ],
            "action": [
                "Flexion du poignet ; inclinaison radiale (fléchisseur radial) ou "
                "ulnaire (fléchisseur ulnaire)",
                "Flexion des doigts au niveau des articulations interphalangiennes "
                "proximales (fléchisseur superficiel)",
                "Pronation de l'avant-bras (rond pronateur)",
            ],
            "innervation": [
                "Nerf médian (C6-T1) pour tous ces muscles",
                "Sauf le fléchisseur ulnaire du carpe : nerf ulnaire (C8-T1, ou C7-C8 selon "
                "les auteurs)",
            ],
            "vascularisation": [
                "Branches des artères ulnaire et radiale",
            ],
            "clinical": [
                "Épicondylite médiale (ancienne épitrochléite, « coude du golfeur ») : "
                "tendinopathie du "
                "tendon commun",
                "Le long palmaire, absent chez environ 15 % des sujets, sert de greffon "
                "tendineux",
                "Syndrome de Volkmann : ischémie de la loge antérieure (fracture "
                "supra-condylienne de l'enfant) aboutissant à une rétraction en griffe",
            ],
        },
        fact=(
            "Serrez le poing en fléchissant le poignet : le tendon du long palmaire "
            "saille au milieu du poignet, s'il est présent."
        ),
    ),
    "A": StructureText(
        name="Muscle droit de l'abdomen",
        old_names=["grand droit de l'abdomen"],
        kind=_KIND,
        region="Paroi antérieure de l'abdomen",
        count="2 (pair)",
        description=(
            "Long muscle plat vertical de part et d'autre de la ligne blanche, "
            "contenu dans la gaine des muscles droits formée par les aponévroses des "
            "muscles larges de l'abdomen."
        ),
        sections={
            "insertions": [
                "Insertion inférieure : crête pubienne et symphyse pubienne",
                "Insertion supérieure : cartilages costaux 5 à 7 et processus xiphoïde",
                "Interrompu par 3 à 4 intersections tendineuses (« tablette de chocolat »)",
            ],
            "action": [
                "Flexion du tronc (enroulement) et rétroversion du bassin",
                "Augmente la pression abdominale : expiration forcée, défécation, "
                "accouchement",
            ],
            "innervation": [
                "Nerfs intercostaux 7 à 11 et nerf subcostal (rameaux antérieurs T7-T12)",
            ],
            "vascularisation": [
                "Artères épigastriques supérieure (de la thoracique interne) et "
                "inférieure (de l'iliaque externe), anastomosées dans la gaine",
            ],
            "clinical": [
                "Diastasis des muscles droits : écartement de la ligne blanche, "
                "fréquent après la grossesse",
                "Défense ou contracture abdominale : signe de péritonite",
                "Hématome de la gaine du muscle droit (rupture de l'artère épigastrique "
                "inférieure, patient sous anticoagulant)",
            ],
        },
        fact=(
            "Les intersections tendineuses témoigneraient de l'origine métamérique du "
            "muscle (myotomes embryonnaires)."
        ),
    ),
    "O": StructureText(
        name="Muscle oblique externe de l'abdomen",
        old_names=["grand oblique"],
        kind=_KIND,
        region="Paroi antérolatérale de l'abdomen",
        count="2 (pair)",
        description=(
            "Le plus superficiel et le plus grand des trois muscles larges de "
            "l'abdomen. Ses fibres descendent en avant et en dedans, comme des « mains "
            "dans les poches », puis se prolongent par une large aponévrose."
        ),
        sections={
            "insertions": [
                "Origine : faces externes des côtes 5 à 12, par des digitations",
                "Terminaison : moitié antérieure de la lèvre externe de la crête iliaque, "
                "ligne blanche (par son aponévrose), tubercule pubien",
                "Le bord inférieur de son aponévrose forme le ligament inguinal, de "
                "l'épine iliaque antéro-supérieure au tubercule pubien",
            ],
            "action": [
                "Unilatéral : inclinaison du tronc du même côté et rotation du tronc "
                "vers le côté opposé",
                "Bilatéral : flexion du tronc, expiration forcée, augmentation de la "
                "pression abdominale",
            ],
            "innervation": [
                "Nerfs intercostaux inférieurs et nerf subcostal (T7-T12) ; participation "
                "du nerf ilio-hypogastrique (L1) selon les auteurs",
            ],
            "vascularisation": [
                "Artères intercostales postérieures inférieures, subcostale, et branches "
                "des artères épigastrique inférieure et circonflexe iliaque profonde",
            ],
            "clinical": [
                "Son aponévrose est percée par l'anneau inguinal superficiel, lieu de "
                "sortie des hernies inguinales",
                "Le ligament inguinal sépare l'abdomen de la cuisse : repère des hernies "
                "inguinales (au-dessus) et fémorales (au-dessous)",
                "Incision de McBurney (appendicectomie) : on dissocie ses fibres dans "
                "leur sens sans les couper",
            ],
        },
        fact=(
            "Pour tourner le tronc vers la droite, on utilise l'oblique externe gauche "
            "et l'oblique interne droit."
        ),
    ),
    "Z": StructureText(
        name="Muscle sartorius",
        old_names=["couturier"],
        kind=_KIND,
        region="Cuisse, loge antérieure",
        count="2 (pair)",
        description=(
            "Muscle rubané, le plus long du corps, qui croise la cuisse en diagonale "
            "de l'épine iliaque antéro-supérieure à la face médiale du tibia. "
            "Biarticulaire, il croise la hanche et le genou."
        ),
        sections={
            "insertions": [
                "Origine : épine iliaque antéro-supérieure",
                "Terminaison : face médiale de l'extrémité supérieure du tibia, dans la "
                "patte d'oie (avec le gracile et le semi-tendineux)",
            ],
            "action": [
                "Hanche : flexion, abduction et rotation latérale",
                "Genou : flexion",
                "Ensemble : position de l'« assis en tailleur »",
            ],
            "innervation": [
                "Nerf fémoral (L2-L3)",
            ],
            "vascularisation": [
                "Branches musculaires de l'artère fémorale, artère descendante du genou",
            ],
            "clinical": [
                "Bord latéral du trigone fémoral (ancien triangle de Scarpa ; ligament "
                "inguinal en haut, long "
                "adducteur en dedans) qui contient nerf, artère et veine fémoraux",
                "Recouvre le canal des adducteurs (ancien canal de Hunter), traversé par "
                "l'artère et la veine "
                "fémorales",
                "Arrachement de l'épine iliaque antéro-supérieure chez l'adolescent sportif",
            ],
        },
        fact=(
            "Son nom vient du latin sartor, « tailleur » : il permet la position "
            "jambes croisées des tailleurs d'autrefois."
        ),
    ),
    "Q": StructureText(
        name="Muscle quadriceps fémoral",
        old_names=["quadriceps crural"],
        kind=_KIND,
        region="Cuisse, loge antérieure",
        count="2 (pair), à quatre chefs",
        description=(
            "Muscle le plus volumineux de la loge antérieure de la cuisse, formé de "
            "quatre chefs qui convergent sur la patella. C'est le seul extenseur du "
            "genou."
        ),
        sections={
            "parts": [
                "Muscle droit fémoral : seul chef biarticulaire (hanche et genou)",
                "Muscle vaste latéral",
                "Muscle vaste médial",
                "Muscle vaste intermédiaire, profond, sous le droit fémoral",
            ],
            "insertions": [
                "Droit fémoral : épine iliaque antéro-inférieure (tendon direct) et "
                "sillon supra-acétabulaire (tendon réfléchi)",
                "Vastes : diaphyse fémorale (lèvres de la ligne âpre, faces antérieure "
                "et latérale)",
                "Terminaison commune : tendon quadricipital, patella, puis ligament "
                "patellaire sur la tubérosité tibiale",
            ],
            "action": [
                "Extension du genou (seul extenseur)",
                "Droit fémoral : flexion de la hanche",
                "Vaste médial : stabilise la patella et s'oppose à sa luxation latérale",
            ],
            "innervation": [
                "Nerf fémoral (L2-L4)",
            ],
            "vascularisation": [
                "Artère circonflexe fémorale latérale (de la fémorale profonde) "
                "principalement, et branches de l'artère fémorale",
            ],
            "clinical": [
                "Réflexe patellaire (ancien réflexe rotulien) : explore surtout L4 (L3-L4)",
                "Paralysie du nerf fémoral : extension du genou impossible, chutes à la "
                "descente des escaliers",
                "Amyotrophie rapide (surtout du vaste médial) après immobilisation ou "
                "lésion du genou",
                "Maladie d'Osgood-Schlatter : traction douloureuse sur la tubérosité "
                "tibiale chez l'adolescent",
            ],
        },
        fact=(
            "La patella est un os sésamoïde inclus dans le tendon du quadriceps : elle "
            "augmente son bras de levier."
        ),
    ),
    "G": StructureText(
        name="Muscles adducteurs de la cuisse",
        kind=_GROUP,
        region="Cuisse, loge médiale",
        count="5 muscles de chaque côté",
        description=(
            "Groupe de muscles de la loge médiale de la cuisse, tendus du pubis et de "
            "l'ischium au fémur (et au tibia pour le gracile). De face, on voit "
            "surtout le long adducteur et le gracile."
        ),
        sections={
            "parts": [
                "Muscle pectiné",
                "Muscle long adducteur (ancien moyen adducteur)",
                "Muscle court adducteur (ancien petit adducteur)",
                "Muscle grand adducteur",
                "Muscle gracile (ancien droit interne)",
            ],
            "insertions": [
                "Origine : pecten du pubis (pectiné), corps et branche inférieure du pubis, "
                "branche de l'ischium, "
                "tubérosité ischiatique (grand adducteur)",
                "Terminaison : ligne pectinée et lèvre médiale de la ligne âpre du fémur, "
                "tubercule de l'adducteur (grand adducteur)",
                "Gracile : face médiale du tibia, dans la patte d'oie",
            ],
            "action": [
                "Adduction de la hanche (serrer les cuisses)",
                "Participation à la flexion de la hanche (pectiné, long et court "
                "adducteurs)",
                "Partie ischio-condylaire du grand adducteur : extension de la hanche",
            ],
            "innervation": [
                "Nerf obturateur (L2-L4) pour l'essentiel",
                "Pectiné : nerf fémoral (parfois aussi obturateur)",
                "Partie ischio-condylaire du grand adducteur : nerf sciatique (contingent "
                "tibial)",
            ],
            "vascularisation": [
                "Artère obturatrice, artère fémorale profonde (artères perforantes) et "
                "artère circonflexe fémorale médiale",
            ],
            "clinical": [
                "Le long adducteur forme le bord médial du trigone fémoral (ancien triangle "
                "de Scarpa)",
                "Hiatus du grand adducteur, à la sortie du canal des adducteurs (ancien canal "
                "de Hunter) : les vaisseaux fémoraux y deviennent poplités",
                "Pubalgie et lésions des adducteurs, fréquentes chez les footballeurs",
                "Le tendon du gracile sert de greffon pour reconstruire le ligament "
                "croisé antérieur (technique DIDT)",
            ],
        },
        fact=(
            "Le gracile est le seul adducteur qui croise le genou : on peut le prélever "
            "sans perte fonctionnelle notable."
        ),
    ),
    "J": StructureText(
        name="Muscle tibial antérieur",
        old_names=["jambier antérieur"],
        kind=_KIND,
        region="Jambe, loge antérieure",
        count="2 (pair)",
        description=(
            "Muscle le plus superficiel et le plus puissant de la loge antérieure de "
            "la jambe, contre la face latérale du tibia. Son tendon est bien visible "
            "en avant de la cheville quand on relève le pied."
        ),
        sections={
            "insertions": [
                "Origine : condyle latéral et deux tiers supérieurs de la face latérale "
                "du tibia, membrane interosseuse",
                "Terminaison : face médiale du cunéiforme médial et base du 1er "
                "métatarsien",
            ],
            "action": [
                "Flexion dorsale de la cheville (« releveur » du pied)",
                "Inversion du pied (adduction et supination)",
                "À la marche : relève le pied pendant la phase oscillante et freine sa "
                "chute après l'attaque du talon",
            ],
            "innervation": [
                "Nerf fibulaire profond (L4-L5), ancien nerf tibial antérieur",
            ],
            "vascularisation": [
                "Artère tibiale antérieure",
            ],
            "clinical": [
                "Lésion du nerf fibulaire commun au col de la fibula (plâtre, fracture, "
                "jambes croisées) : pied tombant et marche en steppage",
                "Syndrome de la loge antérieure de la jambe : urgence chirurgicale "
                "(aponévrotomie)",
                "Déficit des releveurs : marche sur les talons impossible (racines L4-L5)",
            ],
        },
        fact=(
            "Son tendon est le plus médial et le plus saillant des tendons de la face "
            "antérieure de la cheville."
        ),
    ),
    "L": StructureText(
        name="Muscle long fibulaire",
        old_names=["long péronier latéral"],
        kind=_KIND,
        region="Jambe, loge latérale (fibulaire)",
        count="2 (pair)",
        description=(
            "Muscle superficiel de la loge latérale de la jambe, contre la fibula. Son "
            "tendon passe derrière la malléole latérale puis traverse la plante du "
            "pied sous le cuboïde."
        ),
        sections={
            "insertions": [
                "Origine : tête et deux tiers supérieurs de la face latérale de la fibula",
                "Terminaison : base du 1er métatarsien et cunéiforme médial (face "
                "plantaire), après un trajet plantaire oblique",
            ],
            "action": [
                "Éversion du pied (abduction et pronation)",
                "Flexion plantaire accessoire de la cheville",
                "Soutient l'arche transversale du pied ; forme avec le tibial antérieur "
                "un « étrier » sous le pied",
            ],
            "innervation": [
                "Nerf fibulaire superficiel (L5-S1), ancien nerf musculo-cutané de la jambe",
            ],
            "vascularisation": [
                "Branches de l'artère fibulaire et de l'artère tibiale antérieure",
            ],
            "clinical": [
                "Protège la cheville contre l'entorse en inversion (ligament collatéral "
                "latéral)",
                "Luxation des tendons fibulaires en avant de la malléole latérale",
                "Lésion du nerf fibulaire commun : pied en varus équin (perte des "
                "éverseurs et des releveurs)",
            ],
        },
        fact=(
            "Son tendon change deux fois de direction, derrière la malléole latérale "
            "puis sous le cuboïde, comme sur des poulies."
        ),
    ),
    "C": StructureText(
        name="Muscle triceps sural",
        kind=_KIND,
        region="Jambe, loge postérieure (mollet), visible de face en dedans",
        count="2 (pair), à trois chefs",
        description=(
            "Muscle du mollet formé des deux chefs du gastrocnémien et du soléaire, "
            "réunis par le tendon calcanéen. De face, on aperçoit le relief du chef "
            "médial du gastrocnémien en dedans du tibia."
        ),
        sections={
            "parts": [
                "Muscle gastrocnémien (ancien muscle jumeaux), chefs médial et latéral, "
                "superficiels et "
                "biarticulaires",
                "Muscle soléaire, profond, monoarticulaire",
            ],
            "insertions": [
                "Gastrocnémien : faces postérieures des condyles médial et latéral du fémur",
                "Soléaire : tête et face postérieure de la fibula, ligne du muscle "
                "soléaire du tibia, arcade tendineuse du soléaire",
                "Terminaison : tendon calcanéen (d'Achille) sur la face postérieure de "
                "la tubérosité du calcanéus",
            ],
            "action": [
                "Flexion plantaire puissante de la cheville : marche, course, saut, "
                "station sur la pointe des pieds",
                "Gastrocnémien : participe à la flexion du genou",
                "Soléaire : muscle postural (fibres lentes) et pompe veineuse du mollet",
            ],
            "innervation": [
                "Nerf tibial (S1-S2)",
            ],
            "vascularisation": [
                "Artères surales (de l'artère poplitée), branches des artères tibiale "
                "postérieure et fibulaire",
            ],
            "clinical": [
                "Réflexe achilléen : explore la racine S1",
                "Rupture du tendon calcanéen : la pression du mollet ne donne plus de "
                "flexion plantaire (test de Thompson)",
                "Déchirure du chef médial du gastrocnémien (« tennis leg »)",
                "Les veines du soléaire sont un point de départ fréquent des thromboses "
                "veineuses profondes",
            ],
        },
        fact=(
            "Le tendon calcanéen est le tendon le plus épais et le plus résistant du "
            "corps humain."
        ),
    ),
}
