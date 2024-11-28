"""Hapus Cascade

Revision ID: 322c2e5c4001
Revises: bf0d66901a9d
Create Date: 2024-11-08 14:40:44.234669

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '322c2e5c4001'
down_revision = 'bf0d66901a9d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('mahasiswa', schema=None) as batch_op:
        batch_op.drop_constraint('mahasiswa_ibfk_2', type_='foreignkey')
        batch_op.drop_constraint('mahasiswa_ibfk_1', type_='foreignkey')
        batch_op.create_foreign_key(None, 'dosen', ['dosen_dua'], ['id'], ondelete='CASCADE')
        batch_op.create_foreign_key(None, 'dosen', ['dosen_satu'], ['id'], ondelete='CASCADE')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('mahasiswa', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('mahasiswa_ibfk_1', 'dosen', ['dosen_dua'], ['id'])
        batch_op.create_foreign_key('mahasiswa_ibfk_2', 'dosen', ['dosen_satu'], ['id'])

    # ### end Alembic commands ###
