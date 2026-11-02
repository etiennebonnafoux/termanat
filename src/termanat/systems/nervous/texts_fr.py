"""Textes en français (nomenclature anatomique internationale francisée,
celle utilisée en PASS / L.AS). Les anciens noms sont indiqués à titre de
correspondance."""

from __future__ import annotations

from ...model import StructureText

TEXTS: dict[str, StructureText] = {
    "B": StructureText(
        name="Cerveau (hémisphères cérébraux)",
        kind="Système nerveux central : télencéphale",
        region="Loge supratentorielle de la cavité crânienne",
        count="2 hémisphères",
        description=(
            "Partie la plus volumineuse de l'encéphale, formée de deux hémisphères "
            "séparés par la fissure longitudinale et reliés par le corps calleux. "
            "Le cortex (substance grise) recouvre la substance blanche et les noyaux "
            "gris centraux."
        ),
        sections={
            "parts": [
                "Lobes frontal, pariétal, temporal, occipital, et insula au fond du sillon latéral",
                "Sillon central (ancien : scissure de Rolando) entre lobes frontal et pariétal",
                "Sillon latéral (ancien : scissure de Sylvius) au-dessus du lobe temporal",
                "Commissures interhémisphériques, dont le corps calleux, la plus grande",
                "Noyaux gris centraux (noyau caudé, putamen, pallidum) et ventricules latéraux",
            ],
            "function": [
                "Gyrus précentral : aire motrice primaire, commande volontaire de l'hémicorps opposé",
                "Gyrus postcentral : aire somesthésique primaire (sensibilité de l'hémicorps opposé)",
                "Aire de Broca (gyrus frontal inférieur) : expression du langage, hémisphère dominant",
                "Aire de Wernicke (partie postérieure du gyrus temporal supérieur) : compréhension",
                "Lobe occipital : vision (cortex visuel primaire autour du sillon calcarin)",
            ],
            "vascularisation": [
                "Artères cérébrales antérieure et moyenne, branches de l'artère carotide interne",
                "Artère cérébrale postérieure, branche terminale de l'artère basilaire",
                "Cercle artériel du cerveau (polygone de Willis) qui les anastomose à la base",
            ],
            "clinical": [
                "Les voies motrices croisent (décussation des pyramides) : une lésion "
                "d'un hémisphère donne une hémiplégie du côté opposé",
                "AVC sylvien (artère cérébrale moyenne) : hémiplégie à prédominance "
                "brachio-faciale controlatérale, aphasie si hémisphère dominant",
            ],
        },
        fact=(
            "L'homoncule de Penfield montre que la main et la face occupent une "
            "part disproportionnée du cortex moteur et sensitif."
        ),
    ),
    "C": StructureText(
        name="Cervelet",
        kind="Système nerveux central : métencéphale",
        region="Fosse crânienne postérieure, sous la tente du cervelet",
        count="1 (impair et médian)",
        description=(
            "Organe de la coordination, situé en arrière du tronc cérébral auquel "
            "il est relié par trois paires de pédoncules. Sur une vue antérieure il "
            "est caché : il est dessiné ici de façon schématique."
        ),
        sections={
            "parts": [
                "Vermis médian et deux hémisphères cérébelleux latéraux",
                "Cortex plissé en lamelles (folia) et noyaux profonds, dont le noyau dentelé",
                "Pédoncules supérieurs (mésencéphale), moyens (pont) et inférieurs (moelle allongée)",
            ],
            "relations": [
                "En avant : le quatrième ventricule, qui le sépare du pont et de la moelle allongée",
                "En haut : la tente du cervelet, qui le sépare des lobes occipitaux",
                "Vascularisé par les artères cérébelleuses supérieure, antéro-inférieure et postéro-inférieure",
            ],
            "function": [
                "Équilibre : archéocervelet (lobe flocculo-nodulaire), ou vestibulocervelet, lié au système vestibulaire",
                "Tonus et posture : paléocervelet (spinocervelet) ; coordination fine : néocervelet (cérébrocervelet)",
                "Apprentissage moteur ; il agit du même côté du corps (contrôle homolatéral)",
            ],
            "clinical": [
                "Syndrome cérébelleux homolatéral : ataxie, élargissement du polygone de sustentation",
                "Dysmétrie, adiadococinésie, tremblement intentionnel, dysarthrie, nystagmus",
                "Une hernie des tonsilles cérébelleuses dans le foramen magnum comprime la moelle allongée",
            ],
        },
        fact=(
            "Le cervelet ne représente qu'environ 10 % du volume de l'encéphale mais "
            "contient plus de la moitié de ses neurones."
        ),
    ),
    "T": StructureText(
        name="Tronc cérébral",
        kind="Système nerveux central",
        region="Fosse crânienne postérieure, sur le clivus, entre cerveau et moelle spinale",
        count="1 (impair et médian)",
        old_names=["bulbe rachidien (moelle allongée)", "protubérance annulaire (pont)"],
        description=(
            "Segment de l'encéphale qui relie le cerveau à la moelle spinale. Il est "
            "traversé par les grandes voies motrices et sensitives et contient les "
            "noyaux de la plupart des nerfs crâniens."
        ),
        sections={
            "parts": [
                "De haut en bas : mésencéphale, pont et moelle allongée",
                "Pyramides et leur décussation à la face antérieure de la moelle allongée",
                "Origine apparente : III et IV au mésencéphale, V au pont",
                "VI, VII et VIII au sillon bulbo-pontin ; IX, X, XI et XII à la moelle allongée",
            ],
            "function": [
                "Passage des voies ascendantes (sensibilité) et descendantes (voie pyramidale)",
                "Noyaux des nerfs crâniens III à XII (le noyau du XI spinal est dans la moelle cervicale)",
                "Centres vitaux de la moelle allongée : respiration, rythme cardiaque, pression artérielle",
                "Formation réticulée : éveil et vigilance",
            ],
            "clinical": [
                "Syndromes alternes : atteinte d'un nerf crânien du côté de la lésion et "
                "hémiplégie du côté opposé",
                "Syndrome de Wallenberg : infarctus latéral de la moelle allongée (artère "
                "vertébrale ou cérébelleuse postéro-inférieure)",
                "L'abolition de tous les réflexes du tronc cérébral est un critère de mort encéphalique",
            ],
        },
        fact=(
            "Une lésion de la moelle allongée peut être immédiatement mortelle, car "
            "elle abrite les centres de la respiration."
        ),
    ),
    "M": StructureText(
        name="Moelle spinale",
        kind="Système nerveux central",
        region="Canal vertébral, du foramen magnum à la vertèbre L1-L2",
        count="1 (impaire et médiane), 31 paires de nerfs spinaux",
        old_names=["moelle épinière"],
        description=(
            "Cordon nerveux d'environ 45 cm, entouré des méninges (dure-mère, "
            "arachnoïde, pie-mère). Elle fait suite à la moelle allongée et se termine "
            "par le cône médullaire, prolongé par le filum terminal."
        ),
        sections={
            "parts": [
                "Substance grise centrale en forme de H ou de papillon, entourée de substance blanche",
                "Corne postérieure sensitive, corne antérieure motrice, corne latérale "
                "sympathique (T1-L2)",
                "Substance blanche en cordons postérieur, latéral et antérieur (faisceaux de fibres)",
                "Intumescences cervicale (membres supérieurs) et lombo-sacrale (membres inférieurs)",
            ],
            "landmarks": [
                "Chez l'adulte, le cône médullaire se termine en regard du disque L1-L2",
                "Chez le nouveau-né, la moelle descend plus bas, vers L3",
                "31 paires de nerfs spinaux : 8 cervicales, 12 thoraciques, 5 lombales, "
                "5 sacrales, 1 coccygienne",
                "Chaque nerf spinal naît d'une racine postérieure (avec un ganglion "
                "spinal) et d'une racine antérieure",
            ],
            "function": [
                "Conduction des informations entre l'encéphale et le reste du corps",
                "Centres des réflexes médullaires (réflexes ostéotendineux, réflexes viscéraux)",
            ],
            "clinical": [
                "La ponction lombale se fait sous la moelle, en L3-L4 ou L4-L5 (ligne "
                "de Tuffier joignant les crêtes iliaques, vers L4)",
                "Syndrome de Brown-Séquard (hémisection) : déficit moteur et sensibilité "
                "profonde du côté de la lésion, perte thermo-algique du côté opposé",
                "Une section complète donne une paraplégie ou une tétraplégie sous le niveau lésionnel",
            ],
        },
        fact=(
            "La moelle est plus courte que le canal vertébral : la colonne grandit "
            "plus que la moelle, d'où l'obliquité des racines lombales et sacrales."
        ),
    ),
    "Q": StructureText(
        name="Queue de cheval",
        kind="Racines nerveuses spinales",
        region="Canal vertébral lombal et sacral, sous le cône médullaire (L2 à S2)",
        description=(
            "Faisceau des racines lombales, sacrales et coccygienne qui descendent "
            "dans le sac dural sous la fin de la moelle avant de sortir par leurs "
            "foramens intervertébraux et sacraux. Le filum terminal est au centre."
        ),
        sections={
            "parts": [
                "Racines antérieures et postérieures des nerfs L2 à Co1, baignant dans "
                "le liquide cérébrospinal",
                "Filum terminal, prolongement de la pie-mère, fixé au coccyx",
                "Sac dural (citerne lombale) qui se termine vers S2",
            ],
            "relations": [
                "En avant : corps vertébraux lombaux et disques intervertébraux",
                "En arrière : lames et ligaments jaunes, voie d'abord de la ponction lombale",
            ],
            "clinical": [
                "Ponction lombale à faible risque à ce niveau : les racines flottantes "
                "s'écartent de l'aiguille",
                "Syndrome de la queue de cheval (grosse hernie discale) : anesthésie "
                "en selle, troubles sphinctériens, déficit des membres inférieurs",
                "C'est une urgence chirurgicale ; l'atteinte est de type périphérique "
                "(paralysie flasque, aréflexie)",
            ],
        },
        fact=(
            "Son nom vient de l'aspect de ces racines qui, une fois la dure-mère "
            "ouverte, ressemblent à une queue de cheval."
        ),
    ),
    "V": StructureText(
        name="Nerf vague (X)",
        kind="Nerf crânien mixte (10e paire)",
        region="Cou, thorax et abdomen",
        count="2 (droit et gauche)",
        old_names=["nerf pneumogastrique"],
        description=(
            "Le plus long des nerfs crâniens, au trajet « vagabond » jusque dans "
            "l'abdomen. Il porte l'essentiel des fibres parasympathiques du corps, "
            "ainsi que des fibres motrices et sensitives."
        ),
        sections={
            "course": [
                "Sort du crâne par le foramen jugulaire (ancien : trou déchiré postérieur), avec les nerfs IX et XI",
                "Descend dans la gaine carotidienne, en arrière, entre veine jugulaire "
                "interne et artère carotide",
                "Passe en arrière du pédicule pulmonaire puis forme le plexus œsophagien",
                "Traverse le diaphragme par le hiatus œsophagien (T10) sous forme de "
                "troncs vagaux antérieur et postérieur",
            ],
            "branches": [
                "Rameaux pharyngiens et nerf laryngé supérieur",
                "Nerf laryngé récurrent : sous l'artère subclavière à droite, sous "
                "l'arc aortique à gauche",
                "Rameaux cardiaques, pulmonaires et œsophagiens",
                "Rameaux gastriques, cœliaques et hépatiques dans l'abdomen",
            ],
            "territory": [
                "Moteur : muscles du pharynx, du larynx et du voile du palais (sauf le tenseur du voile)",
                "Sensitif : larynx, une partie du méat acoustique externe, viscères thoraciques et abdominaux",
                "Parasympathique : cœur, poumons, tube digestif jusqu'à l'angle colique gauche",
            ],
            "function": [
                "Ralentit le cœur (nœud sino-atrial) et contracte les bronches",
                "Stimule le péristaltisme et les sécrétions digestives",
                "Phonation (muscles du larynx) et déglutition (pharynx)",
            ],
            "clinical": [
                "Lésion du nerf laryngé récurrent (chirurgie thyroïdienne, cancer "
                "pulmonaire à gauche) : dysphonie, voix bitonale",
                "Malaise vagal : bradycardie et hypotension brutales",
                "Manœuvres vagales (massage carotidien, Valsalva) pour arrêter une tachycardie supraventriculaire",
            ],
        },
        fact=(
            "Le nerf laryngé récurrent gauche descend jusque sous l'arc aortique "
            "avant de remonter au larynx : un détour hérité du développement des arcs "
            "pharyngiens (anciennement branchiaux)."
        ),
    ),
    "P": StructureText(
        name="Nerf phrénique",
        kind="Nerf mixte du plexus cervical",
        region="Cou et médiastin",
        count="2 (droit et gauche)",
        description=(
            "Nerf du diaphragme, issu des racines C3, C4 et C5 (surtout C4). Il est "
            "le seul nerf moteur du diaphragme, principal muscle de l'inspiration."
        ),
        sections={
            "course": [
                "Descend sur la face antérieure du muscle scalène antérieur, sous la lame prévertébrale",
                "Entre dans le thorax entre artère et veine subclavières",
                "Descend dans le médiastin en avant du pédicule pulmonaire, entre "
                "péricarde fibreux et plèvre médiastinale",
                "À droite le long de la veine cave supérieure, à gauche sur le ventricule "
                "gauche, jusqu'au diaphragme",
            ],
            "territory": [
                "Moteur : diaphragme (chaque nerf innerve son hémi-diaphragme)",
                "Sensitif : péricarde, plèvre médiastinale et diaphragmatique, péritoine sous-diaphragmatique central",
            ],
            "function": [
                "Contraction du diaphragme à chaque inspiration",
            ],
            "clinical": [
                "Lésion médullaire haute (C3 ou au-dessus) : paralysie respiratoire, ventilation mécanique nécessaire",
                "Paralysie phrénique : coupole diaphragmatique ascensionnée sur la radiographie",
                "Douleur projetée à l'épaule (dermatome C4) lors d'une irritation du diaphragme",
            ],
        },
        fact=(
            "Moyen mnémotechnique anglo-saxon : « C3, 4, 5 keeps the diaphragm alive »."
        ),
    ),
    "X": StructureText(
        name="Plexus brachial",
        kind="Plexus nerveux somatique",
        region="Base du cou, région claviculaire et creux axillaire",
        count="2 (droit et gauche)",
        description=(
            "Réseau formé par les rameaux antérieurs des nerfs spinaux C5 à T1, qui "
            "donne tous les nerfs du membre supérieur. Il passe entre les scalènes "
            "avec l'artère subclavière puis sous la clavicule jusqu'à l'aisselle."
        ),
        sections={
            "parts": [
                "Racines : rameaux antérieurs de C5, C6, C7, C8 et T1",
                "Troncs supérieur (C5-C6), moyen (C7) et inférieur (C8-T1), dans le "
                "défilé interscalénique",
                "Chaque tronc se divise en divisions antérieure et postérieure, en arrière de la clavicule",
                "Faisceaux latéral, médial et postérieur, nommés par rapport à l'artère axillaire",
                "Anciens termes : troncs primaires (troncs) et troncs secondaires (faisceaux)",
            ],
            "branches": [
                "Faisceau latéral : nerf musculo-cutané et racine latérale du nerf médian",
                "Faisceau médial : nerf ulnaire, racine médiale du médian, nerfs cutanés médiaux du bras et de l'avant-bras "
                "(anciens : accessoire du brachial cutané interne, brachial cutané interne)",
                "Faisceau postérieur : nerf axillaire (ancien : nerf circonflexe) et nerf radial",
                "Branches collatérales, dont le nerf thoracique long (C5-C7) du muscle dentelé antérieur",
            ],
            "clinical": [
                "Paralysie haute (Erb-Duchenne, C5-C6), souvent obstétricale : bras en "
                "adduction, rotation médiale, coude tendu",
                "Paralysie basse (Klumpke, C8-T1) : griffe de la main, parfois syndrome "
                "de Claude Bernard-Horner",
                "Bloc interscalénique : anesthésie locorégionale du membre supérieur",
            ],
        },
        fact=(
            "De la racine à la branche : 5 racines, 3 troncs, 6 divisions, 3 faisceaux. "
            "On compte 5 branches terminales en anglais, 7 dans la tradition française "
            "(avec les nerfs cutanés médiaux du bras et de l'avant-bras)."
        ),
    ),
    "K": StructureText(
        name="Nerf musculo-cutané",
        kind="Nerf mixte, branche terminale du plexus brachial",
        region="Loge antérieure du bras, face latérale de l'avant-bras",
        count="2 (droit et gauche)",
        description=(
            "Branche du faisceau latéral (C5-C7), nerf des muscles fléchisseurs du "
            "bras. Il se termine comme nerf sensitif de la face latérale de l'avant-bras."
        ),
        sections={
            "course": [
                "Traverse le muscle coracobrachial",
                "Descend entre biceps brachial et brachial",
                "Devient superficiel au coude, en dehors du tendon du biceps",
            ],
            "territory": [
                "Moteur : coracobrachial, biceps brachial et brachial",
                "Sensitif : face latérale de l'avant-bras (nerf cutané latéral de l'avant-bras)",
            ],
            "clinical": [
                "Lésion rare et isolée : faiblesse de la flexion du coude et de la supination",
                "Abolition du réflexe bicipital (C5-C6) et hypoesthésie latérale de l'avant-bras",
            ],
        },
        fact=(
            "La flexion du coude reste possible malgré sa paralysie, grâce au "
            "muscle brachio-radial innervé par le nerf radial."
        ),
    ),
    "R": StructureText(
        name="Nerf radial",
        kind="Nerf mixte, branche terminale du plexus brachial",
        region="Loge postérieure du bras et de l'avant-bras, dos de la main",
        count="2 (droit et gauche)",
        description=(
            "Branche du faisceau postérieur (C5-T1), la plus volumineuse du plexus "
            "brachial. C'est le nerf de l'extension du coude, du poignet et des doigts."
        ),
        sections={
            "course": [
                "Quitte l'aisselle par la fente huméro-tricipitale avec l'artère profonde du bras",
                "Contourne la face postérieure de l'humérus dans le sillon du nerf radial",
                "Passe en avant de l'épicondyle latéral, entre brachio-radial et brachial",
                "Se divise au coude en branche superficielle sensitive et branche profonde motrice",
            ],
            "branches": [
                "Rameaux du triceps brachial et de l'anconé, au bras",
                "Branche superficielle : sensitive, vers le dos de la main",
                "Branche profonde : traverse le supinateur et devient le nerf interosseux postérieur",
            ],
            "territory": [
                "Moteur : triceps, brachio-radial, extenseurs du poignet et des doigts, supinateur",
                "Moteur : long abducteur et extenseurs du pouce",
                "Sensitif : face postérieure du bras et de l'avant-bras, dos de la main "
                "côté latéral (1re commissure)",
            ],
            "clinical": [
                "Fracture de la diaphyse humérale : atteinte du nerf dans son sillon",
                "Main tombante « en col de cygne » (sans rapport avec la déformation des doigts de même nom "
                "de la polyarthrite) : impossible d'étendre le poignet et les doigts",
                "Compression axillaire (béquilles) : le triceps est alors aussi paralysé",
            ],
        },
        fact=(
            "Après une fracture de l'humérus, on teste toujours l'extension du "
            "poignet et la sensibilité du dos de la 1re commissure."
        ),
    ),
    "D": StructureText(
        name="Nerf médian",
        kind="Nerf mixte, branche terminale du plexus brachial",
        region="Bras, loge antérieure de l'avant-bras, paume de la main",
        count="2 (droit et gauche)",
        description=(
            "Formé par l'union de deux racines (faisceaux latéral et médial, C5-T1) "
            "en avant de l'artère axillaire. C'est le nerf de la pronation, de la "
            "flexion des doigts et de l'opposition du pouce."
        ),
        sections={
            "course": [
                "Au bras, il accompagne l'artère brachiale sans donner de branche",
                "Au coude, en dedans de l'artère brachiale, passe entre les deux chefs du rond pronateur",
                "À l'avant-bras, entre fléchisseurs superficiel et profond des doigts",
                "Au poignet, traverse le canal carpien sous le rétinaculum des fléchisseurs",
            ],
            "branches": [
                "Nerf interosseux antérieur, à l'avant-bras",
                "Rameau cutané palmaire, né avant le canal carpien",
                "Rameau thénarien (récurrent) et nerfs digitaux palmaires",
            ],
            "territory": [
                "Moteur : muscles antérieurs de l'avant-bras, sauf fléchisseur ulnaire du "
                "carpe et moitié médiale du fléchisseur profond",
                "Moteur : muscles thénariens (sauf adducteur du pouce et chef profond du court fléchisseur du pouce) et deux premiers lombricaux",
                "Sensitif : face palmaire des 3 premiers doigts et demi, et face dorsale des deux dernières phalanges de ces doigts",
            ],
            "clinical": [
                "Syndrome du canal carpien : paresthésies nocturnes des 3 premiers doigts, "
                "signes de Tinel et de Phalen",
                "Atrophie thénarienne et perte de l'opposition : « main de singe »",
                "Lésion haute (fracture supracondylienne de l'enfant) : « main de "
                "bénédiction » quand le patient serre le poing",
            ],
        },
        fact=(
            "Le syndrome du canal carpien est le plus fréquent des syndromes "
            "canalaires ; la sensibilité de la paume est souvent épargnée."
        ),
    ),
    "U": StructureText(
        name="Nerf ulnaire",
        kind="Nerf mixte, branche terminale du plexus brachial",
        region="Face médiale du bras, de l'avant-bras et de la main",
        count="2 (droit et gauche)",
        old_names=["nerf cubital"],
        description=(
            "Branche du faisceau médial (C8-T1). C'est le nerf de la motricité fine "
            "de la main : interosseux, hypothénar et adducteur du pouce."
        ),
        sections={
            "course": [
                "Au bras, traverse le septum intermusculaire médial",
                "Passe en arrière de l'épicondyle médial (ancien : épitrochlée), dans le sillon du nerf ulnaire",
                "À l'avant-bras, sous le fléchisseur ulnaire du carpe, en dedans de l'artère ulnaire",
                "Au poignet, passe en dehors du pisiforme dans le canal ulnaire (loge de Guyon)",
            ],
            "branches": [
                "Rameaux du fléchisseur ulnaire du carpe et de la moitié médiale du fléchisseur profond",
                "Rameau dorsal sensitif de la main",
                "Branche superficielle (sensitive) et branche profonde (motrice) à la main",
            ],
            "territory": [
                "Moteur : muscles hypothénariens, tous les interosseux, deux lombricaux médiaux",
                "Moteur : adducteur du pouce et chef profond du court fléchisseur du pouce",
                "Sensitif : bord médial de la main, 5e doigt et moitié médiale du 4e",
            ],
            "clinical": [
                "Choc au coude : décharge électrique jusqu'au 5e doigt (nerf superficiel derrière l'épicondyle)",
                "Griffe ulnaire des 4e et 5e doigts : hyperextension des métacarpo-phalangiennes, "
                "flexion des interphalangiennes",
                "Signe de Froment : le pouce fléchit son interphalangienne pour pincer une feuille",
            ],
        },
        fact=(
            "Paradoxe ulnaire : la griffe est moins marquée si la lésion est haute, "
            "car le fléchisseur profond des doigts 4 et 5 est aussi paralysé."
        ),
    ),
    "I": StructureText(
        name="Nerfs intercostaux",
        kind="Nerfs spinaux mixtes (rameaux antérieurs thoraciques)",
        region="Espaces intercostaux et paroi abdominale antérolatérale",
        count="11 paires (T1 à T11), plus le nerf subcostal (T12)",
        description=(
            "Rameaux antérieurs des nerfs spinaux thoraciques. Ils ne forment pas de "
            "plexus et gardent une disposition segmentaire, en métamères."
        ),
        sections={
            "course": [
                "Chaque nerf court dans le sillon costal, sous le bord inférieur de la côte",
                "Il chemine entre muscles intercostaux interne et intime",
                "Disposition de haut en bas : veine, artère, nerf",
                "Les nerfs T7 à T11 se prolongent dans la paroi abdominale",
            ],
            "branches": [
                "Rameau cutané latéral, sur la ligne axillaire moyenne",
                "Rameau cutané antérieur, près du sternum ou de la ligne médiane",
                "T2 donne le nerf intercostobrachial, sensitif pour la face médiale du bras",
            ],
            "territory": [
                "Moteur : muscles intercostaux et muscles larges de l'abdomen (nerfs inférieurs)",
                "Sensitif : peau du thorax et de l'abdomen en bandes (dermatomes), plèvre et péritoine pariétaux",
                "Repères : T4 au mamelon, T10 à l'ombilic",
            ],
            "clinical": [
                "Ponction pleurale au bord supérieur de la côte inférieure, pour épargner le pédicule",
                "Zona : éruption douloureuse unilatérale le long d'un dermatome",
                "Névralgie intercostale ; bloc intercostal pour l'analgésie des fractures de côtes",
            ],
        },
        fact=(
            "Le zona réactive le virus de la varicelle resté latent dans un ganglion "
            "spinal : l'éruption dessine exactement le territoire d'un nerf."
        ),
    ),
    "F": StructureText(
        name="Nerf fémoral (plexus lombal)",
        kind="Nerf mixte, branche terminale du plexus lombal",
        region="Fosse iliaque, trigone fémoral, loge antérieure de la cuisse",
        count="2 (droit et gauche)",
        old_names=["nerf crural", "plexus lombaire"],
        description=(
            "Plus grosse branche du plexus lombal (rameaux antérieurs L1 à L4, formé "
            "dans le muscle grand psoas). Nerf L2-L4 de l'extension du genou et de la "
            "sensibilité antérieure de la cuisse."
        ),
        sections={
            "parts": [
                "Plexus lombal : nerfs ilio-hypogastrique et ilio-inguinal (anciens : grand et petit "
                "abdomino-génitaux), génito-fémoral (ancien : génito-crural)",
                "Plexus lombal : nerf cutané latéral de la cuisse (ancien : fémoro-cutané), nerf obturateur, nerf fémoral",
            ],
            "course": [
                "Émerge du bord latéral du grand psoas et descend entre psoas et iliaque",
                "Passe sous le ligament inguinal, en dehors de l'artère fémorale, hors de la gaine fémorale",
                "Se divise aussitôt en éventail dans le trigone fémoral",
            ],
            "branches": [
                "Rameaux musculaires du quadriceps et du sartorius",
                "Rameaux cutanés antérieurs de la cuisse",
                "Nerf saphène : traverse le canal des adducteurs, sensitif de la face médiale de la jambe et du pied",
            ],
            "territory": [
                "Moteur : iliaque, sartorius, pectiné (en partie), quadriceps fémoral",
                "Sensitif : faces antérieure et médiale de la cuisse, face médiale de la jambe",
            ],
            "clinical": [
                "Déficit de l'extension du genou (le genou se dérobe) et abolition du réflexe patellaire (L3-L4)",
                "Cruralgie : compression de la racine L3 ou L4 par une hernie discale",
                "Compression par un hématome du psoas sous anticoagulants",
            ],
        },
        fact=(
            "Au pli de l'aine, de dehors en dedans : nerf, artère, veine fémoraux. "
            "Le pouls fémoral guide le bloc du nerf fémoral."
        ),
    ),
    "S": StructureText(
        name="Nerf ischiatique (plexus sacral)",
        kind="Nerf mixte, branche terminale du plexus sacral",
        region="Région glutéale et loge postérieure de la cuisse",
        count="2 (droit et gauche)",
        old_names=["nerf sciatique", "grand nerf sciatique"],
        description=(
            "Le plus gros et le plus long nerf du corps (L4-S3), issu du plexus sacral. "
            "Il réunit dans une même gaine les futurs nerfs tibial et fibulaire commun."
        ),
        sections={
            "parts": [
                "Plexus sacral : tronc lombo-sacral (L4-L5) et rameaux antérieurs S1 à S3, devant le piriforme",
                "Autres branches : nerfs glutéaux et cutané postérieur de la cuisse ; le nerf pudendal (S2-S4) est "
                "rattaché à un plexus pudendal distinct dans la tradition française",
            ],
            "course": [
                "Sort du bassin par le grand foramen ischiatique, sous le muscle piriforme",
                "Descend sous le grand glutéal, entre grand trochanter et tubérosité ischiatique",
                "Descend dans la loge postérieure de la cuisse, sur le grand adducteur",
                "Se divise en général au sommet de la fosse poplitée (niveau variable)",
            ],
            "branches": [
                "Rameaux des muscles ischio-jambiers et de la partie ischiatique du grand adducteur",
                "Branches terminales : nerf tibial et nerf fibulaire commun",
            ],
            "territory": [
                "Moteur : muscles postérieurs de la cuisse et tous les muscles de la jambe et du pied",
                "Sensitif : jambe et pied, sauf le territoire médial du nerf saphène",
            ],
            "clinical": [
                "Lombosciatique : compression de la racine L5 ou S1 par une hernie discale L4-L5 ou L5-S1",
                "Injection intramusculaire au quadrant supéro-latéral de la fesse pour épargner le nerf",
                "Atteinte possible dans les luxations postérieures de hanche",
            ],
        },
        fact=(
            "À sa sortie du bassin, le nerf ischiatique peut mesurer près de 2 cm de large."
        ),
    ),
    "N": StructureText(
        name="Nerf tibial",
        kind="Nerf mixte, branche terminale du nerf ischiatique",
        region="Fosse poplitée, loge postérieure de la jambe, plante du pied",
        count="2 (droit et gauche)",
        old_names=["nerf sciatique poplité interne (SPI)"],
        description=(
            "Branche terminale médiale du nerf ischiatique (L4-S3). C'est le nerf de "
            "la flexion plantaire, de la flexion des orteils et de la sensibilité de la plante."
        ),
        sections={
            "course": [
                "Descend au milieu de la fosse poplitée, en superficie par rapport aux vaisseaux poplités",
                "Passe sous l'arcade du soléaire (segment autrefois appelé nerf tibial postérieur) "
                "et descend avec l'artère tibiale postérieure",
                "Passe en arrière de la malléole médiale, dans le canal tarsien",
                "Se divise en nerfs plantaires médial et latéral",
            ],
            "branches": [
                "Nerf cutané sural médial, qui participe au nerf sural",
                "Rameaux des muscles gastrocnémien, soléaire, poplité, tibial postérieur et fléchisseurs des orteils",
                "Rameaux calcanéens médiaux ; nerfs plantaires médial et latéral",
            ],
            "territory": [
                "Moteur : loge postérieure de la jambe et muscles plantaires du pied",
                "Sensitif : plante du pied et talon",
            ],
            "clinical": [
                "Paralysie : impossible de marcher sur la pointe des pieds",
                "Abolition du réflexe achilléen (S1)",
                "Syndrome du canal tarsien : paresthésies plantaires",
            ],
        },
        fact=(
            "Dans la fosse poplitée, de la superficie vers la profondeur : nerf "
            "tibial, veine poplitée, artère poplitée."
        ),
    ),
    "G": StructureText(
        name="Nerf fibulaire commun",
        kind="Nerf mixte, branche terminale du nerf ischiatique",
        region="Fosse poplitée, col de la fibula, loges antérieure et latérale de la jambe",
        count="2 (droit et gauche)",
        old_names=["nerf sciatique poplité externe (SPE)", "nerf péronier commun"],
        description=(
            "Branche terminale latérale du nerf ischiatique (L4-S2). C'est le nerf de "
            "la flexion dorsale de la cheville et des orteils et de l'éversion du pied."
        ),
        sections={
            "course": [
                "Longe le bord médial du biceps fémoral dans la partie latérale de la fosse poplitée",
                "Contourne le col de la fibula, très superficiel, sous la peau",
                "Traverse le muscle long fibulaire et se divise en deux branches",
            ],
            "branches": [
                "Nerf fibulaire superficiel (ancien : musculo-cutané de la jambe) : loge latérale",
                "Nerf fibulaire profond (ancien : tibial antérieur) : loge antérieure",
                "Nerf cutané sural latéral",
            ],
            "territory": [
                "Moteur : long et court fibulaires (éversion) par le nerf superficiel",
                "Moteur : tibial antérieur et extenseurs des orteils (flexion dorsale) par le nerf profond",
                "Sensitif : face latérale de la jambe, dos du pied, 1re commissure (nerf profond)",
            ],
            "clinical": [
                "Nerf le plus souvent lésé du membre inférieur : fracture du col de la "
                "fibula, plâtre trop serré, jambes croisées",
                "Pied tombant (steppage) : le patient lève haut le genou pour ne pas accrocher la pointe",
            ],
        },
        fact=(
            "Le col de la fibula est l'endroit où l'on peut faire rouler le nerf "
            "sous le doigt, d'où sa vulnérabilité."
        ),
    ),
}
