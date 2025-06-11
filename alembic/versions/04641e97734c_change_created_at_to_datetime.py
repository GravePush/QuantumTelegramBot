"""change_created_at_to_datetime

Revision ID: 04641e97734c
Revises: 5aa94d5fa331
Create Date: 2025-06-10 10:47:57.197088

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '04641e97734c'
down_revision: Union[str, None] = '5aa94d5fa331'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
