"""Textes en français (nomenclature anatomique internationale francisée,
celle utilisée en PASS / L.AS). Les anciens noms sont indiqués à titre de
correspondance."""

from __future__ import annotations

from ...model import StructureText

TEXTS: dict[str, StructureText] = {
    "H": StructureText(
        name="Cœur",
        kind="Organe musculaire creux",
        region=(
            "Thorax, médiastin moyen (classification internationale ; « médiastin "
            "antérieur » dans certains ouvrages français), dans le péricarde"
        ),
        count="1",
        description=(
            "Pompe musculaire à quatre cavités : deux atriums et deux ventricules. "
            "Le cœur droit envoie le sang pauvre en oxygène aux poumons (petite "
            "circulation), le cœur gauche envoie le sang oxygéné à tout le corps "
            "(grande circulation). Il pèse environ 250 à 300 g ; les deux tiers sont "
            "à gauche de la ligne médiane et l'apex est orienté en avant, en bas et "
            "à gauche."
        ),
        sections={
            "parts": [
                "Atrium droit : reçoit les veines caves supérieure et inférieure et le "
                "sinus coronaire ; il porte l'auricule droite",
                "Ventricule droit : forme l'essentiel de la face antérieure "
                "(sterno-costale) et éjecte dans le tronc pulmonaire",
                "Atrium gauche : reçoit les quatre veines pulmonaires ; c'est la "
                "cavité la plus postérieure",
                "Ventricule gauche : paroi la plus épaisse (environ 10 mm), forme "
                "l'apex et éjecte dans l'aorte",
                "Valves atrioventriculaires : tricuspide à droite, mitrale (bicuspide) "
                "à gauche, tenues par cordages tendineux et muscles papillaires",
                "Valves artérielles : pulmonaire et aortique, chacune à trois "
                "valvules semi-lunaires",
                "Paroi : endocarde, myocarde, épicarde ; le tout entouré par le "
                "péricarde (fibreux et séreux)",
                "Tissu nodal : nœud sinu-atrial, nœud atrioventriculaire, faisceau "
                "atrioventriculaire (de His) et ses branches, réseau de Purkinje",
            ],
            "relations": [
                "En avant : sternum et cartilages costaux 3 à 6, plèvres et bords "
                "antérieurs des poumons (incisure cardiaque du poumon gauche)",
                "En arrière : œsophage, au contact de l'atrium gauche, et aorte "
                "thoracique descendante",
                "En bas : centre tendineux du diaphragme (face diaphragmatique)",
                "Latéralement : nerfs phréniques, plèvres médiastinales et poumons",
                "Apex : 5e espace intercostal gauche, sur la ligne médio-claviculaire "
                "(choc de pointe)",
            ],
            "vascularisation": [
                "Artère coronaire droite (sinus aortique droit) : cœur droit, nœud "
                "sinu-atrial (environ 60 % des cas) et nœud atrioventriculaire "
                "(environ 80 à 90 %)",
                "Artère coronaire gauche (sinus aortique gauche) : tronc court qui se "
                "divise en artère interventriculaire antérieure et artère circonflexe",
                "Veines du cœur (grande, moyenne, petite) drainées par le sinus "
                "coronaire dans l'atrium droit",
            ],
            "innervation": [
                "Automatisme propre : le nœud sinu-atrial donne le rythme (60 à 100 "
                "battements par minute au repos)",
                "Sympathique (ganglions cervicaux et thoraciques hauts) : accélère et "
                "renforce les contractions",
                "Parasympathique (nerfs vagues, X) : ralentit le cœur",
            ],
            "clinical": [
                "Infarctus du myocarde : occlusion d'une artère coronaire, souvent "
                "l'interventriculaire antérieure",
                "Foyers d'auscultation : aortique (2e espace intercostal droit), "
                "pulmonaire (2e gauche), tricuspide (4e-5e gauche au bord du sternum), "
                "mitral (apex)",
                "Valvulopathies fréquentes : rétrécissement aortique, insuffisance "
                "mitrale",
                "Tamponnade : épanchement dans le péricarde qui comprime le cœur",
            ],
        },
        fact=(
            "Le cœur bat environ 100 000 fois par jour et éjecte environ 5 litres de "
            "sang par minute au repos."
        ),
        old_names=[
            "oreillettes (pour les atriums)",
            "valvules sigmoïdes (pour les valves artérielles)",
        ],
    ),
    "A": StructureText(
        name="Aorte ascendante et arc de l'aorte",
        old_names=["crosse de l'aorte", "crosse aortique"],
        kind="Artère élastique",
        region="Thorax : médiastin moyen (aorte ascendante) puis supérieur (arc)",
        count="1 (impaire)",
        description=(
            "Début de l'aorte. L'aorte ascendante naît du ventricule gauche ; l'arc "
            "de l'aorte se courbe en arrière et à gauche au-dessus du pédicule "
            "pulmonaire gauche, puis se continue par l'aorte thoracique descendante "
            "(cachée derrière le cœur sur la figure). Le tronc brachiocéphalique est "
            "inclus ici."
        ),
        sections={
            "parts": [
                "Aorte ascendante (environ 5 cm), dans le péricarde, avec les trois "
                "sinus aortiques juste au-dessus de la valve aortique",
                "Arc de l'aorte, dans le médiastin supérieur, en arrière du manubrium "
                "sternal",
                "Isthme aortique : jonction rétrécie entre l'arc et l'aorte "
                "descendante, au niveau du ligament artériel",
            ],
            "course": [
                "L'aorte ascendante monte en avant et à droite jusqu'au 2e cartilage "
                "costal droit",
                "L'arc se porte en arrière et à gauche, en avant puis à gauche de la "
                "trachée ; son sommet est au milieu du manubrium",
                "Il se termine à gauche du corps de T4, au niveau de l'angle sternal",
            ],
            "branches": [
                "Artères coronaires droite et gauche, nées des sinus de l'aorte "
                "ascendante",
                "Tronc brachiocéphalique (à droite) : se divise en artères subclavière "
                "droite et carotide commune droite",
                "Artère carotide commune gauche",
                "Artère subclavière gauche",
            ],
            "relations": [
                "Aorte ascendante : tronc pulmonaire en avant puis à gauche, veine "
                "cave supérieure à droite",
                "La veine brachiocéphalique gauche croise en avant les branches de "
                "l'arc",
                "Sous l'arc : bifurcation du tronc pulmonaire, ligament artériel et "
                "nerf laryngé récurrent gauche qui contourne l'arc",
                "À gauche : nerfs phrénique et vague gauches ; à droite et en arrière : "
                "trachée et œsophage",
            ],
            "clinical": [
                "Coarctation de l'aorte : rétrécissement congénital près de l'isthme ; "
                "hypertension aux membres supérieurs, pouls fémoraux faibles",
                "Dissection aortique : déchirure de l'intima, douleur thoracique "
                "brutale et intense irradiant dans le dos",
                "Rupture traumatique à l'isthme lors des décélérations brutales "
                "(accidents de la route)",
                "Anévrisme de l'arc : peut comprimer le nerf laryngé récurrent gauche "
                "et donner une dysphonie",
            ],
        },
        fact=(
            "Le ligament artériel, sous l'arc, est le reste du conduit artériel qui, "
            "chez le fœtus, faisait passer le sang du tronc pulmonaire à l'aorte en "
            "évitant les poumons."
        ),
    ),
    "P": StructureText(
        name="Tronc pulmonaire",
        old_names=["artère pulmonaire (tronc de l')"],
        kind="Artère élastique (transporte du sang pauvre en oxygène)",
        region="Thorax, médiastin moyen, dans le péricarde",
        count="1 (impair)",
        description=(
            "Artère qui conduit le sang pauvre en oxygène du ventricule droit vers "
            "les poumons : c'est une artère, mais elle transporte du sang « veineux », "
            "d'où sa couleur bleu-violet sur la figure. Les veines pulmonaires "
            "ramènent ensuite le sang oxygéné à l'atrium gauche."
        ),
        sections={
            "course": [
                "Naît du cône artériel (infundibulum) du ventricule droit, au-delà de "
                "la valve pulmonaire",
                "Monte en arrière et à gauche sur environ 5 cm, d'abord en avant puis "
                "à gauche de l'aorte ascendante",
                "Se divise sous la concavité de l'arc de l'aorte, vers T4-T5, en "
                "avant et à gauche de la bifurcation trachéale",
            ],
            "branches": [
                "Artère pulmonaire droite : longue, passe en arrière de l'aorte "
                "ascendante et de la veine cave supérieure vers le hile droit",
                "Artère pulmonaire gauche : courte, passe en avant de l'aorte "
                "descendante et de la bronche principale gauche",
                "Ligament artériel : relie l'origine de l'artère pulmonaire gauche à "
                "la face inférieure de l'arc de l'aorte",
            ],
            "relations": [
                "Entouré avec l'aorte ascendante par une même gaine de péricarde "
                "séreux ; le sinus transverse du péricarde passe en arrière",
                "Tronc pulmonaire et aorte s'enroulent l'un autour de l'autre en "
                "spirale",
                "Auricules droite et gauche de part et d'autre de son origine, près "
                "des artères coronaires",
            ],
            "clinical": [
                "Embolie pulmonaire : obstruction par un caillot, le plus souvent venu "
                "d'une thrombose veineuse profonde des membres inférieurs",
                "Persistance du conduit artériel : shunt de l'aorte vers le tronc "
                "pulmonaire, souffle continu",
                "Foyer d'auscultation pulmonaire : 2e espace intercostal gauche, au "
                "bord du sternum",
                "Hypertension pulmonaire : la pression normale est d'environ "
                "25/10 mmHg",
            ],
        },
        fact=(
            "La pression dans le tronc pulmonaire est environ cinq fois plus faible "
            "que dans l'aorte : la petite circulation est un circuit à basse pression."
        ),
    ),
    "S": StructureText(
        name="Veine cave supérieure",
        kind="Veine de gros calibre, sans valvule",
        region="Thorax, médiastin supérieur puis moyen, à droite",
        count="1 (impaire)",
        description=(
            "Grosse veine courte (environ 7 cm) qui ramène à l'atrium droit le sang "
            "de la tête, du cou, des membres supérieurs et de la paroi thoracique."
        ),
        sections={
            "course": [
                "Formée par l'union des veines brachiocéphaliques droite et gauche "
                "derrière le 1er cartilage costal droit",
                "Descend verticalement à droite de l'aorte ascendante",
                "Reçoit en arrière la veine azygos, dont l'arc passe au-dessus du "
                "pédicule pulmonaire droit",
                "S'abouche dans la partie haute de l'atrium droit, au niveau du 3e "
                "cartilage costal droit",
            ],
            "territory": [
                "Tête et cou (veines jugulaires internes et externes)",
                "Membres supérieurs (veines subclavières)",
                "Paroi thoracique et une partie de la paroi abdominale postérieure, "
                "par le système azygos",
            ],
            "relations": [
                "À gauche : aorte ascendante",
                "À droite : nerf phrénique droit, plèvre médiastinale et poumon droit",
                "En arrière : trachée en haut, puis pédicule pulmonaire droit",
            ],
            "clinical": [
                "Syndrome cave supérieur (cancer bronchique, lymphome) : œdème du "
                "visage et du cou « en pèlerine », circulation veineuse collatérale",
                "L'extrémité des cathéters veineux centraux est placée à la jonction "
                "entre veine cave supérieure et atrium droit",
                "Sur la radiographie de thorax, elle forme le bord droit supérieur de "
                "l'ombre médiastinale",
            ],
        },
        fact=(
            "Comme elle n'a pas de valvule, la pression veineuse centrale qu'on y "
            "mesure reflète la pression de l'atrium droit."
        ),
    ),
    "I": StructureText(
        name="Veine cave inférieure",
        kind="Veine de gros calibre",
        region="Abdomen (rétropéritoine) puis thorax, à droite de l'aorte",
        count="1 (impaire)",
        description=(
            "Plus grosse veine du corps. Elle ramène à l'atrium droit le sang des "
            "membres inférieurs, du bassin, des reins et du foie. Le sang du tube "
            "digestif et de la rate n'y arrive qu'après avoir traversé le foie par "
            "la veine porte."
        ),
        sections={
            "course": [
                "Formée par l'union des deux veines iliaques communes, en avant et à "
                "droite de L5",
                "Monte dans le rétropéritoine, à droite de l'aorte abdominale, devant "
                "le flanc droit des corps vertébraux",
                "Passe dans un sillon de la face postérieure du foie",
                "Traverse le centre tendineux du diaphragme par le foramen de la "
                "veine cave (niveau T8)",
                "Se termine presque aussitôt dans la partie basse de l'atrium droit",
            ],
            "territory": [
                "Membres inférieurs et bassin, par les veines iliaques communes",
                "Veines rénales ; la gauche reçoit aussi les veines surrénale et "
                "gonadique gauches, les droites vont directement dans la veine cave",
                "Foie, par les veines hépatiques, juste sous le diaphragme",
                "Paroi abdominale postérieure : veines lombales et phréniques "
                "inférieures",
            ],
            "relations": [
                "À gauche : aorte abdominale",
                "En avant : duodénum (3e partie), tête du pancréas, racine du "
                "mésentère, foie",
                "En arrière : colonne lombale, pilier droit du diaphragme, tronc "
                "sympathique droit",
                "La veine rénale gauche la rejoint en passant devant l'aorte, sous "
                "l'artère mésentérique supérieure",
            ],
            "clinical": [
                "Thrombose veineuse profonde : en cas d'embolie pulmonaire récidivante, "
                "un filtre cave peut être posé sous les veines rénales",
                "Compression par l'utérus gravide en décubitus dorsal (malaise, "
                "hypotension) : on installe la femme enceinte sur le côté gauche",
                "Située à droite, elle rend la veine rénale droite très courte : on "
                "préfère prélever le rein gauche chez un donneur vivant",
            ],
        },
        fact=(
            "Son foramen est dans le centre tendineux du diaphragme : la contraction "
            "du diaphragme à l'inspiration ne l'écrase pas, et la baisse de pression "
            "thoracique aide le retour veineux."
        ),
    ),
    "C": StructureText(
        name="Artère carotide commune",
        old_names=["artère carotide primitive"],
        kind="Artère élastique",
        region="Cou (et médiastin supérieur pour la gauche)",
        count="2 (droite et gauche)",
        description=(
            "Principale artère de la tête et du cou. La droite naît du tronc "
            "brachiocéphalique, la gauche directement de l'arc de l'aorte (elle a "
            "donc une portion thoracique). Elle ne donne classiquement aucune branche "
            "avant sa bifurcation en artères carotides interne et externe."
        ),
        sections={
            "course": [
                "Droite : naît du tronc brachiocéphalique derrière l'articulation "
                "sterno-claviculaire droite",
                "Gauche : naît de l'arc de l'aorte et monte dans le médiastin "
                "supérieur jusqu'à l'articulation sterno-claviculaire gauche",
                "Monte dans le cou dans la gaine carotidienne, le long de la trachée "
                "puis du larynx",
                "Se divise au niveau du bord supérieur du cartilage thyroïde, vers C4 "
                "(C3 à C4 selon les ouvrages)",
            ],
            "branches": [
                "Pas de branche collatérale (classiquement)",
                "Artère carotide interne : encéphale et œil ; elle ne donne aucune "
                "branche dans le cou",
                "Artère carotide externe : cou, face et cuir chevelu (thyroïdienne "
                "supérieure, linguale, faciale, temporale superficielle, maxillaire...)",
            ],
            "relations": [
                "Gaine carotidienne : veine jugulaire interne latérale, nerf vague en "
                "arrière entre artère et veine",
                "En avant : muscle sterno-cléido-mastoïdien, sous son bord antérieur, "
                "et muscle omo-hyoïdien",
                "En arrière : processus transverses cervicaux (tubercule carotidien de "
                "C6) et tronc sympathique cervical",
                "En dedans : trachée, œsophage, glande thyroïde, puis larynx et "
                "pharynx",
            ],
            "clinical": [
                "Pouls carotidien : au bord antérieur du sterno-cléido-mastoïdien, à "
                "hauteur du cartilage thyroïde",
                "Sinus carotidien (barorécepteur, nerf glosso-pharyngien IX) au début "
                "de la carotide interne : son massage ralentit le cœur",
                "Glomus carotidien : chémorécepteur situé dans la bifurcation",
                "Sténose athéromateuse de la bifurcation : cause d'accident vasculaire "
                "cérébral ischémique, traitée par endartériectomie",
            ],
        },
        fact=(
            "On ne palpe qu'une carotide à la fois : comprimer les deux pourrait "
            "réduire le débit sanguin cérébral."
        ),
    ),
    "J": StructureText(
        name="Veine jugulaire interne",
        kind="Veine profonde de gros calibre",
        region="Cou",
        count="2 (droite et gauche)",
        description=(
            "Principale veine de la tête et du cou : elle draine l'encéphale (par les "
            "sinus de la dure-mère), la face et le cou. Elle accompagne les artères "
            "carotides interne puis commune dans la gaine carotidienne."
        ),
        sections={
            "course": [
                "Naît au foramen jugulaire en continuité avec le sinus sigmoïde "
                "(bulbe supérieur)",
                "Descend dans la gaine carotidienne, latérale aux artères carotides "
                "interne puis commune",
                "Se termine derrière l'extrémité médiale de la clavicule en s'unissant "
                "à la veine subclavière pour former la veine brachiocéphalique",
            ],
            "territory": [
                "Encéphale et méninges, par les sinus veineux de la dure-mère",
                "Face et cou : veines faciale, linguale, pharyngiennes, thyroïdiennes "
                "supérieure et moyenne",
                "À sa terminaison (angle veineux) : conduit thoracique à gauche, "
                "conduit lymphatique droit à droite",
            ],
            "relations": [
                "Dans la gaine carotidienne, latérale à l'artère, avec le nerf vague "
                "en arrière entre les deux",
                "Recouverte par le muscle sterno-cléido-mastoïdien",
                "En bas, elle est dans le petit triangle entre les chefs sternal et "
                "claviculaire du sterno-cléido-mastoïdien",
                "Longée par les nœuds lymphatiques cervicaux profonds (chaîne "
                "jugulaire)",
            ],
            "clinical": [
                "Voie d'abord classique du cathéter veineux central, plutôt à droite "
                "(trajet direct vers la veine cave supérieure), sous échographie",
                "Pouls veineux jugulaire et turgescence jugulaire : signes "
                "d'élévation de la pression de l'atrium droit (insuffisance cardiaque "
                "droite)",
                "Curage ganglionnaire jugulo-carotidien dans les cancers de la tête "
                "et du cou",
            ],
        },
        fact=(
            "La jugulaire interne droite est dans l'axe de la veine cave supérieure : "
            "c'est la route la plus directe vers le cœur pour un cathéter."
        ),
    ),
    "U": StructureText(
        name="Artère subclavière",
        old_names=["artère sous-clavière"],
        kind="Artère élastique",
        region="Base du cou et sommet du thorax",
        count="2 (droite et gauche)",
        description=(
            "Artère du membre supérieur, qui irrigue aussi une partie de l'encéphale, "
            "du cou et de la paroi thoracique. La droite naît du tronc "
            "brachiocéphalique, la gauche de l'arc de l'aorte."
        ),
        sections={
            "course": [
                "Décrit une courbe au-dessus du dôme pleural et de la 1re côte",
                "Passe entre les muscles scalène antérieur (en avant) et scalène "
                "moyen (en arrière) : défilé des scalènes",
                "Trois parties : en dedans, en arrière et en dehors du scalène "
                "antérieur",
                "Devient l'artère axillaire au bord latéral de la 1re côte",
            ],
            "branches": [
                "Artère vertébrale : monte dans les foramens transversaires de C6 à "
                "C1 ; tronc cérébral, cervelet, lobes occipitaux",
                "Artère thoracique interne : descend derrière les cartilages costaux, "
                "à 1 cm du bord du sternum",
                "Tronc thyro-cervical (dont l'artère thyroïdienne inférieure) et tronc "
                "costo-cervical",
                "Artère dorsale de la scapula, inconstante comme branche directe",
            ],
            "relations": [
                "En avant : veine subclavière, séparée de l'artère par le scalène "
                "antérieur et le nerf phrénique qu'il porte",
                "En arrière et au-dessus : troncs du plexus brachial, qui passent avec "
                "l'artère entre les scalènes",
                "En bas : dôme pleural et apex du poumon, sillon de l'artère "
                "subclavière sur la 1re côte",
            ],
            "clinical": [
                "Syndrome du défilé thoraco-brachial (côte cervicale, scalènes) : "
                "compression de l'artère et du plexus brachial",
                "Syndrome de vol subclavier : sténose avant l'artère vertébrale ; le "
                "bras « vole » du sang à l'encéphale par la vertébrale",
                "Compression d'urgence au-dessus de la clavicule, contre la 1re côte, "
                "en cas d'hémorragie du membre supérieur",
            ],
        },
        fact=(
            "L'artère thoracique interne gauche, branche de la subclavière, est le "
            "greffon de référence pour un pontage de l'artère interventriculaire "
            "antérieure."
        ),
    ),
    "X": StructureText(
        name="Artère brachiale",
        old_names=["artère humérale"],
        kind="Artère musculaire (distributrice)",
        region="Bras, face médiale",
        count="2 (droite et gauche)",
        description=(
            "Artère du bras, suite de l'artère axillaire. Elle se termine dans la "
            "fosse cubitale (pli du coude) en artères radiale et ulnaire."
        ),
        sections={
            "course": [
                "Commence au bord inférieur du muscle grand rond",
                "Descend à la face médiale du bras, dans le sillon bicipital médial, "
                "le long du bord médial du biceps",
                "Se termine dans la fosse cubitale, en regard du col du radius, un peu "
                "sous le pli du coude",
            ],
            "branches": [
                "Artère profonde du bras : accompagne le nerf radial dans le sillon du "
                "nerf radial de l'humérus",
                "Artères collatérales ulnaires supérieure et inférieure, pour le réseau "
                "anastomotique du coude",
                "Branches terminales : artère radiale et artère ulnaire",
            ],
            "relations": [
                "Nerf médian : latéral en haut, il croise l'artère en avant au milieu "
                "du bras et devient médial en bas",
                "Accompagnée de deux veines brachiales",
                "Au coude : sous l'aponévrose bicipitale, médiale au tendon du biceps "
                "et latérale au nerf médian",
            ],
            "clinical": [
                "Mesure de la pression artérielle : brassard au bras, stéthoscope sur "
                "l'artère au pli du coude",
                "Pouls brachial au pli du coude, en dedans du tendon du biceps",
                "Fracture supracondylienne de l'humérus chez l'enfant : risque de "
                "lésion artérielle et de syndrome des loges (ischémie de Volkmann)",
            ],
        },
        fact=(
            "Les bruits de Korotkoff, entendus au stéthoscope pendant la prise de "
            "tension, naissent dans l'artère brachiale sous le brassard."
        ),
    ),
    "R": StructureText(
        name="Artère radiale",
        kind="Artère musculaire (distributrice)",
        region="Avant-bras (côté latéral), poignet et main",
        count="2 (droite et gauche)",
        description=(
            "Branche terminale latérale de l'artère brachiale. Elle suit le côté du "
            "pouce (le radius) et forme dans la paume l'essentiel de l'arcade "
            "palmaire profonde."
        ),
        sections={
            "course": [
                "Naît dans la fosse cubitale, en regard du col du radius",
                "Descend à la face antérieure de l'avant-bras sous le muscle "
                "brachio-radial, puis entre les tendons du brachio-radial et du "
                "fléchisseur radial du carpe",
                "Contourne le bord latéral du carpe dans la tabatière anatomique, puis "
                "entre dans la paume entre les deux chefs du 1er interosseux dorsal",
            ],
            "branches": [
                "Artère récurrente radiale, pour le réseau anastomotique du coude",
                "Rameau palmaire superficiel, qui complète l'arcade palmaire "
                "superficielle",
                "Artère principale du pouce ; elle se termine en arcade palmaire "
                "profonde avec la branche profonde de l'artère ulnaire",
            ],
            "relations": [
                "Recouverte par le muscle brachio-radial au tiers supérieur de "
                "l'avant-bras",
                "La branche superficielle du nerf radial est latérale à elle au tiers "
                "moyen",
                "Au poignet, juste sous la peau, sur le radius, en dehors du tendon du "
                "fléchisseur radial du carpe",
            ],
            "clinical": [
                "Pouls radial : le site de palpation habituel, au poignet, en dehors "
                "du tendon du fléchisseur radial du carpe",
                "Ponction pour gaz du sang artériel ; voie d'abord radiale des "
                "coronarographies",
                "Test d'Allen avant ponction : vérifie que l'artère ulnaire peut "
                "irriguer seule la main",
            ],
        },
        fact=(
            "Au poignet elle repose directement sur le radius : c'est pour cela que "
            "le pouls y est si facile à prendre."
        ),
    ),
    "N": StructureText(
        name="Artère ulnaire",
        old_names=["artère cubitale"],
        kind="Artère musculaire (distributrice)",
        region="Avant-bras (côté médial), poignet et main",
        count="2 (droite et gauche)",
        description=(
            "Branche terminale médiale, la plus grosse, de l'artère brachiale. Elle "
            "suit le côté de l'auriculaire (l'ulna) et forme surtout l'arcade "
            "palmaire superficielle."
        ),
        sections={
            "course": [
                "Naît dans la fosse cubitale, en regard du col du radius",
                "Passe en profondeur du muscle rond pronateur, puis descend sous le "
                "muscle fléchisseur ulnaire du carpe",
                "Au poignet, passe en avant du rétinaculum des fléchisseurs, en dehors "
                "du pisiforme, dans le canal ulnaire (loge de Guyon)",
            ],
            "branches": [
                "Artères récurrentes ulnaires, pour le réseau anastomotique du coude",
                "Artère interosseuse commune, qui donne les interosseuses antérieure "
                "et postérieure",
                "Se termine en arcade palmaire superficielle, complétée par le rameau "
                "palmaire superficiel de la radiale",
            ],
            "relations": [
                "Le nerf ulnaire la rejoint au tiers moyen de l'avant-bras et reste "
                "médial à elle jusqu'au poignet",
                "Recouverte par les muscles fléchisseurs superficiels de l'avant-bras",
                "Dans le canal ulnaire (de Guyon), avec le nerf ulnaire, en dehors du "
                "pisiforme",
            ],
            "clinical": [
                "Pouls ulnaire, moins net que le radial, en dehors du tendon du "
                "fléchisseur ulnaire du carpe",
                "Test d'Allen : on comprime radiale et ulnaire, puis on relâche "
                "l'ulnaire pour voir la main se recolorer",
                "Syndrome du marteau hypothénarien : lésion de l'artère par des chocs "
                "répétés du talon de la main",
            ],
        },
        fact=(
            "Les arcades palmaires relient radiale et ulnaire : la main reste en "
            "général bien irriguée si l'une des deux est interrompue."
        ),
    ),
    "B": StructureText(
        name="Aorte abdominale",
        kind="Artère élastique",
        region="Abdomen, rétropéritoine, devant la colonne lombale",
        count="1 (impaire)",
        description=(
            "Partie de l'aorte située sous le diaphragme, de l'hiatus aortique (T12) "
            "à sa bifurcation en artères iliaques communes (L4). Elle donne des "
            "branches viscérales impaires (tube digestif), viscérales paires (reins, "
            "surrénales, gonades) et pariétales."
        ),
        sections={
            "course": [
                "Entre dans l'abdomen par l'hiatus aortique du diaphragme, en arrière, "
                "au niveau de T12",
                "Descend devant les corps vertébraux lombaux, un peu à gauche de la "
                "ligne médiane",
                "Se divise en artères iliaques communes devant L4, un peu sous et à "
                "gauche de l'ombilic",
            ],
            "branches": [
                "Viscérales impaires : tronc cœliaque (T12), artère mésentérique "
                "supérieure (L1), artère mésentérique inférieure (L3)",
                "Viscérales paires : artères surrénales moyennes, artères rénales "
                "(L1-L2), artères testiculaires ou ovariques",
                "Pariétales : artères phréniques inférieures et quatre paires "
                "d'artères lombales",
                "Terminales : artères iliaques communes, et une petite artère sacrale "
                "médiane",
            ],
            "relations": [
                "À droite : veine cave inférieure",
                "En avant : pancréas, veine rénale gauche, 3e partie du duodénum, "
                "racine du mésentère",
                "En arrière : corps vertébraux lombaux et veines lombales gauches",
                "Entourée par le plexus nerveux aortique et les nœuds lymphatiques "
                "lombaux",
            ],
            "clinical": [
                "Anévrisme de l'aorte abdominale : dilatation (diamètre de 3 cm ou "
                "plus), le plus souvent sous les artères rénales ; risque de rupture",
                "Facteurs de risque : homme âgé, tabac, hypertension ; dépistage par "
                "échographie",
                "Syndrome de Leriche : occlusion de la bifurcation aortique "
                "(claudication des fesses, pouls fémoraux abolis, impuissance)",
            ],
        },
        fact=(
            "Chez une personne mince, on sent battre l'aorte abdominale en appuyant "
            "profondément juste au-dessus de l'ombilic."
        ),
    ),
    "T": StructureText(
        name="Tronc cœliaque",
        kind="Artère viscérale (tronc court)",
        region="Abdomen, étage supramésocolique",
        count="1 (impair)",
        description=(
            "Première branche viscérale impaire de l'aorte abdominale, longue de 1 à "
            "2 cm. Il irrigue les organes de l'intestin antérieur : estomac, début du "
            "duodénum, foie et voies biliaires, pancréas, et aussi la rate."
        ),
        sections={
            "course": [
                "Naît de la face antérieure de l'aorte juste sous l'hiatus aortique, "
                "au niveau de T12",
                "Se dirige en avant au-dessus du bord supérieur du pancréas",
                "Se divise rapidement en trois branches (trépied cœliaque)",
            ],
            "branches": [
                "Artère gastrique gauche (ancienne coronaire stomachique) : petite "
                "courbure de l'estomac et œsophage abdominal",
                "Artère hépatique commune : donne l'artère gastro-duodénale puis "
                "devient l'artère hépatique propre (foie, vésicule par l'artère "
                "cystique)",
                "Artère splénique : longe le bord supérieur du pancréas vers la rate, "
                "donne les artères gastriques courtes et gastro-omentale gauche",
            ],
            "territory": [
                "Œsophage abdominal, estomac, duodénum jusqu'à la papille majeure",
                "Foie, vésicule biliaire et voies biliaires, pancréas (avec la "
                "mésentérique supérieure), rate",
                "Anastomoses avec l'artère mésentérique supérieure par les arcades "
                "pancréatico-duodénales",
            ],
            "clinical": [
                "Ulcère de la face postérieure du duodénum : peut éroder l'artère "
                "gastro-duodénale et saigner abondamment",
                "Syndrome du ligament arqué médian : compression du tronc par le "
                "diaphragme",
                "Variations fréquentes des artères hépatiques, importantes en "
                "chirurgie et en transplantation",
            ],
        },
        fact="Son nom vient du grec koilia, le ventre.",
    ),
    "K": StructureText(
        name="Artère rénale",
        kind="Artère viscérale paire",
        region="Abdomen, rétropéritoine",
        count="2 (droite et gauche)",
        description=(
            "Branche latérale de l'aorte abdominale qui gagne le hile du rein. Les "
            "deux reins reçoivent environ 20 à 25 % du débit cardiaque."
        ),
        sections={
            "course": [
                "Naît de la face latérale de l'aorte vers le disque L1-L2, juste sous "
                "l'artère mésentérique supérieure",
                "La droite, plus longue, passe en arrière de la veine cave inférieure",
                "Se divise près du hile en branches antérieure et postérieure au "
                "pelvis rénal, puis en artères segmentaires",
            ],
            "branches": [
                "Artère surrénale inférieure",
                "Rameaux urétéraux pour le haut de l'uretère",
                "Artères segmentaires : terminales, sans anastomoses entre elles",
            ],
            "relations": [
                "Dans le pédicule rénal, d'avant en arrière : veine rénale, artère "
                "rénale, pelvis rénal",
                "La veine rénale gauche, longue, passe en avant de l'aorte sous "
                "l'artère mésentérique supérieure",
                "Artères rénales accessoires (polaires) fréquentes, nées directement "
                "de l'aorte",
            ],
            "clinical": [
                "Sténose de l'artère rénale (athérome, dysplasie fibromusculaire) : "
                "hypertension artérielle secondaire, dite réno-vasculaire",
                "Occlusion d'une artère segmentaire ou polaire : infarctus du "
                "territoire correspondant, car ces artères sont terminales",
                "En transplantation, l'artère du greffon est branchée sur l'artère "
                "iliaque externe",
            ],
        },
        fact=(
            "Le sang traverse les reins si vite qu'ils filtrent tout le plasma "
            "environ 60 fois par jour (180 litres de filtrat glomérulaire)."
        ),
    ),
    "L": StructureText(
        name="Artère iliaque commune",
        old_names=["artère iliaque primitive"],
        kind="Artère de gros calibre",
        region="Abdomen et entrée du bassin",
        count="2 (droite et gauche)",
        description=(
            "Branche terminale de l'aorte abdominale, courte (4 à 5 cm). Elle se "
            "divise en artère iliaque interne pour le bassin et artère iliaque externe "
            "pour le membre inférieur."
        ),
        sections={
            "course": [
                "Naît de la bifurcation aortique, devant L4",
                "Descend en bas et en dehors le long du bord médial du muscle grand "
                "psoas",
                "Se divise devant l'articulation sacro-iliaque, au niveau du disque "
                "L5-S1",
            ],
            "branches": [
                "Pas de branche collatérale importante",
                "Artère iliaque interne : viscères du bassin, périnée, fesse (artères "
                "glutéales)",
                "Artère iliaque externe : passe sous le ligament inguinal et devient "
                "l'artère fémorale",
            ],
            "relations": [
                "L'uretère croise en avant la bifurcation iliaque",
                "La veine iliaque commune gauche passe en arrière de l'artère iliaque "
                "commune droite pour rejoindre la veine cave inférieure",
                "Recouverte par le péritoine pariétal postérieur ; nœuds lymphatiques "
                "iliaques communs autour",
            ],
            "clinical": [
                "Syndrome de May-Thurner (Cockett) : la veine iliaque commune gauche "
                "écrasée par l'artère droite favorise les thromboses à gauche",
                "Anévrismes iliaques, souvent associés à un anévrisme de l'aorte "
                "abdominale",
                "Artériopathie : sténoses traitées par angioplastie ou pontage "
                "aorto-bi-iliaque ou aorto-bifémoral",
            ],
        },
        fact=(
            "La bifurcation aortique se projette à peu près sur la ligne qui relie "
            "les sommets des crêtes iliaques (L4)."
        ),
    ),
    "F": StructureText(
        name="Artère fémorale",
        old_names=[
            "en clinique : artère fémorale commune (au-dessus de la fémorale "
            "profonde) et fémorale superficielle (au-dessous)"
        ],
        kind="Artère musculaire (distributrice)",
        region="Cuisse",
        count="2 (droite et gauche)",
        description=(
            "Principale artère du membre inférieur, suite de l'artère iliaque externe "
            "sous le ligament inguinal. Elle devient l'artère poplitée en traversant "
            "le hiatus du muscle grand adducteur."
        ),
        sections={
            "course": [
                "Commence derrière le ligament inguinal, au point médio-inguinal "
                "(entre épine iliaque antéro-supérieure et symphyse pubienne)",
                "Traverse de haut en bas le trigone fémoral (triangle de Scarpa)",
                "Descend dans le canal des adducteurs (canal de Hunter), sous le "
                "muscle sartorius",
                "Traverse le hiatus du grand adducteur, à l'union des tiers moyen et "
                "inférieur de la cuisse, et devient l'artère poplitée",
            ],
            "branches": [
                "Branches superficielles : épigastrique superficielle, circonflexe "
                "iliaque superficielle, pudendales externes",
                "Artère profonde de la cuisse, environ 4 cm sous le ligament inguinal, "
                "avec les artères circonflexes fémorales et les perforantes",
                "Artère descendante du genou",
            ],
            "relations": [
                "Dans le trigone fémoral, de dehors en dedans : nerf fémoral, artère "
                "fémorale, veine fémorale, puis canal fémoral",
                "Trigone fémoral : ligament inguinal en haut, sartorius en dehors, "
                "long adducteur en dedans",
                "Dans le canal des adducteurs : avec la veine fémorale et le nerf "
                "saphène",
            ],
            "clinical": [
                "Pouls fémoral au point médio-inguinal, juste sous le ligament "
                "inguinal",
                "Voie d'abord artérielle classique des cathétérismes (coronarographie, "
                "angioplastie) ; la veine, médiale, sert à l'abord veineux",
                "Artériopathie oblitérante des membres inférieurs : sténoses "
                "fréquentes dans le canal des adducteurs, claudication intermittente",
                "Hernie fémorale : dans le canal fémoral, en dedans de la veine "
                "fémorale",
            ],
        },
        fact=(
            "L'artère circonflexe fémorale médiale, issue de l'artère profonde de la "
            "cuisse, irrigue surtout la tête du fémur : une fracture du col peut la "
            "léser et entraîner une nécrose."
        ),
    ),
    "G": StructureText(
        name="Artère poplitée",
        kind="Artère musculaire (distributrice)",
        region="Genou, fosse poplitée (vue ici par transparence)",
        count="2 (droite et gauche)",
        description=(
            "Suite de l'artère fémorale derrière le genou, c'est l'élément le plus "
            "profond de la fosse poplitée. Elle se divise sous le genou en artère "
            "tibiale antérieure et tronc tibio-fibulaire."
        ),
        sections={
            "course": [
                "Commence au hiatus du grand adducteur",
                "Traverse la fosse poplitée en arrière du fémur puis de la capsule du "
                "genou",
                "Se termine au bord inférieur du muscle poplité, sous l'arcade du "
                "muscle soléaire",
            ],
            "branches": [
                "Artères géniculaires (supérieures, moyenne, inférieures) : réseau "
                "anastomotique du genou",
                "Artères surales pour les muscles gastrocnémiens",
                "Artère tibiale antérieure : loge antérieure de la jambe, puis artère "
                "dorsale du pied (ancienne pédieuse)",
                "Tronc tibio-fibulaire : artère tibiale postérieure et artère fibulaire "
                "(ancienne péronière)",
            ],
            "relations": [
                "De la profondeur vers la superficie : artère, veine poplitée, nerf "
                "tibial",
                "En avant : face poplitée du fémur et capsule du genou",
                "Fosse poplitée en losange : biceps fémoral en haut et en dehors, "
                "semi-membraneux et semi-tendineux en haut et en dedans, gastrocnémiens "
                "en bas",
            ],
            "clinical": [
                "Pouls poplité : difficile à sentir, genou un peu fléchi, en appuyant "
                "profondément au fond de la fosse",
                "Lésion artérielle à rechercher systématiquement après une luxation "
                "du genou",
                "Anévrisme poplité : le plus fréquent des anévrismes périphériques, "
                "souvent bilatéral",
            ],
        },
        fact=(
            "Ses branches donnent deux pouls du pied : dorsal du pied, entre les "
            "tendons des longs extenseurs de l'hallux et des orteils, et tibial "
            "postérieur, derrière la malléole médiale."
        ),
        old_names=["tronc tibio-péronier (pour le tronc tibio-fibulaire)"],
    ),
    "V": StructureText(
        name="Grande veine saphène",
        old_names=["veine saphène interne"],
        kind="Veine superficielle",
        region="Membre inférieur, face médiale, tissu sous-cutané",
        count="2 (droite et gauche)",
        description=(
            "Plus longue veine du corps, du pied à l'aine. Veine superficielle de la "
            "face médiale du membre inférieur, elle se jette dans la veine fémorale "
            "sous le ligament inguinal."
        ),
        sections={
            "course": [
                "Naît de l'extrémité médiale de l'arcade veineuse dorsale du pied",
                "Passe en avant de la malléole médiale, où sa position est constante",
                "Monte à la face médiale de la jambe, passe en arrière des condyles "
                "médiaux au genou, puis à la face antéro-médiale de la cuisse",
                "Traverse le hiatus saphène environ 3 à 4 cm sous et en dehors du "
                "tubercule pubien et se jette dans la veine fémorale (crosse)",
            ],
            "territory": [
                "Réseau superficiel du pied et des faces médiales de la jambe et de la "
                "cuisse",
                "Près de la crosse : veines épigastrique superficielle, circonflexe "
                "iliaque superficielle et pudendales externes",
                "Reliée aux veines profondes par des veines perforantes munies de "
                "valvules",
            ],
            "relations": [
                "Accompagnée à la jambe par le nerf saphène, qui peut être lésé lors "
                "de son prélèvement",
                "Dans le tissu sous-cutané, au-dessus du fascia profond (fascia lata à "
                "la cuisse)",
                "Nombreuses valvules qui dirigent le sang vers le haut et vers la "
                "profondeur",
            ],
            "clinical": [
                "Varices : insuffisance des valvules, souvent à la jonction "
                "saphéno-fémorale",
                "Abord veineux d'urgence en avant de la malléole médiale",
                "Greffon de pontage coronaire ou des membres, retourné ou dévalvulé à "
                "cause des valvules",
                "La thrombose veineuse profonde touche les veines profondes ; une "
                "thrombose de la saphène est dite superficielle",
            ],
        },
        fact=(
            "Devant la malléole médiale, on la voit et on la sent chez presque tout "
            "le monde : c'est un repère fiable même en urgence."
        ),
    ),
}
