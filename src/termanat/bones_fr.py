"""Textes en français (nomenclature anatomique internationale francisée,
celle utilisée en PASS / L.AS). Les anciens noms sont indiqués à titre de
correspondance."""

from __future__ import annotations

from .bones import BoneText

TEXTS: dict[str, BoneText] = {
    "S": BoneText(
        name="Crâne",
        region="Tête",
        count="21 os soudés : 8 os du neurocrâne + 13 os de la face (mandibule à part)",
        kind="Os plats pour la voûte, os irréguliers pour la base et la face",
        description=(
            "Le neurocrâne (boîte crânienne) protège l'encéphale ; le viscérocrâne "
            "(massif facial) porte les organes des sens et le début des voies "
            "aérodigestives. Neurocrâne : frontal, 2 pariétaux, 2 temporaux, "
            "occipital, sphénoïde, ethmoïde. Face : 2 maxillaires, 2 zygomatiques, "
            "2 nasaux, 2 lacrymaux, 2 palatins, 2 cornets nasaux inférieurs, vomer."
        ),
        landmarks=[
            "Sutures coronale (frontal / pariétaux), sagittale (entre les pariétaux) "
            "et lambdoïde (pariétaux / occipital) ; bregma et lambda à leurs jonctions",
            "Ptérion : jonction frontal, pariétal, temporal et grande aile du sphénoïde",
            "Foramen magnum et condyles occipitaux (occipital)",
            "Processus mastoïde et méat acoustique externe (temporal)",
            "Selle turcique du sphénoïde, qui loge l'hypophyse",
            "Lame criblée de l'ethmoïde, traversée par les nerfs olfactifs",
            "Orbites, cavité nasale, fosses crâniennes antérieure, moyenne et postérieure",
        ],
        joints=[
            "Sutures : articulations fibreuses (synarthroses), quasi immobiles",
            "Articulation temporo-mandibulaire (ATM) avec la mandibule",
            "Articulation atlanto-occipitale avec l'atlas (C1)",
        ],
        clinical=[
            "Le ptérion est mince et recouvre l'artère méningée moyenne : un choc "
            "à ce niveau peut donner un hématome extradural",
            "Fracture de la base du crâne : ecchymose périorbitaire « en lunettes », "
            "ecchymose rétro-auriculaire (signe de Battle), rhinorrhée ou otorrhée de "
            "liquide cérébrospinal",
            "Fontanelles du nouveau-né : postérieure (lambda) fermée vers 2 mois, "
            "antérieure (bregma) vers 18-24 mois",
        ],
        fact=(
            "Les fontanelles laissent le crâne se déformer lors de l'accouchement "
            "et le cerveau grandir pendant les premiers mois."
        ),
    ),
    "M": BoneText(
        name="Mandibule",
        old_names=["maxillaire inférieur"],
        region="Tête",
        count="1 (os impair et médian)",
        kind="Os irrégulier",
        description=(
            "Os de la mâchoire inférieure, en forme de fer à cheval. Elle porte les "
            "dents inférieures et c'est le seul os du crâne mobile par une "
            "articulation synoviale (hors osselets de l'oreille)."
        ),
        landmarks=[
            "Corps (avec la partie alvéolaire) et deux branches (rami) réunis à l'angle "
            "de la mandibule",
            "Processus condylaire (tête et col de la mandibule) en arrière, processus "
            "coronoïde en avant, séparés par l'incisure mandibulaire",
            "Symphyse et protubérance mentonnières",
            "Foramen mentonnier (nerf et vaisseaux mentonniers)",
            "Foramen mandibulaire, face médiale de la branche (nerf alvéolaire inférieur)",
        ],
        joints=[
            "Articulation temporo-mandibulaire (ATM) : synoviale bicondylienne avec un "
            "disque articulaire ; la tête de la mandibule s'articule avec la fosse "
            "mandibulaire du temporal",
            "Articulations dento-alvéolaires (gomphoses) avec les dents",
        ],
        clinical=[
            "Muscles masticateurs : masséter (face latérale de la branche), temporal "
            "(processus coronoïde), ptérygoïdiens médial et latéral",
            "Fractures souvent doubles, car la mandibule forme un anneau avec la base "
            "du crâne : chercher une 2e fracture (souvent condylienne)",
            "Luxation de l'ATM : la tête passe en avant du tubercule articulaire, "
            "bouche bloquée ouverte",
            "Anesthésie dentaire du nerf alvéolaire inférieur au foramen mandibulaire",
        ],
        fact="C'est l'os le plus volumineux et le plus solide de la face.",
    ),
    "C": BoneText(
        name="Vertèbres cervicales",
        region="Cou",
        count="7 (C1 à C7)",
        kind="Os irréguliers",
        description=(
            "Vertèbres du cou, petites et très mobiles. Elles forment la lordose "
            "cervicale, portent la tête et protègent la moelle spinale cervicale."
        ),
        landmarks=[
            "Foramen transversaire dans chaque processus transverse : passage de "
            "l'artère vertébrale (de C6 à C1)",
            "Processus épineux bifides de C3 à C6 ; uncus (processus unciformes) "
            "sur les bords du plateau supérieur",
            "C1, atlas : pas de corps ni de processus épineux, deux masses latérales "
            "réunies par les arcs antérieur et postérieur",
            "C2, axis : dent de l'axis (processus odontoïde), pivot de la rotation",
            "C7, vertèbre proéminente : long processus épineux non bifide, palpable "
            "à la base du cou",
        ],
        joints=[
            "Atlanto-occipitale (condyles occipitaux / masses latérales de C1) : "
            "flexion-extension, le « oui »",
            "Atlanto-axiale (dent de C2 / arc antérieur de C1) : rotation, le « non »",
            "Pas de disque intervertébral entre occiput et C1 ni entre C1 et C2 ; "
            "disques à partir de C2-C3",
        ],
        clinical=[
            "Fracture de Jefferson : éclatement de l'atlas par compression axiale "
            "(plongeon en eau peu profonde)",
            "Fracture de la dent de l'axis ; fracture « du pendu » des isthmes de C2",
            "Entorses cervicales, traumatisme en « coup de fouet » ; névralgie "
            "cervico-brachiale par arthrose unco-vertébrale",
        ],
        fact=(
            "Presque tous les mammifères ont 7 vertèbres cervicales, la girafe "
            "comme la souris."
        ),
    ),
    "X": BoneText(
        name="Scapula",
        old_names=["omoplate"],
        region="Épaule (ceinture scapulaire)",
        count="2",
        kind="Os plat",
        description=(
            "Os plat triangulaire plaqué contre la face postérieure du thorax, entre "
            "la 2e et la 7e côte. De face, on ne voit que l'acromion, au sommet de "
            "l'épaule."
        ),
        landmarks=[
            "Épine de la scapula, qui se termine latéralement par l'acromion",
            "Fosses supra-épineuse et infra-épineuse (face postérieure), fosse "
            "subscapulaire (face antérieure, costale)",
            "Cavité glénoïdale, bordée par le labrum glénoïdal",
            "Processus coracoïde : insertion du petit pectoral, du coraco-brachial "
            "et du chef court du biceps",
            "Incisure scapulaire (nerf suprascapulaire) ; angle inférieur en regard "
            "de T7",
        ],
        joints=[
            "Gléno-humérale (scapulo-humérale) : sphéroïde, l'articulation la plus "
            "mobile du corps",
            "Acromio-claviculaire",
            "Scapulo-thoracique : espace de glissement, sans surfaces articulaires vraies",
        ],
        clinical=[
            "Coiffe des rotateurs : supra-épineux, infra-épineux, petit rond, "
            "subscapulaire",
            "Luxation antérieure de l'épaule (antéro-médiale, anciennement "
            "« antéro-interne », la plus fréquente) : vérifier le nerf axillaire "
            "(sensibilité du moignon de l'épaule)",
            "Scapula alata (décollement du bord médial) : paralysie du dentelé "
            "antérieur par atteinte du nerf thoracique long",
        ],
        fact=(
            "La cavité glénoïdale est petite et peu profonde : l'épaule gagne en "
            "mobilité ce qu'elle perd en stabilité."
        ),
    ),
    "L": BoneText(
        name="Clavicule",
        region="Épaule (ceinture scapulaire)",
        count="2",
        kind="Os long (atypique : pas de cavité médullaire nette)",
        description=(
            "Os en forme de S italique, horizontal, entre le sternum et l'acromion. "
            "Il maintient le membre supérieur écarté du thorax : c'est le seul lien "
            "osseux entre le membre supérieur et le tronc."
        ),
        landmarks=[
            "Extrémité sternale (médiale) et extrémité acromiale (latérale), aplatie",
            "Deux courbures : convexe en avant sur ses 2/3 médiaux, concave en avant "
            "sur son 1/3 latéral",
            "Tubercule conoïde et ligne trapézoïde (ligaments coraco-claviculaires)",
            "Sillon du muscle subclavier à la face inférieure",
        ],
        joints=[
            "Sterno-claviculaire : en selle, avec un disque articulaire",
            "Acromio-claviculaire : plane",
        ],
        clinical=[
            "Fracture très fréquente (chute sur le moignon de l'épaule ou la main), "
            "surtout au tiers moyen",
            "Le fragment médial monte (sterno-cléido-mastoïdien), le fragment latéral "
            "descend sous le poids du membre",
            "Rapport en arrière avec les vaisseaux subclaviers et le plexus brachial",
            "Disjonction acromio-claviculaire : « touche de piano »",
        ],
        fact=(
            "Premier os à s'ossifier chez l'embryon (5e-6e semaine), son extrémité "
            "sternale est l'une des dernières à se souder, vers 25 ans."
        ),
    ),
    "T": BoneText(
        name="Sternum",
        region="Thorax",
        count="1 (os impair et médian)",
        kind="Os plat",
        description=(
            "Os plat de la paroi antérieure du thorax, en forme de glaive : "
            "manubrium (poignée), corps (lame) et processus xiphoïde (pointe)."
        ),
        landmarks=[
            "Incisure jugulaire au bord supérieur du manubrium ; incisures claviculaires",
            "Angle sternal (de Louis), jonction manubrium-corps : en regard du 2e "
            "cartilage costal et du disque T4-T5",
            "Incisures costales pour les cartilages des 7 premières côtes",
            "Processus xiphoïde, cartilagineux puis ossifié tardivement",
        ],
        joints=[
            "Sterno-claviculaires",
            "Sterno-costales avec les cartilages costaux 1 à 7 (la 1re est une "
            "synchondrose)",
            "Manubrio-sternale (symphyse)",
        ],
        clinical=[
            "L'angle sternal sert à compter les côtes : la 2e côte s'y attache. "
            "Il marque aussi le niveau de la bifurcation trachéale et de la crosse "
            "de l'aorte",
            "Ponction sternale pour le myélogramme (moelle osseuse)",
            "Sternotomie médiane : voie d'abord de la chirurgie cardiaque",
            "Massage cardiaque : compression de la moitié inférieure du sternum",
        ],
        fact=(
            "Chez l'adulte, le sternum garde une moelle rouge qui produit des "
            "cellules sanguines toute la vie."
        ),
    ),
    "R": BoneText(
        name="Côtes",
        region="Thorax",
        count="24 (12 paires)",
        kind="Os plats (os longs aplatis et courbés)",
        description=(
            "Arcs osseux qui forment la cage thoracique avec les vertèbres thoraciques "
            "et le sternum. Elles protègent cœur et poumons et participent à la "
            "ventilation."
        ),
        landmarks=[
            "Vraies côtes (1 à 7) : reliées directement au sternum par leur cartilage",
            "Fausses côtes (8 à 10 au sens strict, 8 à 12 au sens large) : leur "
            "cartilage rejoint celui de la côte du dessus et forme le rebord costal",
            "Côtes flottantes (11 et 12) : libres en avant",
            "Côte type : tête (2 facettes, une seule pour les côtes 1, 11 et 12), col, "
            "tubercule, angle, corps",
            "Sillon costal au bord inférieur de la face interne : paquet "
            "vasculo-nerveux intercostal (veine, artère, nerf de haut en bas)",
            "1re côte : courte, large et plate, tubercule du scalène antérieur entre "
            "les sillons de la veine et de l'artère subclavières",
        ],
        joints=[
            "Costo-vertébrales : la tête s'articule avec les corps de deux vertèbres "
            "(même niveau et au-dessus), sauf les côtes 1, 11 et 12 (une seule)",
            "Costo-transversaires : le tubercule s'articule avec le processus transverse "
            "(absentes pour les côtes 11 et 12)",
            "Sterno-costales et chondro-costales en avant",
        ],
        clinical=[
            "Ponction ou drainage pleural au bord supérieur de la côte inférieure, "
            "pour éviter le paquet intercostal",
            "Volet costal : plusieurs côtes cassées en deux endroits, le segment "
            "bouge à l'envers lors de la respiration (respiration paradoxale)",
            "Côte cervicale surnuméraire : syndrome du défilé thoraco-brachial",
        ],
        fact=(
            "Hommes et femmes ont le même nombre de côtes : 12 paires, contrairement "
            "à une vieille croyance."
        ),
    ),
    "H": BoneText(
        name="Humérus",
        region="Bras",
        count="2",
        kind="Os long",
        description=(
            "Os unique du bras, de l'épaule au coude. Son extrémité distale "
            "aplatie s'appelle la palette humérale."
        ),
        old_names=["trochiter (tubercule majeur)", "trochin (tubercule mineur)",
                   "épitrochlée (épicondyle médial)", "épicondyle (épicondyle latéral)",
                   "condyle huméral (capitulum)"],
        landmarks=[
            "Tête humérale (regarde en haut, en dedans et en arrière), col anatomique",
            "Tubercule majeur (supra-épineux, infra-épineux, petit rond) et tubercule "
            "mineur (subscapulaire)",
            "Sillon intertuberculaire : tendon du chef long du biceps",
            "Col chirurgical, sous les tubercules",
            "Tubérosité deltoïdienne ; sillon du nerf radial à la face postérieure",
            "Capitulum (s'articule avec le radius) et trochlée (avec l'ulna)",
            "Épicondyles latéral et médial ; fosses olécrânienne (en arrière), "
            "coronoïdienne et radiale (en avant)",
        ],
        joints=[
            "Gléno-humérale (épaule) : sphéroïde",
            "Coude : huméro-ulnaire (ginglyme / trochléenne) et huméro-radiale",
        ],
        clinical=[
            "Fracture du col chirurgical (sujet âgé) : risque pour le nerf axillaire",
            "Fracture de la diaphyse : le nerf radial peut être lésé dans son sillon "
            "(main tombante, « en col de cygne »)",
            "Fracture supra-condylienne de l'enfant : risque pour l'artère brachiale "
            "et le nerf médian",
            "Nerf ulnaire en arrière de l'épicondyle médial",
        ],
        fact=(
            "La décharge « électrique » ressentie quand on se cogne le coude vient "
            "du nerf ulnaire, comprimé contre l'épicondyle médial de l'humérus."
        ),
    ),
    "D": BoneText(
        name="Radius",
        region="Avant-bras",
        count="2",
        kind="Os long",
        description=(
            "Os latéral de l'avant-bras (côté pouce en position anatomique). Il "
            "tourne autour de l'ulna pour la pronation et la supination, et porte "
            "le carpe."
        ),
        landmarks=[
            "Tête radiale cylindrique : fovéa articulaire en haut, circonférence "
            "articulaire autour",
            "Col du radius ; tubérosité radiale (insertion du biceps brachial)",
            "Bord interosseux (membrane interosseuse avec l'ulna)",
            "Processus styloïde radial, plus bas d'environ 1 cm que celui de l'ulna",
            "Incisure ulnaire ; surface articulaire carpienne (scaphoïde et lunatum)",
            "Tubercule dorsal (de Lister)",
        ],
        joints=[
            "Huméro-radiale (capitulum)",
            "Radio-ulnaires proximale et distale, deux trochoïdes : en haut, la tête "
            "tourne dans l'anneau formé par l'incisure radiale de l'ulna et le "
            "ligament annulaire",
            "Radio-carpienne (poignet) : ellipsoïde",
        ],
        clinical=[
            "Fracture de Pouteau-Colles : extrémité distale, déplacement postérieur "
            "« en dos de fourchette », chute sur la paume du sujet âgé ostéoporotique",
            "Fracture de Goyrand-Smith : même niveau, déplacement antérieur",
            "Pronation douloureuse du jeune enfant : traction sur le bras, la tête "
            "s'échappe partiellement du ligament annulaire, qui s'interpose dans "
            "l'articulation",
            "Fracture de Galeazzi : diaphyse radiale + luxation radio-ulnaire distale",
        ],
        fact="Le pouls radial se prend en avant de l'extrémité distale du radius.",
    ),
    "U": BoneText(
        name="Ulna",
        old_names=["cubitus"],
        region="Avant-bras",
        count="2",
        kind="Os long",
        description=(
            "Os médial de l'avant-bras (côté auriculaire). Il est fixe pendant la "
            "pronation-supination et forme l'essentiel du coude."
        ),
        landmarks=[
            "Olécrâne (pointe du coude, insertion du triceps) et processus coronoïde",
            "Incisure trochléaire (avec la trochlée humérale)",
            "Incisure radiale (avec la tête du radius)",
            "Tubérosité ulnaire (insertion du brachial)",
            "Bord interosseux ; tête de l'ulna et processus styloïde ulnaire en bas",
        ],
        joints=[
            "Huméro-ulnaire : ginglyme (flexion-extension du coude)",
            "Radio-ulnaires proximale et distale",
            "Pas de contact direct avec le carpe : le complexe fibro-cartilagineux "
            "triangulaire s'interpose",
        ],
        clinical=[
            "Fracture de l'olécrâne : le triceps écarte les fragments",
            "Fracture de Monteggia : diaphyse ulnaire + luxation de la tête radiale",
            "Le nerf ulnaire passe en arrière de l'épicondyle médial, juste à côté "
            "de l'olécrâne",
        ],
        fact="La pointe du coude sur laquelle on s'appuie est l'olécrâne de l'ulna.",
    ),
    "A": BoneText(
        name="Os de la main",
        region="Main",
        count="54 (27 par main) : 8 os du carpe, 5 métacarpiens, 14 phalanges",
        kind="Os courts (carpe), os longs (métacarpiens et phalanges)",
        description=(
            "Carpe (poignet), métacarpe (paume) et phalanges (doigts). Chaque doigt "
            "a 3 phalanges (proximale, moyenne, distale), sauf le pouce qui en a 2."
        ),
        old_names=["semi-lunaire (lunatum)", "pyramidal (triquetrum)",
                   "grand os (capitatum)", "os crochu (hamatum)",
                   "phalange, phalangine, phalangette (phalanges proximale, "
                   "moyenne, distale)"],
        landmarks=[
            "Rangée proximale du carpe, de latéral à médial : scaphoïde, lunatum, "
            "triquetrum, pisiforme",
            "Rangée distale : trapèze, trapézoïde, capitatum, hamatum",
            "Canal ulnaire (de Guyon) : entre le pisiforme (en dedans) et l'hamulus de "
            "l'hamatum (en dehors) ; nerf et artère ulnaires",
            "Canal carpien : sillon carpien fermé par le rétinaculum des fléchisseurs ; "
            "contient le nerf médian et 9 tendons fléchisseurs",
            "Tabatière anatomique : le scaphoïde est palpable dans son fond",
        ],
        joints=[
            "Radio-carpienne et médio-carpienne (poignet)",
            "Carpo-métacarpiennes, dont la trapézo-métacarpienne du pouce, en selle, "
            "qui permet l'opposition",
            "Métacarpo-phalangiennes et interphalangiennes proximales et distales",
        ],
        clinical=[
            "Fracture du scaphoïde (la plus fréquente du carpe) : douleur de la "
            "tabatière anatomique, risque de pseudarthrose et de nécrose du pôle "
            "proximal (vascularisation rétrograde)",
            "Syndrome du canal carpien : compression du nerf médian",
            "Fracture du col du 5e métacarpien : « fracture du boxeur »",
        ],
        fact=(
            "Les deux mains et poignets réunis contiennent plus d'un quart des os du "
            "corps."
        ),
    ),
    "V": BoneText(
        name="Vertèbres lombaires",
        old_names=["apophyses (processus)", "apophyses costiformes (processus "
                   "costiformes)"],
        region="Bas du dos",
        count="5 (L1 à L5)",
        kind="Os irréguliers",
        description=(
            "Vertèbres du bas du dos, les plus massives car elles portent le poids "
            "du tronc. Elles forment la lordose lombaire. (Les 12 vertèbres "
            "thoraciques sont cachées par le sternum sur cette vue de face.)"
        ),
        landmarks=[
            "Corps volumineux, réniforme",
            "Pas de foramen transversaire ni de fossettes costales",
            "Processus costiformes (« transverses »), vestiges de côtes ; processus "
            "mamillaires et accessoires",
            "Processus épineux rectangulaire et horizontal",
            "Processus articulaires orientés dans le plan sagittal : peu de rotation",
        ],
        joints=[
            "Disques intervertébraux (symphyses) entre les corps",
            "Articulations zygapophysaires entre processus articulaires",
            "Lombo-sacrale (L5-S1)",
        ],
        clinical=[
            "La moelle spinale s'arrête vers L1-L2 chez l'adulte : ponction lombaire "
            "en L3-L4 ou L4-L5 (ligne de Tuffier, entre les crêtes iliaques, passe "
            "par L4 ou l'espace L4-L5)",
            "Hernie discale surtout en L4-L5 et L5-S1 : sciatique L5 ou S1",
            "Spondylolisthésis : glissement de L5 sur S1, souvent par lyse isthmique",
        ],
        fact=(
            "La lombalgie est l'une des premières causes d'arrêt de travail et de "
            "consultation en médecine générale."
        ),
    ),
    "Y": BoneText(
        name="Sacrum et coccyx",
        region="Bassin",
        count="1 + 1 (5 vertèbres sacrales et 3 à 5 coccygiennes soudées)",
        kind="Os irréguliers",
        description=(
            "Le sacrum est un os triangulaire fait de 5 vertèbres soudées, coincé "
            "entre les deux os coxaux. Le coccyx, vestige de la queue, le prolonge "
            "vers le bas."
        ),
        landmarks=[
            "Base du sacrum (plateau de S1) avec le promontoire, ailes du sacrum",
            "Face pelvienne : 4 paires de foramens sacraux antérieurs",
            "Face dorsale : crête sacrale médiane, foramens sacraux postérieurs",
            "Surfaces auriculaires latérales (articulation sacro-iliaque)",
            "Canal sacral se terminant par le hiatus sacral",
        ],
        joints=[
            "Lombo-sacrale (L5-S1)",
            "Sacro-iliaques (synoviales, très peu mobiles)",
            "Sacro-coccygienne",
        ],
        clinical=[
            "Promontoire : repère obstétrical (diamètre promonto-rétro-pubien du "
            "détroit supérieur)",
            "Hiatus sacral : voie de l'anesthésie péridurale caudale",
            "Coccygodynie (douleur du coccyx) après une chute sur les fesses",
        ],
        fact="Le coccyx est le vestige de la queue de nos ancêtres.",
    ),
    "P": BoneText(
        name="Os coxal",
        old_names=["os iliaque", "échancrures sciatiques (incisures ischiatiques)"],
        region="Bassin (ceinture pelvienne)",
        count="2",
        kind="Os plat (et irrégulier)",
        description=(
            "Chaque os coxal réunit trois os, l'ilium, l'ischium et le pubis, soudés "
            "au niveau de l'acétabulum à l'adolescence (cartilage en Y). Avec le "
            "sacrum et le coccyx, les deux os coxaux forment le bassin (pelvis)."
        ),
        landmarks=[
            "Crête iliaque ; épines iliaques antéro-supérieure (EIAS : sartorius, "
            "ligament inguinal) et antéro-inférieure (droit fémoral)",
            "Épine iliaque postéro-supérieure (fossettes lombaires) ; fosse iliaque",
            "Acétabulum : surface semi-lunaire, fosse et incisure acétabulaires",
            "Foramen obturé, fermé par la membrane obturatrice",
            "Tubérosité ischiatique (ischio-jambiers, appui en position assise) ; "
            "épine ischiatique ; grande et petite incisures ischiatiques",
            "Tubercule pubien, surface symphysaire ; ligne arquée (détroit supérieur)",
        ],
        joints=[
            "Coxo-fémorale (hanche) : sphéroïde",
            "Sacro-iliaque",
            "Symphyse pubienne (fibrocartilage)",
        ],
        clinical=[
            "Biopsie ostéo-médullaire à la crête iliaque postérieure",
            "Injection intramusculaire dans le quadrant supéro-latéral de la fesse, "
            "pour éviter le nerf sciatique",
            "Fracture du bassin : risque hémorragique majeur",
            "Bassin féminin : détroit supérieur plus large et arrondi, angle "
            "sous-pubien plus ouvert",
        ],
        fact=(
            "On distingue souvent un squelette d'homme de celui d'une femme par le "
            "seul bassin."
        ),
    ),
    "F": BoneText(
        name="Fémur",
        region="Cuisse",
        count="2",
        kind="Os long",
        description=(
            "Os unique de la cuisse, de la hanche au genou. C'est l'os le plus long "
            "et le plus solide du corps."
        ),
        landmarks=[
            "Tête fémorale (fovéa de la tête : ligament de la tête fémorale), col",
            "Angle cervico-diaphysaire d'environ 125-130° ; antéversion du col "
            "d'environ 15°",
            "Grand trochanter (moyen et petit fessiers), petit trochanter (ilio-psoas)",
            "Ligne intertrochantérique en avant, crête intertrochantérique en arrière",
            "Ligne âpre à la face postérieure de la diaphyse (adducteurs, vastes)",
            "Condyles médial et latéral, fosse intercondylaire, épicondyles, tubercule "
            "de l'adducteur, surface patellaire (trochlée)",
        ],
        joints=[
            "Coxo-fémorale (hanche)",
            "Fémoro-tibiale et fémoro-patellaire (genou)",
        ],
        clinical=[
            "Fracture du col du fémur du sujet âgé : membre raccourci et en rotation "
            "latérale ; risque de nécrose de la tête (artères circonflexes)",
            "Fracture de la diaphyse : saignement important (1 L ou plus), choc possible",
            "Coxa vara / coxa valga : angle cervico-diaphysaire diminué ou augmenté",
        ],
        fact="Il mesure environ un quart de la taille d'une personne.",
    ),
    "K": BoneText(
        name="Patella",
        old_names=["rotule"],
        region="Genou",
        count="2",
        kind="Os sésamoïde",
        description=(
            "Os triangulaire inclus dans le tendon du quadriceps, en avant du genou. "
            "Il protège l'articulation et augmente le bras de levier du quadriceps."
        ),
        landmarks=[
            "Base en haut (tendon quadricipital), apex en bas (ligament patellaire)",
            "Face antérieure palpable sous la peau",
            "Face articulaire postérieure : facettes latérale (la plus grande) et "
            "médiale, séparées par une crête",
        ],
        joints=["Fémoro-patellaire, avec la surface patellaire (trochlée) du fémur"],
        clinical=[
            "Luxation latérale de la patella, surtout chez l'adolescente",
            "Fracture par chute sur le genou ; ne pas confondre avec une patella "
            "bipartita (variante normale)",
            "Réflexe patellaire (rotulien) : percussion du ligament patellaire, "
            "racines L3-L4 (L4 surtout)",
        ],
        fact="C'est le plus grand os sésamoïde du corps (un os qui pousse dans un tendon).",
    ),
    "B": BoneText(
        name="Tibia",
        region="Jambe",
        count="2",
        kind="Os long",
        description=(
            "Os médial et volumineux de la jambe. C'est lui qui porte le poids du "
            "corps du genou à la cheville."
        ),
        landmarks=[
            "Plateau tibial : condyles médial et latéral",
            "Éminence intercondylaire (épines tibiales) ; aires intercondylaires où "
            "s'insèrent les ligaments croisés",
            "Tubérosité tibiale : insertion du ligament patellaire",
            "Bord antérieur (crête tibiale) et face médiale, sous-cutanés",
            "Ligne du muscle soléaire à la face postérieure",
            "Malléole médiale ; incisure fibulaire en bas",
        ],
        joints=[
            "Fémoro-tibiale (genou)",
            "Tibio-fibulaires proximale (synoviale) et distale (syndesmose)",
            "Talo-crurale (cheville) avec le talus",
        ],
        clinical=[
            "Fractures fréquentes, souvent ouvertes car la face médiale est juste "
            "sous la peau",
            "Maladie d'Osgood-Schlatter : douleur de la tubérosité tibiale chez "
            "l'adolescent sportif",
            "Voie intra-osseuse d'urgence dans le tibia proximal",
        ],
        fact=(
            "En latin, tibia désigne à la fois l'os de la jambe et une flûte, "
            "instrument parfois taillé dans un os."
        ),
    ),
    "I": BoneText(
        name="Fibula",
        old_names=["péroné"],
        region="Jambe",
        count="2",
        kind="Os long",
        description=(
            "Os latéral et grêle de la jambe. Il porte peu de poids mais sert "
            "d'insertion à de nombreux muscles et stabilise la cheville."
        ),
        landmarks=[
            "Tête de la fibula avec son apex ; col de la fibula",
            "Diaphyse fine, triangulaire",
            "Malléole latérale : descend plus bas que la malléole médiale",
        ],
        joints=[
            "Tibio-fibulaires proximale et distale",
            "Talo-crurale (cheville) par la malléole latérale",
            "Ne s'articule pas avec le fémur : elle ne participe pas au genou",
        ],
        clinical=[
            "Le nerf fibulaire commun contourne le col de la fibula : une fracture "
            "ou un plâtre trop serré peut donner un pied tombant (steppage)",
            "Fractures de la cheville (malléolaires, bimalléolaires)",
            "Greffon de fibula vascularisée pour reconstruire la mandibule",
        ],
        fact=(
            "On peut en retirer un long segment sans gêner la marche, d'où son usage "
            "comme greffon."
        ),
    ),
    "O": BoneText(
        name="Os du pied",
        region="Pied",
        count="52 (26 par pied) : 7 os du tarse, 5 métatarsiens, 14 phalanges",
        kind="Os courts (tarse), os longs (métatarsiens et phalanges)",
        description=(
            "Tarse, métatarse et phalanges forment une voûte plantaire qui amortit "
            "et transmet le poids du corps au sol."
        ),
        old_names=["astragale (talus)", "calcanéum (calcanéus)",
                   "scaphoïde tarsien (naviculaire)",
                   "tibio-tarsienne (articulation talo-crurale)"],
        landmarks=[
            "Tarse postérieur : talus (aucune insertion musculaire) et calcanéus",
            "Tarse antérieur : naviculaire, cuboïde, cunéiformes médial, "
            "intermédiaire et latéral",
            "Trochlée du talus, prise dans la mortaise tibio-fibulaire",
            "Tubérosité du calcanéus (tendon calcanéen, d'Achille) ; sustentaculum tali",
            "Arches longitudinales médiale et latérale, arche transversale",
        ],
        joints=[
            "Talo-crurale (cheville) : flexion dorsale et plantaire",
            "Sous-talienne : inversion et éversion",
            "Transverse du tarse (Chopart) et tarso-métatarsienne (Lisfranc)",
            "Métatarso-phalangiennes et interphalangiennes",
        ],
        clinical=[
            "Entorse latérale de la cheville : ligament talo-fibulaire antérieur",
            "Fracture de la base du 5e métatarsien (arrachement par le court fibulaire)",
            "Fracture de fatigue des 2e-3e métatarsiens (fracture de Deutschländer, "
            "« fracture de la marche »)",
            "Hallux valgus",
        ],
        fact="Le calcanéus est le plus gros os du pied.",
    ),
}
