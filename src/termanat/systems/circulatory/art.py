"""ASCII art of the heart and main vessels (anterior view).

Front view in anatomical position: the left of the screen is the subject's
*right* side. The heart lies slightly to the right of the screen centre with its
apex pointing to the screen's right; the venae cavae are on the screen's left of
the aorta. The faint body silhouette is decoration (``.`` in the mask).

Mask keys: H heart, A ascending aorta + aortic arch (with the brachiocephalic
trunk), P pulmonary trunk, S superior vena cava, I inferior vena cava,
C common carotid, J internal jugular, U subclavian, X brachial, R radial,
N ulnar, B abdominal aorta, T coeliac trunk, K renal artery, L common iliac,
F femoral, G popliteal, V great saphenous vein.
"""

from __future__ import annotations

_ART = r"""
                .-'''''-.
               /         \
               |         |
               \         /
                '.     .'
                |: | | :|
                |: | | :|
          __..--': | | :'--..__
     .-'___________| |___________'-.
    /  /         ||| ||          \  \
   |  |   _      ||.---.      _   |  |
   |  |  | |     |||______   | |  |  |
   |  |  | |     ||| |       | |  |  |
   |  |  | |    .-''''''-.   | |  |  |
   |  |  | |   /  \      '.  | |  |  |
   |  |  | |   |   \       \ | |  |  |
   |  |  | |   \    \      | | |  |  |
   |  |  | |    '.   \     / | |  |  |
   | / \ | |      '-. \   .' | | / \ |
   | | | | |     || '-.\.-'  | | | | |
   | | | | |     || ||=<     | | | | |
   | | | | |     || ||       | | | | |
   | | | | |  ---||-||----   | | | | |
   | | | | |     || ||       | | | | |
   | | | | |       /  \      | | | | |
   \     / |      /    \     | \     /
    |   |  |     /      \    |  |   |
    \___/  |    /   .    |   |  \___/
           |   | : / \ : |   |
           |   | : | | : |   |
           |   \ : | | : /   |
           |    | :| |: |    |
           |    | :| |: |    |
           |    | :| |: |    |
           |   / \:| |:/ \   |
           |      :| |:      |
         (_________) (_________)
"""

_MASK = r"""
                .........
               .         .
               .         .
               .         .
                ..     ..
                .J C C J.
                .J C C J.
          .......J C C J.......
     ...UUUUUUUUUUUA CUUUUUUUUUUU...
    .  X         SSA CU          X  .
   .  X   .      SSAAAAA      .   X  .
   .  X  . .     SSAPPPPPP   . .  X  .
   .  X  . .     SSA P       . .  X  .
   .  X  . .    HHHHHHHHHH   . .  X  .
   .  X  . .   H  H      HH  . .  X  .
   .  X  . .   H   H       H . .  X  .
   .  X  . .   H    H      H . .  X  .
   .  X  . .    HH   H     H . .  X  .
   . R N . .      HHH H   HH . . N R .
   . R N . .     II HHHHHHH  . . N R .
   . R N . .     II BBTT     . . N R .
   . R N . .     II BB       . . N R .
   . R N . .  KKKIIKBBKKKK   . . N R .
   . R N . .     II BB       . . N R .
   . R N . .       L  L      . . N R .
   .     . .      L    L     . .     .
    .   .  .     L      L    .  .   .
    .....  .    F   .    F   .  .....
           .   F V . . V F   .
           .   F V . . V F   .
           .   F V . . V F   .
           .    F V. .V F    .
           .    G V. .V G    .
           .    G V. .V G    .
           .   G GV. .VG G   .
           .      V. .V      .
         ........... ...........
"""

ART: list[str] = _ART.split("\n")[1:-1]
MASK: list[str] = _MASK.split("\n")[1:-1]
