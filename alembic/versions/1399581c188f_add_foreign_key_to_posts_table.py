"""add foreign-key to posts table

Revision ID: 1399581c188f
Revises: ca3fd1808a89
Create Date: 2023-07-31 14:02:48.282344

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1399581c188f'
down_revision = 'ca3fd1808a89'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('user_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_users_fk', source_table="posts", referent_table="users",
        local_cols=['user_id'], remote_cols=['id'], ondelete="CASCADE")
    pass


def downgrade() -> None:
    op.drop_constraint('post_users_fk', table_name="posts")
    op.drop_column('posts', 'user_id')
    pass
