"""buat table dosen

Revision ID: 9bd9c52e39f6
Revises: 19796ce5ecf1
Create Date: 2024-11-07 20:18:17.090886

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9bd9c52e39f6'
down_revision = '19796ce5ecf1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('dosen',
    sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
    sa.Column('nidn', sa.String(length=30), nullable=False),
    sa.Column('nama', sa.String(length=50), nullable=False),
    sa.Column('phone', sa.String(length=13), nullable=False),
    sa.Column('alamat', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('dosen')
    # ### end Alembic commands ###
