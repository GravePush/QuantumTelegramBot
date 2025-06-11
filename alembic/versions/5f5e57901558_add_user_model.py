"""add user model

Revision ID: 5f5e57901558
Revises: e91d2ec2ef03
Create Date: 2025-06-10 17:43:08.531576

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5f5e57901558'
down_revision: Union[str, None] = 'e91d2ec2ef03'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
