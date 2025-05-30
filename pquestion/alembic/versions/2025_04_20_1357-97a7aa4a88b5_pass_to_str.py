"""pass to str

Revision ID: 97a7aa4a88b5
Revises: 505bb187fecb
Create Date: 2025-04-20 13:57:59.610470

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = "97a7aa4a88b5"
down_revision: Union[str, None] = "505bb187fecb"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "users",
        "password",
        existing_type=postgresql.BYTEA(),
        type_=sa.String(),
        existing_nullable=False,
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "users",
        "password",
        existing_type=sa.String(),
        type_=postgresql.BYTEA(),
        existing_nullable=False,
    )
    # ### end Alembic commands ###
