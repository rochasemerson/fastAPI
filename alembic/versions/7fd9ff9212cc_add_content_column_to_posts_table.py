"""add content column to posts table

Revision ID: 7fd9ff9212cc
Revises: d674ef17f581
Create Date: 2023-07-27 16:33:07.559709

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7fd9ff9212cc'
down_revision = 'd674ef17f581'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
