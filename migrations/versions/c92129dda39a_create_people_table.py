"""create people table

Revision ID: c92129dda39a
Revises: 
Create Date: 2016-09-27 17:29:36.819424

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'c92129dda39a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'people',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(255), nullable=False),
    )


def downgrade():
    op.drop_table('people')
