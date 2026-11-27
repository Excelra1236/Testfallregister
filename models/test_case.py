from dataclasses import dataclass, field
from uuid import UUID, uuid4

@dataclass
class TestCase:
    title: str
    description: str
    expected_result: str
    id: UUID = field(default_factory=uuid4, init=False)
    





