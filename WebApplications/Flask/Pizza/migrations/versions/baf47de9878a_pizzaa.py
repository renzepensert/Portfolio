"""pizzaa

Revision ID: baf47de9878a
Revises: 336fba3aa1a8
Create Date: 2020-05-13 14:47:01.920868

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'baf47de9878a'
down_revision = '336fba3aa1a8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('rpizza',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=60), nullable=True),
    sa.Column('price', sa.Float(precision=5), nullable=True),
    sa.Column('price2', sa.Float(precision=5), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('spizza',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=60), nullable=True),
    sa.Column('price', sa.Float(precision=5), nullable=True),
    sa.Column('price2', sa.Float(precision=5), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.drop_table('pizza')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pizza',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=60), autoincrement=False, nullable=True),
    sa.Column('price', sa.REAL(), autoincrement=False, nullable=True),
    sa.Column('price2', sa.REAL(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='pizza_pkey'),
    sa.UniqueConstraint('name', name='pizza_name_key')
    )
    op.drop_table('spizza')
    op.drop_table('rpizza')
    # ### end Alembic commands ###
