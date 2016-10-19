import sqlalchemy as sa
from alembic import op

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
    op.drop_table('people')  # pragma: no cover
