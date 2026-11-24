from dataclasses import dataclass, field
from uuid import UUID, uuid4

@dataclass
class TestCase:
    titel: str
    beskrivning: str
    förväntat_resultat: str
    id: UUID = field(default_factory=uuid4, init=False)
    





