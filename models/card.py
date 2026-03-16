from dataclasses import dataclass, field
from enum import Enum
from typing import Optional



class CardLayout(str, Enum):
    NORMAL = "normal"
    TRANSFORM = "transform"
    MODAL_DFC = "modal_dfc"
    ADVENTURE = "adventure"
    SPLIT = "split"
    FLIP = "flip"
    MELD = "meld"
    SAGA = "saga"
    OTHER = "other"


@dataclass
class CardFace:
    """face of a card - for both single and double faced cards"""
    name: str
    mana_cost:str
    type_line:str
    oracle_text:str
    flavor_text:str
    power: Optional[str] = None                                                 # None for non-creatures
    toughness: Optional[str] = None
    loyalty:Optional[str] = None                                                # None for planeswalkers
    defense: Optional[str] = None                                               # None for battles
    art_crop_url: Optional[str] = None                                          # scryfall art

@dataclass
class Card:
    scryfall_id:str
    name: str
    layout:CardLayout
    faces: list[CardFace] = field(default_factory=list)
    cmc:float = 0.0
    color_identity: list[str] = field(default_factory=list)

    @property
    def is_multifaced(self) -> bool:
        return len(self.faces) > 1
    @property
    def primary_face(self) -> CardFace:
        return self.faces[0]