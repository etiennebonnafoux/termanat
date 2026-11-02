"""Reference data for the bones drawn on the skeleton."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Bone:
    key: str  # one-letter id used in the skeleton mask
    name: str
    latin: str
    region: str
    count: str  # how many of them an adult has
    description: str
    fact: str


BONES: list[Bone] = [
    Bone(
        "S", "Skull", "Cranium", "Head",
        "21 fused bones (8 cranial + 13 facial)",
        "Protects the brain and the sense organs. Its bones are joined by "
        "immovable joints called sutures.",
        "A newborn's skull has soft gaps, the fontanelles, that let it pass "
        "through the birth canal and let the brain grow.",
    ),
    Bone(
        "M", "Jaw bone", "Mandibula", "Head", "1",
        "The lower jaw. It holds the lower teeth and hinges on the skull at "
        "the temporomandibular joint.",
        "It is the only bone of the skull that can move, and the strongest "
        "bone of the face.",
    ),
    Bone(
        "C", "Cervical vertebrae", "Vertebrae cervicales", "Neck", "7",
        "The vertebrae of the neck. They support the head and let it nod and "
        "turn.",
        "The first two have names: C1 is the atlas (it carries the head) and "
        "C2 is the axis (the head turns around it). A giraffe also has 7!",
    ),
    Bone(
        "X", "Shoulder blade", "Scapula", "Shoulder", "2",
        "A flat triangular bone on the back of the ribcage. From the front, "
        "only its tip, the acromion, is visible at the top of the shoulder.",
        "Its shallow socket, the glenoid cavity, makes the shoulder the most "
        "mobile joint of the body, and the easiest to dislocate.",
    ),
    Bone(
        "L", "Collarbone", "Clavicula", "Shoulder", "2",
        "An S-shaped bone that links the sternum to the shoulder blade and "
        "holds the arm away from the body.",
        "It is the first bone to start hardening in the embryo, and one of "
        "the most commonly broken.",
    ),
    Bone(
        "T", "Breastbone", "Sternum", "Chest", "1",
        "A flat bone in the middle of the chest, made of three parts: the "
        "manubrium, the body and the xiphoid process (the pointy tip).",
        "Its red marrow keeps making blood cells throughout adult life.",
    ),
    Bone(
        "R", "Ribs", "Costae", "Chest", "24 (12 pairs)",
        "Curved bones forming the ribcage, which protects the heart and lungs "
        "and moves when you breathe.",
        "Pairs 1-7 are 'true' ribs (attached to the sternum), 8-10 are "
        "'false' ribs and 11-12 are 'floating' ribs.",
    ),
    Bone(
        "H", "Upper arm bone", "Humerus", "Arm", "2",
        "The long bone of the upper arm, from the shoulder to the elbow.",
        "Hitting your 'funny bone' actually means pinching the ulnar nerve "
        "where it runs along the humerus at the elbow.",
    ),
    Bone(
        "D", "Radius", "Radius", "Forearm", "2",
        "The forearm bone on the thumb side (the outer side when the palm "
        "faces forward).",
        "It rotates around the ulna to turn the palm up or down: "
        "supination and pronation.",
    ),
    Bone(
        "U", "Ulna", "Ulna", "Forearm", "2",
        "The forearm bone on the little-finger side (the inner side when the "
        "palm faces forward).",
        "The bony point of your elbow, the olecranon, is the top of the ulna.",
    ),
    Bone(
        "A", "Hand bones", "Ossa manus", "Hand", "54 (27 per hand)",
        "8 carpals form the wrist, 5 metacarpals form the palm and 14 "
        "phalanges form the fingers.",
        "Your two hands and wrists hold more than a quarter of all the bones "
        "in your body.",
    ),
    Bone(
        "V", "Lumbar vertebrae", "Vertebrae lumbales", "Lower back", "5",
        "The vertebrae of the lower back. They are the largest vertebrae "
        "because they carry most of the body's weight. (The 12 thoracic "
        "vertebrae are hidden behind the sternum in this view.)",
        "The lumbar region is where most back pain happens.",
    ),
    Bone(
        "Y", "Sacrum and coccyx", "Os sacrum et os coccygis", "Pelvis",
        "1 + 1 (made of 5 and 3-5 fused vertebrae)",
        "The sacrum is a triangle of fused vertebrae wedged between the hip "
        "bones. The coccyx, or tailbone, hangs below it.",
        "The coccyx is the remnant of a tail.",
    ),
    Bone(
        "P", "Hip bone", "Os coxae", "Pelvis", "2",
        "Each hip bone is three bones fused together: the ilium, the ischium "
        "and the pubis. With the sacrum they form the pelvis.",
        "A woman's pelvis is usually wider and rounder, to allow childbirth.",
    ),
    Bone(
        "F", "Thigh bone", "Femur", "Thigh", "2",
        "The bone of the thigh, from the hip to the knee. Its round head fits "
        "into a socket of the hip bone.",
        "It is the longest and strongest bone of the body, about a quarter "
        "of your height.",
    ),
    Bone(
        "K", "Kneecap", "Patella", "Knee", "2",
        "A small bone in front of the knee that protects the joint and gives "
        "leverage to the thigh muscles.",
        "It is the largest sesamoid bone: a bone that grows inside a tendon.",
    ),
    Bone(
        "B", "Shinbone", "Tibia", "Leg", "2",
        "The large inner bone of the lower leg. It carries the body's weight "
        "from the knee to the ankle.",
        "Its front edge lies right under the skin, which is why knocking your "
        "shin hurts so much.",
    ),
    Bone(
        "I", "Fibula", "Fibula", "Leg", "2",
        "The thin outer bone of the lower leg. It carries little weight but "
        "anchors muscles and stabilises the ankle.",
        "Surgeons sometimes take a piece of it to rebuild other bones, such "
        "as the jaw.",
    ),
    Bone(
        "O", "Foot bones", "Ossa pedis", "Foot", "52 (26 per foot)",
        "7 tarsals (including the heel bone), 5 metatarsals and 14 "
        "phalanges.",
        "The heel bone, the calcaneus, is the largest bone of the foot.",
    ),
]

BY_KEY: dict[str, Bone] = {b.key: b for b in BONES}
